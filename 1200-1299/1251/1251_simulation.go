package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

const (
	forget = 1001 // a grave untouched for 1000 days can go on the next day
	notice = 101  // and only when no neighbour was visited in the last 100
)

// intHeap is a min-heap of ints; a release is day*cells+grave
type intHeap []int

func (h intHeap) Len() int            { return len(h) }
func (h intHeap) Less(i, j int) bool  { return h[i] < h[j] }
func (h intHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *intHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *intHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	cells := n * m
	// the client in each grave (0 if free), the last burial or visit of that
	// client, the last visit next door and the day the grave may be freed
	owner, touched := make([]int, cells), make([]int, cells)
	nearVisit, release := make([]int, cells), make([]int, cells)
	var graveOf []int // grave of each client, -1 if none
	free, pending := &intHeap{}, &intHeap{}
	for g := 0; g < cells; g++ {
		*free = append(*free, g)
		nearVisit[g] = -notice
	}
	schedule := func(g int) {
		release[g] = max(touched[g]+forget, nearVisit[g]+notice)
		heap.Push(pending, release[g]*cells+g)
	}
	cremated := 0
	for {
		var day int
		var kind string
		if _, err := fmt.Fscan(in, &day, &kind); err != nil {
			break
		}
		// graves free at the start of the day, before its events
		for pending.Len() > 0 && (*pending)[0]/cells <= day {
			top := heap.Pop(pending).(int)
			g := top % cells
			if owner[g] != 0 && release[g] == top/cells {
				graveOf[owner[g]-1] = -1
				owner[g] = 0
				heap.Push(free, g)
			}
		}
		if kind == "d" {
			graveOf = append(graveOf, -1)
			if free.Len() == 0 {
				cremated++
				continue
			}
			g := heap.Pop(free).(int)
			owner[g] = len(graveOf)
			graveOf[len(graveOf)-1] = g
			touched[g] = day
			schedule(g)
			continue
		}
		var client int
		fmt.Fscan(in, &client)
		g := graveOf[client-1]
		if g < 0 {
			continue
		}
		touched[g] = day
		schedule(g)
		r, c := g/m, g%m
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				nr, nc := r+dr, c+dc
				if (dr != 0 || dc != 0) && nr >= 0 && nr < n && nc >= 0 && nc < m {
					k := nr*m + nc
					nearVisit[k] = day
					if owner[k] != 0 {
						schedule(k)
					}
				}
			}
		}
	}
	fmt.Println(cremated)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
