package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	const space = ' '
	nextInt := func() int64 {
		for data[position] <= space {
			position++
		}
		sign := int64(1)
		if data[position] == '-' {
			sign = -1
			position++
		}
		value := int64(0)
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int64(data[position]-'0')
			position++
		}
		return sign * value
	}
	n, m := int(nextInt()), int(nextInt())
	board := make([]int64, n*m)
	for i := range board {
		board[i] = nextInt()
	}
	for data[position] <= space {
		position++
	}
	end := position
	for end < len(data) && data[end] > space {
		end++
	}
	s := data[position:end]
	directions := "RDLU"
	dx, dy := []int{0, 1, 0, -1}, []int{1, 0, -1, 0}
	cell := func(row, col int) int64 {
		if row < 0 || row >= n || col < 0 || col >= m {
			return 0
		}
		return board[row*m+col]
	}
	x, y := make([]int, len(s)+1), make([]int, len(s)+1)
	cost := make([]int64, len(s)+1)
	cost[0] = cell(0, 0)
	for i, command := range s {
		d := 0
		for directions[d] != command {
			d++
		}
		x[i+1], y[i+1] = x[i]+dx[d], y[i]+dy[d]
		cost[i+1] = cell(x[i+1], y[i+1])
	}
	best := int64(0)
	source, target := 0, 0
	for d := range directions {
		left, right, leftMax, rightMax := int64(0), int64(0), int64(0), int64(0)
		leftAt, rightAt := 0, -1
		for i, command := range s {
			// Prefix maxima select the best endpoint for each translated interval.
			if left > leftMax {
				leftMax, leftAt = left, i
			}
			left += cell(x[i]+dx[d], y[i]+dy[d]) - cost[i+1]
			if command == directions[d] && left-leftMax < best {
				best, source, target = left-leftMax, i, leftAt
			}
			if command == directions[d] && (rightAt == -1 || right > rightMax) {
				rightMax, rightAt = right, i
			}
			right += cell(x[i+1]-dx[d], y[i+1]-dy[d]) - cost[i]
			if rightAt != -1 && right-rightMax < best {
				best, source, target = right-rightMax, rightAt, i
			}
		}
	}
	moved := s[source]
	remaining := append(append([]byte{}, s[:source]...), s[source+1:]...)
	answer := append([]byte{}, remaining[:target]...)
	answer = append(answer, moved)
	answer = append(answer, remaining[target:]...)
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, string(answer))
	out.Flush()
}
