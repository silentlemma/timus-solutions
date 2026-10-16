package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// joining i and j whenever i + j > n gives student i a degree of i up to
	// the middle and i - 1 after it, so only one degree is shared, by two
	var pairs [][2]int
	for i := 1; i <= n; i++ {
		for j := i + 1; j <= n; j++ {
			if i+j > n {
				pairs = append(pairs, [2]int{i, j})
			}
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fprintln(writer, len(pairs))
	for _, p := range pairs {
		fmt.Fprintln(writer, p[0], p[1])
	}
}
