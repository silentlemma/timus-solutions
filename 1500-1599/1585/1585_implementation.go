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
	// every record is two words, the kind and "Penguin"
	seen := map[string]int{}
	best := ""
	for i := 0; i < n; i++ {
		var kind, penguin string
		fmt.Fscan(in, &kind, &penguin)
		seen[kind]++
		if best == "" || seen[kind] > seen[best] {
			best = kind
		}
	}
	fmt.Println(best + " Penguin")
}
