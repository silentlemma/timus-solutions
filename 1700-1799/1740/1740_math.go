package main

import "fmt"

func main() {
	var l, k, h int
	fmt.Scan(&l, &k, &h)
	// the time to reach x is x h / k plus a part that repeats every k km
	// and lies between 0 and h, so the last l mod k km take 0 to h hours
	whole, slowest := l/k, l/k
	if l%k > 0 {
		slowest++
	}
	fmt.Printf("%.8f %.8f\n", float64(whole*h), float64(slowest*h))
}
