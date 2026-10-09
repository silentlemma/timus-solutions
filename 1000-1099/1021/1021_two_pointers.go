package main

import (
	"bufio"
	"fmt"
	"os"
)

const target = 10000

func readList(in *bufio.Reader) []int {
	var n int
	fmt.Fscan(in, &n)
	v := make([]int, n)
	for i := range v {
		fmt.Fscan(in, &v[i])
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	up, down := readList(in), readList(in)
	// up increases and down decreases: walking both forward, a sum that is
	// too small can only grow by moving in up, a sum too big only shrink in down
	i, j := 0, 0
	for i < len(up) && j < len(down) && up[i]+down[j] != target {
		if up[i]+down[j] < target {
			i++
		} else {
			j++
		}
	}
	if i < len(up) && j < len(down) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
