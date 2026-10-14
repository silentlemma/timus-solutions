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
	count := map[string]int{}
	largest := 0
	for i := 0; i < 1<<n; i++ {
		var name, prefecture string
		fmt.Fscan(in, &name, &prefecture)
		count[prefecture]++
		if count[prefecture] > largest {
			largest = count[prefecture]
		}
	}
	// c wrestlers of one prefecture can avoid each other in all rounds but
	// ceil(log2 c) of them, and dealing the wrestlers sorted by prefecture
	// round-robin into that many top-level groups achieves it for all at once
	unsafe := 0
	for 1<<unsafe < largest {
		unsafe++
	}
	fmt.Println(n - unsafe)
}
