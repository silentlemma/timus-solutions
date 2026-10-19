package main

import (
	"bufio"
	"fmt"
	"os"
)

type Matcher struct {
	edges                         [][]int
	left, right, distance, cursor []int
	shortest                      int
}

func (h *Matcher) layer() bool {
	count := len(h.edges)
	h.shortest = count + 1
	queue := make([]int, 0, count)
	for u := 0; u < count; u++ {
		h.distance[u] = -1
		h.cursor[u] = 0
		if h.left[u] < 0 {
			h.distance[u] = 0
			queue = append(queue, u)
		}
	}
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		if h.distance[u] >= h.shortest {
			continue
		}
		for _, v := range h.edges[u] {
			mate := h.right[v]
			if mate < 0 {
				h.shortest = h.distance[u] + 1
			} else if h.distance[mate] < 0 {
				h.distance[mate] = h.distance[u] + 1
				queue = append(queue, mate)
			}
		}
	}
	return h.shortest <= count
}

func (h *Matcher) augment(u int) bool {
	for h.cursor[u] < len(h.edges[u]) {
		v := h.edges[u][h.cursor[u]]
		h.cursor[u]++
		mate := h.right[v]
		if (mate < 0 && h.distance[u]+1 == h.shortest) ||
			(mate >= 0 && h.distance[mate] == h.distance[u]+1 && h.augment(mate)) {
			h.left[u] = v
			h.right[v] = u
			return true
		}
	}
	h.distance[u] = -1
	return false
}

func solve(a, b int, records [][2]int) [][2]int {
	entries, exits := make([]int, 0), make([]int, 0)
	for _, record := range records {
		if record[1] == 0 {
			entries = append(entries, record[0])
		} else {
			exits = append(exits, record[0])
		}
	}
	if len(entries) != len(exits) {
		return nil
	}
	count := len(entries)
	h := Matcher{
		edges: make([][]int, count), left: make([]int, count), right: make([]int, count),
		distance: make([]int, count), cursor: make([]int, count),
	}
	for u, entry := range entries {
		h.left[u] = -1
		h.right[u] = -1
		for v, exit := range exits {
			duration := exit - entry
			if duration > 0 && (duration <= b || duration >= a) {
				h.edges[u] = append(h.edges[u], v)
			}
		}
	}
	total := 0
	for h.layer() {
		for u := 0; u < count; u++ {
			if h.left[u] < 0 && h.augment(u) {
				total++
			}
		}
	}
	if total != count {
		return nil
	}
	answer := make([][2]int, count)
	for u, entry := range entries {
		answer[u] = [2]int{entry, exits[h.left[u]]}
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var a, b, n int
	fmt.Fscan(input, &a, &b, &n)
	records := make([][2]int, n)
	for i := range records {
		fmt.Fscan(input, &records[i][0], &records[i][1])
	}
	answer := solve(a, b, records)
	if answer == nil {
		fmt.Fprintln(output, "Liar")
	} else {
		fmt.Fprintln(output, "No reason")
		for _, pair := range answer {
			fmt.Fprintln(output, pair[0], pair[1])
		}
	}
}
