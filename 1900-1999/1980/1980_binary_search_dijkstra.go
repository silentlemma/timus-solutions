package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
)

const searchSteps = 60
const safetyMargin = 1e-8

type Edge struct{ a, b, speed, length int }
type Link struct{ vertex, road int }
type State struct {
	time   float64
	vertex int
}
type Queue []State

func (q Queue) Len() int            { return len(q) }
func (q Queue) Less(i, j int) bool  { return q[i].time < q[j].time }
func (q Queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *Queue) Push(x interface{}) { *q = append(*q, x.(State)) }
func (q *Queue) Pop() interface{} {
	old := *q
	v := old[len(old)-1]
	*q = old[:len(old)-1]
	return v
}

func solve(n int, edges []Edge, deadline float64) (float64, []int) {
	graph := make([][]Link, n)
	totalLength := 0
	for id, e := range edges {
		graph[e.a] = append(graph[e.a], Link{e.b, id})
		graph[e.b] = append(graph[e.b], Link{e.a, id})
		totalLength += e.length
	}
	parent := make([]int, n)
	shortest := func(extra float64) bool {
		cost := make([]float64, len(edges))
		for i, e := range edges {
			cost[i] = float64(e.length) / (float64(e.speed) + extra)
		}
		distance := make([]float64, n)
		for i := range distance {
			distance[i] = math.Inf(1)
			parent[i] = -1
		}
		distance[0] = 0
		queue := &Queue{{0, 0}}
		for queue.Len() > 0 {
			state := heap.Pop(queue).(State)
			if state.time != distance[state.vertex] {
				continue
			}
			if state.vertex == n-1 {
				return true
			}
			for _, link := range graph[state.vertex] {
				candidate := state.time + cost[link.road]
				if candidate <= deadline && candidate < distance[link.vertex] {
					distance[link.vertex] = candidate
					parent[link.vertex] = link.road
					heap.Push(queue, State{candidate, link.vertex})
				}
			}
		}
		return false
	}
	low, high := 0.0, 0.0
	if !shortest(0) {
		high = float64(totalLength) / deadline
		for step := 0; step < searchSteps; step++ {
			middle := (low + high) / 2
			if middle == low || middle == high {
				break
			}
			if shortest(middle) {
				high = middle
			} else {
				low = middle
			}
		}
		shortest(high)
	}
	extra := high + safetyMargin*math.Max(1, high)
	path := []int{}
	for vertex := n - 1; vertex != 0; {
		id := parent[vertex]
		path = append(path, id+1)
		vertex = edges[id].a ^ edges[id].b ^ vertex
	}
	for a, b := 0, len(path)-1; a < b; a, b = a+1, b-1 {
		path[a], path[b] = path[b], path[a]
	}
	return extra, path
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	edges := make([]Edge, m)
	for i := range edges {
		e := &edges[i]
		fmt.Fscan(in, &e.a, &e.b, &e.speed, &e.length)
		e.a--
		e.b--
	}
	var deadline float64
	fmt.Fscan(in, &deadline)
	extra, path := solve(n, edges, deadline)
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(out, "%.12f %d\n", extra, len(path))
	for i, id := range path {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, id)
	}
	fmt.Fprintln(out)
	out.Flush()
}
