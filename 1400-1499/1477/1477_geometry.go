package main

import (
	"bufio"
	"fmt"
	"os"
)

const axes = 3

type vec [axes]int64

func cross(a, b vec) vec {
	return vec{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}

func dot(a, b vec) int64 { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }

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

func max(values ...int) int {
	best := values[0]
	for _, v := range values {
		if v > best {
			best = v
		}
	}
	return best
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	points := make([]vec, n)
	for i := range points {
		fmt.Fscan(reader, &points[i][0], &points[i][1], &points[i][2])
	}

	// every plane through the origin and two non-parallel points, once
	normals := map[vec]bool{}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			c := cross(points[i], points[j])
			g := gcd(gcd(c[0], c[1]), c[2])
			if g == 0 {
				continue
			}
			lead := c[0]
			if lead == 0 {
				lead = c[1]
			}
			if lead == 0 {
				lead = c[2]
			}
			if lead < 0 {
				g = -g
			}
			for k := range c {
				c[k] /= g
			}
			normals[c] = true
		}
	}

	best := 1 // a single airplane is always visible
	for normal := range normals {
		above, below := 0, 0
		var circle []vec
		for _, p := range points {
			s := dot(normal, p)
			if s > 0 {
				above++
			} else if s < 0 {
				below++
			} else {
				circle = append(circle, p)
			}
		}
		// a slight tilt shows the points of the circle in its best open half:
		// its edge passes through one of them, which a tilt adds as well
		half := 0
		for _, z := range circle {
			edge := cross(normal, z)
			ahead, behind := 0, 0
			for _, p := range circle {
				if s := dot(edge, p); s > 0 {
					ahead++
				} else if s < 0 {
					behind++
				}
			}
			half = max(half, ahead+1, behind+1)
		}
		best = max(best, above+half, below+half)
	}
	fmt.Println(best)
}
