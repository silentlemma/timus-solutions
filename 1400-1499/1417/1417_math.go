package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// rows A x = 1: every player move then earns the same; x scaled to sum 1 is the answer
	rows := make([][]float64, n)
	for i := range rows {
		rows[i] = make([]float64, n+1)
		for j := 0; j < n; j++ {
			fmt.Fscan(in, &rows[i][j])
		}
		rows[i][n] = 1
	}
	for col := 0; col < n; col++ {
		pivot := col
		for r := col + 1; r < n; r++ {
			if math.Abs(rows[r][col]) > math.Abs(rows[pivot][col]) {
				pivot = r
			}
		}
		rows[col], rows[pivot] = rows[pivot], rows[col]
		for r := col + 1; r < n; r++ {
			f := rows[r][col] / rows[col][col]
			for j := col; j <= n; j++ {
				rows[r][j] -= f * rows[col][j]
			}
		}
	}
	x := make([]float64, n)
	total := 0.0
	for i := n - 1; i >= 0; i-- {
		s := rows[i][n]
		for j := i + 1; j < n; j++ {
			s -= rows[i][j] * x[j]
		}
		x[i] = s / rows[i][i]
		total += x[i]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < n; i++ {
		fmt.Fprintf(out, "%.5f\n", x[i]/total)
	}
}
