package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	count := make([]int, n+1)
	for i := 0; i < m; i++ {
		var x int
		fmt.Fscan(in, &x)
		count[x]++
	}
	// card k shows k - 1 and k, so the number x fits cards x and x + 1; going
	// up from the smallest number, card x is useless to anything later, so it
	// is taken first
	used := make([]bool, n+2)
	for x := 0; x <= n; x++ {
		for card := x; card <= x+1 && count[x] > 0; card++ {
			if card >= 1 && card <= n && !used[card] {
				used[card] = true
				count[x]--
			}
		}
		if count[x] > 0 {
			fmt.Println("NO")
			return
		}
	}
	fmt.Println("YES")
}
