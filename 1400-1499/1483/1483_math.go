package main

import "fmt"

const win = 3

func main() {
	var n int
	fmt.Scan(&n)
	// every match gives out at least 2 points (a draw) and at most win,
	// so the leader has at least the average of all draws and the last team
	// at most the average of all wins; both bounds can be reached
	fmt.Println(n-1, win*(n-1)/2)
}
