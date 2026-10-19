package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

type Network struct {
	direct, broadcast []int64
	parent            []int
	root              int
}

func newNetwork(initial []int64, edges [][2]int, root int) *Network {
	size := len(initial)
	neighbors := make([][]int, size)
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		neighbors[a] = append(neighbors[a], b)
		neighbors[b] = append(neighbors[b], a)
	}
	parent := make([]int, size)
	for i := range parent {
		parent[i] = -1
	}
	parent[root] = root
	order := make([]int, 1, size)
	order[0] = root
	for at := 0; at < len(order); at++ {
		vertex := order[at]
		for _, next := range neighbors[vertex] {
			if parent[next] == -1 {
				parent[next] = vertex
				order = append(order, next)
			}
		}
	}
	return &Network{append([]int64(nil), initial...), make([]int64, size), parent, root}
}

func (network *Network) process(kind, vertex int) int64 {
	value := network.direct[vertex]
	if vertex != network.root {
		value += network.broadcast[network.parent[vertex]]
		if value >= modulus {
			value -= modulus
		}
	}
	if kind == 2 {
		return value
	}
	network.broadcast[vertex] += value
	if network.broadcast[vertex] >= modulus {
		network.broadcast[vertex] -= modulus
	}
	if vertex != network.root {
		above := network.parent[vertex]
		network.direct[above] += value
		if network.direct[above] >= modulus {
			network.direct[above] -= modulus
		}
	}
	return -1
}

func nextInt(reader *bufio.Reader) int {
	value := 0
	ch, err := reader.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = reader.ReadByte()
	}
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch, err = reader.ReadByte()
	}
	return value
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	size := nextInt(reader)
	if size == 0 {
		return
	}
	initial := make([]int64, size)
	for i := range initial {
		initial[i] = int64(nextInt(reader))
	}
	edges := make([][2]int, size-1)
	for i := range edges {
		edges[i] = [2]int{nextInt(reader) - 1, nextInt(reader) - 1}
	}
	network := newNetwork(initial, edges, 0)
	count := nextInt(reader)
	for i := 0; i < count; i++ {
		kind, vertex := nextInt(reader), nextInt(reader)-1
		answer := network.process(kind, vertex)
		if answer >= 0 {
			fmt.Fprintln(writer, answer)
		}
	}
}
