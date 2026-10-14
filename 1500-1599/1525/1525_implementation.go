package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	const axes = 3
	var size [axes]int64
	var program string
	fmt.Fscan(in, &size[0], &size[1], &size[2])
	fmt.Fscan(in, &program) // stays empty when there are no instructions
	// the moves along each axis: decrease, increase
	down, up := "ldb", "ruf"
	total := int64(1)
	for a := range size {
		// each move keeps neighbouring starts at most one apart and in order,
		// so the finishes fill the range between the extreme starts
		low, high := int64(1), size[a]
		for i := 0; i < len(program); i++ {
			switch program[i] {
			case up[a]:
				if low < size[a] {
					low++
				}
				if high < size[a] {
					high++
				}
			case down[a]:
				if low > 1 {
					low--
				}
				if high > 1 {
					high--
				}
			}
		}
		total *= high - low + 1
	}
	fmt.Println(total)
}
