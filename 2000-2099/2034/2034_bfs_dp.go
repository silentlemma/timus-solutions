package main

import (
	"bufio"
	"fmt"
	"os"
)

func bfs(neighbors [][]int, source int) ([]int, []int) {
	distance := make([]int, len(neighbors))
	for i := range distance {
		distance[i] = -1
	}
	distance[source] = 0
	order := make([]int, 1, len(neighbors))
	order[0] = source
	for at := 0; at < len(order); at++ {
		vertex := order[at]
		for _, next := range neighbors[vertex] {
			if distance[next] < 0 {
				distance[next] = distance[vertex] + 1
				order = append(order, next)
			}
		}
	}
	return distance, order
}

func solve(size int, edges [][2]int, start, finish, origin int) int {
	neighbors := make([][]int, size)
	for _, edge := range edges {
		a, b := edge[0], edge[1]
		neighbors[a] = append(neighbors[a], b)
		neighbors[b] = append(neighbors[b], a)
	}
	depth, order := bfs(neighbors, start)
	clearance, _ := bfs(neighbors, origin)
	best := make([]int, size)
	for i := range best {
		best[i] = -1
	}
	best[start] = clearance[start]
	for _, vertex := range order {
		for _, next := range neighbors[vertex] {
			if depth[next] == depth[vertex]+1 {
				candidate := best[vertex]
				if clearance[next] < candidate {
					candidate = clearance[next]
				}
				if candidate > best[next] {
					best[next] = candidate
				}
			}
		}
	}
	return best[finish]
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
	input := bufio.NewReader(os.Stdin)
	size, count := nextInt(input), nextInt(input)
	if size == 0 {
		return
	}
	edges := make([][2]int, count)
	for i := range edges {
		edges[i] = [2]int{nextInt(input) - 1, nextInt(input) - 1}
	}
	start, finish, origin := nextInt(input)-1, nextInt(input)-1, nextInt(input)-1
	fmt.Println(solve(size, edges, start, finish, origin))
}
