package main

import (
	"bufio"
	"io/ioutil"
	"math"
	"os"
	"runtime/debug"
	"sort"
	"strconv"
)

const (
	scale     = 30   // decimal digits kept after the point
	landmarks = 1024 // evenly spread start points for the walks
	floatBits = 64
	quad      = 4 // edges in a group: an edge and its rotations
	lastRot   = 3 // the last rotation, also the mask of the rotations
	outBuffer = 1 << 16
)

// error bounds of the floating-point filters
const (
	orientErr     = 3.3306690621773722e-16
	inCircleErr   = 1.1102230246251565e-15
	ten           = 10
	limbs         = 16
	limbBits      = 32
	fixedLimbs    = 4  // a coordinate times 10^scale fits in 128 bits
	lazyGC        = 20 // percent of heap growth between collections
	edgesPerPoint = 3  // a triangulation of k points has fewer than 3k edges
	keyBits       = 32
	epsBits       = 24 // eps = 2^-24 on squared distances
)

// Big is a signed integer modulo 2^512 in 32-bit limbs; every value used here
// is far below 2^511, so the arithmetic is exact.
type Big [limbs]uint32

func small(v int64) Big {
	var r Big
	u := uint64(v)
	fill := uint32(0)
	if v < 0 {
		fill = ^uint32(0)
	}
	for i := range r {
		if i < 2 {
			r[i] = uint32(u)
			u >>= limbBits
		} else {
			r[i] = fill
		}
	}
	return r
}

func add(x, y *Big) Big {
	var r Big
	carry := uint64(0)
	for i := range r {
		carry += uint64(x[i]) + uint64(y[i])
		r[i] = uint32(carry)
		carry >>= limbBits
	}
	return r
}

func sub(x, y *Big) Big {
	var r Big
	borrow := int64(0)
	for i := range r {
		z := int64(x[i]) - int64(y[i]) + borrow
		r[i] = uint32(z)
		borrow = 0
		if z < 0 {
			borrow = -1
		}
	}
	return r
}

func mul(x, y *Big) Big {
	var acc [limbs]uint64
	for i := 0; i < limbs; i++ {
		if x[i] == 0 {
			continue
		}
		carry := uint64(0)
		for j := 0; i+j < limbs; j++ {
			z := uint64(x[i])*uint64(y[j]) + acc[i+j] + carry
			acc[i+j] = uint64(uint32(z))
			carry = z >> limbBits
		}
	}
	var r Big
	for i := range r {
		r[i] = uint32(acc[i])
	}
	return r
}

// x = x * m + a for a non-negative x
func mulSmallAdd(x *Big, m, a uint32) {
	carry := uint64(a)
	for i := range x {
		z := uint64(x[i])*uint64(m) + carry
		x[i] = uint32(z)
		carry = z >> limbBits
	}
}

func sign(x *Big) int {
	if x[limbs-1]>>(limbBits-1) != 0 {
		return -1
	}
	for _, v := range x {
		if v != 0 {
			return 1
		}
	}
	return 0
}

func compare(x, y *Big) int {
	d := sub(x, y)
	return sign(&d)
}

func abs(x Big) Big {
	if sign(&x) < 0 {
		var zero Big
		return sub(&zero, &x)
	}
	return x
}

// fixed is a coordinate times 10^scale: a signed 128-bit integer
type fixed [fixedLimbs]uint32

func widen(f *fixed) Big {
	var r Big
	copy(r[:], f[:])
	if f[fixedLimbs-1]>>(limbBits-1) != 0 {
		for i := fixedLimbs; i < limbs; i++ {
			r[i] = ^uint32(0)
		}
	}
	return r
}

func narrow(b Big) (f fixed) {
	copy(f[:], b[:fixedLimbs])
	return f
}

func compareFixed(a, b *fixed) int {
	x, y := widen(a), widen(b)
	return compare(&x, &y)
}

type point struct {
	x, y        fixed // the coordinates times 10^scale, exact
	fx, fy      float64
	first, last int // the cockroaches at this point: ids[first:last]
}

var pts []point

