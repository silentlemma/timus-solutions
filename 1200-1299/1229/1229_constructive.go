package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	first := make([][]int, n)
	second := make([][]int, n)
	for i := range first {
		first[i] = make([]int, m)
		second[i] = make([]int, m)
		for j := range first[i] {
			fmt.Fscan(in, &first[i][j])
		}
	}
	label := 0
	// cover every 2 x 2 block with two bricks: lying flat unless a brick of
	// the first layer fills its top or bottom row, and then standing, which
	// no first-layer brick can match, as that brick holds a cell of each column
	for i := 0; i < n; i += 2 {
		for j := 0; j < m; j += 2 {
			flat := first[i][j] != first[i][j+1] && first[i+1][j] != first[i+1][j+1]
			a, b := label+1, label+2
			label = b
			if flat {
				second[i][j], second[i][j+1] = a, a
				second[i+1][j], second[i+1][j+1] = b, b
			} else {
				second[i][j], second[i+1][j] = a, a
				second[i][j+1], second[i+1][j+1] = b, b
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, row := range second {
		for j, v := range row {
			if j > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(v))
		}
		out.WriteByte('\n')
	}
}
