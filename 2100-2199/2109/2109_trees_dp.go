package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const bufferSize = 65536

type scanner struct {
	data  []byte
	index int
}

func (in *scanner) nextInt() int {
	for in.index < len(in.data) && in.data[in.index] <= ' ' {
		in.index++
	}
	value := 0
	for in.index < len(in.data) && in.data[in.index] > ' ' {
		value = value*10 + int(in.data[in.index]-'0')
		in.index++
	}
	return value
}

func find(representative []int, vertex int) int {
	for representative[vertex] != vertex {
		representative[vertex] = representative[representative[vertex]]
		vertex = representative[vertex]
	}
	return vertex
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n := in.nextInt()
	head := make([]int, n+1)
	for vertex := range head {
		head[vertex] = -1
	}
	to := make([]int, 2*(n-1))
	next := make([]int, len(to))
	for edge := 0; edge < len(to); edge += 2 {
		u, v := in.nextInt(), in.nextInt()
		to[edge], next[edge], head[u] = v, head[u], edge
		to[edge+1], next[edge+1], head[v] = u, head[v], edge+1
	}

	parent := make([]int, n+1)
	representative := make([]int, n+1)
	tin := make([]int, n+1)
	for vertex := range tin {
		tin[vertex] = -1
		representative[vertex] = vertex
	}
	parent[1] = 1
	order := make([]int, 0, n)
	adjacent := make([]int, n-1)
	stack := make([]int, 1, 2*n)
	stack[0] = 1
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if u < 0 {
			representative[-u] = parent[-u]
			continue
		}
		tin[u] = len(order)
		order = append(order, u)
		// Finished subtrees point to their nearest active ancestor.
		if u > 1 && tin[u-1] >= 0 {
			adjacent[u-2] = tin[find(representative, u-1)]
		}
		if u < n && tin[u+1] >= 0 {
			adjacent[u-1] = tin[find(representative, u+1)]
		}
		stack = append(stack, -u)
		for edge := head[u]; edge != -1; edge = next[edge] {
			v := to[edge]
			if v != parent[u] {
				parent[v] = u
				stack = append(stack, v)
			}
		}
	}

	logarithm := make([]int, n+1)
	for length := 2; length <= n; length++ {
		logarithm[length] = logarithm[length/2] + 1
	}
	table := [][]int{adjacent}
	for span := 1; 2*span <= len(adjacent); span *= 2 {
		previous := table[len(table)-1]
		row := make([]int, len(adjacent)-2*span+1)
		for index := range row {
			value := previous[index]
			if previous[index+span] < value {
				value = previous[index+span]
			}
			row[index] = value
		}
		table = append(table, row)
	}

	queries := in.nextInt()
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	answerText := make([]byte, 0, 10)
	for query := 0; query < queries; query++ {
		left, right := in.nextInt(), in.nextInt()
		answer := left
		if left < right {
			level := logarithm[right-left]
			row := table[level]
			value := row[left-1]
			other := row[right-1-(1<<uint(level))]
			if other < value {
				value = other
			}
			answer = order[value]
		}
		answerText = strconv.AppendInt(answerText[:0], int64(answer), 10)
		out.Write(answerText)
		out.WriteByte('\n')
	}
	out.Flush()
}
