package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strconv"
)

const (
	maxBits = 128
	half    = 64
	word    = 32
	decimal = 10
)

// a 128-bit number as its high and low 64-bit halves
type wide struct{ hi, lo uint64 }

func bitLength(x wide) int {
	if x.hi != 0 {
		return maxBits - bits.LeadingZeros64(x.hi)
	}
	return half - bits.LeadingZeros64(x.lo)
}

func atLeast(x, y wide) bool {
	return x.hi > y.hi || (x.hi == y.hi && x.lo >= y.lo)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() uint64 {
		sc.Scan()
		v, _ := strconv.ParseUint(sc.Text(), decimal, word)
		return v
	}
	n := int(next())
	a := make([]wide, n)
	for i := range a {
		w1, w2, w3, w4 := next(), next(), next(), next()
		a[i] = wide{w1<<word | w2, w3<<word | w4}
	}
	// a number of bit length L is at least every power of ten that is
	// shorter, and at least the one power of length L only if it reaches it
	var base [maxBits + 1]int
	var has [maxBits + 1]bool
	var limit [maxBits + 1]wide
	p := wide{0, decimal}
	for {
		l := bitLength(p)
		has[l] = true
		limit[l] = p
		for k := l + 1; k <= maxBits; k++ {
			base[k]++
		}
		if p.hi > ^uint64(0)/decimal {
			break
		}
		carry, lo := bits.Mul64(p.lo, decimal)
		p = wide{p.hi*decimal + carry, lo}
	}
	total := int64(0)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			x := wide{a[i].hi ^ a[j].hi, a[i].lo ^ a[j].lo}
			l := bitLength(x)
			total += int64(base[l])
			if has[l] && atLeast(x, limit[l]) {
				total++
			}
		}
	}
	fmt.Println(2 * total) // every pair counts in both orders
}
