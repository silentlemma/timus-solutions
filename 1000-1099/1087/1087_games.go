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
	moves := make([]int, m)
	for i := range moves {
		fmt.Fscan(in, &moves[i])
	}
	// win[x]: the player to move with x stones left wins; with none left the
	// other player has just taken the last stone and lost
	win := make([]bool, n+1)
	win[0] = true
	for x := 1; x <= n; x++ {
		for _, k := range moves {
			if k <= x && !win[x-k] {
				win[x] = true
			}
		}
	}
	if win[n] {
		fmt.Println(1)
	} else {
		fmt.Println(2)
	}
}
