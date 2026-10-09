package main

import "fmt"

func main() {
	var n int
	var marks string
	fmt.Scan(&n, &marks)
	k := len(marks)
	// multiply n, n - k, ... while the factor stays positive
	product := 1
	for factor := n; factor > 0; factor -= k {
		product *= factor
	}
	fmt.Println(product)
}
