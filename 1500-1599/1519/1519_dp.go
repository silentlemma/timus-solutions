package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	// the ends of a path piece, matched like brackets
	opening, closing = 1, 2
	flip             = opening ^ closing // turns one end into the other
	bits             = 2                 // bits per plug
	mask             = 3                 // one plug
)

// partner finds the plug matching the bracket at pos, searching towards step.
func partner(state uint64, pos, step int) int {
	for depth := 0; ; pos += step {
		switch state >> uint(bits*pos) & mask {
		case opening:
			depth += step
		case closing:
			depth -= step
		}
		if depth == 0 {
			return pos
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	free := make([][]bool, n+1)
	for i := range free {
		free[i] = make([]bool, m+1)
	}
	last := 0
	for i := 0; i < n; i++ {
		var row string
		fmt.Fscan(in, &row)
		for j := 0; j < m; j++ {
			if row[j] == '.' {
				free[i][j] = true
				last = i*m + j
			}
		}
	}
	// a state holds m + 1 plugs: plug j is the left side of the current cell
	// when j is its column, plug j + 1 its upper side; the rest are the lower
	// sides of the row above or this row
	ways := map[uint64]uint64{0: 1}
	total := uint64(0)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			next := make(map[uint64]uint64, 2*len(ways))
			sl, su := uint(bits*j), uint(bits*(j+1))
			clear := ^(uint64(mask) << sl) & ^(uint64(mask) << su)
			down, right := free[i+1][j], free[i][j+1]
			for state, count := range ways {
				left, up, base := state>>sl&mask, state>>su&mask, state&clear
				switch {
				case !free[i][j]:
					if left == 0 && up == 0 {
						next[state] += count
					}
				case left == 0 && up == 0:
					if down && right {
						next[base|opening<<sl|closing<<su] += count
					}
				case left == 0 || up == 0:
					end := left | up
					if down {
						next[base|end<<sl] += count
					}
					if right {
						next[base|end<<su] += count
					}
				case left == up:
					// two openings or two closings: the far end of one of the
					// joined pieces changes its kind
					var far int
					if left == opening {
						far = partner(state, j+1, 1)
					} else {
						far = partner(state, j, -1)
					}
					next[base^flip<<uint(bits*far)] += count
				case left == closing:
					next[base] += count
				case i*m+j == last && base == 0:
					total += count // the loop closes on the last free cell
				}
			}
			ways = next
		}
		// the next row starts with an empty left plug
		shifted := make(map[uint64]uint64, len(ways))
		for state, count := range ways {
			shifted[state<<bits] += count
		}
		ways = shifted
	}
	fmt.Println(total)
}