// the squared distance from point i to (qx, qy), exact: scale * 2 digits
func dist2(i int, qx, qy *Big) Big {
	px, py := widen(&pts[i].x), widen(&pts[i].y)
	dx, dy := sub(&px, qx), sub(&py, qy)
	dx, dy = abs(dx), abs(dy)
	sx, sy := mul(&dx, &dx), mul(&dy, &dy)
	return add(&sx, &sy)
}

func dist2f(i int, x, y float64) float64 {
	dx, dy := pts[i].fx-x, pts[i].fy-y
	return dx*dx + dy*dy
}

// Each predicate is evaluated in floating point first; when the result is
// within the rounding error, it is recomputed exactly on the decimals.
func diff(a, b int) (Big, Big) {
	ax, ay, bx, by := widen(&pts[a].x), widen(&pts[a].y), widen(&pts[b].x), widen(&pts[b].y)
	return sub(&ax, &bx), sub(&ay, &by)
}

func cross(ax, ay, bx, by *Big) Big {
	l, r := mul(ax, by), mul(ay, bx)
	return sub(&l, &r)
}

func lift(x, y *Big) Big {
	a, b := mul(x, x), mul(y, y)
	return add(&a, &b)
}

func orient(a, b, c int) int {
	l := (pts[a].fx - pts[c].fx) * (pts[b].fy - pts[c].fy)
	r := (pts[a].fy - pts[c].fy) * (pts[b].fx - pts[c].fx)
	det, err := l-r, orientErr*math.Abs(l+r)
	if det > err {
		return 1
	}
	if det < -err {
		return -1
	}
	ax, ay := diff(a, c)
	bx, by := diff(b, c)
	d := cross(&ax, &ay, &bx, &by)
	return sign(&d)
}

func exactInCircle(a, b, c, d int) bool {
	adx, ady := diff(a, d)
	bdx, bdy := diff(b, d)
	cdx, cdy := diff(c, d)
	ab, bc := cross(&adx, &ady, &bdx, &bdy), cross(&bdx, &bdy, &cdx, &cdy)
	ca := cross(&cdx, &cdy, &adx, &ady)
	al, bl, cl := lift(&adx, &ady), lift(&bdx, &bdy), lift(&cdx, &cdy)
	t1, t2, t3 := mul(&al, &bc), mul(&bl, &ca), mul(&cl, &ab)
	s := add(&t1, &t2)
	s = add(&s, &t3)
	return sign(&s) > 0
}

// d lies strictly inside the circle through a, b, c (counterclockwise)
func inCircle(a, b, c, d int) bool {
	adx, ady := pts[a].fx-pts[d].fx, pts[a].fy-pts[d].fy
	bdx, bdy := pts[b].fx-pts[d].fx, pts[b].fy-pts[d].fy
	cdx, cdy := pts[c].fx-pts[d].fx, pts[c].fy-pts[d].fy
	bdxcdy, cdxbdy := bdx*cdy, cdx*bdy
	cdxady, adxcdy := cdx*ady, adx*cdy
	adxbdy, bdxady := adx*bdy, bdx*ady
	al, bl, cl := adx*adx+ady*ady, bdx*bdx+bdy*bdy, cdx*cdx+cdy*cdy
	det := al*(bdxcdy-cdxbdy) + bl*(cdxady-adxcdy) + cl*(adxbdy-bdxady)
	permanent := (math.Abs(bdxcdy)+math.Abs(cdxbdy))*al + (math.Abs(cdxady)+math.Abs(adxcdy))*bl +
		(math.Abs(adxbdy)+math.Abs(bdxady))*cl
	err := inCircleErr * permanent
	if det > err {
		return true
	}
	if det < -err {
		return false
	}
	return exactInCircle(a, b, c, d)
}

// Delaunay triangulation by divide and conquer on quad-edges: edge e, its
// rotations within one group of four, rev(e) the same edge reversed.
var (
	orig, nextEdge []int32
	freeEdges      []int
	active         []bool
)

