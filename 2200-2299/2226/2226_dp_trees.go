package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const maxLength = 1000000000
const infinity = maxLength + 1

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	pos := 0
	nextInt := func() int {
		for pos < len(data) && data[pos] <= ' ' {
			pos++
		}
		value := 0
		for pos < len(data) && data[pos] >= '0' && data[pos] <= '9' {
			value = value*10 + int(data[pos]-'0')
			pos++
		}
		return value
	}
	n := nextInt()
	graph := make([][]int, n+1)
	first, second := make([]int, n+1), make([]int, n+1)
	shortest, nextShortest := make([]int, n+1), make([]int, n+1)
	for v := 1; v <= n; v++ {
		shortest[v], nextShortest[v] = infinity, infinity
	}
	add := func(u, v, length int) {
		graph[u] = append(graph[u], v)
		if length < shortest[u] {
			nextShortest[u], second[u] = shortest[u], first[u]
			shortest[u], first[u] = length, v
		} else if length < nextShortest[u] {
			nextShortest[u], second[u] = length, v
		}
	}
	for i := 1; i < n; i++ {
		u, v, length := nextInt(), nextInt(), nextInt()
		add(u, v, length)
		add(v, u, length)
	}
	parent := make([]int, n+1)
	order := make([]int, 1, n)
	order[0] = 1
	for i := 0; i < n; i++ {
		v := order[i]
		for _, u := range graph[v] {
			if u != parent[v] {
				parent[u] = v
				order = append(order, u)
			}
		}
	}

	// down[v] is the endpoint after arriving at v from its parent.
	down, up := make([]int, n+1), make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		v := order[i]
		u := first[v]
		if u == parent[v] {
			u = second[v]
		}
		down[v] = v
		if u != 0 {
			down[v] = down[u]
		}
	}
	// up[v] is the endpoint after leaving v for its parent.
	for i := 1; i < n; i++ {
		v := order[i]
		p := parent[v]
		u := first[p]
		if u == v {
			u = second[p]
		}
		if u == 0 {
			up[v] = p
		} else if u == parent[p] {
			up[v] = up[p]
		} else {
			up[v] = down[u]
		}
	}
	output := make([]byte, 0)
	for v := 1; v <= n; v++ {
		if v != 1 {
			output = append(output, ' ')
		}
		answer := down[v]
		if first[v] == parent[v] {
			answer = up[v]
		}
		output = strconv.AppendInt(output, int64(answer), 10)
	}
	output = append(output, '\n')
	writer := bufio.NewWriter(os.Stdout)
	writer.Write(output)
	writer.Flush()
}
