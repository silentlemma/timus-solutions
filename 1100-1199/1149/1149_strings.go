package main

import (
	"fmt"
	"strconv"
	"strings"
)

// sine is sin(1-sin(2+sin(3-...sin(n)...))): the sign after k is minus for
// odd k
func sine(n int) string {
	var b strings.Builder
	for k := 1; k <= n; k++ {
		b.WriteString("sin(" + strconv.Itoa(k))
		if k < n {
			if k%2 == 1 {
				b.WriteString("-")
			} else {
				b.WriteString("+")
			}
		}
	}
	b.WriteString(strings.Repeat(")", n))
	return b.String()
}

func main() {
	var n int
	fmt.Scan(&n)
	var out strings.Builder
	out.WriteString(strings.Repeat("(", n-1))
	for i := 1; i <= n; i++ {
		out.WriteString(sine(i) + "+" + strconv.Itoa(n-i+1))
		if i < n {
			out.WriteString(")")
		}
	}
	fmt.Println(out.String())
}
