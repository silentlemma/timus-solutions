package main

import (
	"bufio"
	"fmt"
	"os"
)

const unreached = -2
const unknown = -1
const maxEdges = 100000

func solve(values, offsets, edges []int) []int {
	entry := make([]int, len(values))
	for i := range entry {
		entry[i] = unreached
	}
	entry[0] = 0
	pending := make([]int, 1, 2*len(values))
	for head := 0; head < len(pending); head++ {
		vertex := pending[head]
		offered := values[vertex]
		if offered == 0 {
			offered = entry[vertex]
		}
		for at := offsets[vertex]; at < offsets[vertex+1]; at++ {
			target := edges[at]
			old := entry[target]
			merged := unknown
			if old == unreached {
				merged = offered
			} else if old == offered {
				merged = old
			}
			if old != merged {
				entry[target] = merged
				pending = append(pending, target)
			}
		}
	}
	return entry
}

func word(value int) string {
	if value == unknown {
		return "unknown"
	}
	if value == 0 {
		return "sober"
	}
	return fmt.Sprint(value)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	values, offsets := make([]int, n), make([]int, n+1)
	edges := make([]int, 0, maxEdges)
	for i := range values {
		var degree int
		fmt.Fscan(in, &values[i], &degree)
		for j := 0; j < degree; j++ {
			var target int
			fmt.Fscan(in, &target)
			edges = append(edges, target-1)
		}
		offsets[i+1] = len(edges)
	}
	entry := solve(values, offsets, edges)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i, before := range entry {
		after := values[i]
		if after == 0 {
			after = before
		}
		fmt.Fprintln(out, word(before), word(after))
	}
}
