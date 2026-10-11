package main

import "fmt"

const dwarfs = 7

func main() {
	var digits string
	fmt.Scan(&digits)
	// the number has up to 51 digits, so take it modulo 7 digit by digit
	rest := 0
	for _, d := range digits {
		rest = (rest*10 + int(d-'0')) % dwarfs
	}
	fmt.Println(rest)
}
