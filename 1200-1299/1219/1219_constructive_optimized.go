package main

import (
	"bufio"
	"os"
)

const (
	letters = 26
	order   = 3
	length  = 1000000
)

var (
	a     = make([]int, letters*order)
	cycle []int
)

// gen builds a de bruijn sequence: every word of order letters once around
// the cycle.
func gen(t, p int) {
	if t > order {
		if order%p == 0 {
			cycle = append(cycle, a[1:p+1]...)
		}
		return
	}
	a[t] = a[t-p]
	gen(t+1, p)
	for j := a[t-p] + 1; j < letters; j++ {
		a[t] = j
		gen(t+1, t)
	}
}

func main() {
	gen(1, 1)
	// one cycle has 26^3 letters; stream it instead of retaining a million-byte output.
	block := make([]byte, len(cycle))
	for i, value := range cycle {
		block[i] = byte('a' + value)
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	remaining := length
	for remaining >= len(block) {
		w.Write(block)
		remaining -= len(block)
	}
	w.Write(block[:remaining])
	w.WriteByte('\n')
}
