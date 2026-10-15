package main

import (
	"bufio"
	"fmt"
	"os"
)

const shares = 3 // a bill is split three ways

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, total int64
	var m int
	fmt.Fscan(in, &n, &m)
	for i := 1; i <= m; i++ {
		var bill int64
		fmt.Fscan(in, &bill)
		total += bill
		// Vanya's share total / 3 exceeds n exactly when total > 3n
		if total > shares*n {
			fmt.Printf("Free after %d times.\n", i)
			return
		}
	}
	fmt.Println("Team.GOV!")
}
