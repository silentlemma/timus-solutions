package main

import (
	"fmt"
	"strings"
)

const (
	cells       = 4                        // the program needs at most four cells
	values      = 27                       // a cell holds 0 or a letter, kept as 0 or 1 to 26
	others      = values * values * values // states of the cells away from the pointer
	states      = cells * others
	letterBase  = 'a' - 1
	unreachable = 1 << 30
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	var s string
	fmt.Scan(&s)
	// a state, after a letter is printed, is the pointer's cell (holding that
	// letter) and the values of the other three cells, left to right; the
	// used cells form a block of four that holds the start cell somewhere
	cost := make([]int, states)
	for i := range cost {
		cost[i] = unreachable
	}
	for start := 0; start < cells; start++ {
		cost[start*others] = 0
	}
	var cameFrom [][]int32
	previous := 0 // the value under the pointer: 0 before the first letter
	for _, c := range []byte(s) {
		letter := int(c) - letterBase
		next := make([]int, states)
		back := make([]int32, states)
		for i := range next {
			next[i] = unreachable
		}
		for state, here := range cost {
			if here == unreachable {
				continue
			}
			p, rest := state/others, state%others
			digits := [cells - 1]int{rest / (values * values), rest / values % values, rest % values}
			var w [cells]int
			for cell, k := 0, 0; cell < cells; cell++ {
				if cell == p {
					w[cell] = previous
				} else {
					w[cell] = digits[k]
					k++
				}
			}
			for q := 0; q < cells; q++ {
				change := letter + letterBase
				if w[q] != 0 {
					change = letter - w[q]
				}
				total := here + abs(p-q) + abs(change) + 1
				code := 0
				for cell := 0; cell < cells; cell++ {
					if cell != q {
						code = code*values + w[cell]
					}
				}
				code += q * others
				if total < next[code] {
					next[code] = total
					back[code] = int32(state)
				}
			}
		}
		cameFrom = append(cameFrom, back)
		cost = next
		previous = letter
	}
	// walk back to recover the cells used, then write the program
	state := 0
	for st := range cost {
		if cost[st] < cost[state] {
			state = st
		}
	}
	used := make([]int, len(s)+1)
	for i := len(s); i > 0; i-- {
		used[i] = state / others
		state = int(cameFrom[i-1][state])
	}
	used[0] = state / others
	var held [cells]int
	var out strings.Builder
	for i := 0; i < len(s); i++ {
		p, q, letter := used[i], used[i+1], int(s[i])-letterBase
		if q > p {
			out.WriteString(strings.Repeat(">", q-p))
		} else {
			out.WriteString(strings.Repeat("<", p-q))
		}
		change := letter + letterBase
		if held[q] != 0 {
			change = letter - held[q]
		}
		if change > 0 {
			out.WriteString(strings.Repeat("+", change))
		} else {
			out.WriteString(strings.Repeat("-", -change))
		}
		out.WriteByte('.')
		held[q] = letter
	}
	fmt.Println(out.String())
}
