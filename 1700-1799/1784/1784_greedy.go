package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	piles = 4
	ranks = 13
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var suits [piles][ranks]byte
	for i := 0; i < piles; i++ {
		for j := 0; j < ranks; j++ {
			var card string
			if _, err := fmt.Fscan(reader, &card); err != nil {
				return
			}
			suits[i][j] = card[len(card)-1]
		}
	}
	moves := 0
	for level := 0; level+1 < ranks; level++ {
		// once the cards above level j sit in one-suit runs, the run ending
		// at level j of pile i must go onto the card one rank lower in its
		// suit, which lies at level j + 1 of pile target[i]
		holder := map[byte]int{}
		for k := 0; k < piles; k++ {
			holder[suits[k][level+1]] = k
		}
		var target [piles]int
		for i := 0; i < piles; i++ {
			target[i] = holder[suits[i][level]]
		}
		// every pile with a change of suit here needs one move, and each
		// cycle of such piles needs one more, to a new pile and back
		var seen [piles]bool
		for i := 0; i < piles; i++ {
			if target[i] == i || seen[i] {
				continue
			}
			moves++
			for k := i; !seen[k]; k = target[k] {
				seen[k] = true
				moves++
			}
		}
	}
	fmt.Println(moves)
}
