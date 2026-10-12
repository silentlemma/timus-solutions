package main

import (
	"bufio"
	"os"
	"strconv"
)

const ids = 40001

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	children := make([][]int, ids)
	root := -1
	for i := 0; i < n; i++ {
		node, parent := next(), next()
		if parent < 0 {
			root = node
		} else {
			children[parent] = append(children[parent], node)
		}
	}
	// enter[v] and leave[v] bound the times of the whole subtree of v
	enter, leave := make([]int, ids), make([]int, ids)
	for i := range enter {
		enter[i], leave[i] = -1, -1
	}
	clock, stack := 0, []int{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if node >= 0 {
			enter[node] = clock
			clock++
			stack = append(stack, ^node)
			stack = append(stack, children[node]...)
		} else {
			leave[^node] = clock
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for q := next(); q > 0; q-- {
		a, b := next(), next()
		switch {
		case enter[a] >= 0 && enter[a] <= enter[b] && enter[b] < leave[a]:
			out.WriteString("1\n")
		case enter[b] >= 0 && enter[b] <= enter[a] && enter[a] < leave[b]:
			out.WriteString("2\n")
		default:
			out.WriteString("0\n")
		}
	}
}
