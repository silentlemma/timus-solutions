package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const cell = 1e-3 // distinct crossing points are at least this far apart
const same = 1e-4 // two estimates of one point are much closer than this

type key struct{ x, y int64 }

// groups merges the estimates of the points on one circle and returns how
// many estimates each point got
func groups(xs, ys []float64) []int {
	grid := map[key][]int{}
	var sizes []int
	var sx, sy []float64
	for e := range xs {
		x, y := xs[e], ys[e]
		cx, cy := int64(math.Floor(x/cell)), int64(math.Floor(y/cell))
		found := -1
		for gx := cx - 1; gx <= cx+1; gx++ {
			for gy := cy - 1; gy <= cy+1; gy++ {
				for _, p := range grid[key{gx, gy}] {
					if math.Abs(sx[p]-x) < same && math.Abs(sy[p]-y) < same {
						found = p
					}
				}
			}
		}
		if found < 0 {
			grid[key{cx, cy}] = append(grid[key{cx, cy}], len(sizes))
			sizes = append(sizes, 1)
			sx = append(sx, x)
			sy = append(sy, y)
		} else {
			sizes[found]++
		}
	}
	return sizes
}

type circle struct{ x, y, r int64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// a cut made twice is still one cut
	seen := map[circle]bool{}
	var circles []circle
	for i := 0; i < n; i++ {
		var c circle
		fmt.Fscan(in, &c.x, &c.y, &c.r)
		if !seen[c] {
			seen[c] = true
			circles = append(circles, c)
		}
	}
	k := len(circles)
	parent := make([]int, k)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(a int) int {
		for parent[a] != a {
			parent[a] = parent[parent[a]]
			a = parent[a]
		}
		return a
	}
	// the estimates of the crossing points on each circle: one table of all
	// points would not fit in the memory limit
	xs := make([][]float64, k)
	ys := make([][]float64, k)
	for i := 0; i < k; i++ {
		c1 := circles[i]
		for j := i + 1; j < k; j++ {
			c2 := circles[j]
			dx, dy := c2.x-c1.x, c2.y-c1.y
			d2 := dx*dx + dy*dy
			if d2 > (c1.r+c2.r)*(c1.r+c2.r) || d2 < (c1.r-c2.r)*(c1.r-c2.r) {
				continue // apart, or one inside the other
			}
			// the crossings are p1 + (m * (dx, dy) +- sqrt(K) * (-dy, dx)) / (2 d2), K exact
			m := d2 + c1.r*c1.r - c2.r*c2.r
			root := math.Sqrt(float64((2*c1.r)*(2*c1.r)*d2 - m*m))
			for _, sign := range []float64{1, -1} {
				x := float64(c1.x) + (float64(m*dx)-sign*root*float64(dy))/float64(2*d2)
				y := float64(c1.y) + (float64(m*dy)+sign*root*float64(dx))/float64(2*d2)
				for _, c := range []int{i, j} {
					xs[c] = append(xs[c], x)
					ys[c] = append(ys[c], y)
				}
				if root == 0 {
					break
				}
			}
			parent[find(i)] = find(j)
		}
	}
	// a group of s estimates on a circle is a point on s + 1 circles, so it
	// adds 1 / (s + 1) vertex; shared[c] counts such groups for c circles
	edges, components := 0, 0
	shared := map[int]int{}
	for i := 0; i < k; i++ {
		sizes := groups(xs[i], ys[i])
		xs[i], ys[i] = nil, nil
		if len(sizes) == 0 {
			sizes = []int{0} // a circle with no crossings: one vertex, one edge
		}
		edges += len(sizes)
		for _, s := range sizes {
			shared[s+1]++
		}
		if find(i) == i {
			components++
		}
	}
	vertices := 0
	for c, count := range shared {
		vertices += count / c
	}
	// Euler's formula for a plane graph: faces = edges - vertices + components + 1
	fmt.Println(edges - vertices + components + 1)
}
