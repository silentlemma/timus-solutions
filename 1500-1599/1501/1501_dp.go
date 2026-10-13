package main

import (
	"bufio"
	"fmt"
	"os"
)

func balance(pile string) []int {
	d := make([]int, len(pile)+1)
	for i := range pile {
		if pile[i] == '1' {
			d[i+1] = d[i] + 1
		} else {
			d[i+1] = d[i] - 1
		}
	}
	return d
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	var a, b string
	fmt.Fscan(reader, &n, &a, &b)
	// after taking i cards of the first pile and j of the second, the red and
	// the black piles differ by d1[i] + d2[j], where d = 2 * reds - taken
	d1, d2 := balance(a), balance(b)
	// reach[i][j]: the state is allowed and comes from (i - 1, j) or (i, j - 1)
	reach := make([][]bool, n+1)
	for i := 0; i <= n; i++ {
		reach[i] = make([]bool, n+1)
		for j := 0; j <= n; j++ {
			if s := d1[i] + d2[j]; s > 1 || s < -1 {
				continue
			}
			reach[i][j] = (i == 0 && j == 0) || (i > 0 && reach[i-1][j]) || (j > 0 && reach[i][j-1])
		}
	}
	if !reach[n][n] {
		fmt.Println("Impossible")
		return
	}
	// walk back from (n, n): a step left took a card of the second pile
	moves := make([]byte, 0, 2*n)
	for i, j := n, n; i > 0 || j > 0; {
		if j > 0 && reach[i][j-1] {
			moves = append(moves, '2')
			j--
		} else {
			moves = append(moves, '1')
			i--
		}
	}
	for x, y := 0, len(moves)-1; x < y; x, y = x+1, y-1 {
		moves[x], moves[y] = moves[y], moves[x]
	}
	fmt.Println(string(moves))
}
