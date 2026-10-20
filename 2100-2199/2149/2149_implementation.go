package main

import "fmt"

const step = 5 // four characters of a pigeon and a separating column

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var n int
	var top string
	fmt.Scan(&n, &top)
	// halves counts the pigeons that break the pattern with the left half looking
	// left, parity those that break the pattern with even positions looking left,
	// and the two opposite patterns break exactly at the other pigeons
	halves, parity := 0, 0
	for i := 0; i < n; i++ {
		left := top[i*step] == '<'
		if left != (i < n/2) {
			halves++
		}
		if left != (i%2 == 0) {
			parity++
		}
	}
	fmt.Println(min(min(halves, n-halves), min(parity, n-parity)))
}
