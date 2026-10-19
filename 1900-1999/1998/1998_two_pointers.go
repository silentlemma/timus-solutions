package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(weights, events []int64, limit int64) int64 {
	size := len(weights)
	prefix := make([]int64, size+1)
	for i, value := range weights {
		prefix[i+1] = prefix[i] + value
	}
	retreat := make([]int, size+1)
	left := 0
	for height := 1; height <= size; height++ {
		for left+1 < height && prefix[height]-prefix[left+1] > limit {
			left++
		}
		retreat[height] = left
	}
	time := int64(0)
	height := 0
	for _, event := range events {
		ordinary := event - time - 1
		if ordinary >= int64(size-height) {
			return time + int64(size-height)
		}
		height += int(ordinary)
		height = retreat[height]
		time = event
	}
	return time + int64(size-height)
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var n, m int
	var limit int64
	fmt.Fscan(input, &n, &m, &limit)
	weights, events := make([]int64, n), make([]int64, m)
	for i := range weights {
		fmt.Fscan(input, &weights[i])
	}
	for i := range events {
		fmt.Fscan(input, &events[i])
	}
	fmt.Println(solve(weights, events, limit))
}
