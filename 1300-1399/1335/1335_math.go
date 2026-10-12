package main

import "fmt"

func main() {
	var n int64
	fmt.Scan(&n)
	// modulo n^2 + 1 the first number is -1 and the second is n, so the sum
	// of their squares is 1 + n^2, a multiple of n^2 + 1
	fmt.Println(n*n, n*n+n+1, n*n+1)
}
