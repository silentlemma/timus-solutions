package main

import "fmt"

func gcd(x, y int64) int64 {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	var n, m int64
	if _, err := fmt.Scan(&n, &m); err != nil {
		return
	}
	a, b := n-1, m-1
	g := gcd(a, b)
	// the walk takes lcm(a, b) steps and turns every tile it passes over, so
	// a tile passed twice ends up white again; in units of g the crossings
	// are the inner points (x, y) with x and y both odd or both even
	steps := a / g * b
	wide, tall := a/g, b/g
	crossings := (wide/2)*(tall/2) + ((wide-1)/2)*((tall-1)/2)
	fmt.Println(steps + 1 - 2*crossings)
}
