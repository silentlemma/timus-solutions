package main

import (
	"bufio"
	"fmt"
	"os"
)

const forbiddenChoices int64 = 3

func count(n int64) (int64, int64) {
	if n%2 != 0 {
		size := (n - forbiddenChoices) / 2
		if size >= 2 {
			return n * size, 0
		}
		return 0, 0
	}
	half := n / 2
	first, second := half-1, half-2
	if first < 2 {
		first = 0
	}
	if second < 2 {
		second = 0
	}
	return half * (first + second), half * (n - forbiddenChoices)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int64
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	parallel, perpendicular := count(n)
	fmt.Fprintln(out, parallel, perpendicular)
}
