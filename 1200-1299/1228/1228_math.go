package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var s int64
	fmt.Fscan(in, &n, &s)
	// each factor is the next one times the size of the next dimension, and
	// the first one times the size of the first dimension is the whole array
	sizes := make([]int64, n+1)
	sizes[0] = s
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &sizes[i])
	}
	for i := 0; i < n; i++ {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(sizes[i]/sizes[i+1] - 1)
	}
	fmt.Println()
}
