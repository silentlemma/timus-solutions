package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	outputSize = 16
)

const maxBoxes = 500

func root(parent *[maxBoxes + 1]int16, box int16) int16 {
	for parent[box] > 0 {
		boss := parent[box]
		if parent[boss] > 0 {
			parent[box] = parent[boss]
		}
		box = parent[box]
	}
	return box
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		value, _ := strconv.Atoi(in.Text())
		return value
	}
	m, n := int16(next()), next()
	// Zero means unseen, negative means root with its negated component size.
	var parent [maxBoxes + 1]int16
	moves, groups := 0, 0
	for box := int16(1); box <= m; box++ {
		for k := 0; k < n; k++ {
			colour := int16(next())
			if colour == box {
				continue
			}
			moves++
			if parent[box] == 0 {
				parent[box] = -1
				groups++
			}
			if parent[colour] == 0 {
				parent[colour] = -1
				groups++
			}
			a, b := root(&parent, box), root(&parent, colour)
			if a == b {
				continue
			}
			if parent[a] > parent[b] {
				a, b = b, a
			}
			parent[a] += parent[b]
			parent[b] = a
			groups--
		}
	}
	if moves > 0 {
		moves += groups - 1
	}
	var answer [outputSize]byte
	os.Stdout.Write(append(strconv.AppendInt(answer[:0], int64(moves), 10), '\n'))
}
