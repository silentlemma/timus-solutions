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
	// cutting a shorter piece off a longer one keeps the gcd of all lengths,
	// so the last piece is always the gcd and the answer is never ambiguous
	var g int64
	for i := 0; i < n; i++ {
		var length int64
		fmt.Fscan(in, &length)
		for length != 0 {
			g, length = length, g%length
		}
	}
	fmt.Println(g)
}
