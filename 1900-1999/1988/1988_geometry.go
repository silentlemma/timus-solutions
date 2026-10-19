package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const dimensions = 3
const iterations = 80

type vector [dimensions]int64

func dot(a, b vector) int64 {
	var total int64
	for i := range a {
		total += a[i] * b[i]
	}
	return total
}

func meetingTime(carrier, ship vector, speed float64) float64 {
	radiusSquared, distanceSquared := dot(carrier, carrier), dot(ship, ship)
	radius, distance := math.Sqrt(float64(radiusSquared)), math.Sqrt(float64(distanceSquared))
	delta := distanceSquared - radiusSquared
	tangent, radialGap := math.Sqrt(float64(delta)), float64(delta)/(distance+radius)
	cross := vector{carrier[1]*ship[2] - carrier[2]*ship[1],
		carrier[2]*ship[0] - carrier[0]*ship[2], carrier[0]*ship[1] - carrier[1]*ship[0]}
	angle := math.Atan2(math.Sqrt(float64(dot(cross, cross))), float64(dot(carrier, ship)))
	visibleAngle := math.Atan2(tangent, radius)
	shipLength := func(beta float64) float64 {
		if beta <= visibleAngle {
			sideways := 2 * math.Sqrt(distance*radius) * math.Sin(beta/2)
			return math.Hypot(radialGap, sideways)
		}
		return tangent + radius*(beta-visibleAngle)
	}
	radialTime := radialGap / speed
	if radius*angle <= radialTime {
		return radialTime
	}
	low, high := 0.0, angle
	for step := 0; step < iterations; step++ {
		beta := (low + high) / 2
		if radius*(angle-beta) > shipLength(beta)/speed {
			low = beta
		} else {
			high = beta
		}
	}
	beta := (low + high) / 2
	return math.Max(radius*(angle-beta), shipLength(beta)/speed)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var carrier, ship vector
	for i := range carrier {
		fmt.Fscan(in, &carrier[i])
	}
	for i := range ship {
		fmt.Fscan(in, &ship[i])
	}
	var speed float64
	fmt.Fscan(in, &speed)
	fmt.Printf("%.10f\n", meetingTime(carrier, ship, speed))
}
