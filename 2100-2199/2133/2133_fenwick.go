package main

import (
	"io/ioutil"
	"os"
	"sort"
	"strconv"
)

const update = 1

type input struct {
	data []byte
	pos  int
}

func (in *input) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func minimum(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func add(tree []int, index, delta int) {
	for index < len(tree) {
		tree[index] += delta
		index += index & -index
	}
}

func prefix(tree []int, index int) int {
	total := 0
	for index > 0 {
		total += tree[index]
		index -= index & -index
	}
	return total
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n := in.nextInt()
	heights := make([]int, n)
	coordinates := make([]int, n)
	for i := range heights {
		heights[i] = in.nextInt()
		coordinates[i] = heights[i]
	}
	q := in.nextInt()
	positions := make([]int, q)
	values := make([]int, q)
	for i := range positions {
		positions[i] = -1
		if in.nextInt() == update {
			positions[i] = in.nextInt() - 1
		}
		values[i] = in.nextInt()
		coordinates = append(coordinates, values[i])
	}
	sort.Ints(coordinates)
	size := 0
	for _, value := range coordinates {
		if size == 0 || coordinates[size-1] != value {
			coordinates[size] = value
			size++
		}
	}
	coordinates = coordinates[:size]
	for i, value := range heights {
		heights[i] = sort.SearchInts(coordinates, value) + 1
	}
	for i, value := range values {
		values[i] = sort.SearchInts(coordinates, value) + 1
	}
	tree := make([]int, size+1)
	// Each active building contributes one, and each active adjacency removes one.
	for i, value := range heights {
		tree[value]++
		if i > 0 {
			tree[minimum(heights[i-1], value)]--
		}
	}
	for i := 1; i <= size; i++ {
		parent := i + (i & -i)
		if parent <= size {
			tree[parent] += tree[i]
		}
	}
	output := make([]byte, 0)
	for operation, position := range positions {
		value := values[operation]
		if position < 0 {
			answer := 1 - prefix(tree, value-1)
			output = strconv.AppendInt(output, int64(answer), 10)
			output = append(output, '\n')
			continue
		}
		old := heights[position]
		if old == value {
			continue
		}
		add(tree, old, -1)
		add(tree, value, 1)
		for neighbor := position - 1; neighbor <= position+1; neighbor += 2 {
			if neighbor < 0 || neighbor >= n {
				continue
			}
			before := minimum(old, heights[neighbor])
			after := minimum(value, heights[neighbor])
			if before != after {
				add(tree, before, 1)
				add(tree, after, -1)
			}
		}
		heights[position] = value
	}
	os.Stdout.Write(output)
}
