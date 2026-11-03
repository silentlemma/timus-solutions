package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const teamSize = 3

var clash []uint32
var answer int

func search(mask uint32, selected int) {
	if selected+bits.OnesCount32(mask) <= answer {
		return
	}
	chosen, degree := 0, 0
	for remaining := mask; remaining != 0; remaining &= remaining - 1 {
		i := bits.TrailingZeros32(remaining)
		count := bits.OnesCount32(mask & clash[i])
		if count > degree {
			chosen, degree = i, count
		}
	}
	// An edgeless remainder is taken whole; otherwise try the most
	// conflicting team first to obtain a useful bound for the skip branch.
	if degree <= 1 {
		if value := selected + bits.OnesCount32(mask); value > answer {
			answer = value
		}
		return
	}
	search(mask&^clash[chosen], selected+1)
	search(mask&^(1<<uint(chosen)), selected)
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(input, &k)
	teams := make([][teamSize]string, k)
	for i := range teams {
		for j := range teams[i] {
			fmt.Fscan(input, &teams[i][j])
		}
	}
	clash = make([]uint32, k)
	for i := range teams {
		for j := range teams {
			for _, first := range teams[i] {
				for _, second := range teams[j] {
					if first == second {
						clash[i] |= 1 << uint(j)
					}
				}
			}
		}
	}
	search((1<<uint(k))-1, 0)
	fmt.Println(answer)
}
