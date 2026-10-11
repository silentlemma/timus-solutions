package main

import (
	"bufio"
	"fmt"
	"os"
)

const many = 2

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var weight, n int
	fmt.Fscan(in, &weight, &n)
	card := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &card[i])
	}
	// ways[i][s]: how many sets of the first i cards weigh s, counted up to 2
	ways := make([][]uint8, n+1)
	ways[0] = make([]uint8, weight+1)
	ways[0][0] = 1
	for i := 1; i <= n; i++ {
		ways[i] = append([]uint8(nil), ways[i-1]...)
		for s := card[i]; s <= weight; s++ {
			if c := ways[i][s] + ways[i-1][s-card[i]]; c < many {
				ways[i][s] = c
			} else {
				ways[i][s] = many
			}
		}
	}
	switch ways[n][weight] {
	case 0:
		fmt.Fprintln(out, 0)
		return
	case many:
		fmt.Fprintln(out, -1)
		return
	}
	// the only set: card i is in it exactly when the rest cannot be made
	// from the cards before it
	missing := make([]bool, n+1)
	for i, s := n, weight; i >= 1; i-- {
		if ways[i-1][s] == 1 {
			missing[i] = true
		} else {
			s -= card[i]
		}
	}
	first := true
	for i := 1; i <= n; i++ {
		if missing[i] {
			if !first {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, i)
			first = false
		}
	}
	fmt.Fprintln(out)
}
