package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const capacity = 100 // the largest single credit

func clamp(x int) int {
	if x < 0 {
		return 0
	}
	if x > capacity {
		return capacity
	}
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	rows, cols := make([]int, n), make([]int, n)
	for i := range rows {
		fmt.Fscan(in, &rows[i])
	}
	top := 0
	for j := range cols {
		fmt.Fscan(in, &cols[j])
		if cols[j] > top {
			top = cols[j]
		}
	}
	// take from the fullest columns first: lower them all towards a level
	taken := func(level int) int {
		sum := 0
		for _, c := range cols {
			sum += clamp(c - level)
		}
		return sum
	}
	matrix := make([][]int, 0, n)
	for _, need := range rows {
		if taken(0) < need {
			fmt.Println("NO")
			return
		}
		lo, hi := 0, top
		for lo < hi { // the lowest level that takes no more than needed
			mid := (lo + hi) / 2
			if taken(mid) <= need {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		row := make([]int, n)
		extra := need
		for j, c := range cols {
			row[j] = clamp(c - lo)
			extra -= row[j]
		}
		for j := 0; j < n && extra > 0; j++ {
			// one more unit from columns that stand exactly at the level
			if row[j] < capacity && cols[j]-row[j] == lo && lo > 0 {
				row[j]++
				extra--
			}
		}
		for j := range cols {
			cols[j] -= row[j]
		}
		matrix = append(matrix, row)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString("YES\n")
	for _, row := range matrix {
		for j, x := range row {
			if j > 0 {
				out.WriteByte(' ')
			}
			out.WriteString(strconv.Itoa(x))
		}
		out.WriteByte('\n')
	}
}
