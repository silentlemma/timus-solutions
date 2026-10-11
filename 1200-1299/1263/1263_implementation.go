package main

import (
	"bufio"
	"fmt"
	"os"
)

const percent = 100

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	votes := make([]int, n+1)
	for i := 0; i < m; i++ {
		var c int
		fmt.Fscan(in, &c)
		votes[c]++
	}
	for _, v := range votes[1:] {
		fmt.Fprintf(out, "%.2f%%\n", percent*float64(v)/float64(m))
	}
}
