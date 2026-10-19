package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const (
	directionCount = 4
	leftTurn       = 3
)

var rowStep = [directionCount]int{-1, 0, 1, 0}
var colStep = [directionCount]int{0, 1, 0, -1}

type input struct {
	data []byte
	pos  int
}

func (in *input) token() []byte {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	start := in.pos
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		in.pos++
	}
	return in.data[start:in.pos]
}

func (in *input) integer() int {
	value := 0
	for _, digit := range in.token() {
		value = value*10 + int(digit-'0')
	}
	return value
}

type segmentTree struct {
	base int
	data []int
}

func newSegmentTree(size int) segmentTree {
	base := 1
	for base < size {
		base *= 2
	}
	return segmentTree{base, make([]int, base*2)}
}

func (tree *segmentTree) update(position, value int) {
	position += tree.base
	for position > 0 {
		tree.data[position] = value
		position /= 2
	}
}

func (tree *segmentTree) query(left, right int) int {
	left += tree.base
	right += tree.base
	answer := 0
	for left < right {
		if left%2 == 1 {
			if tree.data[left] > answer {
				answer = tree.data[left]
			}
			left++
		}
		if right%2 == 1 {
			right--
			if tree.data[right] > answer {
				answer = tree.data[right]
			}
		}
		left /= 2
		right /= 2
	}
	return answer
}

type event struct {
	time, row, col int
	turn           byte
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n, m := in.integer(), in.integer()
	grid := make([][]byte, n*2-1)
	root := 0
	for row := range grid {
		grid[row] = in.token()
		if row%2 == 0 {
			for col := 0; col < m; col++ {
				if grid[row][col*2] == 'S' {
					root = row/2*m + col
				}
			}
		}
	}
	count := n * m
	parent := make([]int, count)
	depth := make([]int, count)
	firstChild := make([]int, count)
	nextSibling := make([]int, count)
	chosen := make([]int, count)
	incoming := make([]int, count)
	desired := make([]byte, count)
	tin := make([]int, count)
	size := make([]int, count)
	heavy := make([]int, count)
	head := make([]int, count)
	endpoint := make([]int, count)
	for vertex := 0; vertex < count; vertex++ {
		firstChild[vertex], nextSibling[vertex] = count, count
		chosen[vertex], heavy[vertex] = count, count
	}
	parent[root] = root
	stack := []int{root}
	order := make([]int, 0, count)
	for len(stack) > 0 {
		vertex := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		tin[vertex] = len(order)
		order = append(order, vertex)
		row, col := vertex/m, vertex%m
		for direction := 0; direction < directionCount; direction++ {
			nr, nc := row+rowStep[direction], col+colStep[direction]
			if nr < 0 || nr >= n || nc < 0 || nc >= m {
				continue
			}
			track := grid[row*2+rowStep[direction]][col*2+colStep[direction]]
			if track != '-' && track != '|' {
				continue
			}
			child := nr*m + nc
			if child == parent[vertex] {
				continue
			}
			parent[child], depth[child] = vertex, depth[vertex]+1
			incoming[child] = direction
			turn := (direction - incoming[vertex] + directionCount) % directionCount
			desired[child] = 'F'
			if turn == 1 {
				desired[child] = 'R'
			} else if turn == leftTurn {
				desired[child] = 'L'
			}
			if vertex == root || desired[child] == grid[row*2][col*2] {
				chosen[vertex] = child
			}
			nextSibling[child], firstChild[vertex] = firstChild[vertex], child
			stack = append(stack, child)
		}
	}
	for index := len(order) - 1; index >= 0; index-- {
		vertex := order[index]
		size[vertex] = 1
		for child := firstChild[vertex]; child != count; child = nextSibling[child] {
			size[vertex] += size[child]
			if heavy[vertex] == count || size[child] > size[heavy[vertex]] {
				heavy[vertex] = child
			}
		}
		endpoint[vertex] = vertex
		if chosen[vertex] != count {
			endpoint[vertex] = endpoint[chosen[vertex]]
		}
	}
	head[root] = root
	for _, vertex := range order {
		for child := firstChild[vertex]; child != count; child = nextSibling[child] {
			head[child] = child
			if child == heavy[vertex] {
				head[child] = head[vertex]
			}
		}
	}
	lca := func(first, second int) int {
		for head[first] != head[second] {
			if depth[head[first]] < depth[head[second]] {
				first, second = second, first
			}
			first = parent[head[first]]
		}
		if depth[first] < depth[second] {
			return first
		}
		return second
	}
	queries := in.integer()
	history := make([]int, queries+1)
	tree := newSegmentTree(len(order))
	events := make([]event, 0)
	previous := count
	for index := 1; index <= queries; index++ {
		time, row, col := in.integer(), in.integer()-1, in.integer()-1
		destination := row*m + col
		history[index] = destination
		if destination == previous {
			continue
		}
		previous = destination
		subtree := root
		for {
			latest := tree.query(tin[subtree], tin[subtree]+size[subtree])
			old := endpoint[subtree]
			if latest != 0 {
				old = history[latest]
			}
			if old == destination {
				break
			}
			vertex := lca(destination, old)
			child := firstChild[vertex]
			for tin[destination] < tin[child] || tin[destination] >= tin[child]+size[child] {
				child = nextSibling[child]
			}
			events = append(events, event{
				time + depth[vertex], vertex/m + 1, vertex%m + 1, desired[child],
			})
			subtree = child
		}
		// New timestamps exceed every old value, including all ancestors in the tree.
		tree.update(tin[destination], index)
	}
	sort.Slice(events, func(first, second int) bool {
		a, b := events[first], events[second]
		if a.time != b.time {
			return a.time < b.time
		}
		if a.row != b.row {
			return a.row < b.row
		}
		if a.col != b.col {
			return a.col < b.col
		}
		return a.turn < b.turn
	})
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, len(events))
	for _, change := range events {
		fmt.Fprintf(out, "%d %d %d %c\n", change.time, change.row, change.col, change.turn)
	}
	out.Flush()
}
