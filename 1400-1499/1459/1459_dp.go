package main

import (
	"fmt"
	"sort"
)

const (
	mod     = 1000000000
	opening = 1 // plugs are brackets: the two ends of one path
	closing = 2
	bits    = 2 // a plug state keeps two bits per plug
	mask    = 1<<bits - 1
)

var width int

func get(code, k int) int { return code >> (bits * k) & mask }

func with(code, k, v int) int { return code&^(mask<<(bits*k)) | v<<(bits*k) }

// the bracket matching plug k: rightwards for an opening one, leftwards otherwise
func partner(code, k int) int {
	step, depth := -1, 0
	if get(code, k) == opening {
		step = 1
	}
	for j := k; ; j += step {
		if get(code, j) == get(code, k) {
			depth++
		} else if get(code, j) != 0 {
			depth--
		}
		if depth == 0 {
			return j
		}
	}
}

// run one row of cells over a plug state and return the states it can leave
// below; plug c is the left plug of cell c, plug c + 1 its upper plug
func rowMoves(start int, last bool) map[int]int64 {
	states := map[int]int64{start << bits: 1}
	for c := 0; c < width; c++ {
		next := map[int]int64{}
		for p, ways := range states {
			left, up := get(p, c), get(p, c+1)
			put := func(q, down, right int) {
				next[with(with(q, c, down), c+1, right)] += ways
			}
			switch {
			case left == 0 && up == 0:
				if c+1 < width && !last {
					put(p, opening, closing) // a new path turning right and down
				}
			case left != 0 && up != 0:
				q := p
				if left == opening && up == closing {
					// closing the cycle: only at the very last cell, with nothing else open
					if last && c == width-1 && with(with(p, c, 0), c+1, 0) == 0 {
						put(p, 0, 0)
					}
					continue
				}
				if left == opening && up == opening {
					q = with(q, partner(q, c+1), opening)
				} else if left == closing && up == closing {
					q = with(q, partner(q, c), closing)
				}
				put(q, 0, 0)
			default:
				plug := left + up
				if !last {
					put(p, plug, 0)
				}
				if c+1 < width {
					put(p, 0, plug)
				}
			}
		}
		states = next
	}
	result := map[int]int64{}
	for p, ways := range states {
		if get(p, width) == 0 {
			result[p] = ways % mod
		}
	}
	return result
}

func multiply(a, b [][]int64) [][]int64 {
	n := len(a)
	c := make([][]int64, n)
	for i := range c {
		c[i] = make([]int64, n)
		for k := 0; k < n; k++ {
			if a[i][k] != 0 {
				for j := 0; j < n; j++ {
					c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % mod
				}
			}
		}
	}
	return c
}

func main() {
	var height int64
	fmt.Scan(&width, &height)
	// every plug state that a row can leave behind, reached from the empty one
	index := map[int]int{0: 0}
	order := []int{0}
	for i := 0; i < len(order); i++ {
		moves := rowMoves(order[i], false)
		keys := make([]int, 0, len(moves))
		for t := range moves {
			keys = append(keys, t)
		}
		sort.Ints(keys)
		for _, t := range keys {
			if _, ok := index[t]; !ok {
				index[t] = len(order)
				order = append(order, t)
			}
		}
	}
	size := len(order)
	step := make([][]int64, size)
	power := make([][]int64, size)
	for i := range step {
		step[i] = make([]int64, size)
		power[i] = make([]int64, size)
		power[i][i] = 1
		for t, ways := range rowMoves(order[i], false) {
			step[i][index[t]] = ways
		}
	}
	// the first height - 1 rows by fast powering, then the last row that closes the cycle
	for e := height - 1; e > 0; e >>= 1 {
		if e&1 == 1 {
			power = multiply(power, step)
		}
		step = multiply(step, step)
	}
	var total int64
	for i := range order {
		if closed, ok := rowMoves(order[i], true)[0]; ok {
			total = (total + power[0][i]*closed) % mod
		}
	}
	fmt.Println(2 * total % mod) // every cycle can be walked in two directions
}
