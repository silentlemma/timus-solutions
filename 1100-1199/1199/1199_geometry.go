package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	safe = 0.1
	inf  = 1e300
	same = 1e-9
)

type pt struct{ x, y float64 }

type polygon struct {
	v, d      []pt // corners and the edge vectors leaving them
	cx, cy, r float64
}

// pos is a place on a boundary: edge index and position along that edge.
type pos struct {
	edge int
	t    float64
}

// pointEdges finds the nearest point of the edges to p if closer than
// *best, updating *best (squared distance) and *where.
func pointEdges(p pt, poly *polygon, best *float64, where *pos) bool {
	found := false
	for i := range poly.v {
		wx, wy := p.x-poly.v[i].x, p.y-poly.v[i].y
		dx, dy := poly.d[i].x, poly.d[i].y
		d2 := dx*dx + dy*dy
		t := wx*dx + wy*dy
		var q float64
		if t <= 0 {
			q, t = wx*wx+wy*wy, 0
		} else if t >= d2 {
			q, t = (wx-dx)*(wx-dx)+(wy-dy)*(wy-dy), 1
		} else {
			c := wx*dy - wy*dx
			q, t = c*c/d2, t/d2
		}
		if q < *best {
			*best, *where, found = q, pos{i, t}, true
		}
	}
	return found
}

// polyPoly returns the squared distance between two polygons and where it
// is reached on each.
func polyPoly(a, b *polygon) (float64, pos, pos) {
	best := inf
	var onA, onB pos
	for side := 0; side < 2; side++ {
		own, other := a, b
		if side == 1 {
			own, other = b, a
		}
		for k, p := range own.v {
			var there pos
			if pointEdges(p, other, &best, &there) {
				here := pos{k, 0}
				if side == 1 {
					onA, onB = there, here
				} else {
					onA, onB = here, there
				}
			}
		}
	}
	return best, onA, onB
}

func at(poly *polygon, p pos) pt {
	return pt{poly.v[p.edge].x + poly.d[p.edge].x*p.t, poly.v[p.edge].y + poly.d[p.edge].y*p.t}
}

// walk appends the corners passed going along the boundary from src to
// dst, in the direction with fewer of them.
func walk(poly *polygon, src, dst pos, path []pt) []pt {
	k := len(poly.v)
	fwd, back := ((dst.edge-src.edge)%k+k)%k, ((src.edge-dst.edge)%k+k)%k
	if fwd == 0 && dst.t < src.t {
		fwd = k
	}
	if back == 0 && dst.t > src.t {
		back = k
	}
	if fwd <= back {
		for s := 0; s < fwd; s++ {
			path = append(path, poly.v[(src.edge+1+s)%k])
		}
	} else {
		for s := 0; s < back; s++ {
			path = append(path, poly.v[((src.edge-s)%k+k)%k])
		}
	}
	return path
}