func rot(e int) int    { return (e &^ lastRot) | ((e + 1) & lastRot) }
func invrot(e int) int { return (e &^ lastRot) | ((e + lastRot) & lastRot) }
func rev(e int) int    { return e ^ 2 }
func org(e int) int    { return int(orig[e]) }
func nxt(e int) int    { return int(nextEdge[e]) }
func dest(e int) int   { return org(rev(e)) }
func lnext(e int) int  { return rot(nxt(invrot(e))) }
func oprev(e int) int  { return rot(nxt(rot(e))) }

func makeEdge(a, b int) int {
	var e int
	if len(freeEdges) > 0 {
		e = freeEdges[len(freeEdges)-1]
		freeEdges = freeEdges[:len(freeEdges)-1]
	} else {
		e = len(orig)
		orig = append(orig, 0, 0, 0, 0)
		nextEdge = append(nextEdge, 0, 0, 0, 0)
		active = append(active, false)
	}
	E := int32(e)
	orig[e], orig[e+1], orig[e+2], orig[e+lastRot] = int32(a), -1, int32(b), -1
	nextEdge[e], nextEdge[e+2] = E, E+2
	nextEdge[e+1], nextEdge[e+lastRot] = E+lastRot, E+1
	active[e>>2] = true
	return e
}

func splice(a, b int) {
	alpha, beta := rot(nxt(a)), rot(nxt(b))
	nextEdge[alpha], nextEdge[beta] = nextEdge[beta], nextEdge[alpha]
	nextEdge[a], nextEdge[b] = nextEdge[b], nextEdge[a]
}

func deleteEdge(e int) {
	splice(e, oprev(e))
	splice(rev(e), oprev(rev(e)))
	active[e>>2] = false
	freeEdges = append(freeEdges, e&^3)
}

func connect(a, b int) int {
	e := makeEdge(dest(a), org(b))
	splice(e, lnext(a))
	splice(rev(e), b)
	return e
}

func leftOf(p, e int) bool  { return orient(org(e), dest(e), p) > 0 }
func rightOf(p, e int) bool { return orient(org(e), dest(e), p) < 0 }

// points l..r (sorted by x, then y); returns the counterclockwise hull edge
// out of the leftmost point and the clockwise one out of the rightmost
func build(l, r int) (int, int) {
	if r-l == 1 {
		e := makeEdge(l, r)
		return e, rev(e)
	}
	if r-l == 2 {
		a, b := makeEdge(l, l+1), makeEdge(l+1, r)
		splice(rev(a), b)
		turn := orient(l, l+1, r)
		if turn == 0 {
			return a, rev(b)
		}
		c := connect(b, a)
		if turn > 0 {
			return a, rev(b)
		}
		return rev(c), c
	}
	mid := (l + r) / 2
	ldo, ldi := build(l, mid)
	rdi, rdo := build(mid+1, r)
	for { // the lower common tangent
		if leftOf(org(rdi), ldi) {
			ldi = lnext(ldi)
		} else if rightOf(org(ldi), rdi) {
			rdi = nxt(rev(rdi))
		} else {
			break
		}
	}
	basel := connect(rev(rdi), ldi)
	valid := func(e int) bool { return rightOf(dest(e), basel) }
	if org(ldi) == org(ldo) {
		ldo = rev(basel)
	}
	if org(rdi) == org(rdo) {
		rdo = basel
	}
	for { // zip the halves upward
		lc := nxt(rev(basel))
		if valid(lc) {
			for inCircle(dest(basel), org(basel), dest(lc), dest(nxt(lc))) {
				t := nxt(lc)
				deleteEdge(lc)
				lc = t
			}
		}
		rc := oprev(basel)
		if valid(rc) {
			for inCircle(dest(basel), org(basel), dest(rc), dest(oprev(rc))) {
				t := oprev(rc)
				deleteEdge(rc)
				rc = t
			}
		}
		lv, rv := valid(lc), valid(rc)
		if !lv && !rv {
			break
		}
		if !lv || (rv && inCircle(dest(lc), org(lc), org(rc), dest(rc))) {
			basel = connect(rc, rev(basel))
		} else {
			basel = connect(rev(basel), rev(lc))
		}
	}
	return ldo, rdo
}

