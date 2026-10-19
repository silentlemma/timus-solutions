package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, k := next(), next()
	ex, ey := make([]int, n), make([]int, n)
	incident := make([][]int, k+1)
	for i := 0; i < n; i++ {
		ex[i], ey[i] = next(), next()
		incident[ex[i]] = append(incident[ex[i]], i)
		incident[ey[i]] = append(incident[ey[i]], i)
	}
	winner := make([]int, n)
	degree := make([]int, k+1)
	open := func(v int) int { // a pair of v without a winner yet
		for _, i := range incident[v] {
			if winner[i] == 0 {
				return i
			}
		}
		return -1
	}
	// every team may win at most one pair: a team with a single open pair takes
	// it, which never hurts, and the pair is closed for the other team
	var leaves []int
	for v := 1; v <= k; v++ {
		degree[v] = len(incident[v])
		if degree[v] == 1 {
			leaves = append(leaves, v)
		}
	}
	for len(leaves) > 0 {
		v := leaves[len(leaves)-1]
		leaves = leaves[:len(leaves)-1]
		if degree[v] != 1 {
			continue
		}
		i := open(v)
		u := ex[i] + ey[i] - v
		winner[i] = v
		degree[v] = 0
		degree[u]--
		if degree[u] == 1 {
			leaves = append(leaves, u)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// what is left must be disjoint cycles (every degree 2); each cycle is walked
	// and every pair is won by the team it leads to
	for v := 1; v <= k; v++ {
		if degree[v] > 2 {
			out.WriteString("No\n")
			return
		}
	}
	for start := 1; start <= k; start++ {
		if degree[start] != 2 {
			continue
		}
		for v := start; ; {
			i := open(v)
			u := ex[i] + ey[i] - v
			winner[i] = u
			degree[v]--
			degree[u]--
			v = u
			if v == start {
				break
			}
		}
	}
	out.WriteString("Yes\n")
	for _, w := range winner {
		out.WriteString(strconv.Itoa(w))
		out.WriteByte('\n')
	}
}
