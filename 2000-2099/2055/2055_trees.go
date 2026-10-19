package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type Edge struct{ weight, first, second, id int }
type DisjointSet struct{ parent []int }

func newDisjointSet(size int) *DisjointSet {
	result := &DisjointSet{make([]int, size)}
	for i := range result.parent {
		result.parent[i] = -1
	}
	return result
}
func (set *DisjointSet) root(vertex int) int {
	for set.parent[vertex] >= 0 {
		if set.parent[set.parent[vertex]] >= 0 {
			set.parent[vertex] = set.parent[set.parent[vertex]]
		}
		vertex = set.parent[vertex]
	}
	return vertex
}
func (set *DisjointSet) unite(first, second int) bool {
	first, second = set.root(first), set.root(second)
	if first == second {
		return false
	}
	if set.parent[first] > set.parent[second] {
		first, second = second, first
	}
	set.parent[first] += set.parent[second]
	set.parent[second] = first
	return true
}

type LinkCut struct {
	left, right, parent, minimum, key, ancestors []int
	reverse                                      []bool
}

func newLinkCut(vertices, edges int) *LinkCut {
	size := 2 * vertices
	tree := &LinkCut{left: make([]int, size), right: make([]int, size), parent: make([]int, size),
		minimum: make([]int, size), key: make([]int, size), reverse: make([]bool, size)}
	for i := 0; i < size; i++ {
		tree.minimum[i], tree.key[i] = i, edges+1
	}
	return tree
}
func (tree *LinkCut) auxiliaryRoot(vertex int) bool {
	ancestor := tree.parent[vertex]
	return ancestor == 0 || (tree.left[ancestor] != vertex && tree.right[ancestor] != vertex)
}
func (tree *LinkCut) pull(vertex int) {
	best := vertex
	first, second := tree.minimum[tree.left[vertex]], tree.minimum[tree.right[vertex]]
	if tree.key[first] < tree.key[best] {
		best = first
	}
	if tree.key[second] < tree.key[best] {
		best = second
	}
	tree.minimum[vertex] = best
}
func (tree *LinkCut) toggle(vertex int) {
	if vertex != 0 {
		tree.left[vertex], tree.right[vertex] = tree.right[vertex], tree.left[vertex]
		tree.reverse[vertex] = !tree.reverse[vertex]
	}
}
func (tree *LinkCut) rotate(vertex int) {
	ancestor := tree.parent[vertex]
	grandparent := tree.parent[ancestor]
	var child int
	if tree.left[ancestor] == vertex {
		child = tree.right[vertex]
		tree.left[ancestor], tree.right[vertex] = child, ancestor
	} else {
		child = tree.left[vertex]
		tree.right[ancestor], tree.left[vertex] = child, ancestor
	}
	if child != 0 {
		tree.parent[child] = ancestor
	}
	if grandparent != 0 {
		if tree.left[grandparent] == ancestor {
			tree.left[grandparent] = vertex
		} else if tree.right[grandparent] == ancestor {
			tree.right[grandparent] = vertex
		}
	}
	tree.parent[vertex], tree.parent[ancestor] = grandparent, vertex
	tree.pull(ancestor)
	tree.pull(vertex)
}
func (tree *LinkCut) splay(vertex int) {
	tree.ancestors = tree.ancestors[:0]
	node := vertex
	tree.ancestors = append(tree.ancestors, node)
	for !tree.auxiliaryRoot(node) {
		node = tree.parent[node]
		tree.ancestors = append(tree.ancestors, node)
	}
	for i := len(tree.ancestors) - 1; i >= 0; i-- {
		node = tree.ancestors[i]
		if tree.reverse[node] {
			tree.toggle(tree.left[node])
			tree.toggle(tree.right[node])
			tree.reverse[node] = false
		}
	}
	for !tree.auxiliaryRoot(vertex) {
		ancestor := tree.parent[vertex]
		grandparent := tree.parent[ancestor]
		if !tree.auxiliaryRoot(ancestor) {
			if (tree.left[grandparent] == ancestor) == (tree.left[ancestor] == vertex) {
				tree.rotate(ancestor)
			} else {
				tree.rotate(vertex)
			}
		}
		tree.rotate(vertex)
	}
}
func (tree *LinkCut) access(vertex int) {
	last := 0
	for node := vertex; node != 0; node = tree.parent[node] {
		tree.splay(node)
		tree.right[node] = last
		if last != 0 {
			tree.parent[last] = node
		}
		tree.pull(node)
		last = node
	}
	tree.splay(vertex)
}
func (tree *LinkCut) makeRoot(vertex int) { tree.access(vertex); tree.toggle(vertex) }
func (tree *LinkCut) add(first, second, node, rank int) {
	tree.key[node] = rank
	tree.makeRoot(first)
	tree.parent[first] = node
	tree.makeRoot(second)
	tree.parent[second] = node
}
func (tree *LinkCut) replaceMinimum(first, second, rank int) int {
	tree.makeRoot(first)
	tree.access(second)
	edge := tree.minimum[second]
	tree.splay(edge)
	old := tree.key[edge]
	tree.toggle(tree.left[edge])
	tree.toggle(tree.right[edge])
	tree.key[edge] = rank
	tree.pull(edge)
	return old
}
func solve(vertices int, edges []Edge) []int {
	forest := newLinkCut(vertices, len(edges))
	components := newDisjointSet(vertices)
	active := make([]bool, len(edges))
	count, lower, bestLeft, bestRight, bestWidth := 0, 0, 0, 0, -1
	for rank, edge := range edges {
		if components.unite(edge.first, edge.second) {
			count++
			forest.add(edge.first+1, edge.second+1, vertices+count, rank)
		} else {
			active[forest.replaceMinimum(edge.first+1, edge.second+1, rank)] = false
		}
		active[rank] = true
		for !active[lower] {
			lower++
		}
		if count == vertices-1 {
			width := edge.weight - edges[lower].weight
			if bestWidth < 0 || width < bestWidth {
				bestWidth, bestLeft, bestRight = width, lower, rank
			}
			if bestWidth == 0 {
				break
			}
		}
	}
	components = newDisjointSet(vertices)
	chosen := make([]int, 0, vertices-1)
	for rank := bestLeft; rank <= bestRight; rank++ {
		edge := edges[rank]
		if components.unite(edge.first, edge.second) {
			chosen = append(chosen, edge.id)
			if len(chosen) == vertices-1 {
				break
			}
		}
	}
	return chosen
}
func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var vertices, count int
	fmt.Fscan(input, &vertices, &count)
	edges := make([]Edge, count)
	for i := range edges {
		fmt.Fscan(input, &edges[i].first, &edges[i].second, &edges[i].weight)
		edges[i].first--
		edges[i].second--
		edges[i].id = i + 1
	}
	sort.Slice(edges, func(i, j int) bool {
		a, b := edges[i], edges[j]
		if a.weight != b.weight {
			return a.weight < b.weight
		}
		if a.first != b.first {
			return a.first < b.first
		}
		if a.second != b.second {
			return a.second < b.second
		}
		return a.id < b.id
	})
	for i, value := range solve(vertices, edges) {
		if i != 0 {
			fmt.Fprint(output, " ")
		}
		fmt.Fprint(output, value)
	}
	fmt.Fprintln(output)
}
