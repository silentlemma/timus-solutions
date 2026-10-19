package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type point struct{ x, y int64 }
type direction struct {
	key   float64
	x, y  int64
	other int
}

func minimumDistance(points []point) float64 {
	best := math.Inf(1)
	directions := make([]direction, 0, len(points))
	for pivot := 0; pivot+1 < len(points); pivot++ {
		directions = directions[:0]
		var totalX, totalY int64
		for other, p := range points {
			dx, dy := p.x-points[pivot].x, p.y-points[pivot].y
			if dx == 0 && dy == 0 {
				continue
			}
			if dy < 0 || (dy == 0 && dx < 0) {
				dx, dy = -dx, -dy
			}
			ax := dx
			if ax < 0 {
				ax = -ax
			}
			directions = append(directions, direction{-float64(dx) / float64(ax+dy), dx, dy, other})
			totalX += dx
			totalY += dy
		}
		sort.Slice(directions, func(i, j int) bool { return directions[i].key < directions[j].key })
		for _, d := range directions {
			if d.other > pivot {
				numerator := d.x*totalY - d.y*totalX
				if numerator == 0 {
					return 0
				}
				value := float64(numerator) / math.Sqrt(float64(d.x*d.x+d.y*d.y))
				if value < best {
					best = value
				}
			}
			totalX -= 2 * d.x
			totalY -= 2 * d.y
		}
	}
	if math.IsInf(best, 1) {
		return 0
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	points := make([]point, n)
	for i := range points {
		fmt.Fscan(in, &points[i].x, &points[i].y)
	}
	fmt.Fprintf(out, "%.12f\n", minimumDistance(points))
}
