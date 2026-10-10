package main

import "fmt"

const side = 8

var jumps = [8][2]int{{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}}

func main() {
	var n int
	fmt.Scan(&n)
	for t := 0; t < n; t++ {
		var square string
		fmt.Scan(&square)
		col, row, count := int(square[0]-'a'), int(square[1]-'1'), 0
		// the knight attacks every square one jump away that is on the board
		for _, j := range jumps {
			c, r := col+j[0], row+j[1]
			if c >= 0 && c < side && r >= 0 && r < side {
				count++
			}
		}
		fmt.Println(count)
	}
}
