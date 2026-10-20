package main

import (
	"bufio"
	"fmt"
	"os"
)

type tree struct {
	parent []int
	order  []int
}

func readTree(in *bufio.Reader, n int) tree {
	parent := make([]int, n)
	children := make([][]int, n)
	for vertex := 1; vertex < n; vertex++ {
		fmt.Fscan(in, &parent[vertex])
		p := parent[vertex]
		children[p] = append(children[p], vertex)
	}

	order := make([]int, 0, n)
	stack := []int{0}
	for len(stack) > 0 {
		vertex := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, vertex)
		for i := len(children[vertex]) - 1; i >= 0; i-- {
			stack = append(stack, children[vertex][i])
		}
	}
	return tree{parent, order}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	a := readTree(in, n)
	b := readTree(in, n)
	label := make([]int, n)
	for i := 0; i < n; i++ {
		label[b.order[i]] = a.order[i]
	}

	operations := make([][2]int, 0, n)
	for i := 1; i < n; i++ {
		vertex := a.order[i]
		previous := a.order[i-1]
		if a.parent[vertex] != previous {
			operations = append(operations, [2]int{vertex, previous})
		}
	}
	// Undo the target's flattening after matching the two preorder paths.
	for i := n - 1; i > 0; i-- {
		vertex := b.order[i]
		if b.parent[vertex] != b.order[i-1] {
			operations = append(operations, [2]int{label[vertex], label[b.parent[vertex]]})
		}
	}

	fmt.Fprintln(out, len(operations))
	for _, operation := range operations {
		fmt.Fprintln(out, operation[0], operation[1])
	}
}
