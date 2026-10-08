package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	w := make([]int, n)
	total := 0
	for i := range w {
		fmt.Fscan(reader, &w[i])
		total += w[i]
	}

	// reach[s]: some stones weigh exactly s; the lighter pile is at most total/2
	half := total / 2
	reach := make([]bool, half+1)
	reach[0] = true
	for _, x := range w {
		for s := half; s >= x; s-- {
			if reach[s-x] {
				reach[s] = true
			}
		}
	}
	s := half
	for !reach[s] {
		s--
	}
	fmt.Println(total - 2*s)
}
