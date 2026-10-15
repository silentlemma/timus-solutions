package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

const cycleCut = 3 // a cycle on s vertices has path(s - 1) + path(s - 3) sets

var (
	enemy []uint64
	path  []uint64 // independent sets of a path on s vertices
	memo  = map[uint64]uint64{}
)

func count(mask uint64) uint64 {
	if mask == 0 {
		return 1
	}
	if v, ok := memo[mask]; ok {
		return v
	}
	// split into connected parts, which multiply
	low := mask & -mask
	part, frontier := low, low
	for frontier != 0 {
		bit := frontier & -frontier
		frontier ^= bit
		grow := enemy[bits.TrailingZeros64(bit)] & mask &^ part
		part |= grow
		frontier |= grow
	}
	var result uint64
	if part != mask {
		result = count(part) * count(mask&^part)
	} else {
		size := bits.OnesCount64(mask)
		pivot, most, least := -1, -1, size
		for rest := mask; rest != 0; rest &= rest - 1 {
			v := bits.TrailingZeros64(rest)
			degree := bits.OnesCount64(enemy[v] & mask)
			if degree < least {
				least = degree
			}
			if degree > most {
				pivot, most = v, degree
			}
		}
		switch {
		case least == size-1:
			result = uint64(size + 1) // all pairs are enemies: nobody or one robot
		case most <= 2 && least <= 1:
			result = path[size]
		case most <= 2:
			result = path[size-1] + path[size-cycleCut]
		default:
			// branch on a vertex of most enemies: leave it out, or take it
			// and drop all its enemies
			bit := uint64(1) << uint(pivot)
			result = count(mask&^bit) + count(mask&^(enemy[pivot]|bit))
		}
	}
	memo[mask] = result
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	enemy = make([]uint64, n)
	for i := 0; i < n; i++ {
		var row string
		fmt.Fscan(in, &row)
		for j := 0; j < n; j++ {
			if i != j && row[j] == '0' {
				enemy[i] |= 1 << uint(j)
			}
		}
	}
	// a working group is a clique of friends, that is an independent set of
	// the graph of non-friends; every group plus the empty one is a day, so
	// the day of rusting is the number of independent sets, empty included
	path = []uint64{1, 2}
	for s := 2; s <= n; s++ {
		path = append(path, path[s-1]+path[s-2])
	}
	fmt.Println(count(1<<uint(n) - 1))
}
