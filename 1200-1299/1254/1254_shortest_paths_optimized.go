package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

type node struct {
	cell      int
	dist, key float64
}

func (a node) before(b node) bool {
	return a.key < b.key || (a.key == b.key && a.dist > b.dist)
}

type frontier []node

func (q *frontier) push(value node) {
	h := append(*q, value)
	i := len(h) - 1
	for i > 0 {
		parent := (i - 1) / 2
		if !value.before(h[parent]) {
			break
		}
		h[i] = h[parent]
		i = parent
	}
	h[i] = value
	*q = h
}

func (q *frontier) pop() node {
	h := *q
	first, last := h[0], h[len(h)-1]
	h = h[:len(h)-1]
	if len(h) != 0 {
		i := 0
		for child := 1; child < len(h); child = i*2 + 1 {
			if child+1 < len(h) && h[child+1].before(h[child]) {
				child++
			}
			if !h[child].before(last) {
				break
			}
			h[i] = h[child]
			i = child
		}
		h[i] = last
	}
	*q = h
	return first
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var cols, rows, bombs int
	var speed float64
	fmt.Fscan(input, &cols, &rows, &bombs, &speed)
	width := cols + 2
	free := make([]bool, (rows+2)*width)
	openCells := 0
	for row := 1; row <= rows; row++ {
		var line string
		fmt.Fscan(input, &line)
		for col := 1; col <= cols && col <= len(line); col++ {
			if line[col-1] == '.' {
				free[row*width+col] = true
				openCells++
			}
		}
	}
	var x, y int
	fmt.Fscan(input, &x, &y)
	at := y*width + x
	if !free[at] {
		free[at] = true
		openCells++
	}
	steps := [...]int{1, -1, width, -width, width + 1, width - 1, 1 - width, -width - 1}
	cost := [...]float64{1, 1, 1, 1, math.Sqrt2, math.Sqrt2, math.Sqrt2, math.Sqrt2}
	part := make([]int, len(free))
	stack := make([]int, 0, openCells)
	for cell, open := range free {
		if !open || part[cell] != 0 {
			continue
		}
		part[cell] = cell
		stack = append(stack, cell)
		for len(stack) != 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, step := range steps {
				if next := v + step; free[next] && part[next] == 0 {
					part[next] = cell
					stack = append(stack, next)
				}
			}
		}
	}
	distance := make([]float64, len(free))
	visited := make([]int, len(free))
	q := make(frontier, 0, openCells)
	walk := func(from, to, search int) float64 {
		targetX, targetY := to%width, to/width
		estimate := func(cell int) float64 {
			dx, dy := abs(cell%width-targetX), abs(cell/width-targetY)
			if dx < dy {
				dx, dy = dy, dx
			}
			return float64(dx-dy) + math.Sqrt2*float64(dy)
		}
		if openCells == rows*cols {
			return estimate(from)
		}
		// A search number keeps old distances out of the next walk.
		q = append(q[:0], node{cell: from, key: estimate(from)})
		visited[from], distance[from] = search, 0
		for len(q) != 0 {
			cur := q.pop()
			if cur.dist != distance[cur.cell] {
				continue
			}
			if cur.cell == to {
				return cur.dist
			}
			for i, step := range steps {
				next, d := cur.cell+step, cur.dist+cost[i]
				if free[next] && (visited[next] != search || d < distance[next]) {
					visited[next], distance[next] = search, d
					q.push(node{next, d, d + estimate(next)})
				}
			}
		}
		return 0 // Connected components guarantee that the goal is reachable.
	}

	known := make(map[[2]int]float64, bombs)
	total := 0.0
	for i := 1; i <= bombs; i++ {
		fmt.Fscan(input, &x, &y)
		target := y*width + x
		if part[target] != part[at] || target == at {
			continue
		}
		key := [2]int{at, target}
		if at > target {
			key = [2]int{target, at}
		}
		length, ok := known[key]
		if !ok {
			length = walk(at, target, i)
			known[key] = length
		}
		total += length
		at = target
	}
	fmt.Printf("%.2f\n", total/speed)
}
