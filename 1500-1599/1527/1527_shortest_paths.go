package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type road struct{ u, v, toll, time, height int }

type state struct{ time, paid, v int }

type minHeap []state

func (h minHeap) Len() int { return len(h) }
func (h minHeap) Less(i, j int) bool {
	if h[i].time != h[j].time {
		return h[i].time < h[j].time
	}
	if h[i].paid != h[j].paid {
		return h[i].paid < h[j].paid
	}
	return h[i].v < h[j].v
}
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(state)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

var (
	n, s, f, budget, limit int
	roads                  []road
	out                    [][]int
)

// route finds a route from s to f within the limits using roads no higher
// than height, as road numbers, and whether there is one.
func route(height int) ([]int, bool) {
	const none = -1
	// best[v][c]: the least time to v with c tolls paid
	best := make([][]int, n+1)
	cameBy := make([][]int, n+1)
	for v := range best {
		best[v] = make([]int, budget+1)
		cameBy[v] = make([]int, budget+1)
		for c := range best[v] {
			best[v][c], cameBy[v][c] = none, none
		}
	}
	best[s][0] = 0
	h := &minHeap{{0, 0, s}}
	for h.Len() > 0 {
		cur := heap.Pop(h).(state)
		time, paid, v := cur.time, cur.paid, cur.v
		if best[v][paid] != time {
			continue
		}
		// a state is useless if fewer tolls already reach v as fast
		beaten := false
		for c := 0; c < paid && !beaten; c++ {
			beaten = best[v][c] != none && best[v][c] <= time
		}
		if beaten {
			continue
		}
		if v == f {
			var path []int
			for cameBy[v][paid] != none {
				r := roads[cameBy[v][paid]]
				path = append(path, cameBy[v][paid]+1)
				paid -= r.toll
				v = r.u
			}
			for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
				path[i], path[j] = path[j], path[i]
			}
			return path, true
		}
		for _, idx := range out[v] {
			r := roads[idx]
			nt, np := time+r.time, paid+r.toll
			fits := r.height <= height && np <= budget && nt <= limit
			if fits && (best[r.v][np] == none || nt < best[r.v][np]) {
				best[r.v][np] = nt
				cameBy[r.v][np] = idx
				heap.Push(h, state{nt, np, r.v})
			}
		}
	}
	return nil, false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var m int
	fmt.Fscan(in, &n, &m, &s, &f, &budget, &limit)
	roads = make([]road, m)
	out = make([][]int, n+1)
	heights := make([]int, m)
	for i := range roads {
		r := &roads[i]
		fmt.Fscan(in, &r.u, &r.v, &r.toll, &r.time, &r.height)
		out[r.u] = append(out[r.u], i)
		heights[i] = r.height
	}
	if s == f {
		fmt.Print("0\n0\n\n")
		return
	}
	// shorter parallel roads first, to avoid obsolete heap entries
	for _, edges := range out {
		sort.SliceStable(edges, func(i, j int) bool {
			return roads[edges[i]].time < roads[edges[j]].time
		})
	}
	// a cheapest route repeats no city, so it pays at most n - 1 tolls
	if budget > n-1 {
		budget = n - 1
	}
	sort.Ints(heights)
	found := func(h int) bool {
		_, ok := route(h)
		return ok
	}
	if !found(heights[m-1]) {
		fmt.Println(-1)
		return
	}
	lo, hi := 0, m-1
	for lo < hi {
		mid := (lo + hi) / 2
		if found(heights[mid]) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	path, _ := route(heights[lo])
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintln(w, heights[lo])
	fmt.Fprintln(w, len(path))
	for i, idx := range path {
		if i > 0 {
			w.WriteByte(' ')
		}
		w.WriteString(strconv.Itoa(idx))
	}
	w.WriteByte('\n')
}
