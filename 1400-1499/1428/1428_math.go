package main

import "fmt"

func main() {
	var a, b, c uint
	fmt.Scan(&a, &b, &c)
	// 2^(C-1) + 2^(C-1) = 2^C, and A and B both divide C - 1
	fmt.Println(int64(1) << ((c - 1) / a))
	fmt.Println(int64(1) << ((c - 1) / b))
	fmt.Println(2)
}
