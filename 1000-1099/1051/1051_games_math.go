package main

import "fmt"

// three stones in a row can be cleared down to one, which settles the 2D case
const group = 3

func main() {
	var m, n int
	fmt.Scan(&m, &n)
	if m > n {
		m, n = n, m
	}
	switch {
	case m == 1:
		fmt.Println((n + 1) / 2)
	case m%group == 0 || n%group == 0:
		fmt.Println(2)
	default:
		fmt.Println(1)
	}
}
