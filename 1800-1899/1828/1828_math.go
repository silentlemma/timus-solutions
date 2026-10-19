package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int64
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	// least squares line through the points (i, a_i), i = 0 .. n - 1:
	// the normal equations give the step and then the first term
	sumX := n * (n - 1) / 2
	var sumXX, sumA, sumXA int64
	for i := int64(0); i < n; i++ {
		var v int64
		fmt.Fscan(in, &v)
		sumXX += i * i
		sumA += v
		sumXA += i * v
	}
	step := float64(n*sumXA-sumX*sumA) / float64(n*sumXX-sumX*sumX)
	first := (float64(sumA) - step*float64(sumX)) / float64(n)
	fmt.Printf("%.9f %.9f\n", first, step)
}
