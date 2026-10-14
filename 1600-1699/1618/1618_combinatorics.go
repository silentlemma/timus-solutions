package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const (
	mod  = 10007
	most = 512 // the product of the sizes is at most this
)

// sizes gives the length of the arrays at each depth, ending with 0 for the empty ones.
func sizes(text []byte) []int {
	var open, dims []int
	for _, ch := range text {
		switch ch {
		case '[':
			if len(open) > 0 {
				open[len(open)-1]++
			}
			open = append(open, 0)
		case ']':
			depth := len(open) - 1
			for len(dims) <= depth {
				dims = append(dims, 0)
			}
			dims[depth] = open[depth]
			open = open[:depth]
		}
	}
	return dims
}

func main() {
	text, _ := ioutil.ReadAll(os.Stdin)
	dims := sizes(text)
	if len(dims) == 1 {
		fmt.Println(1)
		return
	}
	// Stirling numbers of the second kind: ways to split m references into k objects
	stirling := make([][]int, most+1)
	for m := range stirling {
		stirling[m] = make([]int, most+1)
	}
	stirling[0][0] = 1
	for m := 1; m <= most; m++ {
		for k := 1; k <= m; k++ {
			stirling[m][k] = (stirling[m-1][k-1] + k*stirling[m-1][k]) % mod
		}
	}
	// m references to empty arrays: any partition of them (Bell numbers)
	ways := make([]int, most+1)
	for m := 0; m <= most; m++ {
		sum := 0
		for k := 0; k <= m; k++ {
			sum += stirling[m][k]
		}
		ways[m] = sum % mod
	}
	// the references at depth i number at most dims[0] * ... * dims[i - 1]
	slots := []int{1}
	for _, d := range dims[:len(dims)-1] {
		slots = append(slots, slots[len(slots)-1]*d)
	}
	for i := len(dims) - 2; i >= 1; i-- {
		width := dims[i]
		// m references to arrays of this depth: k distinct arrays, whose
		// k * width elements are configured one level down
		upper := most / width
		if slots[i] < upper {
			upper = slots[i]
		}
		next := make([]int, most+1)
		for m := 1; m <= upper; m++ {
			sum := 0
			for k := 1; k <= m; k++ {
				sum += stirling[m][k] * ways[k*width]
			}
			next[m] = sum % mod
		}
		ways = next
	}
	fmt.Println(ways[dims[0]])
}
