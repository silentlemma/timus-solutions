package main

import (
	"bufio"
	"fmt"
	"os"
)

const moveCount = 8
const pieceCount = 5

var moves = [moveCount][2]int64{
	{-2, -1}, {-2, 1}, {-1, -2}, {-1, 2},
	{1, -2}, {1, 2}, {2, -1}, {2, 1},
}

func minimum(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func solve(n, x, y int64) [pieceCount]int64 {
	a, b := int64(1), int64(1)
	if x > 1 {
		a++
	}
	if x < n {
		a++
	}
	if y > 1 {
		b++
	}
	if y < n {
		b++
	}
	king := a*b - 1
	knight := int64(0)
	for _, move := range moves {
		nx, ny := x+move[0], y+move[1]
		if 1 <= nx && nx <= n && 1 <= ny && ny <= n {
			knight++
		}
	}
	bishop := minimum(x-1, y-1) + minimum(x-1, n-y) + minimum(n-x, y-1) + minimum(n-x, n-y)
	rook := 2 * (n - 1)
	return [pieceCount]int64{king, knight, bishop, rook, rook + bishop}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, x, y int64
	fmt.Fscan(in, &n, &x, &y)
	labels := [pieceCount]string{"King", "Knight", "Bishop", "Rook", "Queen"}
	for i, value := range solve(n, x, y) {
		fmt.Printf("%s: %d\n", labels[i], value)
	}
}
