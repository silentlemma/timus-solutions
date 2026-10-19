package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const smallLimit = 7
const stableMin = 8
const extraCount = 6
const period = "babbaa"

func construct(n, count int) string {
	minimum := stableMin
	if n <= smallLimit {
		minimum = n
	} else if n == stableMin {
		minimum = smallLimit
	}
	if count < minimum {
		return "NO"
	}
	if count == n {
		return strings.Repeat("a", n)
	}
	if n == stableMin {
		return "aababbaa"
	}
	run := count - extraCount
	tail := n - run
	return strings.Repeat("a", run) + strings.Repeat(period, (tail+len(period)-1)/len(period))[:tail]
}
func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	for count := 1; count <= n; count++ {
		fmt.Fprintf(out, "%d : %s\n", count, construct(n, count))
	}
}
