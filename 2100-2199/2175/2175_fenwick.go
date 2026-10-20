package main

import (
	"bufio"
	"io/ioutil"
	"os"
	"strconv"
)

const absent = -1

type scanner struct {
	data []byte
	pos  int
}

func (in *scanner) integer() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	var value int64
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

type prefixMaximum struct {
	values []int64
	tree   []int
}

func (prefix *prefixMaximum) better(candidate, current int) bool {
	return current == absent || prefix.values[candidate] > prefix.values[current] ||
		(prefix.values[candidate] == prefix.values[current] && candidate < current)
}

func newPrefixMaximum(values []int64) *prefixMaximum {
	prefix := &prefixMaximum{values: values, tree: make([]int, len(values)+1)}
	for node := range prefix.tree {
		prefix.tree[node] = absent
	}
	for node := 1; node <= len(values); node++ {
		if prefix.better(node-1, prefix.tree[node]) {
			prefix.tree[node] = node - 1
		}
		parent := node + (node & -node)
		if parent <= len(values) && prefix.better(prefix.tree[node], prefix.tree[parent]) {
			prefix.tree[parent] = prefix.tree[node]
		}
	}
	return prefix
}

func (prefix *prefixMaximum) query(end int) int {
	result := absent
	for node := end; node > 0; node -= node & -node {
		if prefix.better(prefix.tree[node], result) {
			result = prefix.tree[node]
		}
	}
	return result
}

func (prefix *prefixMaximum) update(position int) {
	for node := position + 1; node <= len(prefix.values); node += node & -node {
		winner := prefix.tree[node]
		// A stored index sees the increase immediately; ancestors may store another index.
		if winner != position && !prefix.better(position, winner) {
			break
		}
		prefix.tree[node] = position
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	size := int(in.integer())
	values := make([]int64, size)
	for position := range values {
		values[position] = in.integer()
	}
	next := make([]int, size)
	for position := range next {
		next[position] = absent
	}
	last, count := 0, 1
	next[0] = size
	for position := 1; position < size; position++ {
		if values[position] > values[last] {
			next[last] = position
			next[position] = size
			last = position
			count++
		}
	}
	prefix := newPrefixMaximum(values)
	queries := int(in.integer())
	output := make([]byte, 0, queries*2)
	for query := 0; query < queries; query++ {
		position := int(in.integer()) - 1
		increment := in.integer()
		if increment != 0 {
			values[position] += increment
			if next[position] == absent {
				previous := prefix.query(position)
				if values[position] > values[previous] {
					next[position] = next[previous]
					next[previous] = position
					count++
				}
			}
			if next[position] != absent {
				following := next[position]
				for following < size && values[following] <= values[position] {
					removed := following
					following = next[following]
					next[removed] = absent
					count--
				}
				next[position] = following
			}
			prefix.update(position)
		}
		output = strconv.AppendInt(output, int64(count), 10)
		output = append(output, '\n')
	}
	writer := bufio.NewWriter(os.Stdout)
	_, _ = writer.Write(output)
	_ = writer.Flush()
}
