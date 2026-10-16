package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// the best split of a prime p < 31623 never uses a prime above 700
const bound = 1000

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	p := n
	for d := int64(2); d*d <= n; d++ {
		if n%d == 0 {
			p = d
			break
		}
	}
	// the largest gcd is n / p: the pockets hold n/p times parts adding up
	// to p, and the lcm is n/p times the lcm of the parts. Parts that are
	// powers of distinct primes, padded with ones, give the best lcm
	unit := n / p
	limit := int(p)
	var groups [][]int
	composite := make([]bool, bound)
	for q := 2; q < bound && q < limit; q++ {
		if composite[q] {
			continue
		}
		for m := q * q; m < bound; m += q {
			composite[m] = true
		}
		var powers []int
		for w := q; w < limit; w *= q {
			powers = append(powers, w)
		}
		groups = append(groups, powers)
	}
	// best[s]: the largest log of an lcm of parts with weight at most s
	best := make([]float64, limit+1)
	choices := make([][]byte, len(groups))
	for g, powers := range groups {
		next := append([]float64(nil), best...)
		choice := make([]byte, limit+1)
		for e, w := range powers {
			value := math.Log(float64(w))
			for s := w; s <= limit; s++ {
				if candidate := best[s-w] + value; candidate > next[s] {
					next[s] = candidate
					choice[s] = byte(e + 1)
				}
			}
		}
		best = next
		choices[g] = choice
	}
	var parts []int
	s, used := limit, 0
	for g := len(groups) - 1; g >= 0; g-- {
		if e := choices[g][s]; e > 0 {
			w := groups[g][e-1]
			parts = append(parts, w)
			s -= w
			used += w
		}
	}
	for ; used < limit; used++ {
		parts = append(parts, 1)
	}
	words := make([]string, len(parts))
	for i, part := range parts {
		words[i] = strconv.FormatInt(int64(part)*unit, 10)
	}
	fmt.Println(strings.Join(words, " "))
}
