package main

import (
	"fmt"
	"math/bits"
)

const alphabet = 26

func main() {
	var n int
	var word string
	fmt.Scan(&n, &word)
	size := len(word)
	// placing the remaining letter whose next occurrence is farthest moves at
	// least k places when k letters remain, so a universal word needs
	// n + (n - 1) + ... + 1 letters
	if size < n*(n+1)/2 {
		fmt.Println("NO")
		return
	}
	fail := int16(size + 1)
	// after[c][p]: the place just after the first c at or after place p
	after := make([][]int16, alphabet)
	for c := range after {
		after[c] = make([]int16, size+2)
		after[c][size], after[c][size+1] = fail, fail
		for p := size - 1; p >= 0; p-- {
			if int(word[p]-'a') == c {
				after[c][p] = int16(p + 1)
			} else {
				after[c][p] = after[c][p+1]
			}
		}
	}
	// reach[mask]: how far the greedy embedding gets for the worst order of
	// the letters in mask; submasks come first in increasing order, and one
	// failing mask makes the whole set fail, so the table stops there
	reach := []int16{0}
	for mask := uint32(1); mask < uint32(1)<<uint(n); mask++ {
		best := int16(0)
		for rest := mask; rest != 0; rest &= rest - 1 {
			letter := bits.TrailingZeros32(rest)
			if pos := after[letter][reach[mask^(1<<uint(letter))]]; pos > best {
				best = pos
			}
		}
		if best == fail {
			fmt.Println("NO")
			return
		}
		reach = append(reach, best)
	}
	fmt.Println("YES")
}
