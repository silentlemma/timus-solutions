package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const (
	edges     = 30
	colours   = 30
	rotations = 60
	// the rotations other than the identity: how many there are and the
	// cycle length on the edges; a half-turn also keeps two edges in place
	faceTurns, faceCycle     = 24, 5
	vertexTurns, vertexCycle = 20, 3
	halfTurns, halfCycle     = 15, 2
)

// cycles counts colourings of cycles of this length that use each colour
// counts[c] times, or 0 if some count does not split into whole cycles.
func cycles(counts []int64, length int64) *big.Int {
	ways := big.NewInt(1)
	used := int64(0)
	for _, c := range counts {
		if c%length != 0 {
			return big.NewInt(0)
		}
		used += c / length
		ways.Mul(ways, new(big.Int).Binomial(used, c/length))
	}
	return ways
}

func main() {
	in := bufio.NewReader(os.Stdin)
	counts := make([]int64, colours+1)
	for i := 0; i < edges; i++ {
		var c int
		fmt.Fscan(in, &c)
		counts[c]++
	}
	total := cycles(counts, 1)
	total.Add(total, new(big.Int).Mul(big.NewInt(faceTurns), cycles(counts, faceCycle)))
	total.Add(total, new(big.Int).Mul(big.NewInt(vertexTurns), cycles(counts, vertexCycle)))
	// a half-turn: colour the two kept edges first, in order
	kept := big.NewInt(0)
	rest := make([]int64, colours+1)
	for a := range counts {
		for b := range counts {
			copy(rest, counts)
			rest[a]--
			rest[b]--
			if rest[a] >= 0 && rest[b] >= 0 {
				kept.Add(kept, cycles(rest, halfCycle))
			}
		}
	}
	total.Add(total, kept.Mul(kept, big.NewInt(halfTurns)))
	fmt.Println(total.Div(total, big.NewInt(rotations)))
}
