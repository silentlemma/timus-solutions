package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	// wall: anything that is not a digit acts like a digit too large for
	// every base
	wall     = 36
	smallest = 2
)

func value(ch byte) int {
	switch {
	case ch >= '0' && ch <= '9':
		return int(ch - '0')
	case ch >= 'A' && ch <= 'Z':
		return int(ch-'A') + 10
	}
	return wall
}

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	// a number in base k starts at every digit below k whose left neighbour
	// is k or more, so each neighbouring pair (left, right) with right < left
	// starts a number in the bases right + 1 .. left
	var pairs [wall + 1][wall + 1]int64
	left := wall
	for _, ch := range data {
		right := value(ch)
		pairs[left][right]++
		left = right
	}
	var count [wall + 2]int64
	for l := 1; l <= wall; l++ {
		for r := 0; r < l; r++ {
			from := r + 1
			if from < smallest {
				from = smallest
			}
			count[from] += pairs[l][r]
			count[l+1] -= pairs[l][r]
		}
	}
	best, running, bestK := int64(-1), int64(0), smallest
	for k := 0; k <= wall; k++ {
		running += count[k]
		if k >= smallest && running > best {
			best, bestK = running, k
		}
	}
	fmt.Println(bestK, best)
}
