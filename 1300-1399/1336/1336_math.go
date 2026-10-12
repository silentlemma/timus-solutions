package main

import "fmt"

func main() {
	var n int64
	fmt.Scan(&n)
	// (n^2)^2 = n^4 = n^3 * n
	fmt.Println(n * n)
	fmt.Println(n)
}
