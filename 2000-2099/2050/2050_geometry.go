package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const dimension = 3
const pointsCount = 4
const axisThreshold = 1900
const axisStep = 2
const angle = 180

type vector [dimension]float64
type answer [2]vector

func dot(a, b vector) float64 {
	total := 0.0
	for i := range a {
		total += a[i] * b[i]
	}
	return total
}

func normalize(a vector) vector {
	length := math.Sqrt(dot(a, a))
	for i := range a {
		a[i] /= length
	}
	return a
}

func axis(middle, displacement, direction, difference vector) answer {
	coefficient := dot(displacement, direction) / (2 * dot(direction, direction))
	var center vector
	unit := normalize(direction)
	for i := range center {
		center[i] = middle[i] + coefficient*difference[i]
	}
	projection := dot(center, unit)
	var result answer
	for i := range center {
		result[0][i] = center[i] - projection*unit[i]
		result[1][i] = result[0][i] + axisStep*unit[i]
	}
	return result
}

func solve(points [pointsCount]vector) answer {
	a, b, c, d := points[0], points[1], points[2], points[pointsCount-1]
	var first, second, middle, displacement, plus, minus vector
	for i := range first {
		first[i], second[i] = b[i]-a[i], d[i]-c[i]
		middle[i], displacement[i] = (a[i]+c[i])/2, c[i]-a[i]
	}
	if dot(first, second) < 0 {
		for i := range second {
			second[i] = -second[i]
		}
	}
	u, v := normalize(first), normalize(second)
	for i := range plus {
		plus[i], minus[i] = u[i]+v[i], u[i]-v[i]
	}
	result := axis(middle, displacement, plus, minus)
	if dot(result[0], result[0]) > axisThreshold*axisThreshold {
		result = axis(middle, displacement, minus, plus)
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var points [pointsCount]vector
	for i := range points {
		for j := range points[i] {
			fmt.Fscan(in, &points[i][j])
		}
	}
	for _, row := range solve(points) {
		fmt.Fprintf(out, "%.15f %.15f %.15f\n", row[0], row[1], row[2])
	}
	fmt.Fprintln(out, angle)
}
