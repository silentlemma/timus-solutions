package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	maxIncoming = 3
	maxDegree   = maxIncoming + 1
	modulus     = int64(1000000007)
)

type fastInput struct {
	data []byte
	pos  int
}

func (in *fastInput) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

type disjointSet struct {
	parent []int
	edges  []int
}

func newDisjointSet(count int) disjointSet {
	parent := make([]int, count)
	for vertex := range parent {
		parent[vertex] = -1
	}
	return disjointSet{parent: parent, edges: make([]int, count)}
}

func (d *disjointSet) find(vertex int) int {
	root := vertex
	for d.parent[root] >= 0 {
		root = d.parent[root]
	}
	for vertex != root {
		next := d.parent[vertex]
		d.parent[vertex] = root
		vertex = next
	}
	return root
}

func (d *disjointSet) addEdge(first, second int) {
	first = d.find(first)
	second = d.find(second)
	if first == second {
		d.edges[first]++
		return
	}
	if d.parent[first] > d.parent[second] {
		first, second = second, first
	}
	d.parent[first] += d.parent[second]
	d.parent[second] = first
	d.edges[first] += d.edges[second] + 1
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil || len(data) == 0 {
		return
	}
	in := fastInput{data: data}
	vertexCount, edgeCount := in.nextInt(), in.nextInt()
	components := newDisjointSet(vertexCount)
	degree := make([]int, vertexCount)
	possible := true
	for edge := 0; edge < edgeCount; edge++ {
		first, second := in.nextInt()-1, in.nextInt()-1
		degree[first]++
		degree[second]++
		if degree[first] > maxDegree || degree[second] > maxDegree {
			possible = false
		}
		components.addEdge(first, second)
	}

	sinks := make([]int, vertexCount)
	for vertex, value := range degree {
		if value <= maxIncoming {
			sinks[components.find(vertex)]++
		}
	}

	answer := int64(1)
	if !possible {
		answer = 0
	}
	for root, parent := range components.parent {
		if parent >= 0 {
			continue
		}
		vertices, edges := -parent, components.edges[root]
		if edges == vertices-1 {
			// A tree has one orientation for each permitted sink.
			answer = answer * int64(sinks[root]) % modulus
		} else if edges == vertices {
			// The unique cycle can be directed either way.
			answer = answer * 2 % modulus
		} else {
			answer = 0
		}
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, answer)
	out.Flush()
}
