package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const (
	fieldSize = 12
	decimal   = 10
)

type segment struct{ left, right, index int }

func number(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	segments := make([]segment, number(input))
	for i := range segments {
		left, right := number(input), number(input)
		if left > right {
			left, right = right, left
		}
		segments[i] = segment{left, right, i + 1}
	}
	sort.Slice(segments, func(i, j int) bool {
		a, b := segments[i], segments[j]
		return a.left > b.left || a.left == b.left && a.right > b.right
	})
	// Decreasing right endpoints within a tie rule out equal left endpoints.
	tails := make([]int, 0, len(segments))
	previous := make([]int, len(segments))
	for i, current := range segments {
		slot := sort.Search(len(tails), func(k int) bool {
			return segments[tails[k]].right >= current.right
		})
		previous[i] = -1
		if slot > 0 {
			previous[i] = tails[slot-1]
		}
		if slot == len(tails) {
			tails = append(tails, i)
		} else {
			tails[slot] = i
		}
	}
	chain := make([]int, len(tails))
	at := tails[len(tails)-1]
	for i := len(chain) - 1; i >= 0; i-- {
		chain[i] = segments[at].index
		at = previous[at]
	}
	output := bufio.NewWriter(os.Stdout)
	var buffer [fieldSize]byte
	line := strconv.AppendInt(buffer[:0], int64(len(chain)), decimal)
	output.Write(append(line, '\n'))
	for i, index := range chain {
		if i != 0 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendInt(buffer[:0], int64(index), decimal))
	}
	output.WriteByte('\n')
	output.Flush()
}
