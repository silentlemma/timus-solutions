package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, k int
	fmt.Fscan(in, &n, &k)
	nums := make([]int, n)
	for i := range nums {
		fmt.Fscan(in, &nums[i])
	}
	height := (n + k - 1) / k // the fewest rows that hold n numbers in k columns
	for row := 0; row < height; row++ {
		// column c holds the numbers c * height ... c * height + height - 1
		for c := 0; c < k && c*height+row < n; c++ {
			fmt.Fprintf(out, "%4d", nums[c*height+row])
		}
		fmt.Fprintln(out)
	}
}
