package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	word := func() string {
		in.Scan()
		return in.Text()
	}
	num := func() int {
		x, _ := strconv.Atoi(word())
		return x
	}
	n := num()
	adj := make([][]int, n+1)
	for i := 0; i < n-1; i++ {
		a, b := num(), num()
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	// heavy-light decomposition: every cave's heavy child continues its chain,
	// and the chains lie consecutively in one segment tree of maxima
	parent, depth := make([]int, n+1), make([]int, n+1)
	parent[1] = -1
	order := []int{1}
	for i := 0; i < len(order); i++ {
		v := order[i]
		for _, u := range adj[v] {
			if u != parent[v] {
				parent[u] = v
				depth[u] = depth[v] + 1
				order = append(order, u)
			}
		}
	}
	size, heavy := make([]int, n+1), make([]int, n+1)
	for i := range size {
		size[i] = 1
	}
	for i := n - 1; i > 0; i-- {
		v := order[i]
		p := parent[v]
		size[p] += size[v]
		if heavy[p] == 0 || size[v] > size[heavy[p]] {
			heavy[p] = v
		}
	}
	head, index := make([]int, n+1), make([]int, n+1)
	next := 0
	for _, v := range order {
		if v == 1 || heavy[parent[v]] != v {
			for u := v; u != 0; u = heavy[u] {
				head[u] = v
				index[u] = next
				next++
			}
		}
	}
	width := 1
	for width < n {
		width *= 2
	}
	tree := make([]int64, 2*width)
	segMax := func(lo, hi int) int64 { // the largest level at the places lo to hi
		var best int64
		for lo, hi = lo+width, hi+width+1; lo < hi; lo, hi = lo>>1, hi>>1 {
			if lo&1 == 1 {
				if tree[lo] > best {
					best = tree[lo]
				}
				lo++
			}
			if hi&1 == 1 {
				hi--
				if tree[hi] > best {
					best = tree[hi]
				}
			}
		}
		return best
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	q := num()
	for i := 0; i < q; i++ {
		kind, u, v := word(), num(), num()
		if kind == "I" {
			at := index[u] + width
			tree[at] += int64(v)
			for at >>= 1; at > 0; at >>= 1 {
				tree[at] = tree[2*at]
				if tree[2*at+1] > tree[at] {
					tree[at] = tree[2*at+1]
				}
			}
			continue
		}
		var best int64
		for head[u] != head[v] {
			if depth[head[u]] < depth[head[v]] {
				u, v = v, u
			}
			if m := segMax(index[head[u]], index[u]); m > best {
				best = m
			}
			u = parent[head[u]]
		}
		lo, hi := index[u], index[v]
		if lo > hi {
			lo, hi = hi, lo
		}
		if m := segMax(lo, hi); m > best {
			best = m
		}
		out.WriteString(strconv.FormatInt(best, 10))
		out.WriteByte('\n')
	}
}
