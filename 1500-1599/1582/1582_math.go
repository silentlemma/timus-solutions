package main

import (
	"fmt"
	"math"
)

const (
	total    = 1000
	half     = 0.5
	outcomes = 3
)

func main() {
	inverse := 0.0
	for i := 0; i < outcomes; i++ {
		var k float64
		fmt.Scan(&k)
		inverse += 1 / k
	}
	// betting in proportion to 1 / k on every outcome pays the same whatever
	// happens, and any other split pays less on some outcome
	fmt.Println(int64(math.Floor(total/inverse + half)))
}
