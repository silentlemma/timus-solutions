package main

import (
	"bufio"
	"fmt"
	"os"
)

const players = 3

func main() {
	reader := bufio.NewReader(os.Stdin)
	own := make([][]int, players)
	for p := range own {
		var n int
		fmt.Fscan(reader, &n)
		own[p] = make([]int, n)
		for i := range own[p] {
			fmt.Fscan(reader, &own[p][i])
		}
	}
	// walk the three sorted lists together, always moving past the
	// smallest current number
	at := make([]int, players)
	common := 0
	for {
		done := false
		for p := 0; p < players; p++ {
			done = done || at[p] == len(own[p])
		}
		if done {
			break
		}
		low, high := own[0][at[0]], own[0][at[0]]
		for p := 1; p < players; p++ {
			v := own[p][at[p]]
			if v < low {
				low = v
			}
			if v > high {
				high = v
			}
		}
		if low == high {
			common++
		}
		for p := 0; p < players; p++ {
			if own[p][at[p]] == low {
				at[p]++
			}
		}
	}
	fmt.Println(common)
}
