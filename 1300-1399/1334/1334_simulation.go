package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const size = 8

var diagonals = [][2]int{{1, 1}, {1, -1}, {-1, 1}, {-1, -1}}

// board holds 0 for an empty square, 1 for white and 2 for black
var board [size][size]int

func inside(c, r int) bool {
	return c >= 0 && c < size && r >= 0 && r < size
}

// some checker has a checker of the other color next to it on a diagonal
// and a free square right behind that one
func canCapture() bool {
	for c := 0; c < size; c++ {
		for r := 0; r < size; r++ {
			if board[c][r] == 0 {
				continue
			}
			for _, d := range diagonals {
				oc, or, lc, lr := c+d[0], r+d[1], c+2*d[0], r+2*d[1]
				if inside(lc, lr) && board[oc][or] != 0 && board[oc][or] != board[c][r] && board[lc][lr] == 0 {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	for number := 1; sc.Scan(); number++ {
		move := strings.ToLower(sc.Text())
		row, _ := strconv.Atoi(move[1:])
		color := 2
		if number%2 == 1 {
			color = 1 // white moves on the odd lines
		}
		board[move[0]-'a'][row-1] = color
		if canCapture() {
			fmt.Println(number)
			return
		}
	}
	fmt.Println("Draw")
}
