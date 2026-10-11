package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var n int
	fmt.Scan(&n)
	half := n / 2
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// 1 + 9 k^2 with k = 11...1 (half ones), and 9 k^2 = k 10^half - k
	switch half {
	case 0:
		fmt.Fprintln(out, "1")
	case 1:
		fmt.Fprintln(out, "10")
	default:
		fmt.Fprintln(out, strings.Repeat("1", half-1)+"0"+strings.Repeat("8", half-2)+"90")
	}
}
