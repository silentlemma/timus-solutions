package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const dimensions = 3
const radius int64 = 100

type intVector [dimensions]int64
type vector [dimensions]float64

func dot(a, b intVector) int64 {
	var result int64
	for i := range a {
		result += a[i] * b[i]
	}
	return result
}

func cross(a, b intVector) intVector {
	return intVector{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}

func area(points [dimensions]intVector) float64 {
	var first, second intVector
	for i := range first {
		first[i] = points[1][i] - points[0][i]
		second[i] = points[2][i] - points[0][i]
	}
	normal := cross(first, second)
	normSquared, offset := dot(normal, normal), dot(normal, points[0])
	residual := radius*radius*normSquared - offset*offset
	if residual <= 0 {
		return 0
	}
	radiusSquared := float64(residual) / float64(normSquared)
	var axis, unitNormal vector
	for i := range axis {
		axis[i] = float64(first[i]) / math.Sqrt(float64(dot(first, first)))
		unitNormal[i] = float64(normal[i]) / math.Sqrt(float64(normSquared))
	}
	other := vector{unitNormal[1]*axis[2] - unitNormal[2]*axis[1],
		unitNormal[2]*axis[0] - unitNormal[0]*axis[2], unitNormal[0]*axis[1] - unitNormal[1]*axis[0]}
	var projected [dimensions][2]float64
	for i, p := range points {
		for j := range p {
			projected[i][0] += float64(p[j]) * axis[j]
			projected[i][1] += float64(p[j]) * other[j]
		}
	}
	total := 0.0
	for i, p := range points {
		following := (i + 1) % dimensions
		var delta intVector
		for j := range delta {
			delta[j] = points[following][j] - p[j]
		}
		quadratic, linear, constant := dot(delta, delta), dot(p, delta), dot(p, p)-radius*radius
		discriminant := linear*linear - quadratic*constant
		cuts := []float64{0, 1}
		low, high := 1.0, 0.0
		if discriminant > 0 {
			stable := -float64(linear) - math.Copysign(math.Sqrt(float64(discriminant)), float64(linear))
			low, high = stable/float64(quadratic), float64(constant)/stable
			if low > high {
				low, high = high, low
			}
			if low > 0 && low < 1 {
				cuts = append(cuts, low)
			}
			if high > 0 && high < 1 {
				cuts = append(cuts, high)
			}
		}
		sort.Float64s(cuts)
		x, y := projected[i][0], projected[i][1]
		dx, dy := projected[following][0]-x, projected[following][1]-y
		for j := 1; j < len(cuts); j++ {
			left, right := cuts[j-1], cuts[j]
			ax, ay := x+left*dx, y+left*dy
			bx, by := x+right*dx, y+right*dy
			signed := ax*by - ay*bx
			middle := (left + right) / 2
			if low < middle && middle < high {
				total += signed
			} else {
				total += radiusSquared * math.Atan2(signed, ax*bx+ay*by)
			}
		}
	}
	return math.Abs(total) / 2
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var points [dimensions]intVector
	for i := range points {
		for j := range points[i] {
			fmt.Fscan(in, &points[i][j])
		}
	}
	fmt.Printf("%.10f\n", area(points))
}
