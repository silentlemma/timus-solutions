package main

import (
	"bufio"
	"container/heap"
	"os"
	"sort"
	"strconv"
)

type minHeap []int

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	var code []int
	for sc.Scan() {
		v, _ := strconv.Atoi(sc.Text())
		code = append(code, v)
	}
	n := len(code) + 1
	// a vertex stays until all its neighbours but one are removed, and each
	// removed neighbour writes the vertex once
	deg := make([]int, n+1)
	for u := range deg {
		deg[u] = 1
	}
	for _, c := range code {
		deg[c]++
	}
	leaves := &minHeap{}
	for u := 1; u <= n; u++ {
		if deg[u] == 1 {
			*leaves = append(*leaves, u)
		}
	}
	heap.Init(leaves)
	adj := make([][]int, n+1)
	for _, c := range code {
		leaf := heap.Pop(leaves).(int)
		adj[leaf] = append(adj[leaf], c)
		adj[c] = append(adj[c], leaf)
		deg[c]--
		if deg[c] == 1 {
			heap.Push(leaves, c)
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for u := 1; u <= n; u++ {
		sort.Ints(adj[u])
		w.WriteString(strconv.Itoa(u))
		w.WriteByte(':')
		for _, x := range adj[u] {
			w.WriteByte(' ')
			w.WriteString(strconv.Itoa(x))
		}
		w.WriteByte('\n')
	}
}
