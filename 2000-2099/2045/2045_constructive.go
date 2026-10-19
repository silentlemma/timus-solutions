package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const tailPattern = "bcd"

func wordFor(n, count int, tail string) string {
	minimum := len(tailPattern)
	if n < minimum {
		minimum = n
	}
	if count < minimum {
		return "NO"
	}
	if n < len(tailPattern) {
		return strings.Repeat("a", n)
	}
	prefix := count - len(tailPattern)
	return strings.Repeat("a", prefix) + tail[:n-prefix]
}

func solve(n int, out *bufio.Writer) {
	tail := strings.Repeat(tailPattern, (n+len(tailPattern)-1)/len(tailPattern))
	for count := 1; count <= n; count++ {
		fmt.Fprintln(out, count, ":", wordFor(n, count, tail))
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	solve(n, out)
}
