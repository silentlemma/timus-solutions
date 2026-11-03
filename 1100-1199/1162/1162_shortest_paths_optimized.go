package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

const rateDigits = 2
const integerBits = 64
const decimalScale int64 = 100

func scaled(text string, places int) string {
	text = strings.TrimPrefix(text, "+")
	parts := strings.SplitN(text, ".", 2)
	fraction := ""
	if len(parts) == 2 {
		fraction = parts[1]
	}
	return parts[0] + fraction + strings.Repeat("0", places-len(fraction))
}

func small(text string) int64 {
	value, _ := strconv.ParseInt(scaled(text, rateDigits), 10, integerBits)
	return value
}

type edge struct {
	from, to  int
	rate, fee int64
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, start int
	var text string
	fmt.Fscan(in, &n, &m, &start, &text)
	start--
	places := rateDigits
	if dot := strings.IndexByte(text, '.'); dot >= 0 && len(text)-dot-1 > places {
		places = len(text) - dot - 1
	}
	initial, _ := new(big.Int).SetString(scaled(text, places), 10)
	// Nonnegative commissions make zero capital an absorbing state.
	if initial.Sign() == 0 {
		fmt.Println("NO")
		return
	}
	var unit, hundred big.Int
	unit.SetString("1"+strings.Repeat("0", places-rateDigits), 10)
	hundred.SetInt64(decimalScale)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	root := func(v int) int {
		for parent[v] != v {
			parent[v] = parent[parent[v]]
			v = parent[v]
		}
		return v
	}
	edges := make([]edge, 0, 2*m)
	for i := 0; i < m; i++ {
		var a, b int
		var rab, cab, rba, cba string
		fmt.Fscan(in, &a, &b, &rab, &cab, &rba, &cba)
		a--
		b--
		parent[root(a)] = root(b)
		edges = append(edges, edge{a, b, small(rab), small(cab)}, edge{b, a, small(rba), small(cba)})
	}
	component, count := root(start), 0
	index := make([]int, n)
	for i := range index {
		index[i] = -1
		if root(i) == component {
			index[i] = count
			count++
		}
	}
	kept := 0
	for _, e := range edges {
		if index[e.from] >= 0 {
			e.from, e.to = index[e.from], index[e.to]
			edges[kept] = e
			kept++
		}
	}
	edges = edges[:kept]
	start = index[start]
	rates, fees := make([]big.Int, len(edges)), make([]big.Int, len(edges))
	for i, e := range edges {
		rates[i].SetInt64(e.rate)
		fees[i].SetInt64(e.fee)
	}
	best, after := make([]big.Int, count), make([]big.Int, count)
	reached, next := make([]bool, count), make([]bool, count)
	best[start].Set(initial)
	reached[start] = true
	var cost, got big.Int
	changed := false
	// Reuse owned buffers and scratch; do not shallow-copy big.Int limbs.
	// Every edge reads only best, preserving the exact per-pass invariant.
	for pass := 0; pass < count; pass++ {
		for i := range best {
			if reached[i] {
				after[i].Mul(&best[i], &hundred)
			}
		}
		copy(next, reached)
		changed = false
		for i, e := range edges {
			if !reached[e.from] {
				continue
			}
			if e.fee == 0 {
				got.Mul(&best[e.from], &rates[i])
			} else {
				cost.Mul(&unit, &fees[i])
				if best[e.from].Cmp(&cost) < 0 {
					continue
				}
				got.Sub(&best[e.from], &cost)
				got.Mul(&got, &rates[i])
			}
			if !next[e.to] || after[e.to].Cmp(&got) < 0 {
				after[e.to].Set(&got)
				next[e.to] = true
				changed = true
			}
		}
		best, after = after, best
		reached, next = next, reached
		unit.Mul(&unit, &hundred)
		initial.Mul(initial, &hundred)
		if best[start].Cmp(initial) > 0 || !changed {
			break
		}
	}
	if best[start].Cmp(initial) > 0 || changed {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
