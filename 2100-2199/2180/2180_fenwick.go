package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const (
	queryOperation = iota
	directOperation
	wholeOperation
	partialOperation
)

type scanner struct {
	data []byte
	pos  int
}

func (input *scanner) token() []byte {
	for input.pos < len(input.data) && input.data[input.pos] <= ' ' {
		input.pos++
	}
	start := input.pos
	for input.pos < len(input.data) && input.data[input.pos] > ' ' {
		input.pos++
	}
	return input.data[start:input.pos]
}

func (input *scanner) number() int {
	value := 0
	for _, digit := range input.token() {
		value = value*10 + int(digit-'0')
	}
	return value
}

type operation struct {
	kind   int
	vertex int
	limit  int
	value  int64
}

type sparseFenwick struct {
	size        int
	coordinates [][]int
	tree        [][]int64
}

func newSparseFenwick(size int) *sparseFenwick {
	return &sparseFenwick{
		size:        size,
		coordinates: make([][]int, size+1),
		tree:        make([][]int64, size+1),
	}
}

func (bit *sparseFenwick) register(position, limit int) {
	for position <= bit.size {
		bit.coordinates[position] = append(bit.coordinates[position], limit)
		position += position & -position
	}
}

func (bit *sparseFenwick) prepare() {
	for position := 1; position <= bit.size; position++ {
		values := bit.coordinates[position]
		sort.Ints(values)
		length := 0
		for _, value := range values {
			if length == 0 || values[length-1] != value {
				values[length] = value
				length++
			}
		}
		bit.coordinates[position] = values[:length]
		bit.tree[position] = make([]int64, length+1)
	}
}

func (bit *sparseFenwick) add(position, limit int, value int64) {
	for position <= bit.size {
		values := bit.coordinates[position]
		rank := len(values) - sort.SearchInts(values, limit)
		tree := bit.tree[position]
		for rank < len(tree) {
			tree[rank] += value
			rank += rank & -rank
		}
		position += position & -position
	}
}

func (bit *sparseFenwick) sum(position, depth int) int64 {
	var result int64
	for position > 0 {
		values := bit.coordinates[position]
		rank := len(values) - sort.SearchInts(values, depth)
		tree := bit.tree[position]
		for rank > 0 {
			result += tree[rank]
			rank -= rank & -rank
		}
		position -= position & -position
	}
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	size := input.number()
	parent := make([]int, size+1)
	firstChild := make([]int, size+1)
	nextSibling := make([]int, size+1)
	depth := make([]int, size+1)
	subtreeSize := make([]int, size+1)
	deepest := make([]int, size+1)
	for vertex := 1; vertex <= size; vertex++ {
		subtreeSize[vertex] = 1
	}
	for vertex := 2; vertex <= size; vertex++ {
		parent[vertex] = input.number()
		depth[vertex] = depth[parent[vertex]] + 1
		deepest[vertex] = depth[vertex]
		nextSibling[vertex] = firstChild[parent[vertex]]
		firstChild[parent[vertex]] = vertex
	}
	for vertex := size; vertex > 1; vertex-- {
		subtreeSize[parent[vertex]] += subtreeSize[vertex]
		if deepest[vertex] > deepest[parent[vertex]] {
			deepest[parent[vertex]] = deepest[vertex]
		}
	}

	entry := make([]int, size+1)
	exit := make([]int, size+1)
	stack := []int{1}
	timer := 0
	for len(stack) > 0 {
		vertex := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		timer++
		entry[vertex] = timer
		exit[vertex] = timer + subtreeSize[vertex] - 1
		for child := firstChild[vertex]; child != 0; child = nextSibling[child] {
			stack = append(stack, child)
		}
	}

	queryCount := input.number()
	operations := make([]operation, 0, queryCount)
	partial := newSparseFenwick(size)
	for index := 0; index < queryCount; index++ {
		symbol := input.token()[0]
		vertex := input.number()
		if symbol == '?' {
			operations = append(operations, operation{kind: queryOperation, vertex: vertex})
			continue
		}
		radius := input.number()
		value := int64(input.number())
		limit := depth[vertex] + radius
		kind := partialOperation
		if radius == 0 {
			kind = directOperation
		} else if limit >= deepest[vertex] {
			kind = wholeOperation
		} else {
			partial.register(entry[vertex], limit)
			partial.register(exit[vertex]+1, limit)
		}
		operations = append(operations, operation{kind, vertex, limit, value})
	}
	partial.prepare()

	direct := make([]int64, size+1)
	whole := make([]int64, size+1)
	output := bufio.NewWriter(os.Stdout)
	for _, current := range operations {
		vertex := current.vertex
		left := entry[vertex]
		right := exit[vertex] + 1
		switch current.kind {
		case queryOperation:
			answer := direct[vertex] + partial.sum(left, depth[vertex])
			for position := left; position > 0; position -= position & -position {
				answer += whole[position]
			}
			fmt.Fprintln(output, answer)
		case directOperation:
			direct[vertex] += current.value
		case wholeOperation:
			for position := left; position <= size; position += position & -position {
				whole[position] += current.value
			}
			for position := right; position <= size; position += position & -position {
				whole[position] -= current.value
			}
		case partialOperation:
			partial.add(left, current.limit, current.value)
			partial.add(right, current.limit, -current.value)
		}
	}
	output.Flush()
}
