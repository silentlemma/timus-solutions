package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var m, n int
	fmt.Fscan(in, &m, &n)
	parent := make([]int, m)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	// a piece of colour c in box b is an edge b -> c; every box has n pieces
	// and should get n back, so each connected group of boxes is an Euler
	// circuit, walked one carried piece per move
	moves := 0
	touched := make([]bool, m)
	for box := 0; box < m; box++ {
		for k := 0; k < n; k++ {
			var colour int
			fmt.Fscan(in, &colour)
			colour--
			if colour != box {
				moves++
				touched[box], touched[colour] = true, true
				parent[find(box)] = find(colour)
			}
		}
	}
	groups := map[int]bool{}
	for x := 0; x < m; x++ {
		if touched[x] {
			groups[find(x)] = true
		}
	}
	// one empty move of the hand between groups
	if moves == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(moves + len(groups) - 1)
	}
}
