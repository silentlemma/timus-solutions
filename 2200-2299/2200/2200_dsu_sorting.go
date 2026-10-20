package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const minimumSide = 3

type reader struct {
	data []byte
	pos  int
}

func (in *reader) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := 1
	if in.data[in.pos] == '-' {
		sign = -1
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return sign * value
}

type board struct {
	xLow, yLow, xHigh, yHigh int
}

type event struct {
	coordinate, low, high, board, kind int
}

type disjointSet struct {
	parent []int
	size   []int
}

func newDisjointSet(count int) *disjointSet {
	dsu := &disjointSet{make([]int, count), make([]int, count)}
	for i := range dsu.parent {
		dsu.parent[i] = i
		dsu.size[i] = 1
	}
	return dsu
}

func (dsu *disjointSet) find(vertex int) int {
	for dsu.parent[vertex] != vertex {
		dsu.parent[vertex] = dsu.parent[dsu.parent[vertex]]
		vertex = dsu.parent[vertex]
	}
	return vertex
}

func (dsu *disjointSet) unite(first, second int) {
	first = dsu.find(first)
	second = dsu.find(second)
	if first == second {
		return
	}
	if dsu.size[first] < dsu.size[second] {
		first, second = second, first
	}
	dsu.parent[second] = first
	dsu.size[first] += dsu.size[second]
}

func connect(events []event, dsu *disjointSet) {
	sort.Slice(events, func(first, second int) bool {
		if events[first].coordinate != events[second].coordinate {
			return events[first].coordinate < events[second].coordinate
		}
		return events[first].low < events[second].low
	})
	last := [2]int{-1, -1}
	for i, current := range events {
		if i == 0 || current.coordinate != events[i-1].coordinate {
			last = [2]int{-1, -1}
		}
		opposite := last[1-current.kind]
		// Same-side intervals are disjoint, so only the latest one can overlap.
		if opposite != -1 && events[opposite].high >= current.low {
			dsu.unite(current.board, events[opposite].board)
		}
		last[current.kind] = i
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := reader{data: data}
	count := in.nextInt()
	in.nextInt()
	startX, startY := in.nextInt(), in.nextInt()
	boards := make([]board, count)
	start := 0
	trapped := false
	for i := range boards {
		current := board{in.nextInt(), in.nextInt(), in.nextInt(), in.nextInt()}
		boards[i] = current
		if current.xLow <= startX && startX < current.xHigh &&
			current.yLow <= startY && startY < current.yHigh {
			start = i
			trapped = current.xHigh-current.xLow == minimumSide &&
				current.yHigh-current.yLow == minimumSide &&
				startX == current.xLow+1 && startY == current.yLow+1
		}
	}
	if trapped {
		fmt.Println(1)
		return
	}
	dsu := newDisjointSet(count)
	events := make([]event, 2*count)
	for i, current := range boards {
		events[2*i] = event{current.xHigh + 1, current.yLow, current.yHigh, i, 0}
		events[2*i+1] = event{current.xLow, current.yLow, current.yHigh, i, 1}
	}
	connect(events, dsu)
	for i, current := range boards {
		events[2*i] = event{current.yHigh + 1, current.xLow, current.xHigh, i, 0}
		events[2*i+1] = event{current.yLow, current.xLow, current.xHigh, i, 1}
	}
	connect(events, dsu)
	fmt.Println(dsu.size[dsu.find(start)])
}
