package main

import "fmt"

const mod = 1000000007

func main() {
	var level int64
	fmt.Scan(&level)
	// the numbers form a perfect binary tree, and the mole walks the tree
	// distance; summing over every edge the nodes below it times the nodes
	// above it gives 2^l ((l - 1)(2^l + 1) - 2 (2^l - 2))
	power, base := int64(1), int64(2)
	for e := level; e > 0; e >>= 1 {
		if e&1 == 1 {
			power = power * base % mod
		}
		base = base * base % mod
	}
	l := level % mod
	inner := ((l-1+mod)%mod*((power+1)%mod)%mod - 2*((power-2+mod)%mod)%mod + mod) % mod
	fmt.Println(power * inner % mod)
}
