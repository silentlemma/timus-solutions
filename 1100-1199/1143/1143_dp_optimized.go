package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const maxCamps = 200
const floatBits = 64
const decimalPlaces = 3

type point struct{ x, y float64 }

func distance(a, b point) float64 {
	x, y := a.x-b.x, a.y-b.y
	return math.Hypot(x, y)
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	read := func() float64 {
		in.Scan()
		value, _ := strconv.ParseFloat(in.Text(), floatBits)
		return value
	}
	var points [maxCamps]point
	var edge, left, right [maxCamps]float64
	for i := 0; i < n; i++ {
		points[i] = point{read(), read()}
	}
	for i := 0; i < n; i++ {
		edge[i] = distance(points[i], points[(i+1)%n])
	}
	for span := 1; span < n; span++ {
		// Preserve the old first arc for the final wraparound update.
		firstLeft, firstRight := left[0], right[0]
		end := span
		for start := 0; start < n; start++ {
			nextLeft, nextRight := firstLeft, firstRight
			if start+1 < n {
				nextLeft, nextRight = left[start+1], right[start+1]
			}
			chord := distance(points[start], points[end])
			beforeEnd := end - 1
			if end == 0 {
				beforeEnd = n - 1
			}
			left[start], right[start] = math.Min(nextLeft+edge[start], nextRight+chord),
				math.Min(left[start]+chord, right[start]+edge[beforeEnd])
			end++
			if end == n {
				end = 0
			}
		}
	}
	best := left[0]
	for i := 0; i < n; i++ {
		best = math.Min(best, math.Min(left[i], right[i]))
	}
	os.Stdout.WriteString(strconv.FormatFloat(best, 'f', decimalPlaces, floatBits) + "\n")
}
