package main

import (
	"bufio"
	"os"
	"strconv"
)

const infinity = 1 << 20

func number(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func maximumSaved(matrix []byte, n int) int {
	stride := n + 1
	rowPrice, colPrice := make([]int, stride), make([]int, stride)
	owner, previous := make([]int, stride), make([]int, stride)
	unmatched := make([]int, 0, n)
	// Row maxima are tight under the initial feasible potentials.
	for row := 1; row <= n; row++ {
		amounts := matrix[row*stride : (row+1)*stride]
		largest := byte(0)
		for _, value := range amounts[1:] {
			if value > largest {
				largest = value
			}
		}
		rowPrice[row] = -int(largest)
		col := 1
		for col <= n && (amounts[col] != largest || owner[col] != 0) {
			col++
		}
		if col <= n {
			owner[col] = row
		} else {
			unmatched = append(unmatched, row)
		}
	}
	slack, remaining := make([]int, stride), make([]int, n)
	visited := make([]int, 0, n)
	for _, row := range unmatched {
		owner[0] = row
		col, left := 0, n
		visited = visited[:0]
		for j := 1; j <= n; j++ {
			slack[j], remaining[j-1] = infinity, j
		}
		for {
			visited = append(visited, col)
			r := owner[col]
			amounts := matrix[r*stride : (r+1)*stride]
			delta, best := infinity, 0
			for pos, j := range remaining[:left] {
				reduced := -int(amounts[j]) - rowPrice[r] - colPrice[j]
				if reduced < slack[j] {
					slack[j], previous[j] = reduced, col
				}
				if slack[j] < delta || (slack[j] == delta && owner[j] == 0 && owner[remaining[best]] != 0) {
					delta, best = slack[j], pos
				}
			}
			if delta != 0 {
				for _, j := range visited {
					rowPrice[owner[j]] += delta
					colPrice[j] -= delta
				}
				for _, j := range remaining[:left] {
					slack[j] -= delta
				}
			}
			col = remaining[best]
			if owner[col] == 0 {
				break
			}
			left--
			remaining[best] = remaining[left]
		}
		for col != 0 {
			prior := previous[col]
			owner[col], col = owner[prior], prior
		}
	}
	saved := 0
	for col := 1; col <= n; col++ {
		saved += int(matrix[owner[col]*stride+col])
	}
	return saved
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n := number(input)
	stride := n + 1
	matrix := make([]byte, stride*stride)
	total := 0
	for row := 1; row <= n; row++ {
		for col := 1; col <= n; col++ {
			value := number(input)
			matrix[row*stride+col] = byte(value)
			total += value
		}
	}
	os.Stdout.WriteString(strconv.Itoa(total-maximumSaved(matrix, n)) + "\n")
}
