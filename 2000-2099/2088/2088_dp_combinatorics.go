package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"sort"
)

const (
	limit = 100
	mod   = int64(1000000007)
)

type score struct {
	exact   *big.Int
	residue int64
}

type event struct {
	value  score
	color  int
	amount int
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func power(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent%2 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		exponent /= 2
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var k, t int
	if _, err := fmt.Fscan(in, &k, &t); err != nil {
		return
	}
	c := make([]int, k+1)
	s := make([]int, k+1)
	r := make([]int, k+1)
	for i := range c {
		fmt.Fscan(in, &c[i])
	}
	n := 0
	for i := range s {
		fmt.Fscan(in, &s[i])
		r[i] = c[i] - s[i]
		n += r[i]
	}
	var x, y int
	fmt.Fscan(in, &x, &y)
	m := n - t

	var choose [limit + 1][limit + 1]big.Int
	var chooseMod [limit + 1][limit + 1]int64
	for i := 0; i <= limit; i++ {
		choose[i][0].SetInt64(1)
		choose[i][i].SetInt64(1)
		chooseMod[i][0] = 1
		chooseMod[i][i] = 1
		for j := 1; j < i; j++ {
			choose[i][j].Add(&choose[i-1][j-1], &choose[i-1][j])
			chooseMod[i][j] = (chooseMod[i-1][j-1] + chooseMod[i-1][j]) % mod
		}
	}

	ways := make([][]big.Int, m+1)
	waysMod := make([][]int64, m+1)
	modBig := big.NewInt(mod)
	for good := 0; good <= m; good++ {
		ways[good] = make([]big.Int, y+1)
		waysMod[good] = make([]int64, y+1)
		var total, term, residue big.Int
		for bound := 0; bound <= y; bound++ {
			other := y - bound
			if bound <= good && other <= m-good {
				term.Mul(&choose[good][bound], &choose[m-good][other])
				total.Add(&total, &term)
			}
			ways[good][bound].Set(&total)
			waysMod[good][bound] = residue.Mod(&total, modBig).Int64()
		}
	}

	answer := int64(0)
	var zero big.Int
	for wild := max(0, t-(n-r[0])); wild <= min(r[0], t); wild++ {
		remaining := t - wild
		valueAt := func(color, amount int) score {
			hand := s[0] + wild + s[color] + amount
			good := c[0] + c[color] - hand
			if hand < x || good > m {
				return score{&zero, 0}
			}
			bound := min(y, hand-x)
			return score{&ways[good][bound], waysMod[good][bound]}
		}
		baseline := score{&zero, 0}
		for color := 1; color <= k; color++ {
			value := valueAt(color, 0)
			if value.exact.Cmp(baseline.exact) > 0 {
				baseline = value
			}
		}
		events := make([]event, 0, n)
		for color := 1; color <= k; color++ {
			for amount := 1; amount <= min(r[color], remaining); amount++ {
				value := valueAt(color, amount)
				if value.exact.Cmp(baseline.exact) < 0 {
					value = baseline
				}
				events = append(events, event{value, color, amount})
			}
		}
		sort.Slice(events, func(i, j int) bool {
			comparison := events[i].value.exact.Cmp(events[j].value.exact)
			if comparison != 0 {
				return comparison < 0
			}
			if events[i].color != events[j].color {
				return events[i].color < events[j].color
			}
			return events[i].amount < events[j].amount
		})

		// Each factor contains the draws admitted for one color so far.
		dp := make([]int64, remaining+1)
		dp[0] = 1
		caps := make([]int, k+1)
		conditional := baseline.residue * dp[remaining] % mod
		for _, current := range events {
			color, amount := current.color, current.amount
			old := dp[remaining]
			quotient := make([]int64, remaining-amount+1)
			coefficients := &chooseMod[r[color]]
			// Formal division removes the old factor, whose constant is one.
			for degree := range quotient {
				value := dp[degree]
				for j := 1; j <= min(caps[color], degree); j++ {
					value = (value - coefficients[j]*quotient[degree-j]%mod + mod) % mod
				}
				quotient[degree] = value
			}
			for degree, value := range quotient {
				index := degree + amount
				dp[index] = (dp[index] + coefficients[amount]*value) % mod
			}
			caps[color] = amount
			added := (dp[remaining] - old + mod) % mod
			conditional = (conditional + current.value.residue*added) % mod
		}
		answer = (answer + chooseMod[r[0]][wild]*conditional) % mod
	}
	denominator := chooseMod[n][t] * chooseMod[m][y] % mod
	fmt.Println(answer * power(denominator, mod-2) % mod)
}
