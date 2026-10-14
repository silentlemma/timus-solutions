package main

import "fmt"

const (
	four = 4 // one corner inside: 4 points, one triangle on each side
	five = 5 // two corners inside: 5 points, one triangle per apex
	six  = 6 // three corners inside: 6 points, the three long diagonals
)

func choose(n int64, k int) int64 {
	c := int64(1)
	for i := 1; i <= k; i++ {
		c = c * (n - int64(k) + int64(i)) / int64(i) // stays below C(n, k) * n
	}
	return c
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// a triangle is fixed by the set of chord ends it uses, and a set of
	// k points on the circle gives a fixed number of triangles
	fmt.Println(choose(n, six) + five*choose(n, five) + four*choose(n, four))
}
