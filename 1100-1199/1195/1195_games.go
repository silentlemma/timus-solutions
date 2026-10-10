package main

import "fmt"

var lines = [8][3]int{
	{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
	{0, 3, 6}, {1, 4, 7}, {2, 5, 8},
	{0, 4, 8}, {2, 4, 6},
}

// outcomes for the side to move: win, draw, loss
const (
	win  = 1
	draw = 0
	loss = -1
)

var board []byte

func won(mark byte) bool {
	for _, l := range lines {
		if board[l[0]] == mark && board[l[1]] == mark && board[l[2]] == mark {
			return true
		}
	}
	return false
}

// play gives the best outcome for the side about to move with mark
func play(mark, other byte) int {
	best, moved := loss, false
	for i := range board {
		if board[i] == '#' {
			moved = true
			board[i] = mark
			result := win
			if !won(mark) {
				result = -play(other, mark)
			}
			if result > best {
				best = result
			}
			board[i] = '#'
		}
	}
	if !moved {
		return draw
	}
	return best
}

func main() {
	for {
		var row string
		if _, err := fmt.Scan(&row); err != nil {
			break
		}
		board = append(board, row...)
	}
	// three moves each have been made, so crosses move now
	switch play('X', 'O') {
	case win:
		fmt.Println("Crosses win")
	case draw:
		fmt.Println("Draw")
	default:
		fmt.Println("Ouths win")
	}
}
