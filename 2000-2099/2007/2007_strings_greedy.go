package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const alphabet = 26
const first = 'a'

func solve(source, modifiers string) string {
	size := len(source)
	var positions [alphabet][]int
	for at := range source {
		c := source[at] - first
		positions[c] = append(positions[c], at)
	}
	var frequency, counts, head, cut, nextPosition, nextCut, delta [alphabet]int
	for at := range modifiers {
		counts[modifiers[at]-first]++
	}
	var bad, available, present uint32
	for c := 0; c < alphabet; c++ {
		frequency[c] = len(positions[c])
		positions[c] = append(positions[c], size)
		cut[c] = counts[c]
		nextPosition[c] = positions[c][0]
		nextCut[c] = size
		if cut[c] < frequency[c] {
			nextCut[c] = positions[c][cut[c]]
		}
		delta[c] = counts[c] - frequency[c]
		if delta[c] < 0 || delta[c]&1 != 0 {
			bad |= 1 << uint(c)
		}
		if counts[c] > 0 {
			available |= 1 << uint(c)
		}
		if frequency[c] > 0 {
			present |= 1 << uint(c)
		}
	}
	at, original, dirty := 0, alphabet, true
	answer := make([]byte, 0, len(source)+len(modifiers))
	for bad != 0 {
		if dirty {
			if at == size {
				original = alphabet
			} else if counts[source[at]-first] == 0 {
				original = int(source[at] - first)
			} else {
				limit := size
				for _, value := range nextCut {
					if value < limit {
						limit = value
					}
				}
				for candidates := present; candidates != 0; candidates &= candidates - 1 {
					c := bits.TrailingZeros32(candidates)
					if nextPosition[c] <= limit {
						original = c
						break
					}
				}
			}
			dirty = false
		}
		modifier := alphabet
		if available != 0 {
			modifier = bits.TrailingZeros32(available)
		}
		c := modifier
		if original <= modifier {
			c = original
			to := nextPosition[c]
			for at < to {
				removed := int(source[at] - first)
				at++
				counts[removed]--
				head[removed]++
				nextPosition[removed] = positions[removed][head[removed]]
				if counts[removed] == 0 {
					available &^= 1 << uint(removed)
				}
				if head[removed] == frequency[removed] {
					present &^= 1 << uint(removed)
				}
			}
			head[c]++
			nextPosition[c] = positions[c][head[c]]
			at++
			if head[c] == frequency[c] {
				present &^= 1 << uint(c)
			}
			cut[c]++
			delta[c]++
			dirty = true
		} else {
			counts[c]--
			if counts[c] == 0 {
				available &^= 1 << uint(c)
			}
			cut[c]--
			delta[c]--
		}
		nextCut[c] = size
		if cut[c] < frequency[c] {
			nextCut[c] = positions[c][cut[c]]
		}
		if delta[c] < 0 || delta[c]&1 != 0 {
			bad |= 1 << uint(c)
		} else {
			bad &^= 1 << uint(c)
		}
		answer = append(answer, byte(c)+first)
	}
	return string(answer)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var source, modifiers string
	fmt.Fscan(in, &source, &modifiers)
	fmt.Println(solve(source, modifiers))
}
