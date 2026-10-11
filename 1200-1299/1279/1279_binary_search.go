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
	// filling the lowest sections first raises every section to a level h
	// and some of them one higher, so the answer is the largest h whose
	// missing containers, the sum of h - height below h, fit into K
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
