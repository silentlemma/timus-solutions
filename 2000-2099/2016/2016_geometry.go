package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const dimensions = 3
const circles = 3
const periodShifts = 2
const tau = 2 * math.Pi

type vector [dimensions]float64

func add(a, b vector) vector {
	for i := range a {
		a[i] += b[i]
	}
	return a
}
func sub(a, b vector) vector {
	for i := range a {
		a[i] -= b[i]
	}
	return a
}
func scale(a vector, value float64) vector {
	for i := range a {
		a[i] *= value
	}
	return a
}
func sumThree(a, b, c float64) float64 {
	sum, correction := 0.0, 0.0
	for _, value := range (vector{a, b, c}) {
		next := sum + value
		if math.Abs(sum) >= math.Abs(value) {
			correction += (sum - next) + value
		} else {
			correction += (value - next) + sum
		}
		sum = next
	}
	return sum + correction
}
func dot(a, b vector) float64 { return sumThree(a[0]*b[0], a[1]*b[1], a[2]*b[2]) }
func cross(a, b vector) vector {
	return vector{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}
func unit(a vector) (vector, float64) {
	length := math.Sqrt(dot(a, a))
	return scale(a, 1/length), length
}
func above(center vector, radius float64, radial, tangent vector, angle, height float64) float64 {
	amplitude := radius * math.Hypot(radial[2], tangent[2])
	if amplitude == 0 {
		if center[2] >= height {
			return radius * angle
		}
		return 0
	}
	ratio := (height - center[2]) / amplitude
	if ratio <= -1 {
		return radius * angle
	}
	if ratio >= 1 {
		return 0
	}
	half, phase, measure := math.Acos(ratio), math.Atan2(tangent[2], radial[2]), 0.0
	for shift := -periodShifts; shift <= periodShifts; shift++ {
		left, right := phase-half+float64(shift)*tau, phase+half+float64(shift)*tau
		measure += math.Max(0, math.Min(angle, right)-math.Max(0, left))
	}
	return radius * measure
}
func solve(speed, acceleration int, centers [circles]vector) float64 {
	start := scale(centers[0], -1)
	squared := dot(start, start)
	radial, radius := unit(start)
	raw := vector{-centers[0][1], centers[0][0], 0}
	tangent, _ := unit(cross(raw, radial))
	height, answer := float64(speed)*float64(speed)/float64(2*acceleration), 0.0
	for i := 0; i < circles; i++ {
		angle := tau
		var relative, normal, toward vector
		rho, distance := 0.0, 0.0
		if i+1 < circles {
			relative = sub(centers[i+1], centers[i])
			var normalLength, crossLength float64
			normal, normalLength = unit(raw)
			var direction vector
			direction, crossLength = unit(cross(raw, relative))
			toward, _ = unit(cross(direction, normal))
			rho = crossLength / normalLength
			distance = dot(relative, raw) / normalLength
			angle = math.Atan2(dot(toward, tangent), dot(toward, radial))
			if angle <= 0 {
				angle += tau
			}
		}
		answer += above(centers[i], radius, radial, tangent, angle, height)
		if i+1 < circles {
			difference := sumThree(squared, -dot(relative, relative), distance*distance)
			delta := difference / (radius + rho)
			radius = math.Hypot(delta, distance)
			radial = scale(sub(scale(toward, delta), scale(normal, distance)), 1/radius)
			squared = sumThree(delta*delta, distance*distance, 0)
			if distance == 0 {
				if delta < 0 {
					raw = scale(raw, -1)
				}
			} else {
				raw = add(scale(normal, delta), scale(toward, distance))
			}
			tangent, _ = unit(cross(raw, radial))
		}
	}
	return answer
}
func main() {
	in, out := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var count int
	fmt.Fscan(in, &count)
	for ; count > 0; count-- {
		var speed, acceleration int
		fmt.Fscan(in, &speed, &acceleration)
		var centers [circles]vector
		for i := range centers {
			for j := range centers[i] {
				fmt.Fscan(in, &centers[i][j])
			}
		}
		fmt.Fprintf(out, "%.12f\n", solve(speed, acceleration, centers))
	}
}
