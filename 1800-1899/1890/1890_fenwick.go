package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

type input struct {
	data []byte
	at   int
}

func (in *input) word() []byte {
	for in.at < len(in.data) && in.data[in.at] <= ' ' {
		in.at++
	}
	start := in.at
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		in.at++
	}
	return in.data[start:in.at]
}

func (in *input) number() int64 {
	var value int64
	for _, digit := range in.word() {
		value = value*10 + int64(digit-'0')
	}
	return value
}

type fenwick struct {
	linear   []int64
	constant []int64
}

func newFenwick(values []int64) fenwick {
	tree := fenwick{make([]int64, len(values)), make([]int64, len(values))}
	for i := 1; i < len(values); i++ {
		difference := values[i] - values[i-1]
		tree.linear[i] = difference
		tree.constant[i] = difference * int64(i-1)
	}
	for i := 1; i < len(values); i++ {
		ancestor := i + (i & -i)
		if ancestor < len(values) {
			tree.linear[ancestor] += tree.linear[i]
			tree.constant[ancestor] += tree.constant[i]
		}
	}
	return tree
}

func (tree *fenwick) suffixAdd(index int, amount int64) {
	weighted := amount * int64(index-1)
	for index < len(tree.linear) {
		tree.linear[index] += amount
		tree.constant[index] += weighted
		index += index & -index
	}
}

func (tree *fenwick) prefixSum(index int) int64 {
	var coefficient, offset int64
	for at := index; at > 0; at -= at & -at {
		coefficient += tree.linear[at]
		offset += tree.constant[at]
	}
	return coefficient*int64(index) - offset
}

func (tree *fenwick) point(index int) int64 {
	var result int64
	for index > 0 {
		result += tree.linear[index]
		index -= index & -index
	}
	return result
}

func (tree *fenwick) values() []int64 {
	// Undo the linear Fenwick build, then integrate the differences.
	for i := len(tree.linear) - 1; i > 0; i-- {
		ancestor := i + (i & -i)
		if ancestor < len(tree.linear) {
			tree.linear[ancestor] -= tree.linear[i]
		}
	}
	for i := 1; i < len(tree.linear); i++ {
		tree.linear[i] += tree.linear[i-1]
	}
	return tree.linear
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n, q := int(in.number()), int(in.number())
	parent, size := make([]int, n), make([]int, n)
	tin, cursor := make([]int, n), make([]int, n)
	salary := make([]int64, n)
	salary[0] = in.number()
	for vertex := 0; vertex < n; vertex++ {
		size[vertex], tin[vertex], cursor[vertex] = 1, 1, 2
		if vertex > 0 {
			parent[vertex], salary[vertex] = int(in.number()), in.number()
		}
	}
	for vertex := n - 1; vertex > 0; vertex-- {
		size[parent[vertex]] += size[vertex]
	}
	// Reserve consecutive child blocks; every parent has a smaller number.
	for vertex := 1; vertex < n; vertex++ {
		boss := parent[vertex]
		tin[vertex] = cursor[boss]
		cursor[boss] += size[vertex]
		cursor[vertex] = tin[vertex] + 1
	}
	initial := make([]int64, n+1)
	for vertex := 0; vertex < n; vertex++ {
		initial[tin[vertex]] = salary[vertex]
	}
	tree := newFenwick(initial)
	for query := 0; query < q; query++ {
		kind := in.word()
		vertex, threshold, amount := int(in.number()), in.number(), in.number()
		left, length := tin[vertex], 1
		if kind[0] == 'd' {
			length = size[vertex]
		}
		total := tree.point(left)
		if length > 1 {
			total = tree.prefixSum(left+length-1) - tree.prefixSum(left-1)
		}
		if total < threshold*int64(length) {
			tree.suffixAdd(left, amount)
			tree.suffixAdd(left+length, -amount)
		}
	}
	finalSalary := tree.values()
	out := bufio.NewWriter(os.Stdout)
	for vertex := 0; vertex < n; vertex++ {
		fmt.Fprintln(out, finalSalary[tin[vertex]])
	}
	out.Flush()
}
