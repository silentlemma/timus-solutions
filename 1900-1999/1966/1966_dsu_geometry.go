package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct{ x, y int64 }

func cross(a, b, c point) int64 { return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x) }
func between(value, a, b int64) bool {
	if a > b {
		a, b = b, a
	}
	return a <= value && value <= b
}
func overlap(a, b, c, d int64) bool {
	if a > b {
		a, b = b, a
	}
	if c > d {
		c, d = d, c
	}
	return a <= d && c <= b
}
func onSegment(p, a, b point) bool {
	return cross(a, b, p) == 0 && between(p.x, a.x, b.x) && between(p.y, a.y, b.y)
}
func straddles(first, second int64) bool {
	return (first <= 0 && second >= 0) || (second <= 0 && first >= 0)
}
func intersects(a, b, c, d point) bool {
	return overlap(a.x, b.x, c.x, d.x) && overlap(a.y, b.y, c.y, d.y) &&
		straddles(cross(a, b, c), cross(a, b, d)) && straddles(cross(c, d, a), cross(c, d, b))
}

type disjointSets struct{ parent, weights []int }

func newSets(size int) *disjointSets {
	sets := &disjointSets{make([]int, size), make([]int, size)}
	for i := range sets.parent {
		sets.parent[i] = i
		sets.weights[i] = 1
	}
	return sets
}
func (sets *disjointSets) find(vertex int) int {
	for sets.parent[vertex] != vertex {
		sets.parent[vertex] = sets.parent[sets.parent[vertex]]
		vertex = sets.parent[vertex]
	}
	return vertex
}
func (sets *disjointSets) unite(first, second int) {
	first, second = sets.find(first), sets.find(second)
	if first == second {
		return
	}
	if sets.weights[first] < sets.weights[second] {
		first, second = second, first
	}
	sets.parent[second] = first
	sets.weights[first] += sets.weights[second]
}

func allReachable(points []point, edges [][2]int) bool {
	sets := newSets(len(points))
	for _, edge := range edges {
		sets.unite(edge[0], edge[1])
	}
	for i, edge := range edges {
		a, b := edge[0], edge[1]
		for _, other := range edges[:i] {
			c, d := other[0], other[1]
			if intersects(points[a], points[b], points[c], points[d]) {
				sets.unite(a, c)
			}
		}
		for vertex, p := range points {
			if onSegment(p, points[a], points[b]) {
				sets.unite(a, vertex)
			}
		}
	}
	root := sets.find(0)
	for vertex := range points {
		if sets.find(vertex) != root {
			return false
		}
	}
	return true
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var size, count int
	fmt.Fscan(input, &size, &count)
	points := make([]point, size)
	for i := range points {
		fmt.Fscan(input, &points[i].x, &points[i].y)
	}
	edges := make([][2]int, count)
	for i := range edges {
		fmt.Fscan(input, &edges[i][0], &edges[i][1])
		edges[i][0]--
		edges[i][1]--
	}
	if allReachable(points, edges) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
