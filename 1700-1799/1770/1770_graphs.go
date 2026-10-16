package main

import (
	"bufio"
	"fmt"
	"os"
)

const far = 1 << 20

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	a := make([][]int, n)
	d := make([][]int, n)
	grid := make([][]byte, n)
	for i := range a {
		a[i] = make([]int, n)
		d[i] = make([]int, n)
		grid[i] = make([]byte, n)
		for j := range a[i] {
			fmt.Fscan(reader, &a[i][j])
		}
	}
	// every road must cost at least the table in both directions, so the
	// cheapest roads allowed are taken: a free road where the table says 0
	// both ways, a road with a board seen from i where it says 1 and 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			d[i][j], grid[i][j] = far, '0'
			if i == j {
				d[i][j] = 0
			} else if a[i][j]+a[j][i] <= 1 {
				d[i][j] = a[i][j]
				grid[i][j] = byte('1' + a[i][j])
			}
		}
	}
	// these roads give the smallest costs any network can have, so the table
	// is right exactly when they give it
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if d[i][k]+d[k][j] < d[i][j] {
					d[i][j] = d[i][k] + d[k][j]
				}
			}
		}
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if d[i][j] != a[i][j] {
				fmt.Fprintln(writer, "NO")
				return
			}
		}
	}
	fmt.Fprintln(writer, "YES")
	for i := 0; i < n; i++ {
		writer.Write(grid[i])
		writer.WriteByte('\n')
	}
}
