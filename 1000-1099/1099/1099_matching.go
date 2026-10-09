package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	n                   int
	adj                 [][]int
	match, parent, base []int
	used, blossom       []bool
)

func lca(a, b int) int {
	seen := make([]bool, n)
	for {
		a = base[a]
		seen[a] = true
		if match[a] < 0 {
			break
		}
		a = parent[match[a]]
	}
	for {
		b = base[b]
		if seen[b] {
			return b
		}
		b = parent[match[b]]
	}
}

func mark(v, b, child int) {
	for base[v] != b {
		blossom[base[v]], blossom[base[match[v]]] = true, true
		parent[v] = child
		child = match[v]
		v = parent[match[v]]
	}
}

// findPath is Edmonds' search from an exposed vertex: an alternating tree
// whose odd cycles (blossoms) are shrunk into their base vertex
func findPath(root int) int {
	used = make([]bool, n)
	parent = make([]int, n)
	for i := range parent {
		parent[i], base[i] = -1, i
	}
	used[root] = true
	queue := []int{root}
	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		for _, to := range adj[v] {
			if base[v] == base[to] || match[v] == to {
				continue
			}
			if to == root || (match[to] >= 0 && parent[match[to]] >= 0) {
				b := lca(v, to)
				blossom = make([]bool, n)
				mark(v, b, to)
				mark(to, b, v)
				for i := 0; i < n; i++ {
					if blossom[base[i]] {
						base[i] = b
						if !used[i] {
							used[i] = true
							queue = append(queue, i)
						}
					}
				}
			} else if parent[to] < 0 {
				parent[to] = v
				if match[to] < 0 {
					return to
				}
				used[match[to]] = true
				queue = append(queue, match[to])
			}
		}
	}
	return -1
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	var nums []int
	for sc.Scan() {
		v, _ := strconv.Atoi(sc.Text())
		nums = append(nums, v)
	}
	n = nums[0]
	seen := make([]map[int]bool, n)
	adj = make([][]int, n)
	for i := range seen {
		seen[i] = map[int]bool{}
	}
	for i := 1; i+1 < len(nums); i += 2 {
		a, b := nums[i]-1, nums[i+1]-1
		if a != b && a >= 0 && a < n && b >= 0 && b < n && !seen[a][b] {
			seen[a][b], seen[b][a] = true, true
			adj[a] = append(adj[a], b)
			adj[b] = append(adj[b], a)
		}
	}
	match = make([]int, n)
	base = make([]int, n)
	for i := range match {
		match[i] = -1
	}
	for v := 0; v < n; v++ {
		if match[v] < 0 {
			for _, u := range adj[v] {
				if match[u] < 0 {
					match[u], match[v] = v, u
					break
				}
			}
		}
	}
	for root := 0; root < n; root++ {
		if match[root] < 0 && len(adj[root]) > 0 {
			for v := findPath(root); v >= 0; {
				pv := parent[v]
				next := match[pv]
				match[v], match[pv] = pv, v
				v = next
			}
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	count := 0
	for v := 0; v < n; v++ {
		if v < match[v] {
			count += 2
		}
	}
	fmt.Fprintln(w, count)
	for v := 0; v < n; v++ {
		if v < match[v] {
			fmt.Fprintln(w, v+1, match[v]+1)
		}
	}
}
