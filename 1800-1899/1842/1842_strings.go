package main

import (
	"bufio"
	"fmt"
	"os"
)

const bufferSize = 1 << 20

// suffixStart returns the start of the lexicographically greatest suffix
// (the least one when flip is set), by the comparison loop of Two-Way
func suffixStart(w []byte, flip bool) int {
	n, best, j, k, p := len(w), -1, 0, 1, 1
	for j+k < n {
		a, b := w[j+k], w[best+k]
		if a != b && (a < b) != flip {
			j += k
			k = 1
			p = j - best
		} else if a == b {
			if k != p {
				k++
			} else {
				j += p
				k = 1
			}
		} else {
			best = j
			j = best + 1
			k = 1
			p = 1
		}
	}
	return best + 1
}

func main() {
	var w []byte
	fmt.Fscan(bufio.NewReaderSize(os.Stdin, bufferSize), &w)
	n := len(w)
	// the longest border gives the period of the word
	border := make([]int, n)
	for i, k := 1, 0; i < n; i++ {
		for k > 0 && w[k] != w[i] {
			k = border[k-1]
		}
		if w[k] == w[i] {
			k++
		}
		border[i] = k
	}
	// the critical factorization theorem: the split before the later of the
	// two greatest suffixes has a local root as long as the period (both are
	// the whole word only for a power of one letter)
	split := 1
	for _, s := range []int{suffixStart(w, false), suffixStart(w, true)} {
		if s > split {
			split = s
		}
	}
	fmt.Println(split, n-border[n-1])
}
