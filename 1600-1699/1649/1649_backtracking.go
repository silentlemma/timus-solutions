package main

import (
	"bufio"
	"fmt"
	"os"
)

const wrap = 4 // a fifth bacterium leaves one: counts go 1, 2, 3, 4, 1, ...

const (
	bad = iota
	first
	last
	either
	wait
)

var (
	n, m int
	// need[v]: how many free neighbours v must see settled after it,
	// modulo 4, stored as 1..4 like the picture; deg[v]: free neighbours
	need, deg []int
	alive     []bool
	adj       [][]int
)

func kind(v int) int {
	d, k := deg[v], need[v]
	switch {
	case k != 1 && k-1 > d:
		return bad
	case d < wrap && k == d+1:
		return first // before all free neighbours
	case d < wrap && k == 1:
		return last // after all of them
	case d == wrap && k == 1:
		return either // an inner cell showing 1: before all or after all
	}
	return wait
}

// take settles v before (isFirst) or after all its free neighbours
func take(v int, isFirst bool) {
	alive[v] = false
	for _, u := range adj[v] {
		if alive[u] {
			deg[u]--
			if !isFirst { // u now sees v settle after it
				need[u]--
				if need[u] == 0 {
					need[u] = wrap
				}
			}
		}
	}
}

// countsFit is necessary: the later-neighbour counts must add up to the
// edges, and touching undecided cells must split into firsts and lasts
func countsFit(cells []int) bool {
	edges, fixed := 0, 0
	open, seen := make([]bool, n*m), make([]bool, n*m)
	var openCells []int
	for _, v := range cells {
		edges += deg[v]
		if kind(v) == either {
			open[v] = true
			openCells = append(openCells, v)
		} else {
			fixed += need[v] - 1
		}
	}
	rest := edges/2 - fixed
	if rest < 0 || rest%wrap != 0 || rest/wrap > len(openCells) {
		return false
	}
	reach := make([]bool, len(openCells)+1) // reach[s]: s firsts possible so far
	reach[0] = true
	for _, s := range openCells {
		if seen[s] {
			continue
		}
		seen[s] = true
		group := []int{s}
		var colour [2]int
		for i := 0; i < len(group); i++ {
			v := group[i]
			colour[(v/m+v%m)%2]++
			for _, u := range adj[v] {
				if alive[u] && open[u] && !seen[u] {
					seen[u] = true
					group = append(group, u)
				}
			}
		}
		next := make([]bool, len(reach))
		for t, ok := range reach {
			for _, c := range colour {
				if ok && t+c < len(next) {
					next[t+c] = true
				}
			}
		}
		reach = next
	}
	return reach[rest/wrap]
}

func components(cells []int) [][]int {
	inside, seen := make([]bool, n*m), make([]bool, n*m)
	for _, v := range cells {
		inside[v] = true
	}
	var parts [][]int
	for _, s := range cells {
		if seen[s] {
			continue
		}
		seen[s] = true
		part := []int{s}
		for i := 0; i < len(part); i++ {
			for _, u := range adj[part[i]] {
				if inside[u] && alive[u] && !seen[u] {
					seen[u] = true
					part = append(part, u)
				}
			}
		}
		parts = append(parts, part)
	}
	return parts
}

// solve gives an order of the free cells, or false if there is none
func solve(cells []int) ([]int, bool) {
	var head, tail []int
	for {
		var queue []int
		for _, v := range cells {
			if k := kind(v); k != either && k != wait {
				queue = append(queue, v)
			}
		}
		moved := false
		for len(queue) > 0 {
			v := queue[len(queue)-1]
			queue = queue[:len(queue)-1]
			if !alive[v] {
				continue
			}
			k := kind(v)
			if k == bad {
				return nil, false
			}
			if k != first && k != last {
				continue
			}
			take(v, k == first)
			if k == first {
				head = append(head, v)
			} else {
				tail = append(tail, v)
			}
			moved = true
			for _, u := range adj[v] {
				if alive[u] {
					queue = append(queue, u)
				}
			}
		}
		var left []int
		for _, v := range cells {
			if alive[v] {
				left = append(left, v)
			}
		}
		cells = left
		if !moved || len(cells) == 0 {
			break
		}
	}
	var middle []int
	if len(cells) > 0 {
		if parts := components(cells); len(parts) > 1 {
			for _, part := range parts {
				order, ok := solve(part)
				if !ok {
					return nil, false
				}
				middle = append(middle, order...)
			}
		} else {
			// the first cell of any order comes before all its neighbours,
			// so with no forced cell left it must be an undecided one
			pick := -1
			for _, v := range cells {
				if kind(v) == either {
					pick = v
					break
				}
			}
			if pick < 0 || !countsFit(cells) {
				return nil, false
			}
			// an undecided cell comes before or after all its neighbours in
			// any order, so trying both ways for one of them misses nothing
			var rest []int
			for _, v := range cells {
				if v != pick {
					rest = append(rest, v)
				}
			}
			found := false
			for _, isFirst := range []bool{true, false} {
				savedNeed := append([]int(nil), need...)
				savedDeg := append([]int(nil), deg...)
				savedAlive := append([]bool(nil), alive...)
				take(pick, isFirst)
				order, ok := solve(rest)
				need, deg, alive = savedNeed, savedDeg, savedAlive
				if ok {
					if isFirst {
						middle = append([]int{pick}, order...)
					} else {
						middle = append(order, pick)
					}
					found = true
					break
				}
			}
			if !found {
				return nil, false
			}
		}
	}
	result := append(head, middle...)
	for i := len(tail) - 1; i >= 0; i-- {
		result = append(result, tail[i])
	}
	return result, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	need = make([]int, n*m)
	for v := range need {
		fmt.Fscan(in, &need[v])
	}
	adj = make([][]int, n*m)
	deg = make([]int, n*m)
	alive = make([]bool, n*m)
	cells := make([]int, n*m)
	for v := range adj {
		r, c := v/m, v%m
		if r > 0 {
			adj[v] = append(adj[v], v-m)
		}
		if r+1 < n {
			adj[v] = append(adj[v], v+m)
		}
		if c > 0 {
			adj[v] = append(adj[v], v-1)
		}
		if c+1 < m {
			adj[v] = append(adj[v], v+1)
		}
		deg[v], alive[v], cells[v] = len(adj[v]), true, v
	}
	order, ok := solve(cells)
	if !ok {
		fmt.Fprintln(out, "No")
		return
	}
	fmt.Fprintln(out, "Yes")
	for _, v := range order {
		fmt.Fprintln(out, v/m+1, v%m+1)
	}
}
