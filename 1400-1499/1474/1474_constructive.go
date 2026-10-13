package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	empty = 0
	white = 1
	black = 2
)

func main() {
	var n int
	fmt.Scan(&n)
	hummocks := make([]int, 2*n+1)
	for i := range hummocks {
		hummocks[i] = black
		if i < n {
			hummocks[i] = white
		}
	}
	hummocks[n] = empty
	hole := n
	var moves []int
	// runs of 1, 2, ..., n, n, n, ..., 1 moves, the colours taking turns,
	// and in a run a frog jumps into the hole when it can and slides otherwise
	var runs []int
	for i := 1; i <= n; i++ {
		runs = append(runs, i)
	}
	runs = append(runs, n)
	for i := n; i >= 1; i-- {
		runs = append(runs, i)
	}
	colour := black
	for _, run := range runs {
		step, other := 1, white // where the frogs come from
		if colour == white {
			step, other = -1, black
		}
		for k := 0; k < run; k++ {
			far, near := hole+2*step, hole+step
			frog := near
			if far >= 0 && far <= 2*n && hummocks[far] == colour && hummocks[near] == other {
				frog = far
			}
			hummocks[hole], hummocks[frog] = colour, empty
			hole = frog
			moves = append(moves, frog)
		}
		colour = other
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	writer.WriteString(strconv.Itoa(len(moves)) + "\n")
	for i, m := range moves {
		if i > 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.Itoa(m))
	}
	writer.WriteByte('\n')
}
