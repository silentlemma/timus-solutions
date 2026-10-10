package main

import (
	"bufio"
	"fmt"
	"os"
)

var cols int
var free []bool

// farthest is a breadth-first search; the free cells form a tree, so
// distances along it are the only paths; it returns the last cell reached
// and its distance
func farthest(start int) (int, int) {
	dist := make([]int32, len(free))
	for k := range dist {
		dist[k] = -1
	}
	dist[start] = 0
	queue := []int{start}
	steps := []int{1, -1, cols, -cols}
	for head := 0; head < len(queue); head++ {
		cur := queue[head]
		for _, s := range steps {
			next := cur + s
			if free[next] && dist[next] < 0 {
				dist[next] = dist[cur] + 1
				queue = append(queue, next)
			}
		}
	}
	last := queue[len(queue)-1]
	return last, int(dist[last])
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var width, height int
	fmt.Fscan(in, &width, &height)
	// a border of walls around the maze keeps every neighbour in range
	cols = width + 2
	free = make([]bool, (height+2)*cols)
	start := -1
	for r := 1; r <= height; r++ {
		var row string
		fmt.Fscan(in, &row)
		for c := 1; c <= width; c++ {
			if row[c-1] == '.' {
				free[r*cols+c] = true
				if start < 0 {
					start = r*cols + c
				}
			}
		}
	}
	// the farthest cell from any cell is an end of a longest path
	end, _ := farthest(start)
	_, length := farthest(end)
	fmt.Println(length)
}
