package main

import "fmt"

const split = 3

func main() {
	var digits string
	fmt.Scan(&digits)
	// no power of two is divisible by 3, so from a multiple of 3 every move
	// leaves a non-multiple, and from a non-multiple taking 1 or 2 stones
	// leaves a multiple; the remainder is also the smallest such move
	rest := 0
	for _, c := range digits {
		rest = (rest + int(c-'0')) % split
	}
	if rest == 0 {
		fmt.Println(2)
	} else {
		fmt.Println(1)
		fmt.Println(rest)
	}
}
