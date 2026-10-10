package main

import "fmt"

// limit: answers above it are reported as 0
const limit = 10000

func main() {
	var m, n, k int
	fmt.Scan(&m, &n, &k)
	// x tiles make one rectangle per divisor pair a * b = x with a <= b, that
	// is half the number of divisors, rounded up
	divisors := make([]int, limit+1)
	for d := 1; d <= limit; d++ {
		for x := d; x <= limit; x += d {
			divisors[x]++
		}
	}
	shapes := func(x int) int { return (divisors[x] + 1) / 2 }
	for t := k + 1; t <= limit; t++ {
		if shapes(t) == n && shapes(t-k) == m {
			fmt.Println(t)
			return
		}
	}
	fmt.Println(0)
}
