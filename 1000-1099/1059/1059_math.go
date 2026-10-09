package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n int
	fmt.Scan(&n)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	// Horner's scheme: ((a0 * X + a1) * X + a2) ... in reverse Polish notation
	fmt.Fprintln(w, 0)
	for i := 1; i <= n; i++ {
		fmt.Fprintf(w, "X\n*\n%d\n+\n", i)
	}
}
