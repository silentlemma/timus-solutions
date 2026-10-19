package main

import (
	"bufio"
	"fmt"
	"os"
)

const points = 5
const end = points - 1
const forbiddenLast = 2
const middleSum = end * (end - 1) / 2

func solve(distance [points][points]int) (int, [points]int) {
	bestCost := -1
	var bestRoute [points]int
	for first := 1; first < end; first++ {
		for last := 1; last < end; last++ {
			if first == last || last == forbiddenLast {
				continue
			}
			middle := middleSum - first - last
			route := [points]int{0, first, middle, last, end}
			cost := 0
			for i := 0; i < end; i++ {
				cost += distance[route[i]][route[i+1]]
			}
			if bestCost < 0 || cost < bestCost {
				bestCost, bestRoute = cost, route
			}
		}
	}
	return bestCost, bestRoute
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var distance [points][points]int
	for i := range distance {
		for j := range distance[i] {
			fmt.Fscan(in, &distance[i][j])
		}
	}
	cost, route := solve(distance)
	fmt.Println(cost)
	for i, point := range route {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(point + 1)
	}
	fmt.Println()
}
