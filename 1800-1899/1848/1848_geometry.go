package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

// item is an edge from its left end to its right end, or a fly when both
// ends meet
type item struct {
	lx, ly, rx, ry int64
	polygon        int
	top            bool // the inside lies below the edge
}

func (s *item) point() bool { return s.lx == s.rx }

// side tells where s lies against t, both crossing the sweep line just
// right of its position: -1 below, 1 above, 0 the same edge or a fly on
// it. The comparison uses the end of one that lies over the other.
func side(s, t *item) int {
	if t.point() || (!s.point() && s.lx < t.lx) {
		return -side(t, s)
	}
	tx, ty := t.rx-t.lx, t.ry-t.ly
	c := tx*(s.ly-t.ly) - ty*(s.lx-t.lx)
	if c == 0 && !s.point() {
		// two edges of one polygon from a common left end
		c = tx*(s.ry-t.ly) - ty*(s.rx-t.lx)
	}
	switch {
	case c > 0:
		return 1
	case c < 0:
		return -1
	}
	return 0
}

// a treap of the active edges from bottom to top
type node struct {
	edge        *item
	left, right *node
	weight      uint32
}

// xorshift random weights
const (
	shiftA = 13
	shiftB = 17
	shiftC = 5
)

var seed uint32 = 2463534242

func random() uint32 {
	seed ^= seed << shiftA
	seed ^= seed >> shiftB
	seed ^= seed << shiftC
	return seed
}

// split cuts t into the edges below key and the rest
func split(t *node, key *item) (*node, *node) {
	if t == nil {
		return nil, nil
	}
	if side(t.edge, key) < 0 {
		l, r := split(t.right, key)
		t.right = l
		return t, r
	}
	l, r := split(t.left, key)
	t.left = r
	return l, t
}

func merge(a, b *node) *node {
	if a == nil {
		return b
	}
	if b == nil {
		return a
	}
	if a.weight > b.weight {
		a.right = merge(a.right, b)
		return a
	}
	b.left = merge(a, b.left)
	return b
}

// dropFirst removes the lowest edge of t
func dropFirst(t *node) *node {
	if t.left == nil {
		return t.right
	}
	t.left = dropFirst(t.left)
	return t
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	at := 0
	next := func() int64 {
		for data[at] != '-' && (data[at] < '0' || data[at] > '9') {
			at++
		}
		negative := data[at] == '-'
		if negative {
			at++
		}
		v := int64(0)
		for at < len(data) && data[at] >= '0' && data[at] <= '9' {
			v = v*10 + int64(data[at]-'0')
			at++
		}
		if negative {
			return -v
		}
		return v
	}
	n := int(next())
	fx, fy := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fx[i], fy[i] = next(), next()
	}
	m := int(next())
	type spot struct{ x, y int64 }
	type span struct {
		low, high int64
		polygon   int
	}
	corners := map[spot]int{}   // vertex -> polygon
	upright := map[int64][]span{} // x -> vertical edges
	var edges []item
	for p := 0; p < m; p++ {
		k := int(next())
		xs, ys := make([]int64, k), make([]int64, k)
		for i := 0; i < k; i++ {
			xs[i], ys[i] = next(), next()
		}
		for i := 0; i < k; i++ {
			ax, ay, bx, by := xs[(i+k-1)%k], ys[(i+k-1)%k], xs[i], ys[i]
			corners[spot{bx, by}] = p
			if ax == bx {
				low, high := ay, by
				if low > high {
					low, high = high, low
				}
				upright[ax] = append(upright[ax], span{low, high, p})
				continue
			}
			// counter-clockwise: the inside is left of the edge, so an edge
			// running right to left has the inside below it
			if ax > bx {
				edges = append(edges, item{bx, by, ax, ay, p, true})
			} else {
				edges = append(edges, item{ax, ay, bx, by, p, false})
			}
		}
	}
	for _, spans := range upright {
		sort.Slice(spans, func(i, j int) bool { return spans[i].low < spans[j].low })
	}
	e := len(edges)
	starts, ends, order := make([]int, e), make([]int, e), make([]int, n)
	for i := range starts {
		starts[i], ends[i] = i, i
	}
	for i := range order {
		order[i] = i
	}
	sort.Slice(starts, func(i, j int) bool { return edges[starts[i]].lx < edges[starts[j]].lx })
	sort.Slice(ends, func(i, j int) bool { return edges[ends[i]].rx < edges[ends[j]].rx })
	sort.Slice(order, func(i, j int) bool { return fx[order[i]] < fx[order[j]] })
	var root *node
	count := make([]int, m)
	si, ei := 0, 0
	for _, f := range order {
		x, y := fx[f], fy[f]
		// sweep every event column up to x; in a column, edges ending there
		// leave before edges starting there come in
		for {
			column := x + 1
			if si < e && edges[starts[si]].lx < column {
				column = edges[starts[si]].lx
			}
			if ei < e && edges[ends[ei]].rx < column {
				column = edges[ends[ei]].rx
			}
			if column > x {
				break
			}
			for ; ei < e && edges[ends[ei]].rx == column; ei++ {
				l, r := split(root, &edges[ends[ei]])
				root = merge(l, dropFirst(r))
			}
			for ; si < e && edges[starts[si]].lx == column; si++ {
				l, r := split(root, &edges[starts[si]])
				root = merge(merge(l, &node{edge: &edges[starts[si]], weight: random()}), r)
			}
		}
		if p, ok := corners[spot{x, y}]; ok {
			count[p]++
			continue
		}
		if spans, ok := upright[x]; ok {
			j := sort.Search(len(spans), func(i int) bool { return spans[i].low > y })
			if j > 0 && spans[j-1].high >= y {
				count[spans[j-1].polygon]++
				continue
			}
		}
		fly := item{x, y, x, y, -1, false}
		var found *item
		for t := root; t != nil; {
			if side(t.edge, &fly) < 0 {
				t = t.right
			} else {
				found, t = t.edge, t.left
			}
		}
		if found != nil && (found.top || side(&fly, found) == 0) {
			count[found.polygon]++
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, c := range count {
		out.WriteString(strconv.Itoa(c))
		out.WriteByte('\n')
	}
}
