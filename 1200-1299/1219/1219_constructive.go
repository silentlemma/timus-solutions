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

// gen builds a de Bruijn sequence: every word of order letters once around
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
	// repeating the cycle keeps every window of three letters a cyclic window
	// of it, so each triple, pair and letter appears almost equally often
	out := make([]byte, length+1)
	for i := 0; i < length; i++ {
		out[i] = byte('a' + cycle[i%len(cycle)])
	}
	out[length] = '\n'
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.Write(out)
}
