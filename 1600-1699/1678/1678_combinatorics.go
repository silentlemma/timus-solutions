package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strings"
)

const (
	ranks     = "23456789TJQKA"
	rankCount = 13
)

var (
	n, m, k   int
	combos    [][]int
	bestCache = map[string]int{}
	fact      []float64
	rivalMemo = map[string][]float64{}
)

func sortDown(a []int) { sort.Sort(sort.Reverse(sort.IntSlice(a))) }

// key turns a shape (sorted counts, all below 256) into a map key.
func key(shape []int) string {
	b := make([]byte, len(shape))
	for i, x := range shape {
		b[i] = byte(x)
	}
	return string(b)
}

// best is the most valuable combination a hand with these sorted counts
// holds, or -1: (v1, ..., vL) fits when the i-th largest count is at
// least the i-th v.
func best(hand []int) int {
	h := key(hand)
	if v, ok := bestCache[h]; ok {
		return v
	}
	found := -1
	for c := len(combos) - 1; c >= 0 && found < 0; c-- {
		need := combos[c]
		fits := len(need) <= len(hand)
		for i := 0; fits && i < len(need); i++ {
			fits = hand[i] >= need[i]
		}
		if fits {
			found = c
		}
	}
	bestCache[h] = found
	return found
}

// partitions lists the partitions of total into at most parts positive
// parts, each decreasing.
func partitions(total, parts int) [][]int {
	var out [][]int
	var cur []int
	var build func(rest, top int)
	build = func(rest, top int) {
		if rest == 0 {
			out = append(out, append([]int(nil), cur...))
			return
		}
		if len(cur) == parts {
			return
		}
		for x := min(rest, top); x > 0; x-- {
			cur = append(cur, x)
			build(rest-x, x)
			cur = cur[:len(cur)-1]
		}
	}
	build(total, total)
	return out
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type state struct {
	shape string
	used  int
}

// the chance, for each combination, that a rival's best one is cheaper,
// shifted by one place. Ranks with equal common counts are interchangeable,
// so each group takes a partition of its share of the rival's cards
func rival(common []int) []float64 {
	ck := key(common)
	if v, ok := rivalMemo[ck]; ok {
		return v
	}
	groups := map[int]int{}
	var order []int
	for _, v := range common {
		if groups[v] == 0 {
			order = append(order, v)
		}
		groups[v]++
	}
	states := map[state]float64{{"", 0}: 1}
	for _, v := range order {
		g := groups[v]
		next := map[state]float64{}
		for st, w := range states {
			for s := 0; s+st.used <= m; s++ {
				for _, p := range partitions(s, g) {
					ways := fact[g] / fact[g-len(p)]
					mult := map[int]int{}
					for _, x := range p {
						mult[x]++
						ways /= fact[x]
					}
					for _, c := range mult {
						ways /= fact[c]
					}
					merged := []int{}
					for i := 0; i < len(st.shape); i++ {
						merged = append(merged, int(st.shape[i]))
					}
					for _, x := range p {
						merged = append(merged, v+x)
					}
					if v > 0 {
						for i := len(p); i < g; i++ {
							merged = append(merged, v)
						}
					}
					sortDown(merged)
					next[state{key(merged), st.used + s}] += w * ways
				}
			}
		}
		states = next
	}
	scale := fact[m] / math.Pow(rankCount, float64(m))
	dist := make([]float64, len(combos)+1)
	for st, w := range states {
		if st.used == m {
			shape := make([]int, len(st.shape))
			for i := range shape {
				shape[i] = int(st.shape[i])
			}
			dist[best(shape)+1] += w * scale
		}
	}
	below := make([]float64, len(combos)+1)
	for c := 0; c < len(combos); c++ {
		below[c+1] = below[c] + dist[c]
	}
	rivalMemo[ck] = below
	return below
}

func main() {
	in := bufio.NewReader(os.Stdin)
	readLine := func() string {
		line, _ := in.ReadString('\n')
		return strings.TrimRight(line, "\r\n")
	}
	fmt.Sscan(readLine(), &n, &m, &k)
	own, shown := make([]int, rankCount), make([]int, rankCount)
	for _, c := range readLine() {
		if i := strings.IndexRune(ranks, c); i >= 0 {
			own[i]++
		}
	}
	shownCount := 0
	for _, c := range readLine() {
		if i := strings.IndexRune(ranks, c); i >= 0 {
			shown[i]++
			shownCount++
		}
	}
	var count int
	fmt.Fscan(in, &count)
	for c := 0; c < count; c++ {
		var size int
		fmt.Fscan(in, &size)
		need := make([]int, size)
		for i := range need {
			fmt.Fscan(in, &need[i])
		}
		sortDown(need)
		combos = append(combos, need)
	}
	fact = make([]float64, m+k+rankCount+1)
	fact[0] = 1
	for i := 1; i < len(fact); i++ {
		fact[i] = fact[i-1] * float64(i)
	}
	// the hidden common cards: every way to spread them over the ranks
	hidden := k - shownCount
	answer, scale := 0.0, fact[hidden]/math.Pow(rankCount, float64(hidden))
	common := make([]int, rankCount)
	var spread func(r, left int, weight float64)
	spread = func(r, left int, weight float64) {
		if r == rankCount-1 {
			common[r] = shown[r] + left
			weight /= fact[left]
			var mine []int
			for i := 0; i < rankCount; i++ {
				if common[i]+own[i] > 0 {
					mine = append(mine, common[i]+own[i])
				}
			}
			sortDown(mine)
			if top := best(mine); top >= 0 {
				sorted := append([]int(nil), common...)
				sortDown(sorted)
				beat := rival(sorted)[top+1]
				answer += weight * scale * math.Pow(beat, float64(n-1))
			}
			return
		}
		for x := 0; x <= left; x++ {
			common[r] = shown[r] + x
			spread(r+1, left-x, weight/fact[x])
		}
	}
	spread(0, hidden, 1)
	fmt.Printf("%.10f\n", answer)
}
