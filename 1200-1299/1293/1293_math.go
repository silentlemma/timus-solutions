package main

import "fmt"

func main() {
	var n, a, b int64
	fmt.Scan(&n, &a, &b)
	// each panel has two sides of A * B square metres
	fmt.Println(2 * n * a * b)
}
