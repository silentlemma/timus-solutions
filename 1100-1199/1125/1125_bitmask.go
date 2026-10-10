package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var m, n int
	fmt.Fscan(in, &m, &n)
	if m == 0 || n == 0 {
		out.WriteString(strings.Repeat("\n", m))
		return
	}
	final := make([]string, m)
	for r := range final {
		fmt.Fscan(in, &final[r])
	}
	// row r as a bit mask of its cells visited an odd number of times
	odd := make([]uint64, m)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			var visits int64
			fmt.Fscan(in, &visits)
			odd[r] |= uint64(visits&1) << uint(c)
		}
	}
	// the offsets of integer length, the cell itself included
	var offsets [][2]int
	for dr := 1 - m; dr < m; dr++ {
		for dc := 1 - n; dc < n; dc++ {
			q := dr*dr + dc*dc
			root := int(math.Round(math.Sqrt(float64(q))))
			if root*root == q {
				offsets = append(offsets, [2]int{dr, dc})
			}
		}
	}
	full := uint64(1)<<uint(n) - 1
	for r := 0; r < m; r++ {
		// bit c is set when cell (r, c) was flipped an odd number of times
		flips := uint64(0)
		for _, o := range offsets {
			if r+o[0] >= 0 && r+o[0] < m {
				row := odd[r+o[0]]
				if o[1] >= 0 {
					flips ^= row >> uint(o[1]) & full
				} else {
					flips ^= row << uint(-o[1]) & full
				}
			}
		}
		line := make([]byte, n)
		for c := 0; c < n; c++ {
			black := final[r][c] == 'B'
			if flips>>uint(c)&1 == 1 {
				black = !black
			}
			line[c] = 'W'
			if black {
				line[c] = 'B'
			}
		}
		out.Write(line)
		out.WriteByte('\n')
	}
}
