package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const percentScale = 100
const probabilityDigits = 12

func safestShortestPath(adjacency [][]int, start, target int) ([]int, float64) {
	var costs [percentScale]float64
	for probability := range costs {
		costs[probability] = -math.Log1p(-float64(probability) / percentScale)
	}
	count := len(adjacency)
	distance, parent := make([]int, count), make([]int, count)
	best := make([]float64, count)
	for city := range distance {
		distance[city], parent[city], best[city] = -1, -1, math.Inf(1)
	}
	distance[start], best[start] = 0, 0
	queue := make([]int, 1, count)
	queue[0] = start
	for head := 0; head < len(queue); head++ {
		city := queue[head]
		if city == target {
			break
		}
		for _, edge := range adjacency[city] {
			neighbor, probability := edge/percentScale, edge%percentScale
			if distance[neighbor] < 0 {
				distance[neighbor] = distance[city] + 1
				queue = append(queue, neighbor)
			}
			if distance[neighbor] == distance[city]+1 {
				candidate := best[city] + costs[probability]
				if candidate < best[neighbor] {
					best[neighbor], parent[neighbor] = candidate, city
				}
			}
		}
	}
	path := []int{}
	for city := target; city >= 0; city = parent[city] {
		path = append(path, city)
	}
	for left, right := 0, len(path)-1; left < right; left, right = left+1, right-1 {
		path[left], path[right] = path[right], path[left]
	}
	return path, -math.Expm1(-best[target])
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count, roads, start, target int
	fmt.Fscan(input, &count, &roads, &start, &target)
	adjacency := make([][]int, count)
	for index := 0; index < roads; index++ {
		var first, second, probability int
		fmt.Fscan(input, &first, &second, &probability)
		first--
		second--
		adjacency[first] = append(adjacency[first], percentScale*second+probability)
		adjacency[second] = append(adjacency[second], percentScale*first+probability)
	}
	path, risk := safestShortestPath(adjacency, start-1, target-1)
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(output, "%d %.*f\n", len(path), probabilityDigits, risk)
	for index, city := range path {
		if index != 0 {
			fmt.Fprint(output, " ")
		}
		fmt.Fprint(output, city+1)
	}
	fmt.Fprintln(output)
	output.Flush()
}
