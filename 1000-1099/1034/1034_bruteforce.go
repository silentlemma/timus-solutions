package main

import (
	"bufio"
	"fmt"
	"os"
)

const moved = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// col[r] is the column of the queen in row r; sum[r+c] and diff[r-c+n]
	// count the queens on each diagonal
	col := make([]int, n)
	sum := make([]int, 2*n)
	diff := make([]int, 2*n)
	for i := 0; i < n; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)
		col[x-1] = y - 1
	}
	for r := 0; r < n; r++ {
		sum[r+col[r]]++
		diff[r-col[r]+n]++
	}
	count := 0
	for a := 0; a < n; a++ {
		for b := a + 1; b < n; b++ {
			for c := b + 1; c < n; c++ {
				rows := [moved]int{a, b, c}
				for _, r := range rows {
					sum[r+col[r]]--
					diff[r-col[r]+n]--
				}
				// all three queens move only when the columns are shifted cyclically
				for shift := 1; shift < moved; shift++ {
					placed := 0
					for ; placed < moved; placed++ {
						r, cl := rows[placed], col[rows[(placed+shift)%moved]]
						if sum[r+cl] > 0 || diff[r-cl+n] > 0 {
							break
						}
						sum[r+cl]++
						diff[r-cl+n]++
					}
					if placed == moved {
						count++
					}
					for placed--; placed >= 0; placed-- {
						r, cl := rows[placed], col[rows[(placed+shift)%moved]]
						sum[r+cl]--
						diff[r-cl+n]--
					}
				}
				for _, r := range rows {
					sum[r+col[r]]++
					diff[r-col[r]+n]++
				}
			}
		}
	}
	fmt.Println(count)
}
