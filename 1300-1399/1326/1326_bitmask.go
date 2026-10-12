package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

type offer struct{ cost, keep int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n)
	var cost, caps []int // caps as a mask over 1..n
	for i := 0; i < n; i++ {
		var price int
		fmt.Fscan(in, &price)
		cost = append(cost, price)
		caps = append(caps, 1<<i)
	}
	fmt.Fscan(in, &m)
	for j := 0; j < m; j++ {
		var price, size int
		fmt.Fscan(in, &price, &size)
		mask := 0
		for k := 0; k < size; k++ {
			var cap int
			fmt.Fscan(in, &cap)
			mask |= 1 << (cap - 1)
		}
		cost = append(cost, price)
		caps = append(caps, mask)
	}
	var count int
	fmt.Fscan(in, &count)
	// the wanted caps get the bits 0, 1, ... of a smaller mask
	bit := make([]int, n)
	wanted := 0
	for k := 0; k < count; k++ {
		var cap int
		fmt.Fscan(in, &cap)
		if bit[cap-1] == 0 {
			bit[cap-1] = 1 << wanted
			wanted++
		}
	}
	full := 1<<wanted - 1
	// offers that hold each wanted cap, as a price and the bits they leave
	byLow := make([][]offer, wanted)
	for j := range cost {
		mask := 0
		for i := 0; i < n; i++ {
			if caps[j]>>i&1 == 1 {
				mask |= bit[i]
			}
		}
		for i := 0; i < wanted; i++ {
			if mask>>i&1 == 1 {
				byLow[i] = append(byLow[i], offer{cost[j], full &^ mask})
			}
		}
	}
	// cheapest[s]: the least money that buys every cap of the set s; some
	// offer must hold its lowest cap
	cheapest := make([]int, full+1)
	for s := 1; s <= full; s++ {
		least := -1
		for _, o := range byLow[bits.TrailingZeros(uint(s))] {
			if value := o.cost + cheapest[s&o.keep]; least < 0 || value < least {
				least = value
			}
		}
		cheapest[s] = least
	}
	fmt.Println(cheapest[full])
}
