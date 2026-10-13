package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type point struct{ x, y int64 }

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func less(a, b []int64) bool {
	for i := 0; i < len(a) && i < len(b); i++ {
		if a[i] != b[i] {
			return a[i] < b[i]
		}
	}
	return len(a) < len(b)
}

// hull: strict convex hull, counterclockwise, of sorted distinct points.
func hull(pts []point) []point {
	h := make([]point, 0, 2*len(pts))
	for _, p := range pts {
		for len(h) >= 2 && cross(h[len(h)-2], h[len(h)-1], p) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, p)
	}
	low := len(h) + 1
	for i := len(pts) - 2; i >= 0; i-- {
		for len(h) >= low && cross(h[len(h)-2], h[len(h)-1], pts[i]) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, pts[i])
	}
	return h[:len(h)-1]
}

// inFrame: coordinates of the points in the frame o + s e1 + t e2 over their
// least common denominator, the denominator first, the pairs sorted if asked.
func inFrame(pts []point, o, e1, e2 point, sortPairs bool) []int64 {
	d := e1.x*e2.y - e1.y*e2.x
	g := d
	pairs := make([][2]int64, len(pts))
	for i, p := range pts {
		qx, qy := p.x-o.x, p.y-o.y
		pairs[i] = [2]int64{qx*e2.y - qy*e2.x, e1.x*qy - e1.y*qx}
		g = gcd(g, gcd(pairs[i][0], pairs[i][1]))
	}
	if sortPairs {
		sort.Slice(pairs, func(i, j int) bool {
			if pairs[i][0] != pairs[j][0] {
				return pairs[i][0] < pairs[j][0]
			}
			return pairs[i][1] < pairs[j][1]
		})
	}
	key := []int64{d / g}
	for _, pr := range pairs {
		key = append(key, pr[0]/g, pr[1]/g)
	}
	return key
}

// canonical is the same for two point lists exactly when an affine map of
// positive determinant takes one onto the other.
func canonical(pts []point) []int64 {
	distinct := append([]point(nil), pts...)
	sort.Slice(distinct, func(i, j int) bool {
		if distinct[i].x != distinct[j].x {
			return distinct[i].x < distinct[j].x
		}
		return distinct[i].y < distinct[j].y
	})
	u := 0
	for _, p := range distinct {
		if u == 0 || distinct[u-1] != p {
			distinct[u] = p
			u++
		}
	}
	distinct = distinct[:u]
	if len(distinct) == 1 {
		return []int64{0, int64(len(pts))}
	}
	h := hull(distinct)
	if len(h) == 2 {
		// on one line: positions from 0 to 1 between the ends, read either way
		dx, dy := h[1].x-h[0].x, h[1].y-h[0].y
		length := dx*dx + dy*dy
		g := length
		forward := make([]int64, len(pts))
		for i, p := range pts {
			forward[i] = (p.x-h[0].x)*dx + (p.y-h[0].y)*dy
			g = gcd(g, forward[i])
		}
		den := length / g
		backward := make([]int64, len(pts))
		for i := range forward {
			forward[i] /= g
			backward[i] = den - forward[i]
		}
		sort.Slice(forward, func(i, j int) bool { return forward[i] < forward[j] })
		sort.Slice(backward, func(i, j int) bool { return backward[i] < backward[j] })
		pick := forward
		if less(backward, forward) {
			pick = backward
		}
		return append([]int64{1, den}, pick...)
	}
	// the frame at hull vertex i: it goes to 0, the next to (1, 0) and the
	// previous to (0, 1); a map of positive determinant keeps the order
	k := len(h)
	frameKey := func(i int, points []point, sortPairs bool) []int64 {
		o, nxt, prv := h[i], h[(i+1)%k], h[(i+k-1)%k]
		e1, e2 := point{nxt.x - o.x, nxt.y - o.y}, point{prv.x - o.x, prv.y - o.y}
		return inFrame(points, o, e1, e2, sortPairs)
	}
	shapes := make([][]int64, k)
	var best []int64
	for i := 0; i < k; i++ {
		turned := append(append([]point(nil), h[i:]...), h[:i]...)
		shapes[i] = frameKey(i, turned, false)
		if best == nil || less(shapes[i], best) {
			best = shapes[i]
		}
	}
	var chosen []int64
	for i := 0; i < k; i++ {
		if !less(shapes[i], best) && !less(best, shapes[i]) {
			candidate := frameKey(i, pts, true)
			if chosen == nil || less(candidate, chosen) {
				chosen = candidate
			}
		}
	}
	return append([]int64{2, int64(k)}, chosen...)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int64 {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return int64(v)
	}
	n := int(next())
	classes := map[string][]int{}
	sizes := map[string]int{}
	var keys []string
	for project := 1; project <= n; project++ {
		m := int(next())
		pts := make([]point, m)
		for i := range pts {
			pts[i] = point{next(), next()}
		}
		var sb strings.Builder
		for _, v := range canonical(pts) {
			sb.WriteString(strconv.FormatInt(v, 10))
			sb.WriteByte(' ')
		}
		key := sb.String()
		if _, ok := classes[key]; !ok {
			keys = append(keys, key)
		}
		classes[key] = append(classes[key], project)
		sizes[key] = m
	}
	// smaller projects first, then by the first project of the class
	sort.Slice(keys, func(i, j int) bool {
		if sizes[keys[i]] != sizes[keys[j]] {
			return sizes[keys[i]] < sizes[keys[j]]
		}
		return classes[keys[i]][0] < classes[keys[j]][0]
	})
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(keys))
	for _, key := range keys {
		for _, project := range classes[key] {
			fmt.Fprint(out, project, " ")
		}
		fmt.Fprintln(out, 0)
	}
}
