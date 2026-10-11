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
	from, to := make([]int, m), make([]int, m)
	for i := 0; i < m; i++ {
		fmt.Fscan(in, &from[i], &to[i])
	}
	place := make([]int, n+1)
	for i := 0; i < n; i++ {
		var subject int
		fmt.Fscan(in, &subject)
		place[subject] = i
	}
	// the plan is right exactly when every rule points forward in it; a
	// rule from a subject to itself can never hold
	for i := 0; i < m; i++ {
		if place[from[i]] >= place[to[i]] {
			fmt.Println("NO")
			return
		}
	}
	fmt.Println("YES")
}
