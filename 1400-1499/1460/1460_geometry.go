package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type pt [2]float64

const (
	corners = 3
	pins    = 4
	wide    = 2 * math.Pi / 3 // 120 degrees
	eps     = 1e-12
)

var root3 = math.Sqrt(3) / 2 // the height of a unit equilateral triangle

// the pairs that share an extra point, each way round
var pairings = [][2][2]int{
	{{0, 1}, {2, 3}}, {{0, 2}, {1, 3}}, {{0, 3}, {1, 2}},
	{{2, 3}, {0, 1}}, {{1, 3}, {0, 2}}, {{1, 2}, {0, 3}},
}

func dist(p, q pt) float64 { return math.Hypot(p[0]-q[0], p[1]-q[1]) }

// the point with the least total distance to three points (see 1451)
func fermat(p [corners]pt) pt {
	for i := 0; i < corners; i++ {
		for j := i + 1; j < corners; j++ {
			if dist(p[i], p[j]) < eps {
				return p[i]
			}
		}
	}
	var angle, side [corners]float64
	for i := 0; i < corners; i++ {
		a, b, c := p[i], p[(i+1)%corners], p[(i+2)%corners]
		ux, uy, wx, wy := b[0]-a[0], b[1]-a[1], c[0]-a[0], c[1]-a[1]
		angle[i] = math.Atan2(math.Abs(ux*wy-uy*wx), ux*wx+uy*wy)
		side[i] = dist(b, c)
	}
	for i := 0; i < corners; i++ {
		if angle[i] >= wide {
			return p[i]
		}
	}
	total, x, y := 0.0, 0.0, 0.0
	for i := 0; i < corners; i++ {
		w := side[i] / math.Sin(angle[i]+math.Pi/corners)
		total += w
		x += w * p[i][0]
		y += w * p[i][1]
	}
	return pt{x / total, y / total}
}

func shortest(p [pins]pt) float64 {
	// trees without extra points: the best spanning tree
	type edge struct {
		length float64
		i, j   int
	}
	var edges []edge
	for i := 0; i < pins; i++ {
		for j := i + 1; j < pins; j++ {
			edges = append(edges, edge{dist(p[i], p[j]), i, j})
		}
	}
	sort.Slice(edges, func(a, b int) bool { return edges[a].length < edges[b].length })
	var group [pins]int
	for i := range group {
		group[i] = i
	}
	root := func(x int) int {
		for group[x] != x {
			x = group[x]
		}
		return x
	}
	best := 0.0
	for _, e := range edges {
		if a, b := root(e.i), root(e.j); a != b {
			group[a] = b
			best += e.length
		}
	}
	// one extra point joining three pins, the fourth wired to one of the four
	for rest := 0; rest < pins; rest++ {
		var trio [corners]pt
		k := 0
		for i := 0; i < pins; i++ {
			if i != rest {
				trio[k] = p[i]
				k++
			}
		}
		s := fermat(trio)
		star, link := 0.0, dist(p[rest], s)
		for _, q := range trio {
			star += dist(s, q)
			link = math.Min(link, dist(p[rest], q))
		}
		best = math.Min(best, star+link)
	}
	// two extra points, {a, b} on one and {c, d} on the other: the Melzak
	// construction gives both, and the real length of that tree is a candidate
	for _, pr := range pairings {
		a, b, c, d := p[pr[0][0]], p[pr[0][1]], p[pr[1][0]], p[pr[1][1]]
		mx, my, dx, dy := (a[0]+b[0])/2, (a[1]+b[1])/2, b[0]-a[0], b[1]-a[1]
		for _, side := range []float64{1, -1} {
			e := pt{mx - side*dy*root3, my + side*dx*root3}
			s2 := fermat([corners]pt{e, c, d})
			s1 := fermat([corners]pt{a, b, s2})
			best = math.Min(best, dist(s1, a)+dist(s1, b)+dist(s1, s2)+dist(s2, c)+dist(s2, d))
		}
	}
	return best
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var tests int
	fmt.Fscan(reader, &tests)
	for ; tests > 0; tests-- {
		var p [pins]pt
		for i := range p {
			fmt.Fscan(reader, &p[i][0], &p[i][1])
		}
		fmt.Printf("%.6f\n", shortest(p))
	}
}
