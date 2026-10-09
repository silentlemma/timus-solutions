package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	// the numbers between 1 and N form one interval whichever side N is on,
	// and its sum is the count times the average of the ends
	count := n - 1
	if count < 0 {
		count = -count
	}
	count++
	fmt.Println((1 + n) * count / 2)
}
