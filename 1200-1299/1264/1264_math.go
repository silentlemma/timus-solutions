package main

import "fmt"

func main() {
	var n, m int64
	fmt.Scan(&n, &m)
	// one line for each element and each value 0..M
	fmt.Println(n * (m + 1))
}
