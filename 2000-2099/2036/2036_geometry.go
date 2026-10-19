package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const triangle = 3
const corners = 4
const closed = 5

type Point struct{ x, y int64 }

func cross(a, b, p Point) int64     { return (b.x-a.x)*(p.y-a.y) - (b.y-a.y)*(p.x-a.x) }
func sameSum(a, b, c, d Point) bool { return a.x+b.x == c.x+d.x && a.y+b.y == c.y+d.y }
func parallelogram(p []Point) bool {
	return sameSum(p[0], p[1], p[2], p[triangle]) ||
		sameSum(p[0], p[2], p[1], p[triangle]) ||
		sameSum(p[0], p[triangle], p[1], p[2])
}
func solve(points []Point) string {
	n := len(points)
	if n <= triangle {
		return strconv.Itoa(n)
	}
	for i := 0; i < triangle; i++ {
		for j := i + 1; j < triangle; j++ {
			outside := 0
			for _, p := range points {
				if cross(points[i], points[j], p) != 0 {
					outside++
					if outside > 1 {
						break
					}
				}
			}
			if outside <= 1 {
				return strconv.Itoa(n)
			}
		}
	}
	if n == corners {
		if parallelogram(points) {
			return strconv.Itoa(closed)
		}
		return "oo"
	}
	if n == closed {
		for center := range points {
			others := make([]Point, 0, corners)
			var sx, sy int64
			for i, p := range points {
				if i != center {
					others = append(others, p)
					sx += p.x
					sy += p.y
				}
			}
			if parallelogram(others) && sx == corners*points[center].x && sy == corners*points[center].y {
				return strconv.Itoa(closed)
			}
		}
	}
	return "oo"
}
func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	points := make([]Point, n)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
	}
	fmt.Fprintln(out, solve(points))
}
