package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, a, b int
	if _, err := fmt.Fscan(in, &n, &m, &a, &b); err != nil {
		return
	}

	var rowTotal, columnTotal, selectedRow, selectedColumn int64
	for index := 1; index <= n; index++ {
		var value int64
		fmt.Fscan(in, &value)
		rowTotal += value
		if index == a {
			selectedRow = value
		}
	}
	for index := 1; index <= m; index++ {
		var value int64
		fmt.Fscan(in, &value)
		columnTotal += value
		if index == b {
			selectedColumn = value
		}
	}

	if rowTotal != columnTotal {
		fmt.Println(0)
		return
	}
	lower := selectedRow + selectedColumn - rowTotal
	if lower < 0 {
		lower = 0
	}
	upper := selectedRow
	if selectedColumn < upper {
		upper = selectedColumn
	}
	fmt.Println(upper - lower + 1)
}
