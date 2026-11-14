package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	rankGap    = 2
	maxRank    = 1000
	roleCount  = 3
	statements = 0
	testdata   = 1
	anything   = 2
)

type group struct {
	rank, role int
	names      []string
}

type edge struct {
	to, reverse, capacity int
}

type network struct {
	edges       [][]edge
	level, next []int
}

func (n *network) add(from, to, capacity int) {
	forward := edge{to, len(n.edges[to]), capacity}
	backward := edge{from, len(n.edges[from]), 0}
	n.edges[from] = append(n.edges[from], forward)
	n.edges[to] = append(n.edges[to], backward)
}

func (n *network) layers(source, sink int, queue []int) bool {
	for i := range n.level {
		n.level[i] = -1
		n.next[i] = 0
	}
	n.level[source] = 0
	queue = append(queue[:0], source)
	for head := 0; head < len(queue); head++ {
		from := queue[head]
		for _, link := range n.edges[from] {
			if link.capacity > 0 && n.level[link.to] < 0 {
				n.level[link.to] = n.level[from] + 1
				queue = append(queue, link.to)
			}
		}
	}
	return n.level[sink] >= 0
}

func (n *network) send(from, sink, amount int) int {
	if from == sink {
		return amount
	}
	for n.next[from] < len(n.edges[from]) {
		link := &n.edges[from][n.next[from]]
		if link.capacity > 0 && n.level[link.to] == n.level[from]+1 {
			limit := amount
			if link.capacity < limit {
				limit = link.capacity
			}
			if sent := n.send(link.to, sink, limit); sent > 0 {
				link.capacity -= sent
				n.edges[link.to][link.reverse].capacity += sent
				return sent
			}
		}
		n.next[from]++
	}
	return 0
}

func writesWith(writer, tester int) bool {
	return writer != testdata && tester != statements
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	input.Scan()
	count, _ := strconv.Atoi(input.Text())
	groups := []group{{}} // Node zero is the source.
	var index [maxRank + 1][roleCount]int
	for i := 0; i < count; i++ {
		input.Scan()
		name := input.Text()
		input.Scan()
		role := anything
		switch input.Text() {
		case "statements":
			role = statements
		case "testdata":
			role = testdata
		}
		input.Scan()
		rank, _ := strconv.Atoi(input.Text())
		id := index[rank][role]
		if id == 0 {
			id = len(groups)
			index[rank][role] = id
			groups = append(groups, group{rank: rank, role: role})
		}
		groups[id].names = append(groups[id].names, name)
	}

	// People with the same rank and role share every partner, so one node
	// represents the group. Its terminal edge limits how many can be used.
	sink := len(groups)
	n := network{make([][]edge, sink+1), make([]int, sink+1), make([]int, sink+1)}
	for id := 1; id < sink; id++ {
		g := groups[id]
		if g.rank/rankGap%2 != 0 {
			n.add(id, sink, len(g.names))
			continue
		}
		n.add(0, id, len(g.names))
		for _, rank := range [...]int{g.rank - rankGap, g.rank + rankGap} {
			if rank < 0 || rank > maxRank {
				continue
			}
			for role, other := range index[rank] {
				if other != 0 && (writesWith(g.role, role) || writesWith(role, g.role)) {
					n.add(id, other, len(g.names))
				}
			}
		}
	}
	queue := make([]int, 0, sink+1)
	total := 0
	for n.layers(0, sink, queue) {
		for sent := n.send(0, sink, count); sent > 0; sent = n.send(0, sink, count) {
			total += sent
		}
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, total)
	used := make([]int, sink)
	for id := 1; id < sink; id++ {
		g := groups[id]
		if g.rank/rankGap%2 != 0 {
			continue
		}
		for _, link := range n.edges[id] {
			if link.to == 0 {
				continue
			}
			other := groups[link.to]
			flow := n.edges[link.to][link.reverse].capacity
			for i := 0; i < flow; i++ {
				a, b := g.names[used[id]], other.names[used[link.to]]
				used[id]++
				used[link.to]++
				if !writesWith(g.role, other.role) {
					a, b = b, a
				}
				fmt.Fprintln(output, a, b)
			}
		}
	}
}
