package main

import (
	"bufio"
	"fmt"
	"os"
)

func minimumChanges(adjacency [][]int, start, target int) int {
	stateCount := 2 * len(adjacency)
	distance := make([]int, stateCount)
	settled := make([]bool, stateCount)
	for i := range distance {
		distance[i] = stateCount
	}
	first := 2 * start
	distance[first], distance[first+1] = 0, 0
	front, back := []int{first, first + 1}, []int{}
	for len(front)+len(back) > 0 {
		if len(front) == 0 {
			// Transfer deferred back entries only when the front stack is exhausted.
			for left, right := 0, len(back)-1; left < right; left, right = left+1, right-1 {
				back[left], back[right] = back[right], back[left]
			}
			front, back = back, front[:0]
		}
		state := front[len(front)-1]
		front = front[:len(front)-1]
		if settled[state] {
			continue
		}
		settled[state] = true
		city, gear := state/2, state&1
		if city == target {
			return distance[state]
		}
		for _, nextState := range adjacency[city] {
			cost := 0
			if nextState&1 != gear {
				cost = 1
			}
			candidate := distance[state] + cost
			if candidate < distance[nextState] {
				distance[nextState] = candidate
				if cost == 0 {
					front = append(front, nextState)
				} else {
					back = append(back, nextState)
				}
			}
		}
	}
	return -1
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count, roads int
	fmt.Fscan(input, &count, &roads)
	adjacency := make([][]int, count)
	for i := 0; i < roads; i++ {
		var lower, upper int
		fmt.Fscan(input, &lower, &upper)
		lower--
		upper--
		adjacency[lower] = append(adjacency[lower], 2*upper)
		adjacency[upper] = append(adjacency[upper], 2*lower+1)
	}
	var start, target int
	fmt.Fscan(input, &start, &target)
	fmt.Println(minimumChanges(adjacency, start-1, target-1))
}
