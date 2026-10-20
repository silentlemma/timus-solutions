package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	suitCount = 3
	rankCount = 9
	tileTypes = suitCount * rankCount
	handSize  = 14
	groupSize = 3
)

func winning(counts [tileTypes]int) bool {
	pairSuit := suitCount
	for suit := 0; suit < suitCount; suit++ {
		total := 0
		for rank := 0; rank < rankCount; rank++ {
			total += counts[suit*rankCount+rank]
		}
		switch total % groupSize {
		case 0:
		case 2:
			if pairSuit != suitCount {
				return false
			}
			pairSuit = suit
		default:
			return false
		}
	}
	if pairSuit == suitCount {
		return false
	}

	for pair := pairSuit * rankCount; pair < (pairSuit+1)*rankCount; pair++ {
		if counts[pair] < 2 {
			continue
		}
		remaining := counts
		remaining[pair] -= 2
		valid := true
		for tile := 0; tile < tileTypes; tile++ {
			needed := remaining[tile] % groupSize
			if needed == 0 {
				continue
			}
			// Three parallel sequences can be replaced by three equal triples.
			if tile%rankCount >= rankCount-2 ||
				remaining[tile+1] < needed || remaining[tile+2] < needed {
				valid = false
				break
			}
			remaining[tile+1] -= needed
			remaining[tile+2] -= needed
		}
		if valid {
			return true
		}
	}
	return false
}

func classify(counts [tileTypes]int) string {
	if winning(counts) {
		return "Tsumo"
	}
	for removed := 0; removed < tileTypes; removed++ {
		if counts[removed] == 0 {
			continue
		}
		counts[removed]--
		for added := 0; added < tileTypes; added++ {
			if added == removed {
				continue
			}
			counts[added]++
			if winning(counts) {
				return "Tenpai"
			}
			counts[added]--
		}
		counts[removed]++
	}
	return "Noten"
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var counts [tileTypes]int
	for tile := 0; tile < handSize; tile++ {
		var token string
		fmt.Fscan(input, &token)
		rank := int(token[0] - '1')
		suit := int(token[1] - 'a')
		counts[suit*rankCount+rank]++
	}
	fmt.Println(classify(counts))
}
