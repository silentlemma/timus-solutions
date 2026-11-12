package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const bufferSize = 65536
const decimalBase = 10
const numberReserve = 8

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func find(rep []uint32, v uint32) uint32 {
	for rep[v] != v {
		rep[v] = rep[rep[v]]
		v = rep[v]
	}
	return v
}

func prepare(n int, in *bufio.Reader) ([]uint32, []uint32, int) {
	head := make([]uint32, n+1)
	to, next := make([]uint32, 2*n-1), make([]uint32, 2*n-1)
	for edge := 1; edge < len(to); edge += 2 {
		a, b := number(in), number(in)
		to[edge] = uint32(b)
		next[edge] = head[a]
		head[a] = uint32(edge)
		to[edge+1] = uint32(a)
		next[edge+1] = head[b]
		head[b] = uint32(edge + 1)
	}
	queries := number(in)
	if queries == 0 {
		return nil, nil, 0
	}
	parent, rep, tin := make([]uint32, n+1), make([]uint32, n+1), make([]uint32, n+1)
	parent[1] = 1
	order := make([]uint32, 0, n)
	adjacent := make([]uint32, n-1)
	stack := make([]int32, 1, n)
	stack[0] = 1
	for len(stack) > 0 {
		event := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if event < 0 {
			v := uint32(-event)
			rep[v] = parent[v]
			continue
		}
		v := uint32(event)
		tin[v] = uint32(len(order) + 1)
		rep[v] = v
		order = append(order, v)
		if v > 1 && tin[v-1] != 0 {
			adjacent[v-2] = tin[find(rep, v-1)] - 1
		}
		if v < uint32(n) && tin[v+1] != 0 {
			adjacent[v-1] = tin[find(rep, v+1)] - 1
		}
		stack = append(stack, -event)
		for e := head[v]; e != 0; e = next[e] {
			w := to[e]
			if w != parent[v] {
				parent[w] = v
				stack = append(stack, int32(w))
			}
		}
	}
	return order, adjacent, queries
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	n := number(in)
	order, adjacent, queries := prepare(n, in)
	if queries == 0 {
		return
	}
	table := [][]uint32{adjacent}
	for span := 1; 2*span <= len(adjacent); span *= 2 {
		previous := table[len(table)-1]
		row := make([]uint32, len(adjacent)-2*span+1)
		for index := range row {
			value := previous[index]
			if previous[index+span] < value {
				value = previous[index+span]
			}
			row[index] = value
		}
		table = append(table, row)
	}
	output := make([]byte, 0, bufferSize)
	for query := 0; query < queries; query++ {
		left, right := number(in), number(in)
		answer := left
		if left < right {
			level := bits.Len(uint(right-left)) - 1
			row := table[level]
			value := row[left-1]
			other := row[right-1-(1<<uint(level))]
			if other < value {
				value = other
			}
			answer = int(order[value])
		}
		if len(output)+numberReserve > cap(output) {
			os.Stdout.Write(output)
			output = output[:0]
		}
		output = strconv.AppendInt(output, int64(answer), decimalBase)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
