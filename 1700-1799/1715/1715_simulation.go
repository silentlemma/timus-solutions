package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	colors = "BGRWY"
	empty  = '.'
)

var n, m int

// bestFigure finds the largest figure of the main colour or of the others,
// ties going to the figure holding the lowest ball, then the leftmost of the
// lowest balls
func bestFigure(board []byte, mainColor byte, takeMain bool) []int {
	seen := make([]bool, n*m)
	var best []int
	bestLow := -1
	for start := 0; start < n*m; start++ {
		color := board[start]
		if seen[start] || color == empty || (color == mainColor) != takeMain {
			continue
		}
		seen[start] = true
		cells := []int{start}
		low := start
		for k := 0; k < len(cells); k++ {
			v := cells[k]
			r, c := v/m, v%m
			if r > low/m || r == low/m && c < low%m {
				low = v
			}
			next := [...]int{v - m, v + m, v - 1, v + 1}
			ok := [...]bool{r > 0, r < n-1, c > 0, c < m-1}
			for d, w := range next {
				if ok[d] && !seen[w] && board[w] == color {
					seen[w] = true
					cells = append(cells, w)
				}
			}
		}
		if len(cells) < 2 {
			continue
		}
		better := best == nil || len(cells) > len(best) ||
			len(cells) == len(best) && (low/m > bestLow/m || low/m == bestLow/m && low%m < bestLow%m)
		if better {
			best, bestLow = cells, low
		}
	}
	return best
}

func removeFigure(board []byte, cells []int) int64 {
	for _, v := range cells {
		board[v] = empty
	}
	// balls fall down, then empty columns close up to the left
	var columns [][]byte
	for c := 0; c < m; c++ {
		var column []byte
		for r := 0; r < n; r++ {
			if board[r*m+c] != empty {
				column = append(column, board[r*m+c])
			}
		}
		if len(column) > 0 {
			padded := append([]byte(strings.Repeat(string(empty), n-len(column))), column...)
			columns = append(columns, padded)
		}
	}
	for c := 0; c < m; c++ {
		for r := 0; r < n; r++ {
			if c < len(columns) {
				board[r*m+c] = columns[c][r]
			} else {
				board[r*m+c] = empty
			}
		}
	}
	k := int64(len(cells))
	return k * (k - 1)
}

func play(start []byte, mainColor byte) int64 {
	board := append([]byte(nil), start...)
	var score int64
	for {
		for {
			cells := bestFigure(board, mainColor, false)
			if cells == nil {
				break
			}
			score += removeFigure(board, cells)
		}
		cells := bestFigure(board, mainColor, true)
		if cells == nil {
			return score
		}
		score += removeFigure(board, cells)
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Fscan(reader, &n, &m)
	var board []byte
	for r := 0; r < n; r++ {
		var row string
		fmt.Fscan(reader, &row)
		board = append(board, row...)
	}
	for i := 0; i < len(colors); i++ {
		if strings.IndexByte(string(board), colors[i]) >= 0 {
			fmt.Printf("%c: %d\n", colors[i], play(board, colors[i]))
		}
	}
}
