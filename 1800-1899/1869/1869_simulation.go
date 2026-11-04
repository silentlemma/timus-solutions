package main

import (
	"bufio"
	"fmt"
	"os"
)

const seats = 36

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	east, west := make([]int, n-1), make([]int, n-1)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			var people int
			fmt.Fscan(in, &people)
			if people == 0 {
				continue
			}
			load := east
			if i > j {
				load = west
			}
			left, right := i, j
			if left > right {
				left, right = right, left
			}
			for leg := left; leg < right; leg++ {
				load[leg] += people
			}
		}
	}
	peak := 0
	for leg := 0; leg < n-1; leg++ {
		if east[leg] > peak {
			peak = east[leg]
		}
		if west[leg] > peak {
			peak = west[leg]
		}
	}
	fmt.Println((peak + seats - 1) / seats)
}
