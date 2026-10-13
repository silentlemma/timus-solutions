package main

import (
	"bufio"
	"fmt"
	"os"
)

const longest = 16   // the longest cycle counted: no snake of length 18 gets out
const shortest = 4   // the shortest cycle on a grid
const lastSnake = 17 // snakes of lengths 2 .. 17 are answered

var h, w, root, limit int
var nearCells [][]int
var dist, rnk, best []int
var onPath, needed []bool

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func walk(v, steps int) {
	for _, u := range nearCells[v] {
		if u == root {
			if steps+1 >= shortest && needed[steps+1] {
				best[steps+1] = dist[root]
				needed[steps+1] = false
			}
		} else if !onPath[u] && rnk[u] > rnk[root] &&
			steps+1+abs(u/w-root/w)+abs(u%w-root%w) <= limit {
			onPath[u] = true
			walk(u, steps+1)
			onPath[u] = false
		}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var r0, c0 int
	fmt.Fscan(in, &h, &w, &r0, &c0)
	start := (r0-1)*w + c0 - 1
	free := make([]bool, h*w)
	for r := 0; r < h; r++ {
		var row string
		fmt.Fscan(in, &row)
		for c := 0; c < w; c++ {
			free[r*w+c] = row[c] == '.'
		}
	}
	free[start] = true
	nearCells = make([][]int, h*w)
	dr, dc := []int{-1, 1, 0, 0}, []int{0, 0, -1, 1}
	for v := 0; v < h*w; v++ {
		for k := range dr {
			nr, nc := v/w+dr[k], v%w+dc[k]
			if nr >= 0 && nr < h && nc >= 0 && nc < w && free[nr*w+nc] {
				nearCells[v] = append(nearCells[v], nr*w+nc)
			}
		}
	}
	// distances from the entrance
	dist = make([]int, h*w)
	for i := range dist {
		dist[i] = -1
	}
	dist[start] = 0
	order := []int{start}
	for i := 0; i < len(order); i++ {
		for _, u := range nearCells[order[i]] {
			if dist[u] < 0 {
				dist[u] = dist[order[i]] + 1
				order = append(order, u)
			}
		}
	}
	// rank: breadth-first position; a cycle is found from its first cell in this order
	rnk = make([]int, h*w)
	for i := range rnk {
		rnk[i] = len(order)
	}
	for i, v := range order {
		rnk[v] = i
	}
	best = make([]int, longest+1)
	needed = make([]bool, longest+1)
	for c := range best {
		best[c] = -1
	}
	for c := shortest; c <= longest; c += 2 {
		needed[c] = true
	}
	onPath = make([]bool, h*w)
	for _, v := range order {
		limit = 0
		for c := shortest; c <= longest; c++ {
			if needed[c] {
				limit = c
			}
		}
		if limit == 0 {
			break
		}
		root = v
		onPath[v] = true
		walk(v, 0)
		onPath[v] = false
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for length := 2; length <= lastSnake; length++ {
		answer := -1
		for c := length; c <= longest; c++ {
			if best[c] >= 0 && (answer < 0 || 2*best[c]+c < answer) {
				answer = 2*best[c] + c
			}
		}
		fmt.Fprintln(out, answer)
	}
}
