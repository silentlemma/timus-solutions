package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

// piece is a node of the tree of pieces, keyed by its smallest content
type piece struct{ low, node int }

type pieceHeap []piece

func (h pieceHeap) Len() int            { return len(h) }
func (h pieceHeap) Less(i, j int) bool  { return h[i].low < h[j].low }
func (h pieceHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *pieceHeap) Push(x interface{}) { *h = append(*h, x.(piece)) }
func (h *pieceHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

// chain: every piece that can ever appear is a maximal run of rings above
// some content; such runs nest, and the children of a run are the runs
// above its smallest content
type chain struct {
	rings, low, grundy []int
	children           [][]int
}

func (c *chain) build(left, right int) int {
	node, m := len(c.low), c.rings[left]
	for _, r := range c.rings[left : right+1] {
		if r < m {
			m = r
		}
	}
	c.low = append(c.low, m)
	c.children = append(c.children, nil)
	c.grundy = append(c.grundy, 0)
	for i := left; i <= right; i++ {
		if c.rings[i] > m {
			j := i
			for j+1 <= right && c.rings[j+1] > m {
				j++
			}
			child := c.build(i, j)
			c.children[node] = append(c.children[node], child)
			i = j
		}
	}
	return node
}

// afterMoves maps x to the xor of the pieces left by removing rings up to x
func (c *chain) afterMoves(node int) map[int]int {
	result := map[int]int{}
	h := &pieceHeap{}
	x := 0
	for _, ch := range c.children[node] {
		heap.Push(h, piece{c.low[ch], ch})
		x ^= c.grundy[ch]
	}
	result[c.low[node]] = x
	for h.Len() > 0 {
		content := (*h)[0].low
		for h.Len() > 0 && (*h)[0].low == content {
			p := heap.Pop(h).(piece)
			x ^= c.grundy[p.node]
			for _, d := range c.children[p.node] {
				x ^= c.grundy[d]
				heap.Push(h, piece{c.low[d], d})
			}
		}
		result[content] = x
	}
	return result
}

func (c *chain) analyse() int {
	c.build(0, len(c.rings)-1)
	// children are built after their parents, so go backwards
	for node := len(c.low) - 1; node >= 0; node-- {
		options := map[int]bool{}
		for _, v := range c.afterMoves(node) {
			options[v] = true
		}
		g := 0
		for options[g] {
			g++
		}
		c.grundy[node] = g
	}
	return c.grundy[0]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	chains := make([]chain, k)
	g := make([]int, k)
	total := 0
	for i := range chains {
		var length int
		fmt.Fscan(in, &length)
		chains[i].rings = make([]int, length)
		for j := range chains[i].rings {
			fmt.Fscan(in, &chains[i].rings[j])
		}
		g[i] = chains[i].analyse()
		total ^= g[i]
	}
	if total == 0 {
		fmt.Println("S")
		return
	}
	// a winning move leaves the chain with the xor of all other chains
	for i := range chains {
		after := chains[i].afterMoves(0)
		for j, r := range chains[i].rings {
			if after[r] == total^g[i] {
				fmt.Printf("G\n%d %d\n", i+1, j+1)
				return
			}
		}
	}
}
