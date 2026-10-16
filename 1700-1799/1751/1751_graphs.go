package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const wordBits = 64

var (
	t, index, low, group []int
	p                    []float64
	onStack              []bool
	deps, groups         [][]int
	stack                []int
	counter              int
)

// hypotheses on one cycle of dependencies are all true or all false,
// and Tarjan's method finds those groups, dependencies first
func visit(v int) {
	index[v], low[v] = counter, counter
	counter++
	stack = append(stack, v)
	onStack[v] = true
	for _, w := range deps[v] {
		if index[w] < 0 {
			visit(w)
			if low[w] < low[v] {
				low[v] = low[w]
			}
		} else if onStack[w] && index[w] < low[v] {
			low[v] = index[w]
		}
	}
	if low[v] == index[v] {
		var members []int
		for {
			w := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			onStack[w] = false
			group[w] = len(groups)
			members = append(members, w)
			if w == v {
				break
			}
		}
		groups = append(groups, members)
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	t = make([]int, n)
	p = make([]float64, n)
	deps = make([][]int, n)
	for i := 0; i < n; i++ {
		var k int
		fmt.Fscan(in, &t[i], &p[i], &k)
		deps[i] = make([]int, k)
		for j := range deps[i] {
			fmt.Fscan(in, &deps[i][j])
			deps[i][j]--
		}
	}
	index = make([]int, n)
	low = make([]int, n)
	group = make([]int, n)
	onStack = make([]bool, n)
	for i := range index {
		index[i] = -1
	}
	for v := 0; v < n; v++ {
		if index[v] < 0 {
			visit(v)
		}
	}
	// a group is worth checking only when every group it rests on is fully
	// admissible; inside it, checks stop at the first failure, so the order
	// by t / (1 - p) is the cheapest
	count := len(groups)
	cost := make([]float64, count)
	sound := make([]float64, count)
	words := (count + wordBits - 1) / wordBits
	reach := make([][]uint64, count)
	for g, members := range groups {
		sort.Slice(members, func(i, j int) bool {
			a, b := members[i], members[j]
			return float64(t[a])*(1-p[b]) < float64(t[b])*(1-p[a])
		})
		still, expected := 1.0, 0.0
		for _, v := range members {
			expected += still * float64(t[v])
			still *= p[v]
		}
		cost[g], sound[g] = expected, still
		reach[g] = make([]uint64, words)
		for _, v := range members {
			for _, w := range deps[v] {
				h := group[w]
				if h == g || reach[g][h/wordBits]>>(h%wordBits)&1 == 1 {
					continue
				}
				for x := range reach[g] {
					reach[g][x] |= reach[h][x]
				}
				reach[g][h/wordBits] |= 1 << (h % wordBits)
			}
		}
	}
	answer := 0.0
	for g := 0; g < count; g++ {
		chance := 1.0
		for h := 0; h < count; h++ {
			if reach[g][h/wordBits]>>(h%wordBits)&1 == 1 {
				chance *= sound[h]
			}
		}
		answer += chance * cost[g]
	}
	fmt.Printf("%.3f\n", answer)
}
