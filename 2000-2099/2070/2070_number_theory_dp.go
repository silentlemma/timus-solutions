package main

import (
	"fmt"
	"math"
)

const fourthRootLimit = 1000
const firstHigherExponent = 4

func floorSqrt(value int64) int {
	root := int64(math.Sqrt(float64(value)))
	for (root+1)*(root+1) <= value {
		root++
	}
	for root*root > value {
		root--
	}
	return int(root)
}

func primeCount(n int) int {
	if n < 2 {
		return 0
	}
	root := floorSqrt(int64(n))
	small, large := make([]int, root+1), make([]int, root+1)
	for i := 1; i <= root; i++ {
		small[i] = i - 1
		large[i] = n/i - 1
	}
	for prime := 2; prime <= root; prime++ {
		if small[prime] == small[prime-1] {
			continue
		}
		before, square := small[prime-1], prime*prime
		// Remove multiples of this prime with remaining factor >= prime.
		// Stored quotient values suffice for every g(v/prime) lookup.
		for i := 1; i <= root && i <= n/square; i++ {
			reduced := n / i / prime
			var count int
			if reduced <= root {
				count = small[reduced]
			} else {
				count = large[n/reduced]
			}
			large[i] -= count - before
		}
		// Descending values preserve the previous-prime layer.
		for value := root; value >= square; value-- {
			small[value] -= small[value/prime] - before
		}
	}
	return large[1]
}

func main() {
	var left, right int64
	fmt.Scan(&left, &right)
	bad := int64(primeCount(floorSqrt(right)) - primeCount(floorSqrt(left-1)))
	composite := make([]bool, fourthRootLimit+1)
	composite[0], composite[1] = true, true
	for p := 2; p*p <= fourthRootLimit; p++ {
		if !composite[p] {
			for multiple := p * p; multiple <= fourthRootLimit; multiple += p {
				composite[multiple] = true
			}
		}
	}
	// k+1 prime and k>=2 implies even k. Beyond squares p^4<=R,
	// so a sieve to the fourth root suffices for all remaining bases.
	for prime := 2; prime <= fourthRootLimit; prime++ {
		if composite[prime] {
			continue
		}
		square := int64(prime) * int64(prime)
		if square > right/square {
			break
		}
		power, exponent := square*square, firstHigherExponent
		for {
			if power >= left && !composite[exponent+1] {
				bad++
			}
			if power > right/square {
				break
			}
			power *= square
			exponent += 2
		}
	}
	fmt.Println(right - left + 1 - bad)
}
