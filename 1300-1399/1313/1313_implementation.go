package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	grid := make([][]string, n)
	for i := range grid {
		grid[i] = make([]string, n)
		for j := range grid[i] {
			in.Scan()
			grid[i][j] = in.Text()
		}
	}
	// diagonal s holds the cells with row + column = s; each is read from
	// its lowest row up
	out := make([]string, 0, n*n)
	for s := 0; s <= 2*n-2; s++ {
		lo := s - n + 1
		if lo < 0 {
			lo = 0
		}
		hi := s
		if hi > n-1 {
			hi = n - 1
		}
		for i := hi; i >= lo; i-- {
			out = append(out, grid[i][s-i])
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString(strings.Join(out, " ") + "\n")
}
