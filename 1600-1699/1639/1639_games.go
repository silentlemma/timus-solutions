package main

import "fmt"

func main() {
	var m, n int
	if _, err := fmt.Scan(&m, &n); err != nil {
		return
	}
	// every break adds one piece, so the game always lasts m * n - 1 moves
	if (m*n-1)%2 == 1 {
		fmt.Println("[:=[first]")
	} else {
		fmt.Println("[second]=:]")
	}
}
