package main

import (
	"bufio"
	"fmt"
	"os"
)

const bufferSize = 4096
const unvisited = ^uint16(0)

var input [bufferSize]byte
var position, available, n, q int
var head, to, following, askHead, askNext, distance, answer, depth, path, stack []uint16

func read() int {
	if position == available {
		available, _ = os.Stdin.Read(input[:])
		position = 0
		if available == 0 {
			return -1
		}
	}
	c := input[position]
	position++
	return int(c)
}

func nextInt() int {
	c := read()
	for c <= ' ' {
		c = read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + c - '0'
		c = read()
	}
	return value
}

func walk(root uint16) uint16 {
	for i := range depth {
		depth[i] = unvisited
	}
	depth[root] = 0
	stack[0] = root
	top, deepest := 1, root
	for top > 0 {
		top--
		vertex := stack[top]
		dv := depth[vertex]
		path[dv] = vertex
		if dv > depth[deepest] {
			deepest = vertex
		}
		for query := askHead[vertex]; query != 0; query = askNext[query] {
			if answer[query] == 0 && distance[query] <= dv {
				answer[query] = path[dv-distance[query]]
			}
		}
		for edge := head[vertex]; edge != 0; edge = following[edge] {
			child := to[edge]
			if depth[child] == unvisited {
				depth[child] = dv + 1
				stack[top] = child
				top++
			}
		}
	}
	return deepest
}

func main() {
	n, q = nextInt(), nextInt()
	// Vertex<=20000, edge<=39998, query<=50000: all IDs fit uint16.
	// One-based indices make zero the missing-link sentinel.
	head = make([]uint16, n+1)
	to = make([]uint16, 2*n)
	following = make([]uint16, 2*n)
	edge := 0
	for i := 0; i < n-1; i++ {
		a, b := nextInt(), nextInt()
		edge++
		to[edge] = uint16(b)
		following[edge] = head[a]
		head[a] = uint16(edge)
		edge++
		to[edge] = uint16(a)
		following[edge] = head[b]
		head[b] = uint16(edge)
	}
	askHead = make([]uint16, n+1)
	askNext = make([]uint16, q+1)
	distance = make([]uint16, q+1)
	answer = make([]uint16, q+1)
	for i := 1; i <= q; i++ {
		vertex := nextInt()
		distance[i] = uint16(nextInt())
		askNext[i] = askHead[vertex]
		askHead[vertex] = uint16(i)
	}
	depth = make([]uint16, n+1)
	path = make([]uint16, n+1)
	stack = make([]uint16, n+1)
	// A path to one of the diameter ends reaches every feasible distance.
	a := walk(1)
	b := walk(a)
	walk(b)
	output := bufio.NewWriter(os.Stdout)
	for _, value := range answer[1:] {
		fmt.Fprintln(output, value)
	}
	output.Flush()
}
