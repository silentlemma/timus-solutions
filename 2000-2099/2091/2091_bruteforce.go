package main

import (
	"bufio"
	"fmt"
	"os"
)

const groups = 4 // both courses, only the first, only the second, neither

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	column := make([][]int, m)
	for j := range column {
		column[j] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(in, &column[j][i])
		}
	}
	best, bestA, bestB := n+1, 0, 0
	// every pair of courses is tried: the four groups of a pair are counted
	// in one pass over the programs
	for a := 0; a < m; a++ {
		for b := a + 1; b < m; b++ {
			var count [groups]int
			for i := 0; i < n; i++ {
				count[2*column[a][i]+column[b][i]]++
			}
			worst := 0
			for _, c := range count {
				if c > worst {
					worst = c
				}
			}
			if worst < best {
				best, bestA, bestB = worst, a+1, b+1
			}
		}
	}
	fmt.Println(best)
	fmt.Println(bestA, bestB)
}
