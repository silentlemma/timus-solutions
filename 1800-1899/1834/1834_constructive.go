package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type run struct{ lo, hi int }

// cut the values 1 .. n greedily into runs of consecutive values whose
// positions alternately rise and fall, the first one as asked
func blocks(pos []int, n int, rising bool) []run {
	var cuts []run
	for v := 1; v <= n; rising = !rising {
		w := v
		for w < n && (pos[w+1] > pos[w]) == rising {
			w++
		}
		cuts = append(cuts, run{v, w})
		v = w + 1
	}
	return cuts
}

// the least k with 2^k >= count
func passes(count int) int {
	k := 0
	for 1<<uint(k) < count {
		k++
	}
	return k
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	cars := make([]int, n)
	pos := make([]int, n+1)
	for i := range cars {
		fmt.Fscan(in, &cars[i])
		pos[cars[i]] = i
	}
	// one pass keeps a chosen set of cars in order and appends the others
	// reversed; over k passes cars end up ordered by their codes of choices
	// in reflected Gray order, reversed once per one in the code
	runs, first := blocks(pos, n, true), 0
	if falling := blocks(pos, n, false); passes(len(runs)) > passes(len(falling)+1) {
		runs, first = falling, 1
	}
	k := passes(len(runs) + first)
	code := make([]int, n+1)
	for i, r := range runs {
		rank := i + first
		for v := r.lo; v <= r.hi; v++ {
			code[v] = rank ^ (rank >> 1)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, k)
	for bit := uint(0); bit < uint(k); bit++ {
		next := make([]int, 0, n)
		for _, v := range cars {
			if code[v]>>bit&1 == 0 {
				next = append(next, v)
			}
		}
		for i := n - 1; i >= 0; i-- {
			if code[cars[i]]>>bit&1 == 1 {
				next = append(next, cars[i])
			}
		}
		cars = next
		for i, v := range cars {
			if i > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(v))
		}
		out.WriteByte('\n')
	}
}
