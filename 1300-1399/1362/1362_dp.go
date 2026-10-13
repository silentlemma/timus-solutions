package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const bufferSize = 1 << 20 // the input can take a megabyte or so

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	readInt := func() int {
		n, c := 0, byte(0)
		for c, _ = in.ReadByte(); c == ' ' || c == '\n' || c == '\r'; c, _ = in.ReadByte() {
		}
		for ; c >= '0' && c <= '9'; c, _ = in.ReadByte() {
			n = n*10 + int(c-'0')
		}
		return n
	}
	n := readInt()
	adj := make([][]int, n+1)
	for boss := 1; boss <= n; boss++ {
		for v := readInt(); v != 0; v = readInt() {
			adj[boss] = append(adj[boss], v)
			adj[v] = append(adj[v], boss)
		}
	}
	root := readInt()
	// calls go both up and down, so the news spreads over the tree rooted
	// at Tanya; order parents before children
	parent := make([]int, n+1)
	parent[root] = -1
	order := []int{root}
	for i := 0; i < len(order); i++ {
		v := order[i]
		for _, u := range adj[v] {
			if u != parent[v] {
				parent[u] = v
				order = append(order, u)
			}
		}
	}
	// the time of v is what it needs to tell its whole subtree; the slowest
	// subtrees are called first, the i-th call starting at minute i
	time := make([]int, n+1)
	kids := make([][]int, n+1)
	for i := len(order) - 1; i >= 0; i-- {
		v := order[i]
		sort.Sort(sort.Reverse(sort.IntSlice(kids[v])))
		for j, t := range kids[v] {
			if t+j+1 > time[v] {
				time[v] = t + j + 1
			}
		}
		if parent[v] > 0 {
			kids[parent[v]] = append(kids[parent[v]], time[v])
		}
	}
	fmt.Println(time[root])
}
