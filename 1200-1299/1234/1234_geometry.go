package main

import (
	"fmt"
	"math"
	"sort"
)

const (
	tenths     = 10
	brickSides = 3
	holeSides  = 2
)

// fits tells whether a p x q rectangle (p >= q) fits into an a x b one (a >= b):
// a turned fit (p > a, q <= b) needs ((a+b)/(p+q))^2 + ((a-b)/(p-q))^2 >= 2
// by Carver's criterion, multiplied out here to stay in integers
func fits(p, q, a, b int64) bool {
	if q > b {
		return false
	}
	if p <= a {
		return true
	}
	s, d := (p+q)*(p+q), (p-q)*(p-q)
	return (a+b)*(a+b)*d+(a-b)*(a-b)*s >= 2*s*d
}

func main() {
	v := make([]int64, brickSides+holeSides)
	for i := range v {
		var x float64
		fmt.Scan(&x)
		v[i] = int64(math.Round(x * tenths))
	}
	brick, hole := v[:brickSides], v[brickSides:]
	sort.Slice(brick, func(i, j int) bool { return brick[i] < brick[j] })
	sort.Slice(hole, func(i, j int) bool { return hole[i] < hole[j] })
	// the face of the two shorter sides is the easiest to put through
	if fits(brick[1], brick[0], hole[1], hole[0]) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
