package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

func seatingCount(size int, requests []int) int64 {
	if size == 2 {
		return 1
	}
	neighbors := make([][]int, size)
	for person, target := range requests {
		duplicate := false
		for _, adjacent := range neighbors[person] {
			if adjacent == target {
				duplicate = true
			}
		}
		if !duplicate {
			neighbors[person] = append(neighbors[person], target)
			neighbors[target] = append(neighbors[target], person)
			if len(neighbors[person]) > 2 || len(neighbors[target]) > 2 {
				return 0
			}
		}
	}
	visited := make([]bool, size)
	components, paths := 0, 0
	for start := 0; start < size; start++ {
		if visited[start] {
			continue
		}
		stack := []int{start}
		visited[start] = true
		vertices, degrees := 0, 0
		for len(stack) > 0 {
			person := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			vertices++
			degrees += len(neighbors[person])
			for _, target := range neighbors[person] {
				if !visited[target] {
					visited[target] = true
					stack = append(stack, target)
				}
			}
		}
		if degrees == 2*vertices {
			if vertices == size {
				return 2
			}
			return 0
		}
		components++
		if vertices > 1 {
			paths++
		}
	}
	answer := int64(1)
	for path := 0; path < paths; path++ {
		answer = answer * 2 % modulus
	}
	for factor := 2; factor < components; factor++ {
		answer = answer * int64(factor) % modulus
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var size, count int
	fmt.Fscan(input, &size, &count)
	requests := make([]int, count)
	for i := range requests {
		fmt.Fscan(input, &requests[i])
		requests[i]--
	}
	fmt.Println(seatingCount(size, requests))
}