func toward(f, p pt, length float64) pt {
	d := math.Hypot(p.x-f.x, p.y-f.y)
	return pt{f.x + (p.x-f.x)*length/d, f.y + (p.y-f.y)*length/d}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var mouse, cheese pt
	var n int
	fmt.Fscan(in, &mouse.x, &mouse.y, &cheese.x, &cheese.y, &n)
	polys := make([]polygon, n)
	for i := range polys {
		poly := &polys[i]
		var k int
		fmt.Fscan(in, &k)
		poly.v = make([]pt, k)
		for j := range poly.v {
			fmt.Fscan(in, &poly.v[j].x, &poly.v[j].y)
			poly.cx += poly.v[j].x / float64(k)
			poly.cy += poly.v[j].y / float64(k)
		}
		// the corners may come in any order, so sort them around the centre
		sort.Slice(poly.v, func(a, b int) bool {
			pa, pb := poly.v[a], poly.v[b]
			return math.Atan2(pa.y-poly.cy, pa.x-poly.cx) < math.Atan2(pb.y-poly.cy, pb.x-poly.cx)
		})
		for j := 0; j < k; j++ {
			next := poly.v[(j+1)%k]
			poly.d = append(poly.d, pt{next.x - poly.v[j].x, next.y - poly.v[j].y})
			poly.r = math.Max(poly.r, math.Hypot(poly.v[j].x-poly.cx, poly.v[j].y-poly.cy))
		}
	}

	// nodes 0..n-1 are the safe zones around the furniture, n the mouse and
	// n + 1 the cheese; an edge costs the dangerous length between them
	toPoint := func(p pt, a int) float64 {
		best := inf
		var where pos
		pointEdges(p, &polys[a], &best, &where)
		return math.Max(0, math.Sqrt(best)-safe)
	}
	start, goal := n, n+1
	dist := make([]float64, n+2)
	parent := make([]int, n+2)
	done := make([]bool, n+2)
	for i := range dist {
		dist[i] = inf
	}
	dist[start] = 0
	for {
		u := -1
		for v := 0; v < n+2; v++ {
			if !done[v] && (u < 0 || dist[v] < dist[u]) {
				u = v
			}
		}
		if u == goal {
			break
		}
		done[u] = true
		for v := 0; v < n+2; v++ {
			if done[v] {
				continue
			}
			var w float64
			if v == goal && u == start {
				w = math.Hypot(mouse.x-cheese.x, mouse.y-cheese.y)
			} else if v == goal {
				w = toPoint(cheese, u)
			} else if u == start {
				w = toPoint(mouse, v)
			} else {
				a, b := &polys[u], &polys[v]
				gap := math.Hypot(a.cx-b.cx, a.cy-b.cy) - a.r - b.r - 2*safe
				if dist[u]+gap >= dist[v] {
					continue
				}
				q, _, _ := polyPoly(a, b)
				w = math.Sqrt(q) - 2*safe
			}
			if dist[u]+w < dist[v] {
				dist[v], parent[v] = dist[u]+w, u
			}
		}
	}
	route := []int{goal}
	for route[len(route)-1] != start {
		route = append(route, parent[route[len(route)-1]])
	}
	for i, j := 0, len(route)-1; i < j; i, j = i+1, j-1 {
		route[i], route[j] = route[j], route[i]
	}

	path := []pt{mouse}
	if len(route) == 2 {
		path = append(path, cheese)
	} else {
		// step from the mouse onto the nearest point of the first piece
		first := &polys[route[1]]
		q := inf
		var here pos
		pointEdges(mouse, first, &q, &here)
		foot := at(first, here)
		if math.Sqrt(q) > safe {
			path = append(path, toward(foot, mouse, safe))
		}
		path = append(path, foot)
		for i := 1; i+2 < len(route); i++ {
			a, b := &polys[route[i]], &polys[route[i+1]]
			_, outPos, inPos := polyPoly(a, b)
			fa, fb := at(a, outPos), at(b, inPos)
			path = walk(a, here, outPos, path)
			path = append(path, fa, toward(fa, fb, safe), toward(fb, fa, safe), fb)
			here = inPos
		}
		last := &polys[route[len(route)-2]]
		q = inf
		var end pos
		pointEdges(cheese, last, &q, &end)
		foot = at(last, end)
		path = walk(last, here, end, path)
		path = append(path, foot)
		if math.Sqrt(q) > safe {
			path = append(path, toward(foot, cheese, safe))
		}
		path = append(path, cheese)
	}

	out := []pt{path[0]}
	for _, p := range path[1:] {
		prev := out[len(out)-1]
		if math.Hypot(p.x-prev.x, p.y-prev.y) > same {
			out = append(out, p)
		}
	}
	if len(out) == 1 {
		out = append(out, path[len(path)-1])
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintln(w, len(out))
	for _, p := range out {
		fmt.Fprintf(w, "%.9f %.9f\n", p.x, p.y)
	}
}
