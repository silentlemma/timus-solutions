package main

import (
	"bufio"
	"math/bits"
	"os"
	"sort"
	"strconv"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, s, d := next(), next(), next()
	type planet struct{ dist, race int }
	planets := make([]planet, n)
	for i := range planets {
		planets[i] = planet{next(), next()}
	}
	sort.Slice(planets, func(i, j int) bool { return planets[i].dist < planets[j].dist })
	dist, race := make([]int, n), make([]int, n)
	for i, p := range planets {
		dist[i], race[i] = p.dist, p.race
	}
	// pieces of planets with gaps of at most d: the tourist moves only
	// inside a piece cut by the range [low, high]
	piece, first := make([]int, n), []int{0}
	for i := 1; i < n; i++ {
		if dist[i]-dist[i-1] > d {
			first = append(first, i)
		}
		piece[i] = len(first) - 1
	}
	first = append(first, n)
	pieces := len(first) - 1
	// head[i]: races from the start of i's piece to i; tail[i]: from i to
	// its end; whole[p]: races of piece p
	head, tail, whole := make([]int, n), make([]int, n), make([]int, pieces)
	mark := make([]int, s+1)
	for i := range mark {
		mark[i] = -1
	}
	for p := 0; p < pieces; p++ {
		seen := 0
		for i := first[p]; i < first[p+1]; i++ {
			if mark[race[i]] != p {
				mark[race[i]] = p
				seen++
			}
			head[i] = seen
		}
		whole[p] = seen
		seen = 0
		for i := first[p+1] - 1; i >= first[p]; i-- {
			if mark[race[i]] != -2-p {
				mark[race[i]] = -2 - p
				seen++
			}
			tail[i] = seen
		}
	}
	// sparse table of the largest whole piece over ranges of pieces
	table := [][]int{whole}
	for step := 1; 2*step <= pieces; step *= 2 {
		last := table[len(table)-1]
		next := make([]int, pieces-2*step+1)
		for i := range next {
			next[i] = max(last[i], last[i+step])
		}
		table = append(table, next)
	}
	largest := func(lo, hi int) int {
		// the largest whole piece among pieces lo..hi - 1
		if lo >= hi {
			return 0
		}
		level := bits.Len(uint(hi-lo)) - 1
		return max(table[level][lo], table[level][hi-1<<level])
	}
	m := next()
	answer := make([]int, m)
	type query struct{ right, left, tourist int }
	var inside []query
	for t := 0; t < m; t++ {
		low, high := next(), next()
		lo := sort.SearchInts(dist, low)
		hi := sort.SearchInts(dist, high+1) - 1
		if lo > hi {
			continue
		}
		if piece[lo] == piece[hi] {
			inside = append(inside, query{hi, lo, t})
		} else {
			answer[t] = max(max(tail[lo], head[hi]), largest(piece[lo]+1, piece[hi]))
		}
	}
	// distinct races in a range: going right, count each race only at its
	// latest planet, in a Fenwick tree
	sort.Slice(inside, func(i, j int) bool { return inside[i].right < inside[j].right })
	tree := make([]int, n+1)
	latest := make([]int, s+1)
	for i := range latest {
		latest[i] = -1
	}
	add := func(k, v int) {
		for k++; k <= n; k += k & -k {
			tree[k] += v
		}
	}
	prefix := func(k int) int {
		total := 0
		for ; k > 0; k -= k & -k {
			total += tree[k]
		}
		return total
	}
	j := 0
	for i := 0; i < n; i++ {
		if latest[race[i]] >= 0 {
			add(latest[race[i]], -1)
		}
		latest[race[i]] = i
		add(i, 1)
		for ; j < len(inside) && inside[j].right == i; j++ {
			answer[inside[j].tourist] = prefix(i+1) - prefix(inside[j].left)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, a := range answer {
		out.WriteString(strconv.Itoa(a))
		out.WriteByte('\n')
	}
}
