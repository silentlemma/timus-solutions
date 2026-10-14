package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
)

const (
	two   = 2
	three = 3
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	marks := make([]int, n)
	for i := range marks {
		fmt.Fscan(in, &marks[i])
	}
	// a nonzero product is +-2^a 3^b: prefix counts of twos and threes
	twos := make([]int, n+1)
	threes := make([]int, n+1)
	zero := false
	for i, x := range marks {
		twos[i+1], threes[i+1] = twos[i], threes[i]
		if x == two || x == -two {
			twos[i+1]++
		}
		if x == three || x == -three {
			threes[i+1]++
		}
		zero = zero || x == 0
	}
	key := func(a, b int) float64 {
		return float64(a)*math.Log(two) + float64(b)*math.Log(three)
	}
	found := false // the exponents of the best positive product
	bestA, bestB := 0, 0
	for i := 0; i < n; {
		if marks[i] == 0 {
			i++
			continue
		}
		// a run without zeros: |x| >= 1, so longer runs never shrink the size
		j := i
		var negatives []int
		for j < n && marks[j] != 0 {
			if marks[j] < 0 {
				negatives = append(negatives, j)
			}
			j++
		}
		spans := [][2]int{{i, j}}
		if len(negatives)%2 == 1 {
			// drop the part up to the first negative or from the last one
			spans = [][2]int{{negatives[0] + 1, j}, {i, negatives[len(negatives)-1]}}
		}
		for _, s := range spans {
			lo, hi := s[0], s[1]
			if lo >= hi {
				continue
			}
			a, b := twos[hi]-twos[lo], threes[hi]-threes[lo]
			if !found || key(a, b) > key(bestA, bestB) {
				found, bestA, bestB = true, a, b
			}
		}
		i = j
	}
	if !found {
		// all marks are zeros or lone negatives
		if zero {
			fmt.Fprintln(out, 0)
		} else {
			fmt.Fprintln(out, marks[0])
		}
		return
	}
	p := new(big.Int).Exp(big.NewInt(two), big.NewInt(int64(bestA)), nil)
	q := new(big.Int).Exp(big.NewInt(three), big.NewInt(int64(bestB)), nil)
	fmt.Fprintln(out, p.Mul(p, q).String())
}
