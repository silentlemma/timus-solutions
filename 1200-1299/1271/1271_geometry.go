package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const corners = 3

type point struct{ x, y int64 }

type axis struct {
	n      point
	lo, hi int64
}

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func dot(n, p point) int64 { return n.x*p.x + n.y*p.y }

// hull is the convex hull, counterclockwise, without points on the edges
func hull(pts []point) []point {
	sort.Slice(pts, func(i, j int) bool {
		return pts[i].x < pts[j].x || pts[i].x == pts[j].x && pts[i].y < pts[j].y
	})
	h := make([]point, 0, 2*len(pts))
	for _, p := range pts {
		for len(h) >= 2 && cross(h[len(h)-2], h[len(h)-1], p) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, p)
	}
	for i, t := len(pts)-2, len(h)+1; i >= 0; i-- {
		for len(h) >= t && cross(h[len(h)-2], h[len(h)-1], pts[i]) <= 0 {
			h = h[:len(h)-1]
		}
		h = append(h, pts[i])
	}
	return h[:len(h)-1]
}

// polygon is an open convex polygon: the places where the tanker hits a ship
type polygon struct {
	v              []point
	x0, x1, y0, y1 int64
	axes           []axis
}

func (g *polygon) project(n point) (int64, int64) {
	lo, hi := dot(n, g.v[0]), dot(n, g.v[0])
	for _, p := range g.v {
		d := dot(n, p)
		if d < lo {
			lo = d
		}
		if d > hi {
			hi = d
		}
	}
	return lo, hi
}

func newPolygon(v []point) *polygon {
	g := &polygon{v: v, x0: v[0].x, x1: v[0].x, y0: v[0].y, y1: v[0].y}
	for _, p := range v {
		g.x0, g.x1 = min(g.x0, p.x), max(g.x1, p.x)
		g.y0, g.y1 = min(g.y0, p.y), max(g.y1, p.y)
	}
	for i, a := range v {
		b := v[(i+1)%len(v)]
		n := point{b.y - a.y, a.x - b.x}
		lo, hi := g.project(n)
		g.axes = append(g.axes, axis{n, lo, hi})
	}
	return g
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

// holds tells whether p is strictly inside
func (g *polygon) holds(p point) bool {
	for i := range g.v {
		if cross(g.v[i], g.v[(i+1)%len(g.v)], p) <= 0 {
			return false
		}
	}
	return true
}

// blocks tells whether the segment pq crosses the inside: no axis separates
// them, neither an edge normal nor the normal of pq itself
func (g *polygon) blocks(p, q point) bool {
	if max(p.x, q.x) <= g.x0 || min(p.x, q.x) >= g.x1 {
		return false
	}
	if max(p.y, q.y) <= g.y0 || min(p.y, q.y) >= g.y1 {
		return false
	}
	for _, ax := range g.axes {
		a, b := dot(ax.n, p), dot(ax.n, q)
		if max(a, b) <= ax.lo || min(a, b) >= ax.hi {
			return false
		}
	}
	n := point{q.y - p.y, p.x - q.x}
	c := dot(n, p)
	lo, hi := g.project(n)
	return lo < c && c < hi
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var dx, dy int64
	fmt.Fscan(in, &dx, &dy)
	tanker := make([]point, corners)
	for i := range tanker {
		fmt.Fscan(in, &tanker[i].x, &tanker[i].y)
	}
	var goal point
	var n int
	fmt.Fscan(in, &goal.x, &goal.y, &n)
	// the tanker is placed by its first corner; offsets of all corners
	start := tanker[0]
	xlo, xhi, ylo, yhi := int64(0), dx, int64(0), dy
	var offsets []point
	for _, t := range tanker {
		o := point{t.x - start.x, t.y - start.y}
		offsets = append(offsets, o)
		xlo, xhi = max(xlo, -o.x), min(xhi, dx-o.x)
		ylo, yhi = max(ylo, -o.y), min(yhi, dy-o.y)
	}
	polygons := make([]*polygon, n)
	for i := range polygons {
		var sums []point
		ship := make([]point, corners)
		for k := range ship {
			fmt.Fscan(in, &ship[k].x, &ship[k].y)
		}
		for _, s := range ship {
			for _, o := range offsets {
				sums = append(sums, point{s.x - o.x, s.y - o.y})
			}
		}
		polygons[i] = newPolygon(hull(sums))
	}
	free := func(p point) bool {
		if p.x < xlo || p.x > xhi || p.y < ylo || p.y > yhi {
			return false
		}
		for _, g := range polygons {
			if g.holds(p) {
				return false
			}
		}
		return true
	}
	if !free(goal) {
		fmt.Println(-1)
		return
	}
	if goal == start {
		fmt.Println("0.000")
		return
	}
	// shortest paths bend only at corners of the forbidden polygons
	points := []point{start, goal}
	seen := map[point]bool{}
	for _, g := range polygons {
		for _, v := range g.v {
			if !seen[v] && free(v) {
				seen[v] = true
				points = append(points, v)
			}
		}
	}
	m := len(points)
	dist := make([]float64, m)
	done := make([]bool, m)
	for i := range dist {
		dist[i] = math.Inf(1)
	}
	dist[0] = 0
	for {
		i := -1
		for j := 0; j < m; j++ {
			if !done[j] && !math.IsInf(dist[j], 1) && (i < 0 || dist[j] < dist[i]) {
				i = j
			}
		}
		if i < 0 || i == 1 {
			break
		}
		done[i] = true
		p := points[i]
		for j, q := range points {
			if done[j] || q == p {
				continue
			}
			nd := dist[i] + math.Hypot(float64(q.x-p.x), float64(q.y-p.y))
			if nd >= dist[j] {
				continue
			}
			clear := true
			for _, g := range polygons {
				if g.blocks(p, q) {
					clear = false
					break
				}
			}
			if clear {
				dist[j] = nd
			}
		}
	}
	if math.IsInf(dist[1], 1) {
		fmt.Println(-1)
	} else {
		fmt.Printf("%.3f\n", dist[1])
	}
}
