package main

import (
	"bufio"
	"os"
	"strconv"
)

const logCells = 17 // 2^17 > 100000 cells

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	word := func() []byte {
		b, _ := in.ReadByte()
		for b == ' ' || b == '\n' || b == '\r' {
			b, _ = in.ReadByte()
		}
		var w []byte
		for b != ' ' && b != '\n' && b != '\r' && b != 0 {
			w = append(w, b)
			var err error
			if b, err = in.ReadByte(); err != nil {
				break
			}
		}
		return w
	}
	number := func() int {
		v, _ := strconv.Atoi(string(word()))
		return v
	}
	h, w := number(), number()
	cells := h * w
	open := make([]bool, cells)
	for r := 0; r < h; r++ {
		row := word()
		for c := 0; c < w; c++ {
			open[r*w+c] = row[c] == '#'
		}
	}
	// the open cells form a tree; root it at the first open cell and keep, for
	// every cell, its parent, depth, the direction of the step from the parent
	// (as the index offset) and the number of turns from the root
	root := 0
	for !open[root] {
		root++
	}
	parent, depth := make([]int, cells), make([]int, cells)
	step, turns := make([]int, cells), make([]int, cells)
	for i := range parent {
		parent[i] = -1
	}
	parent[root] = root
	order := []int{root}
	for k := 0; k < len(order); k++ {
		v := order[k]
		r, c := v/w, v%w
		next := []int{v - w, v + w, v - 1, v + 1}
		fits := []bool{r > 0, r < h-1, c > 0, c < w-1}
		for d, u := range next {
			if fits[d] && open[u] && parent[u] < 0 {
				parent[u] = v
				depth[u] = depth[v] + 1
				step[u] = u - v
				turns[u] = turns[v]
				if v != root && step[v] != u-v {
					turns[u]++
				}
				order = append(order, u)
			}
		}
	}
	// closed cells point at themselves, which keeps the jump table in range
	for v := range parent {
		if parent[v] < 0 {
			parent[v] = v
		}
	}
	up := make([][]int, logCells)
	up[0] = parent
	for b := 1; b < logCells; b++ {
		up[b] = make([]int, cells)
		for v := 0; v < cells; v++ {
			up[b][v] = up[b-1][up[b-1][v]]
		}
	}
	for q := number(); q > 0; q-- {
		r1, c1, r2, c2 := number(), number(), number(), number()
		a, b := (r1-1)*w+c1-1, (r2-1)*w+c2-1
		if depth[a] < depth[b] {
			a, b = b, a
		}
		answer := 0
		if a != b {
			a1, b1 := a, b
			below := false
			if depth[a] > depth[b] {
				// lift a to just below b's depth: if it then hangs from b, b is
				// an ancestor and only the way down from b counts
				for k, bit := depth[a]-depth[b]-1, 0; k > 0; k, bit = k>>1, bit+1 {
					if k&1 == 1 {
						a1 = up[bit][a1]
					}
				}
				below = parent[a1] == b
				if !below {
					a1 = parent[a1]
				}
			}
			if below {
				answer = turns[a] - turns[a1]
			} else {
				for bit := logCells - 1; bit >= 0; bit-- {
					if up[bit][a1] != up[bit][b1] {
						a1, b1 = up[bit][a1], up[bit][b1]
					}
				}
				// a1 and b1 are the children of the meeting cell on the two
				// sides; the path turns there unless it goes straight through
				answer = turns[a] - turns[a1] + turns[b] - turns[b1]
				if step[a1] != -step[b1] {
					answer++
				}
			}
		}
		out.WriteString(strconv.Itoa(answer))
		out.WriteByte('\n')
	}
}
