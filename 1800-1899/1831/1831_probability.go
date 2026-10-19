package main

import (
	"fmt"
	"math"
)

const base = 10

// the chance that two random digits from first .. 9 plus the incoming
// carry reach 10
func carryChance(first, extra int) float64 {
	hits, total := 0, 0
	for a := first; a < base; a++ {
		for b := first; b < base; b++ {
			if a+b+extra >= base {
				hits++
			}
			total++
		}
	}
	return float64(hits) / float64(total)
}

// the chance that one place with digits from first .. 9 shows a and b
func pairChance(first, a, b int) float64 {
	side := float64(base - first)
	if a == b {
		return 1 / (side * side)
	}
	return 2 / (side * side)
}

func main() {
	var k int
	if _, err := fmt.Scan(&k); err != nil {
		return
	}
	// every place costs one written digit and one sum; a carry costs a mark
	// and, unless it leaves the last place, one more second to add it in,
	// a carry out of the last place is written as a digit
	expected, carry := 2*float64(k), 0.0
	for place := 0; place < k; place++ {
		first := 0
		if place == k-1 {
			first = 1
		}
		carry = (1-carry)*carryChance(first, 0) + carry*carryChance(first, 1)
		expected += 2 * carry
	}
	// the first sum of two digits both above 1 takes a second more
	for a := 2; a < base; a++ {
		for b := a; b < base; b++ {
			miss := math.Pow(1-pairChance(0, a, b), float64(k-1)) * (1 - pairChance(1, a, b))
			expected += 1 - miss
		}
	}
	fmt.Printf("%.8f\n", expected)
}
