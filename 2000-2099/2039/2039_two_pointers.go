package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func bit(value bool) int {
	if value {
		return 1
	}
	return 0
}

func solve(grid []string, k int) int64 {
	n, m := len(grid), len(grid[0])
	if k > min(n, m) {
		return 0
	}
	columns := make([]string, m)
	for c := 0; c < m; c++ {
		column := make([]byte, n)
		for r := 0; r < n; r++ {
			column[r] = grid[r][c]
		}
		columns[c] = string(column)
	}
	var answer int64
	for diagonal := 1 - n; diagonal < m; diagonal++ {
		r0, c0 := max(0, -diagonal), max(0, diagonal)
		start, pr, pc, br, bc := 0, -1, -1, 0, 0
		for at := 0; at < min(n-r0, m-c0); at++ {
			r, c := r0+at, c0+at
			for {
				rs, cs := r0+start, c0+start
				last := strings.LastIndexByte(grid[r][cs:c], '0')
				valid := last < 0 || pr < 0 || grid[r][cs:c] == grid[pr][cs:c]
				if valid {
					nrp, ncp := pr, pc
					if last >= 0 {
						nrp = r
						if pr < 0 {
							ncp = cs + last
						}
					}
					lastRow := strings.LastIndexByte(columns[c][rs:r+1], '0')
					valid = lastRow < 0 || nrp < 0 || columns[c][rs:r+1] == columns[ncp][rs:r+1]
					if valid {
						if lastRow >= 0 {
							nrp = rs + lastRow
							ncp = c
						}
						length := at - start + 1
						var nr, nc int
						if pr >= 0 {
							nr = br + bit(grid[r][ncp] == '1')
							nc = bc + bit(columns[c][nrp] == '1')
						} else if nrp < 0 {
							nr, nc = length, length
						} else if last >= 0 {
							nr = length - 1
							nc = strings.Count(grid[r][cs:c+1], "1")
						} else {
							nr = strings.Count(columns[c][rs:r+1], "1")
							nc = length - 1
						}
						if nr <= k && nc <= k {
							pr, pc, br, bc = nrp, ncp, nr, nc
							break
						}
					}
				}
				oldSize := at - start
				if pr < 0 || pr == rs || pc == cs {
					pr, pc = -1, -1
					br, bc = oldSize-1, oldSize-1
				} else {
					br -= bit(grid[rs][pc] == '1')
					bc -= bit(grid[pr][cs] == '1')
				}
				start++
			}
			bound := at - start + 1
			if bound >= k && (pr < r-k+1 || pc < c-k+1) {
				answer++
			}
			if bound > k && br == k && bc == k && pr >= 0 {
				firstR := r0 + start + strings.IndexByte(columns[pc][r0+start:r+1], '1')
				firstC := c0 + start + strings.IndexByte(grid[pr][c0+start:c+1], '1')
				high := min(min(at-k, firstR-r0), min(firstC-c0, min(pr-r0, pc-c0)))
				if high >= start {
					answer += int64(high - start + 1)
				}
			}
		}
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var n, m, k int
	if _, err := fmt.Fscan(input, &n, &m, &k); err != nil {
		return
	}
	grid := make([]string, n)
	for i := range grid {
		fmt.Fscan(input, &grid[i])
	}
	fmt.Println(solve(grid, k))
}
