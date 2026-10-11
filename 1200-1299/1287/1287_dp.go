package main

import (
	"bufio"
	"fmt"
	"os"
)

func max(values ...int) int {
	m := values[0]
	for _, v := range values {
		if v > m {
			m = v
		}
	}
	return m
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	var prev, row string
	// runs ending at each cell of the previous and current row, going
	// down, down-right and down-left
	down, right, left := make([]int, n), make([]int, n), make([]int, n)
	down2, right2, left2 := make([]int, n), make([]int, n), make([]int, n)
	var best [2]int // longest runs of s and of S
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &row)
		across := 0
		for j := 0; j < n; j++ {
			c := row[j]
			if j > 0 && row[j-1] == c {
				across++
			} else {
				across = 1
			}
			down2[j], right2[j], left2[j] = 1, 1, 1
			if i > 0 && prev[j] == c {
				down2[j] = down[j] + 1
			}
			if i > 0 && j > 0 && prev[j-1] == c {
				right2[j] = right[j-1] + 1
			}
			if i > 0 && j+1 < n && prev[j+1] == c {
				left2[j] = left[j+1] + 1
			}
			k := 0
			if c == 'S' {
				k = 1
			}
			best[k] = max(best[k], across, down2[j], right2[j], left2[j])
		}
		down, down2 = down2, down
		right, right2 = right2, right
		left, left2 = left2, left
		prev = row
	}
	switch {
	case best[0] > best[1]:
		fmt.Println("s")
	case best[1] > best[0]:
		fmt.Println("S")
	default:
		fmt.Println("?")
	}
	fmt.Println(max(best[0], best[1]))
}
