package main

import (
	"fmt"
	"math"
)

// area common to discs of radii a and b with centres d apart
func lens(d, a, b int64) float64 {
	if d >= a+b {
		return 0
	}
	small, gap := a, a-b
	if b < a {
		small = b
	} else {
		gap = b - a
	}
	if d <= gap {
		return math.Pi * float64(small*small)
	}
	fd, fa, fb := float64(d), float64(a), float64(b)
	// half-angles seen from each centre, by the law of cosines
	alpha := math.Acos(float64(d*d+a*a-b*b) / (2 * fd * fa))
	beta := math.Acos(float64(d*d+b*b-a*a) / (2 * fd * fb))
	// the kite between both centres and the two crossing points
	kite := math.Sqrt(float64(-d+a+b)*float64(d+a-b)*float64(d-a+b)*float64(d+a+b)) / 2
	return fa*fa*alpha + fb*fb*beta - kite
}

func main() {
	var d, r1, big1, r2, big2 int64
	if _, err := fmt.Scan(&d, &r1, &big1, &r2, &big2); err != nil {
		return
	}
	ring1 := math.Pi * float64(big1*big1-r1*r1)
	ring2 := math.Pi * float64(big2*big2-r2*r2)
	// a ring is a disc minus a smaller one, so their overlap follows by
	// inclusion and exclusion over the four pairs of discs
	common := lens(d, big1, big2) - lens(d, r1, big2) - lens(d, big1, r2) + lens(d, r1, r2)
	fmt.Printf("%.6f\n", ring1+ring2-common)
}
