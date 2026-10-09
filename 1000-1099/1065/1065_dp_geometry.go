package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

type point struct{ x, y int64 }

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	towers := make([]point, n)
	for i := range towers {
		fmt.Fscan(in, &towers[i].x, &towers[i].y)
	}
	monuments := make([]point, m)
	for i := range monuments {
		fmt.Fscan(in, &monuments[i].x, &monuments[i].y)
	}
	dist := make([][]float64, n)
	for i := range dist {
		dist[i] = make([]float64, n)
		for j := range dist[i] {
			dist[i][j] = math.Hypot(float64(towers[i].x-towers[j].x), float64(towers[i].y-towers[j].y))
		}
	}
	best := math.Inf(1)
	if m == 0 {
		// any convex border contains a triangle of its towers that is not
		// longer, so the best border is the shortest triangle with an area
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				for k := j + 1; k < n; k++ {
					if cross(towers[i], towers[j], towers[k]) != 0 {
						best = math.Min(best, dist[i][j]+dist[j][k]+dist[k][i])
					}
				}
			}
		}
	} else {
		// the border goes clockwise, so the inside is on the right of every
		// side: a side i -> j may be used when all monuments are strictly right
		ok := make([][]bool, n)
		for i := range ok {
			ok[i] = make([]bool, n)
			for j := range ok[i] {
				if i == j {
					continue
				}
				all := true
				for _, p := range monuments {
					if cross(towers[i], towers[j], p) >= 0 {
						all = false
						break
					}
				}
				ok[i][j] = all
			}
		}
		// a monument inside rules out degenerate borders; from every first
		// tower, the shortest way around through towers in their order
		for s := 0; s < n; s++ {
			way := make([]float64, n)
			for i := range way {
				way[i] = math.Inf(1)
			}
			way[s] = 0
			for step := 1; step < n; step++ {
				k := (s + step) % n
				for back := 0; back < step; back++ {
					j := (s + back) % n
					if ok[j][k] {
						way[k] = math.Min(way[k], way[j]+dist[j][k])
					}
				}
				if ok[k][s] {
					best = math.Min(best, way[k]+dist[k][s])
				}
			}
		}
	}
	fmt.Printf("%.2f\n", best)
}
