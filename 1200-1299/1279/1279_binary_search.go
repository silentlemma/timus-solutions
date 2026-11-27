package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	var k int64
	fmt.Fscan(in, &n, &m, &k)
	heights := make([]int64, n*m)
	for i := range heights {
		fmt.Fscan(in, &heights[i])
	}
	// Filling the lowest sections raises stacks below the final minimum h to h.
	// Some stacks at h may get one more container; initially taller ones stay put.
	// The answer is the largest h with sum(max(0, h - height)) <= K.
	lo := heights[0]
	for _, h := range heights {
		if h < lo {
			lo = h
		}
	}
	hi := lo + k
	for lo < hi {
		mid := (lo + hi + 1) / 2
		var need int64
		for _, h := range heights {
			if h < mid {
				need += mid - h
			}
		}
		if need <= k {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	fmt.Println(lo)
}
