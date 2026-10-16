package main

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	mod = 1000000009
	// with six sectors the jumps forward and back by three land on the same
	// sector, so that table is counted on its own
	six     = 6
	sixWays = 12
	// from seven sectors on the counts follow a linear recurrence of order
	// 19, found with the Berlekamp-Massey method from counts made by a
	// search over the sectors and checked on every table up to 200 sectors
	firstSectors = 7
	stepText     = "1 2 -1 1 -2 -1 -2 -3 3 -1 5 2 2 1 -2 0 -3 0 -1"
	firstText    = `46 144 110 312 290 670 706 1538 1732 3504 4288 8098
		10568 19044 26042 45222 64220 108382 158324`
)

var steps, first []int64

func parse(text string) []int64 {
	var values []int64
	for _, w := range strings.Fields(text) {
		v, _ := strconv.Atoi(w)
		values = append(values, int64(v))
	}
	return values
}

// times multiplies two polynomials modulo the recurrence's characteristic
// polynomial x^k - sum of steps[j] x^(k-1-j)
func times(p, q []int64) []int64 {
	k := len(steps)
	full := make([]int64, 2*k-1)
	for i := 0; i < k; i++ {
		if p[i] == 0 {
			continue
		}
		for j := 0; j < k; j++ {
			full[i+j] = (full[i+j] + p[i]*q[j]) % mod
		}
	}
	for i := 2*k - 2; i >= k; i-- {
		if full[i] == 0 {
			continue
		}
		for j := 0; j < k; j++ {
			full[i-1-j] = ((full[i-1-j]+full[i]*steps[j])%mod + mod) % mod
		}
	}
	return full[:k]
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	if n == six {
		fmt.Println(sixWays)
		return
	}
	steps = parse(stepText)
	first = parse(firstText)
	k := len(steps)
	// x^(n - 7) reduced by the recurrence gives the count as a mix of the
	// first k counts
	power := make([]int64, k)
	base := make([]int64, k)
	power[0], base[1] = 1, 1
	for e := n - firstSectors; e > 0; e >>= 1 {
		if e&1 == 1 {
			power = times(power, base)
		}
		base = times(base, base)
	}
	var answer int64
	for i := 0; i < k; i++ {
		answer = (answer + power[i]*first[i]) % mod
	}
	fmt.Println(answer)
}
