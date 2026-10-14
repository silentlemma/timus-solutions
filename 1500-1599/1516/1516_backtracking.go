package main

import (
	"fmt"
	"math/bits"
)

const size = 8

type jump struct{ mid, to uint }

var (
	jumps       [size * size][]jump
	total, best int
)

// dfs moves the white checker on square: black and white are the pieces still
// on the board, the mover excluded, removed counts the white pieces taken away
// so far and taken the blacks captured so far.
func dfs(square uint, black, white uint64, removed, taken int) {
	if c := removed + total - taken; c < best { // every black not captured is taken away
		best = c
	}
	for _, j := range jumps[square] {
		if black>>j.mid&1 == 0 {
			continue
		}
		nb, nw, cost := black&^(1<<j.mid), white, removed
		nb &^= 1 << j.to // a black in the way is taken away, uncaptured
		if nw>>j.to&1 == 1 {
			nw &^= 1 << j.to // a white in the way costs one more
			cost++
		}
		dfs(j.to, nb, nw, cost, taken+1)
	}
}

func main() {
	// square (x, y), both from 0, is bit x * size + y; the first input line is y = 7
	var whites, blacks uint64
	for r := 0; r < size; r++ {
		var line string
		fmt.Scan(&line)
		for x := 0; x < size; x++ {
			bit := uint64(1) << uint(x*size+size-1-r)
			switch line[x] {
			case 'W':
				whites |= bit
			case 'B':
				blacks |= bit
			}
		}
	}
	// only squares off the edge can be jumped, so the landing stays on the board
	for x := 0; x < size; x++ {
		for y := 0; y < size; y++ {
			for _, dx := range []int{-1, 1} {
				for _, dy := range []int{-1, 1} {
					tx, ty := x+2*dx, y+2*dy
					if tx >= 0 && tx < size && ty >= 0 && ty < size {
						mid, to := uint((x+dx)*size+y+dy), uint(tx*size+ty)
						jumps[x*size+y] = append(jumps[x*size+y], jump{mid, to})
					}
				}
			}
		}
	}
	total = bits.OnesCount64(blacks)
	best = total // removing every black always wins
	for s := uint(0); s < size*size; s++ {
		if whites>>s&1 == 1 {
			dfs(s, blacks, whites&^(1<<s), 0, 0)
		}
	}
	fmt.Println(best)
}
