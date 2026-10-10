package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	where := make([]int, n+1)
	for i := 0; i < n; i++ {
		var v int
		fmt.Fscan(in, &v)
		where[v] = i
	}
	// rank of the order of 1..k among themselves: element k sweeps once
	// across the order of 1..k-1, to the left in even sweeps and to the
	// right in odd ones, and that order's rank counts the sweeps before
	rank := new(big.Int)
	for k := 2; k <= n; k++ {
		smallerLeft := 0
		for v := 1; v < k; v++ {
			if where[v] < where[k] {
				smallerLeft++
			}
		}
		step := k - 1 - smallerLeft
		if rank.Bit(0) == 1 {
			step = smallerLeft
		}
		rank.Mul(rank, big.NewInt(int64(k)))
		rank.Add(rank, big.NewInt(int64(step)))
	}
	rank.Add(rank, big.NewInt(1))
	fmt.Println(rank.String())
}
