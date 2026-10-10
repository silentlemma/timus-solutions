package main

import (
	"fmt"
	"math"
	"sort"
)

// steps: halvings of the radius interval, far more than double precision needs
const steps = 200

// angle: the largest area belongs to the polygon inscribed in a circle; a
// side of length l sees the centre at the angle 2 asin(l / 2R)
func angle(length, r float64) float64 {
	return 2 * math.Asin(math.Min(1, length/(2*r)))
}

func sum(v []int, r float64) float64 {
	total := 0.0
	for _, s := range v {
		total += angle(float64(s), r)
	}
	return total
}

func main() {
	var n int
	fmt.Scan(&n)
	sides := make([]int, n)
	for i := range sides {
		fmt.Scan(&sides[i])
	}
	sort.Ints(sides)
	longest, rest := sides[n-1], sides[:n-1]
	others := 0
	for _, s := range rest {
		others += s
	}
	if longest >= others {
		fmt.Println("0.00")
		return
	}
	low := float64(longest) / 2
	inside := sum(sides, low) >= 2*math.Pi
	// with the centre inside, the angles fill the full turn; otherwise the
	// longest side's angle equals the sum of the others
	surplus := func(r float64) float64 {
		if inside {
			return sum(sides, r) - 2*math.Pi
		}
		return angle(float64(longest), r) - sum(rest, r)
	}
	high := low
	for surplus(high) > 0 {
		high *= 2
	}
	for k := 0; k < steps; k++ {
		mid := (low + high) / 2
		if surplus(mid) > 0 {
			low = mid
		} else {
			high = mid
		}
	}
	r := (low + high) / 2
	area := 0.0
	for _, s := range rest {
		area += math.Sin(angle(float64(s), r))
	}
	if inside {
		area += math.Sin(angle(float64(longest), r))
	} else {
		area -= math.Sin(angle(float64(longest), r))
	}
	fmt.Printf("%.2f\n", r*r*area/2)
}
