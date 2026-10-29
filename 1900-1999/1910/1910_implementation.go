package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([]int, n)
	for i := range a {
		fmt.Fscan(in, &a[i])
	}
	// try every section as the middle of the three
	best, middle := 0, 0
	for i := 1; i+1 < n; i++ {
		sum := a[i-1] + a[i] + a[i+1]
		if sum > best {
			best, middle = sum, i
		}
	}
	fmt.Println(best, middle+1)
}
