package main

import "fmt"

const (
	mod   = 9973
	coefX = 3
	coefY = 7
)

// step gives g(x, y) = y (x^5 - x + 7) + (x^3 + 3x - x^5) as the map
// y -> a y + b modulo 9973; it depends only on x mod 9973
func step(x int64) (int64, int64) {
	x3 := x * x % mod * x % mod
	x5 := x3 * x % mod * x % mod
	return ((x5-x+coefY)%mod + mod) % mod, ((x3+coefX*x-x5)%mod + mod) % mod
}

func main() {
	var n int64
	fmt.Scan(&n)
	whole, rest := n/mod, n%mod
	// x = 1 .. 9973 compose into one map, the same for every full period
	bigA, bigB := int64(1), int64(0)
	for x := int64(1); x <= mod; x++ {
		a, b := step(x)
		bigA, bigB = a*bigA%mod, (a*bigB+b)%mod
	}
	y := int64(0)
	for k := int64(0); k < whole; k++ {
		y = (bigA*y + bigB) % mod
	}
	for x := int64(1); x <= rest; x++ {
		a, b := step(x)
		y = (a*y + b) % mod
	}
	fmt.Println(y)
}