// The graph: the triangulation plus the neighbours in the order by x and by
// y, as adjacency lists adj[offsetOf[v]:offsetOf[v+1]].
var offsetOf, adj []int32

func edgeKey(a, b int) uint64 {
	if a > b {
		a, b = b, a
	}
	return uint64(a)<<keyBits | uint64(b)
}

func makeGraph(keys []uint64, n int) {
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
	u := 0
	for i, k := range keys {
		if i == 0 || k != keys[u-1] {
			keys[u] = k
			u++
		}
	}
	keys = keys[:u]
	offsetOf = make([]int32, n+1)
	for _, k := range keys {
		offsetOf[k>>keyBits+1]++
		offsetOf[uint32(k)+1]++
	}
	for i := 0; i < n; i++ {
		offsetOf[i+1] += offsetOf[i]
	}
	at := append([]int32(nil), offsetOf[:n]...)
	adj = make([]int32, offsetOf[n])
	for _, k := range keys {
		a, b := int32(k>>keyBits), int32(uint32(k))
		adj[at[a]] = b
		at[a]++
		adj[at[b]] = a
		at[b]++
	}
}

// a decimal number times 10^scale, digits beyond that dropped
func parseFixed(s []byte) Big {
	negative := len(s) > 0 && s[0] == '-'
	if len(s) > 0 && (s[0] == '-' || s[0] == '+') {
		s = s[1:]
	}
	var digits []byte
	fraction, exponent, dot := 0, 0, false
	i := 0
	for ; i < len(s) && s[i] != 'e' && s[i] != 'E'; i++ {
		if s[i] == '.' {
			dot = true
			continue
		}
		digits = append(digits, s[i]-'0')
		if dot {
			fraction++
		}
	}
	if i < len(s) {
		exponent, _ = strconv.Atoi(string(s[i+1:]))
	}
	shift, keep := scale-fraction+exponent, len(digits)
	if shift < 0 {
		keep += shift
		if keep < 0 {
			keep = 0
		}
	}
	var v Big
	for _, d := range digits[:keep] {
		mulSmallAdd(&v, ten, uint32(d))
	}
	for j := 0; j < shift; j++ {
		mulSmallAdd(&v, ten, 0)
	}
	if negative {
		var zero Big
		v = sub(&zero, &v)
	}
	return v
}

// the point nearest to the sweet: a walk on floating point, then an exact one
func nearestPoint(seed int, qx, qy *Big, x, y float64) int {
	cur := seed
	for {
		best, bd := cur, dist2f(cur, x, y)
		for _, w := range adj[offsetOf[cur]:offsetOf[cur+1]] {
			if v := int(w); dist2f(v, x, y) < bd {
				bd, best = dist2f(v, x, y), v
			}
		}
		if best == cur {
			break
		}
		cur = best
	}
	for {
		best, bd := cur, dist2(cur, qx, qy)
		for _, w := range adj[offsetOf[cur]:offsetOf[cur+1]] {
			if z := dist2(int(w), qx, qy); compare(&z, &bd) < 0 {
				bd, best = z, int(w)
			}
		}
		if best == cur {
			return cur
		}
		cur = best
	}
}

