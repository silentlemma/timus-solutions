package main

import (
	"fmt"
	"strconv"
)

func main() {
	// read the codes as strings: fmt.Scan would take a leading 0 for octal
	var a, b string
	fmt.Scan(&a, &b)
	first, _ := strconv.Atoi(a)
	second, _ := strconv.Atoi(b)
	// on night k the thief tries code k on lock 1 when k is even and on
	// lock 2 when k is odd
	if first%2 == 0 || second%2 == 1 {
		fmt.Println("yes")
	} else {
		fmt.Println("no")
	}
}
