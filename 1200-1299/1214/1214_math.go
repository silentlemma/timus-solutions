package main

import "fmt"

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	// each turn of the loop swaps x and y, and there are x + y turns; the
	// sum survives, so an odd sum of positive numbers means one swap
	if x > 0 && y > 0 && (x+y)%2 == 1 {
		x, y = y, x
	}
	fmt.Println(x, y)
}