func main() {
	debug.SetGCPercent(lazyGC)
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	pos := 0
	token := func() []byte {
		for pos < len(data) && data[pos] <= ' ' {
			pos++
		}
		start := pos
		for pos < len(data) && data[pos] > ' ' {
			pos++
		}
		return data[start:pos]
	}
	number := func(t []byte) float64 {
		v, _ := strconv.ParseFloat(string(t), floatBits)
		return v
	}
	out := bufio.NewWriterSize(os.Stdout, outBuffer)
	defer out.Flush()
	m, _ := strconv.Atoi(string(token()))
	raw := make([]point, m)
	for i := range raw {
		tx, ty := token(), token()
		raw[i] = point{narrow(parseFixed(tx)), narrow(parseFixed(ty)), number(tx), number(ty), i, i + 1}
	}
	n, _ := strconv.Atoi(string(token()))
	if n == 0 {
		return
	}
	// equal points become one, keeping all their cockroaches
	sort.Slice(raw, func(i, j int) bool {
		if c := compareFixed(&raw[i].x, &raw[j].x); c != 0 {
			return c < 0
		}
		if c := compareFixed(&raw[i].y, &raw[j].y); c != 0 {
			return c < 0
		}
		return raw[i].first < raw[j].first
	})
	ids := make([]int, 0, m)
	pts = raw[:0] // compacted in place: each point is read before its slot is reused
	for i := 0; i < m; {
		j, start := i, len(ids)
		for ; j < m && raw[j].x == raw[i].x && raw[j].y == raw[i].y; j++ {
			ids = append(ids, raw[j].first+1)
		}
		p := raw[i]
		p.first, p.last = start, len(ids)
		pts = append(pts, p)
		i = j
	}
	k := len(pts)
	var keys []uint64
	collinear := true
	for i := 2; i < k && collinear; i++ {
		collinear = orient(0, 1, i) == 0
	}
	if k > 2 && !collinear {
		most := quad * (edgesPerPoint*k + quad)
		orig, nextEdge = make([]int32, 0, most), make([]int32, 0, most)
		build(0, k-1)
		for q, on := range active {
			if on {
				keys = append(keys, edgeKey(org(q*quad), org(q*quad+2)))
			}
		}
		byY := make([]int, k)
		for i := range byY {
			byY[i] = i
		}
		sort.Slice(byY, func(i, j int) bool {
			a, b := byY[i], byY[j]
			if c := compareFixed(&pts[a].y, &pts[b].y); c != 0 {
				return c < 0
			}
			return compareFixed(&pts[a].x, &pts[b].x) < 0
		})
		for i := 1; i < k; i++ {
			keys = append(keys, edgeKey(byY[i-1], byY[i]))
		}
	}
	for i := 1; i < k; i++ { // neighbours by x; on a line, all edges
		keys = append(keys, edgeKey(i-1, i))
	}
	makeGraph(keys, k)

	// the answer: the nearest point and every point closer than it plus eps,
	// found by a search through the graph from it
	eps, tenB := small(1), small(ten)
	for i := 0; i < 2*scale; i++ {
		eps = mul(&eps, &tenB)
	}
	for i := 0; i < epsBits; i++ { // eps times 10^(2 * scale), an integer
		carry := uint32(0)
		for j := limbs - 1; j >= 0; j-- {
			low := eps[j] & 1
			eps[j] = eps[j]>>1 | carry<<(limbBits-1)
			carry = low
		}
	}
	marks := landmarks
	if k < marks {
		marks = k
	}
	landmark := make([]int, marks)
	for i := range landmark {
		if marks > 1 {
			landmark[i] = i * (k - 1) / (marks - 1)
		}
	}
	seen := make([]int, k)
	var queue, answer []int
	prev := 0
	for stamp := 1; stamp <= n; stamp++ {
		tx, ty := token(), token()
		qx, qy := parseFixed(tx), parseFixed(ty)
		x, y := number(tx), number(ty)
		seed, bd := prev, dist2f(prev, x, y)
		for _, v := range landmark {
			if z := dist2f(v, x, y); z < bd {
				bd, seed = z, v
			}
		}
		best := nearestPoint(seed, &qx, &qy, x, y)
		prev = best
		d := dist2(best, &qx, &qy)
		limit := add(&d, &eps)
		queue = append(queue[:0], best)
		answer = answer[:0]
		seen[best] = stamp
		for h := 0; h < len(queue); h++ {
			v := queue[h]
			if d := dist2(v, &qx, &qy); compare(&d, &limit) >= 0 {
				continue
			}
			answer = append(answer, ids[pts[v].first:pts[v].last]...)
			for _, w := range adj[offsetOf[v]:offsetOf[v+1]] {
				if u := int(w); seen[u] != stamp {
					seen[u] = stamp
					queue = append(queue, u)
				}
			}
		}
		sort.Ints(answer)
		for i, v := range answer {
			if i > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(v))
		}
		out.WriteByte('\n')
	}
}
