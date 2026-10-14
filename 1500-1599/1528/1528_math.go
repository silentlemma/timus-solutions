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
	// g(n) = n by induction, so f(n) = 1 + sum of i f(i) = n f(n - 1) = n!
	for {
		var n, p int64
		if _, err := fmt.Fscan(in, &n, &p); err != nil || (n == 0 && p == 0) {
			return
		}
		r := int64(1)
		if n >= p {
			r = 0 // p itself is a factor of n!
		}
		for i := int64(2); i <= n && r != 0; i++ {
			r = r * i % p
		}
		fmt.Fprintln(out, r)
	}
}
