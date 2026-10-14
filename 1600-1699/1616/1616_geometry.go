package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	eps      = 1e-9
	half     = 0.5 // a cell goes to an owner who held more than half of it
	letters  = 26
	straight = 180 // degrees in a half turn
	corners  = 4
	triangle = 3 // the fewest corners of a polygon with area
)

type point [2]float64

// clip keeps the part of a convex polygon with coordinate axis >= bound (or <=).
func clip(poly []point, axis int, bound float64, keepAbove bool) []point {
	out := make([]point, 0, len(poly)+corners)
	for i := range poly {
		a, b := poly[i], poly[(i+1)%len(poly)]
		var inA, inB bool
		if keepAbove {
			inA, inB = a[axis] >= bound-eps, b[axis] >= bound-eps
		} else {
			inA, inB = a[axis] <= bound+eps, b[axis] <= bound+eps
		}
		if inA != inB {
			t := (bound - a[axis]) / (b[axis] - a[axis])
			out = append(out, point{a[0] + (b[0]-a[0])*t, a[1] + (b[1]-a[1])*t})
		}
		if inB {
			out = append(out, b)
		}
	}
	return out
}

func area(poly []point) float64 {
	total := 0.0
	for i := range poly {
		a, b := poly[i], poly[(i+1)%len(poly)]
		total += a[0]*b[1] - b[0]*a[1]
	}
	return math.Abs(total) / 2
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	var alpha float64
	if _, err := fmt.Fscan(in, &n, &alpha); err != nil {
		return
	}
	grid := make([]string, 2*n)
	for i := range grid {
		fmt.Fscan(in, &grid[i])
	}
	size := 2 * (2 * n) // the new map covers twice the old side
	// owned area of each new cell, per owner letter
	held := make([][letters]float64, size*size)
	rad := alpha * math.Pi / straight
	cosA, sinA := math.Cos(rad), math.Sin(rad)
	for row := 0; row < 2*n; row++ {
		y := n - 1 - row
		for col := 0; col < 2*n; col++ {
			owner := grid[row][col]
			if owner == '.' {
				continue
			}
			x := col - n
			// the axes turn clockwise, so the cell turns counterclockwise
			cx := [corners]int{x, x + 1, x + 1, x}
			cy := [corners]int{y, y, y + 1, y + 1}
			square := make([]point, corners)
			xLo, xHi, yLo, yHi := math.Inf(1), math.Inf(-1), math.Inf(1), math.Inf(-1)
			for k := range square {
				px, py := float64(cx[k]), float64(cy[k])
				square[k] = point{px*cosA - py*sinA, px*sinA + py*cosA}
				xLo, xHi = math.Min(xLo, square[k][0]), math.Max(xHi, square[k][0])
				yLo, yHi = math.Min(yLo, square[k][1]), math.Max(yHi, square[k][1])
			}
			x0, x1 := maxInt(-2*n, int(math.Floor(xLo+eps))), minInt(2*n, int(math.Ceil(xHi-eps)))
			y0, y1 := maxInt(-2*n, int(math.Floor(yLo+eps))), minInt(2*n, int(math.Ceil(yHi-eps)))
			letter := owner - 'a'
			for gy := y0; gy < y1; gy++ {
				for gx := x0; gx < x1; gx++ {
					part := clip(square, 0, float64(gx), true)
					part = clip(part, 0, float64(gx+1), false)
					part = clip(part, 1, float64(gy), true)
					part = clip(part, 1, float64(gy+1), false)
					if len(part) >= triangle {
						held[(2*n-1-gy)*size+gx+2*n][letter] += area(part)
					}
				}
			}
		}
	}
	line := make([]byte, size)
	for r := 0; r < size; r++ {
		for c := 0; c < size; c++ {
			line[c] = '.'
			for i := 0; i < letters; i++ {
				if held[r*size+c][i] > half+eps {
					line[c] = byte('a' + i)
					break
				}
			}
		}
		out.Write(line)
		out.WriteByte('\n')
	}
}

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}
