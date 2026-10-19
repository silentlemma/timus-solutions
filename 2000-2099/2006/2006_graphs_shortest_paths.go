package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
)

const infinityCost = 1000000000
const padding = 2
const directions = 4

type pair struct{ cost, vertex int }
type minHeap []pair

func (h minHeap) Len() int                { return len(h) }
func (h minHeap) Less(i, j int) bool      { return h[i].cost < h[j].cost }
func (h minHeap) Swap(i, j int)           { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(value interface{}) { *h = append(*h, value.(pair)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	n := len(old)
	value := old[n-1]
	*h = old[:n-1]
	return value
}

type edge struct{ first, second int }
type interval struct{ left, right, cost int }

func filled(size, value int) []int {
	result := make([]int, size)
	for i := range result {
		result[i] = value
	}
	return result
}

func bfs(cells []byte, offsets [directions]int, start int) ([]int, []int, []int) {
	distance, parent := filled(len(cells), -1), filled(len(cells), -1)
	distance[start] = 0
	order := []int{start}
	for head := 0; head < len(order); head++ {
		vertex := order[head]
		for _, offset := range offsets {
			other := vertex + offset
			if cells[other] == '.' && distance[other] < 0 {
				distance[other] = distance[vertex] + 1
				parent[other] = vertex
				order = append(order, other)
			}
		}
	}
	return distance, parent, order
}

func solve(grid []string, sr, sc, tr, tc int) (int, int) {
	rows, cols := len(grid), len(grid[0])
	stride := cols + padding
	cells := make([]byte, (rows+padding)*stride)
	for row, content := range grid {
		copy(cells[(row+1)*stride+1:], content)
	}
	start, target := (sr+1)*stride+sc+1, (tr+1)*stride+tc+1
	offsets := [directions]int{-stride, 1, stride, -1}
	ds, parent, order := bfs(cells, offsets, start)
	if ds[target] == 1 {
		for vertex, ch := range cells {
			if ch == '.' && vertex != start && vertex != target {
				return vertex/stride - 1, vertex%stride - 1
			}
		}
	}
	dt, _, _ := bfs(cells, offsets, target)
	path := []int{}
	for vertex := target; vertex != -1; vertex = parent[vertex] {
		path = append(path, vertex)
	}
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	length := len(path) - 1
	position, level := filled(len(cells), -1), filled(len(cells), -1)
	for at, vertex := range path {
		position[vertex] = at
	}
	for _, vertex := range order {
		if position[vertex] >= 0 {
			level[vertex] = position[vertex]
		} else {
			level[vertex] = level[parent[vertex]]
		}
	}
	edges := []edge{}
	detour := filled(len(cells), infinityCost)
	for _, vertex := range order {
		for _, offset := range offsets {
			other := vertex + offset
			if level[vertex] >= level[other] {
				continue
			}
			edges = append(edges, edge{vertex, other})
			if position[other] < 0 && ds[vertex]+1 < detour[other] {
				detour[other] = ds[vertex] + 1
			}
		}
	}
	h := &minHeap{}
	for _, vertex := range order {
		if detour[vertex] < infinityCost {
			heap.Push(h, pair{detour[vertex], vertex})
		}
	}
	for h.Len() > 0 {
		current := heap.Pop(h).(pair)
		distance, vertex := current.cost, current.vertex
		if distance != detour[vertex] {
			continue
		}
		for _, offset := range offsets {
			other := vertex + offset
			if level[other] == level[vertex] && position[other] < 0 && distance+1 < detour[other] {
				detour[other] = distance + 1
				heap.Push(h, pair{distance + 1, other})
			}
		}
	}
	answer := filled(length+1, infinityCost)
	intervals := []interval{}
	for _, e := range edges {
		x, y := e.first, e.second
		left, right := level[x], level[y]
		if left+1 < right {
			intervals = append(intervals, interval{left + 1, right - 1, ds[x] + 1 + dt[y]})
		}
		if position[x] < 0 && 1 <= left && left < length {
			cost := detour[x] + 1 + dt[y]
			if cost < answer[left] {
				answer[left] = cost
			}
		}
	}
	sort.Slice(intervals, func(i, j int) bool { return intervals[i].left < intervals[j].left })
	at, best := 0, 1
	for failed := 1; failed < length; failed++ {
		for at < len(intervals) && intervals[at].left <= failed {
			e := intervals[at]
			heap.Push(h, pair{e.cost, e.right})
			at++
		}
		for h.Len() > 0 && (*h)[0].vertex < failed {
			heap.Pop(h)
		}
		if h.Len() > 0 && (*h)[0].cost < answer[failed] {
			answer[failed] = (*h)[0].cost
		}
		if answer[failed] > answer[best] {
			best = failed
		}
	}
	vertex := path[best]
	return vertex/stride - 1, vertex%stride - 1
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var rows, cols, sr, sc, tr, tc int
	fmt.Fscan(in, &rows, &cols, &sr, &sc, &tr, &tc)
	grid := make([]string, rows)
	for i := range grid {
		fmt.Fscan(in, &grid[i])
	}
	row, col := solve(grid, sr-1, sc-1, tr-1, tc-1)
	fmt.Println(row+1, col+1)
}
