package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

type scanner struct {
	data []byte
	pos  int
}

func (in *scanner) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n, m := in.nextInt(), in.nextInt()
	x, y := int64(in.nextInt()), int64(in.nextInt())
	graph := make([][]int, n)
	reverse := make([][]int, n)
	for edge := 0; edge < m; edge++ {
		from, to := in.nextInt()-1, in.nextInt()-1
		graph[from] = append(graph[from], to)
		reverse[to] = append(reverse[to], from)
	}

	seen := make([]bool, n)
	next := make([]int, n)
	order := make([]int, 0, n)
	stack := make([]int, 0, n)
	for start := 0; start < n; start++ {
		if seen[start] {
			continue
		}
		seen[start] = true
		stack = append(stack, start)
		for len(stack) > 0 {
			vertex := stack[len(stack)-1]
			if next[vertex] < len(graph[vertex]) {
				to := graph[vertex][next[vertex]]
				next[vertex]++
				if !seen[to] {
					seen[to] = true
					stack = append(stack, to)
				}
			} else {
				order = append(order, vertex)
				stack = stack[:len(stack)-1]
			}
		}
	}

	component := make([]int, n)
	for vertex := range component {
		component[vertex] = -1
	}
	componentCount := 0
	for index := len(order) - 1; index >= 0; index-- {
		start := order[index]
		if component[start] != -1 {
			continue
		}
		component[start] = componentCount
		stack = append(stack, start)
		for len(stack) > 0 {
			vertex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, to := range reverse[vertex] {
				if component[to] == -1 {
					component[to] = componentCount
					stack = append(stack, to)
				}
			}
		}
		componentCount++
	}

	weakSeen := make([]bool, n)
	counted := make([]bool, componentCount)
	answer := int64(0)
	for start := 0; start < n; start++ {
		if weakSeen[start] {
			continue
		}
		vertices, components := int64(0), int64(0)
		weakSeen[start] = true
		stack = append(stack, start)
		for len(stack) > 0 {
			vertex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			vertices++
			id := component[vertex]
			if !counted[id] {
				counted[id] = true
				components++
			}
			for _, to := range graph[vertex] {
				if !weakSeen[to] {
					weakSeen[to] = true
					stack = append(stack, to)
				}
			}
			for _, to := range reverse[vertex] {
				if !weakSeen[to] {
					weakSeen[to] = true
					stack = append(stack, to)
				}
			}
		}
		cost := (vertices - 1) * y
		if x < y {
			cost = (vertices-components)*y + (components-1)*x
			cycleCost := vertices * x
			if cycleCost < cost {
				cost = cycleCost
			}
		}
		answer += cost
	}
	fmt.Println(answer)
}
