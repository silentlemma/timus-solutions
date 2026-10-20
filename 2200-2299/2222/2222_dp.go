package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	rows        = 3
	frontier    = 2 * rows
	cells       = frontier + rows
	maskCount   = 1 << rows
	gain        = rows - 1
	unreachable = -1
)

type state [frontier]int

type edge struct {
	target, mask, weight int
}

type layer struct {
	previous, masks []int
}

type sets struct {
	parent [cells]int
}

func (d *sets) root(v int) int {
	for v != d.parent[v] {
		d.parent[v] = d.parent[d.parent[v]]
		v = d.parent[v]
	}
	return v
}

func transition(current state, mask int, finished state) (state, bool) {
	d := sets{}
	for i := range d.parent {
		d.parent[i] = i
	}
	for i := 0; i < frontier; i++ {
		for j := 0; j < i; j++ {
			if current[i] != 0 && current[i] == current[j] {
				d.parent[d.root(i)] = d.root(j)
			}
		}
	}
	var active [cells]bool
	for i := 0; i < frontier; i++ {
		active[i] = current[i] != 0
	}
	for r := 0; r < rows; r++ {
		active[frontier+r] = mask>>uint(r)&1 != 0
	}
	for r := 0; r < rows; r++ {
		if !active[frontier+r] {
			continue
		}
		for c := 0; c < 2; c++ {
			for s := 0; s < rows; s++ {
				distance := r - s
				if distance < 0 {
					distance = -distance
				}
				old := c*rows + s
				if distance != c+1 || !active[old] {
					continue
				}
				a, b := d.root(old), d.root(frontier+r)
				if a == b {
					return state{}, false
				}
				d.parent[a] = b
			}
		}
	}
	var oldRoots, newRoots [cells]bool
	for i := 0; i < cells; i++ {
		if active[i] {
			if i < rows {
				oldRoots[d.root(i)] = true
			} else {
				newRoots[d.root(i)] = true
			}
		}
	}
	lost, oldCount, newCount := false, 0, 0
	for i := 0; i < cells; i++ {
		lost = lost || oldRoots[i] && !newRoots[i]
		if oldRoots[i] {
			oldCount++
		}
		if newRoots[i] {
			newCount++
		}
	}
	if lost {
		if newCount == 0 && oldCount == 1 {
			return finished, true
		}
		return state{}, false
	}
	var labels [cells]int
	var result state
	count := 0
	for i := rows; i < cells; i++ {
		if active[i] {
			root := d.root(i)
			if labels[root] == 0 {
				count++
				labels[root] = count
			}
			result[i-rows] = labels[root]
		}
	}
	return result, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	empty, finished := state{}, state{}
	for i := range finished {
		finished[i] = -1
	}
	states := []state{empty, finished}
	indices := map[state]int{empty: 0, finished: 1}
	edges := [][]edge{}
	for i := 0; i < len(states); i++ {
		current := states[i]
		outgoing := []edge{}
		if current == finished {
			outgoing = append(outgoing, edge{i, 0, 0})
		} else {
			for mask := 0; mask < maskCount; mask++ {
				if current == empty && mask == 0 {
					continue
				}
				target, valid := transition(current, mask, finished)
				if !valid {
					continue
				}
				id, exists := indices[target]
				if !exists {
					id = len(states)
					indices[target] = id
					states = append(states, target)
				}
				weight := 0
				for r := 0; r < rows; r++ {
					weight += mask >> uint(r) & 1
				}
				outgoing = append(outgoing, edge{id, mask, weight})
			}
		}
		edges = append(edges, outgoing)
	}
	size := len(states)
	scores := make([]int, size)
	for i := range scores {
		scores[i] = unreachable
	}
	scores[0] = 0
	history := []layer{}
	stable := false
	for len(history) < n && !stable {
		following := make([]int, size)
		step := layer{make([]int, size), make([]int, size)}
		for i := range following {
			following[i], step.previous[i] = unreachable, unreachable
		}
		for source, outgoing := range edges {
			if scores[source] == unreachable {
				continue
			}
			for _, e := range outgoing {
				candidate := scores[source] + e.weight
				if candidate > following[e.target] {
					following[e.target] = candidate
					step.previous[e.target], step.masks[e.target] = source, e.mask
				}
			}
		}
		// An equal score shift is preserved by every subsequent DP step.
		stable = true
		for i := range scores {
			if !(scores[i] == unreachable && following[i] == unreachable) &&
				!(scores[i] != unreachable && following[i] == scores[i]+gain) {
				stable = false
			}
		}
		scores = following
		history = append(history, step)
	}
	best, vertex := unreachable, 0
	for i, current := range states {
		maximum := current[0]
		for _, label := range current {
			if label > maximum {
				maximum = label
			}
		}
		if (current == finished || maximum == 1) && scores[i] > best {
			best, vertex = scores[i], i
		}
	}
	board := make([]int, n)
	for column := n - 1; column >= 0; column-- {
		index := column
		if index >= len(history) {
			index = len(history) - 1
		}
		board[column] = history[index].masks[vertex]
		vertex = history[index].previous[vertex]
	}
	out := bufio.NewWriter(os.Stdout)
	for row := 0; row < rows; row++ {
		for column, mask := range board {
			if column != 0 {
				out.WriteByte(' ')
			}
			out.WriteByte(byte('0' + (mask >> uint(row) & 1)))
		}
		out.WriteByte('\n')
	}
	out.Flush()
}
