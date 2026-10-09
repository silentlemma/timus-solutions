package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	n   int
	a   [][]bool
	ops [][]int
)

func flip(perm []int) {
	ops = append(ops, append([]int(nil), perm...))
	for r, c := range perm {
		a[r][c] = !a[r][c]
	}
}

func parities() (rows, cols []int) {
	for i := 0; i < n; i++ {
		row, col := 0, 0
		for j := 0; j < n; j++ {
			if a[i][j] {
				row++
			}
			if a[j][i] {
				col++
			}
		}
		if row%2 == 1 {
			rows = append(rows, i)
		}
		if col%2 == 1 {
			cols = append(cols, i)
		}
	}
	return
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var half int
	fmt.Fscan(in, &half)
	n = 2*half + 1
	a = make([][]bool, n)
	for i := range a {
		var row string
		fmt.Fscan(in, &row)
		a[i] = make([]bool, n)
		for j := 0; j < n; j++ {
			a[i][j] = row[j] == '+'
		}
	}
	// two transversals that differ in two rows flip the corners of a
	// rectangle, which keeps every row and column parity; one transversal
	// flips all the parities at once
	rows, cols := parities()
	if len(rows) == n || len(cols) == n {
		diagonal := make([]int, n)
		for i := range diagonal {
			diagonal[i] = i
		}
		flip(diagonal)
		rows, cols = parities()
	}
	// the target keeps the parities with max(|rows|, |cols|) plus signs,
	// and the unmatched lines come in pairs and share line 0
	t := make([][]bool, n)
	for i := range t {
		t[i] = make([]bool, n)
	}
	paired := len(rows)
	if len(cols) < paired {
		paired = len(cols)
	}
	for k := 0; k < paired; k++ {
		t[rows[k]][cols[k]] = true
	}
	for _, r := range rows[paired:] {
		t[r][0] = !t[r][0]
	}
	for _, c := range cols[paired:] {
		t[0][c] = !t[0][c]
	}
	last := n - 1
	for i := 0; i < last; i++ {
		for j := 0; j < last; j++ {
			if a[i][j] == t[i][j] {
				continue
			}
			var rest []int
			for c := 0; c < n; c++ {
				if c != j && c != last {
					rest = append(rest, c)
				}
			}
			perm := make([]int, n)
			for r, k := 0, 0; r < n; r++ {
				switch r {
				case i:
					perm[r] = j
				case last:
					perm[r] = last
				default:
					perm[r] = rest[k]
					k++
				}
			}
			flip(perm)
			perm[i], perm[last] = perm[last], perm[i]
			flip(perm)
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.WriteString("There is solution:\n")
	for _, perm := range ops {
		for r, c := range perm {
			if r > 0 {
				w.WriteString(" ")
			}
			w.WriteString(strconv.Itoa(c + 1))
		}
		w.WriteString("\n")
	}
}
