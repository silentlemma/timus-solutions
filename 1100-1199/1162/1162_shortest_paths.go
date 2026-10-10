package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strings"
)

type exchange struct {
	from, to  int
	rate, fee int64
}

func scaled(text string, places int) *big.Int {
	parts := strings.SplitN(text, ".", 2)
	fraction := ""
	if len(parts) == 2 {
		fraction = parts[1]
	}
	value, _ := new(big.Int).SetString(parts[0]+fraction+strings.Repeat("0", places-len(fraction)), 10)
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, s int
	var text string
	fmt.Fscan(in, &n, &m, &s, &text)
	places := 2
	if dot := strings.IndexByte(text, '.'); dot >= 0 && len(text)-dot-1 > places {
		places = len(text) - dot - 1
	}
	v := scaled(text, places)
	unit := scaled("1", places-2)
	hundred := big.NewInt(100)
	var edges []exchange
	for k := 0; k < m; k++ {
		var a, b int
		var rab, cab, rba, cba string
		fmt.Fscan(in, &a, &b, &rab, &cab, &rba, &cba)
		edges = append(edges, exchange{a, b, scaled(rab, 2).Int64(), scaled(cab, 2).Int64()},
			exchange{b, a, scaled(rba, 2).Int64(), scaled(cba, 2).Int64()})
	}
	// All amounts share an exact denominator, multiplied by 100 each pass.
	// A change on pass n means a reachable gaining cycle.
	best := make([]*big.Int, n+1)
	best[s] = v
	changed := false
	for pass := 0; pass < n; pass++ {
		after := make([]*big.Int, n+1)
		for c, amount := range best {
			if amount != nil {
				after[c] = new(big.Int).Mul(amount, hundred)
			}
		}
		changed = false
		for _, e := range edges {
			cost := new(big.Int).Mul(unit, big.NewInt(e.fee))
			if best[e.from] != nil && best[e.from].Cmp(cost) >= 0 {
				got := new(big.Int).Sub(best[e.from], cost)
				got.Mul(got, big.NewInt(e.rate))
				if after[e.to] == nil || got.Cmp(after[e.to]) > 0 {
					after[e.to] = got
					changed = true
				}
			}
		}
		best = after
		unit = new(big.Int).Mul(unit, hundred)
		v = new(big.Int).Mul(v, hundred)
		if best[s].Cmp(v) > 0 || !changed {
			break
		}
	}
	if best[s].Cmp(v) > 0 || changed {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
