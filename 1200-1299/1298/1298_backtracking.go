package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var moves = [8][2]int{{1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}}

var (
	n    int
	seen [][]bool
	path [][2]int
)

func freeSquares(c, r int) [][2]int {
	var out [][2]int
	for _, m := range moves {
		nc, nr := c+m[0], r+m[1]
		if nc >= 0 && nc < n && nr >= 0 && nr < n && !seen[nc][nr] {
			out = append(out, [2]int{nc, nr})
		}
	}
	return out
}

func tour(c, r int) bool {
	seen[c][r] = true
	path = append(path, [2]int{c, r})
	if len(path) == n*n {
		return true
	}
	// Warnsdorff's rule: try first the squares with the fewest onward
	// moves, and the search still backtracks, so it is exact
	next := freeSquares(c, r)
	degree := make([]int, len(next))
	for i, sq := range next {
		degree[i] = len(freeSquares(sq[0], sq[1]))
	}
	order := make([]int, len(next))
	for i := range order {
		order[i] = i
	}
	sort.SliceStable(order, func(a, b int) bool { return degree[order[a]] < degree[order[b]] })
	for _, i := range order {
		if tour(next[i][0], next[i][1]) {
			return true
		}
	}
	seen[c][r] = false
	path = path[:len(path)-1]
	return false
}

func main() {
	fmt.Scan(&n)
	seen = make([][]bool, n)
	for i := range seen {
		seen[i] = make([]bool, n)
	}
	found := false
	for c := 0; c < n && !found; c++ {
		for r := 0; r < n && !found; r++ {
			found = tour(c, r)
		}
	}
	if !found {
		fmt.Println("IMPOSSIBLE")
		return
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, sq := range path {
		fmt.Fprintf(out, "%c%d\n", 'a'+sq[0], sq[1]+1)
	}
}
