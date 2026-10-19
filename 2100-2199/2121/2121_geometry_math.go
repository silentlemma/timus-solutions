package main

import "fmt"

const sideFactor = 4 // the area is 4a - 1/3

func main() {
	var a uint64
	fmt.Scan(&a)
	// 4a - 1/3 = (4a - 1) + 2/3, and 2/3 rounds to 0.6666666667
	fmt.Printf("%d.6666666667\n", sideFactor*a-1)
}
