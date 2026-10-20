package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	rows           = 7
	columns        = 9
	connect        = 4
	directionCount = 4
	maxMoves       = rows * columns
	firstWin       = 2 * (connect - 1)
)

func makeMasks() ([directionCount]int, [directionCount]uint64) {
	rowSteps := [directionCount]int{1, 0, 1, -1}
	columnSteps := [directionCount]int{0, 1, 1, 1}
	var shifts [directionCount]int
	var masks [directionCount]uint64
	for direction := 0; direction < directionCount; direction++ {
		dr, dc := rowSteps[direction], columnSteps[direction]
		shifts[direction] = dc*rows + dr
		for column := 0; column < columns; column++ {
			for row := 0; row < rows; row++ {
				endRow := row + (connect-1)*dr
				endColumn := column + (connect-1)*dc
				if endRow >= 0 && endRow < rows && endColumn < columns {
					masks[direction] |= uint64(1) << (column*rows + row)
				}
			}
		}
	}
	return shifts, masks
}

func hasWon(board uint64, shifts *[directionCount]int, masks *[directionCount]uint64) bool {
	for direction := 0; direction < directionCount; direction++ {
		shift := shifts[direction]
		pair := board & (board >> shift)
		// The mask excludes lines that wrap across column boundaries.
		if pair&(pair>>(2*shift))&masks[direction] != 0 {
			return true
		}
	}
	return false
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	moves := bytes.TrimSpace(data)
	shifts, masks := makeMasks()
	wins, draws := 0, 0
	for start := 0; start < len(moves); start++ {
		var heights [columns]int
		var boards [2]uint64
		placed := 0
		limit := len(moves) - start
		if limit > maxMoves {
			limit = maxMoves
		}
		for turn := 0; turn < limit; turn++ {
			column := int(moves[start+turn] - '1')
			if heights[column] < rows {
				player := turn & 1
				boards[player] |= uint64(1) << (column*rows + heights[column])
				heights[column]++
				placed++
				if turn >= firstWin && hasWon(boards[player], &shifts, &masks) {
					wins++
					break
				}
			}
			if turn+1 == maxMoves && placed == maxMoves {
				draws++
			}
		}
	}
	fmt.Println(wins, draws)
}
