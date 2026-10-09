package main

import "fmt"

const (
	sideArea      = 9
	entranceSides = 4
)

var (
	di = []int{-1, 1, 0, 0}
	dj = []int{0, 0, -1, 1}
)

func main() {
	var n int
	fmt.Scan(&n)
	grid := make([]string, n)
	for i := range grid {
		fmt.Scan(&grid[i])
	}
	// visit every empty cell reachable from either entrance; each side of
	// such a cell that faces a block or the outer wall is a visible wall
	seen := make([][]bool, n)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	queue := [][2]int{{0, 0}, {n - 1, n - 1}}
	seen[0][0], seen[n-1][n-1] = true, true
	sides := 0
	for head := 0; head < len(queue); head++ {
		i, j := queue[head][0], queue[head][1]
		for d := range di {
			a, b := i+di[d], j+dj[d]
			if a < 0 || b < 0 || a >= n || b >= n || grid[a][b] == '#' {
				sides++
			} else if !seen[a][b] {
				seen[a][b] = true
				queue = append(queue, [2]int{a, b})
			}
		}
	}
	// the outer sides of the two entrance cells are openings, not walls
	fmt.Println((sides - entranceSides) * sideArea)
}
