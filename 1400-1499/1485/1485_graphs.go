package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	win  = 3
	draw = 1
)

var (
	graph               [][]int
	idx, low, comp, stk []int
	onStack             []bool
	counter, components int
)

// visit is Tarjan's search for strongly connected components
func visit(v int) {
	idx[v], low[v] = counter, counter
	counter++
	stk = append(stk, v)
	onStack[v] = true
	for _, u := range graph[v] {
		if idx[u] < 0 {
			visit(u)
			if low[u] < low[v] {
				low[v] = low[u]
			}
		} else if onStack[u] && idx[u] < low[v] {
			low[v] = idx[u]
		}
	}
	if low[v] == idx[v] {
		for {
			u := stk[len(stk)-1]
			stk = stk[:len(stk)-1]
			onStack[u] = false
			comp[u] = components
			if u == v {
				break
			}
		}
		components++
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	said := make([][]int, n)
	for i := range said {
		said[i] = make([]int, n)
		for j := range said[i] {
			fmt.Fscan(reader, &said[i][j])
		}
	}
	// 2-SAT on "captain i tells the truth" (literal 2i) or lies (2i + 1),
	// and i scored against j exactly when the literal of statement (i, j) holds
	literal := func(i, j int) int {
		if said[i][j] == 1 {
			return 2 * i
		}
		return 2*i + 1
	}
	graph = make([][]int, 2*n)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if said[i][j] >= 0 && said[j][i] >= 0 {
				// somebody scores in every match: a or b, so not a -> b
				a, b := literal(i, j), literal(j, i)
				graph[a^1] = append(graph[a^1], b)
				graph[b^1] = append(graph[b^1], a)
			}
		}
	}
	idx, low, comp = make([]int, 2*n), make([]int, 2*n), make([]int, 2*n)
	onStack = make([]bool, 2*n)
	for v := range idx {
		idx[v] = -1
	}
	for v := 0; v < 2*n; v++ {
		if idx[v] < 0 {
			visit(v)
		}
	}
	truthful := make([]bool, n)
	for i := 0; i < n; i++ {
		if comp[2*i] == comp[2*i+1] {
			fmt.Fprintln(writer, "Impossible")
			return
		}
		// Tarjan numbers components in reverse topological order
		truthful[i] = comp[2*i] < comp[2*i+1]
	}
	scored := func(i, j int) bool { return said[i][j] < 0 || (said[i][j] == 1) == truthful[i] }
	table := make([][]int, n)
	for i := range table {
		table[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			a, b := scored(i, j), scored(j, i)
			switch {
			case a && b:
				table[i][j], table[j][i] = draw, draw
			case a:
				table[i][j] = win
			default:
				table[j][i] = win
			}
		}
	}
	for _, row := range table {
		for j, x := range row {
			if j > 0 {
				writer.WriteByte(' ')
			}
			writer.WriteString(strconv.Itoa(x))
		}
		writer.WriteByte('\n')
	}
}
