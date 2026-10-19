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
	// every move adds two heaps, and the game ends when all heaps are ones
	moves := 0
	for i := 0; i < n; i++ {
		var a int
		fmt.Fscan(in, &a)
		moves += (a - 1) / 2
	}
	if moves%2 == 1 {
		fmt.Println("Daenerys")
	} else {
		fmt.Println("Stannis")
	}
}
