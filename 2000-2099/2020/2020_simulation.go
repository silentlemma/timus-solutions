package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(south, north string) int {
	i, j, elapsed := 0, 0, 0
	for i < len(south) && j < len(north) {
		a, b := south[i], north[j]
		goA := a != 'L' || b == 'L'
		goB := b != 'L' || a == 'L'
		if goA {
			i++
		}
		if goB {
			j++
		}
		elapsed++
	}
	return elapsed + len(south) - i + len(north) - j
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var south, north string
	fmt.Fscan(in, &south, &north)
	fmt.Println(solve(south, north))
}
