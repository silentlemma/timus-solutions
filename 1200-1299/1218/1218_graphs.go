package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	params   = 3
	majority = 2
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	names := make([]string, n)
	stats := make([][params]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &names[i])
		for p := 0; p < params; p++ {
			fmt.Fscan(in, &stats[i][p])
		}
	}
	// reach[i][j]: i beats j, directly or through a chain of wins
	reach := make([][]bool, n)
	for i := range reach {
		reach[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			better := 0
			for p := 0; p < params; p++ {
				if stats[i][p] > stats[j][p] {
					better++
				}
			}
			reach[i][j] = i != j && better >= majority
		}
	}
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			if reach[i][k] {
				for j := 0; j < n; j++ {
					reach[i][j] = reach[i][j] || reach[k][j]
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// a Jedi can win when every other one can be beaten along such a chain
	for i := 0; i < n; i++ {
		all := true
		for j := 0; j < n; j++ {
			all = all && (i == j || reach[i][j])
		}
		if all {
			fmt.Fprintln(out, names[i])
		}
	}
}
