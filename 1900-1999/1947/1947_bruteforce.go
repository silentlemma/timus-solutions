package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	sideLength = 5
	portCount  = 4
	cells      = sideLength * sideLength
	minTiles   = 3
)
const (
	top = iota
	right
	bottom
	left
)

var rowStep = [...]int{-1, 0, 1, 0}
var columnStep = [...]int{0, 1, 0, -1}
var opposite = [...]int{bottom, left, top, right}
var connections = [...][portCount]int{{left, bottom, right, top}, {right, top, left, bottom}}
var directions = [...]byte{'L', 'R', 'U', 'D'}
var holeRow = [...]int{0, 0, 1, -1}
var holeColumn = [...]int{1, -1, 0, 0}

func winning(board []byte) bool {
	for side := 0; side < portCount; side++ {
		for offset := 0; offset < sideLength; offset++ {
			row, column := offset, offset
			if side == top {
				row = 0
			}
			if side == bottom {
				row = sideLength - 1
			}
			if side == left {
				column = 0
			}
			if side == right {
				column = sideLength - 1
			}
			incoming, count := side, 0
			var visited [cells * portCount]bool
			var tiles [cells]bool
			for {
				index := row*sideLength + column
				state := index*portCount + incoming
				if board[index] == '*' || visited[state] {
					break
				}
				visited[state] = true
				if !tiles[index] {
					tiles[index] = true
					count++
				}
				kind := 0
				if board[index] != '/' {
					kind = 1
				}
				outgoing := connections[kind][incoming]
				row += rowStep[outgoing]
				column += columnStep[outgoing]
				if row < 0 || row >= sideLength || column < 0 || column >= sideLength {
					if outgoing != side && count >= minTiles {
						return true
					}
					break
				}
				incoming = opposite[outgoing]
			}
		}
	}
	return false
}

func solve(board []byte) string {
	if winning(board) {
		return "WIN"
	}
	empty := 0
	for board[empty] != '*' {
		empty++
	}
	row, column := empty/sideLength, empty%sideLength
	for motion := 0; motion < portCount; motion++ {
		for amount := 1; amount < sideLength; amount++ {
			endRow, endColumn := row+holeRow[motion]*amount, column+holeColumn[motion]*amount
			if endRow < 0 || endRow >= sideLength || endColumn < 0 || endColumn >= sideLength {
				continue
			}
			changed := append([]byte(nil), board...)
			hole := empty
			for step := 0; step < amount; step++ {
				following := hole + holeRow[motion]*sideLength + holeColumn[motion]
				changed[hole], changed[following] = changed[following], changed[hole]
				hole = following
			}
			if winning(changed) {
				return string(directions[motion]) + strconv.Itoa(amount)
			}
		}
	}
	return "FAIL"
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var board []byte
	for index := 0; index < sideLength; index++ {
		var row string
		fmt.Fscan(in, &row)
		board = append(board, []byte(row)...)
	}
	fmt.Println(solve(board))
}
