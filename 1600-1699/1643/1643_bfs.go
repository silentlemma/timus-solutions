package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const (
	inf     = 1 << 29
	letters = 26
	markSet = "$!*" // the two armies and the fortress
)

type cell struct{ r, c int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	if _, err := fmt.Fscan(in, &n, &m); err != nil {
		return
	}
	grid := make([]string, n)
	var gates [letters][]cell
	marks := make([]cell, len(markSet))
	for r := range grid {
		fmt.Fscan(in, &grid[r])
		for c := 0; c < m; c++ {
			ch := grid[r][c]
			if ch >= 'A' && ch <= 'Z' {
				gates[ch-'A'] = append(gates[ch-'A'], cell{r, c})
			}
			if k := strings.IndexByte(markSet, ch); k >= 0 {
				marks[k] = cell{r, c}
			}
		}
	}
	fortress := marks[2]
	// bfs gives the days to every district; teleports are free, so 0-1 BFS
	bfs := func(start, avoid cell) [][]int {
		dist := make([][]int, n)
		for r := range dist {
			dist[r] = make([]int, m)
			for c := range dist[r] {
				dist[r][c] = inf
			}
		}
		var used [letters]bool // teleport letters already spread
		dist[start.r][start.c] = 0
		// free moves keep the current day, so they wait on a stack that is
		// emptied before the queue of next-day moves goes on
		var free []cell
		queue := []cell{start}
		for len(free) > 0 || len(queue) > 0 {
			var at cell
			if len(free) > 0 {
				at = free[len(free)-1]
				free = free[:len(free)-1]
			} else {
				at = queue[0]
				queue = queue[1:]
			}
			d := dist[at.r][at.c]
			if ch := grid[at.r][at.c]; ch >= 'A' && ch <= 'Z' && !used[ch-'A'] {
				used[ch-'A'] = true
				for _, g := range gates[ch-'A'] {
					if dist[g.r][g.c] > d {
						dist[g.r][g.c] = d
						free = append(free, g)
					}
				}
			}
			for dr := -1; dr <= 1; dr++ {
				for dc := -1; dc <= 1; dc++ {
					nr, nc := at.r+dr, at.c+dc
					if (dr == 0 && dc == 0) || nr < 0 || nr >= n || nc < 0 || nc >= m {
						continue
					}
					if grid[nr][nc] == '#' || (cell{nr, nc}) == avoid {
						continue
					}
					if dist[nr][nc] > d+1 {
						dist[nr][nc] = d + 1
						queue = append(queue, cell{nr, nc})
					}
				}
			}
		}
		return dist
	}
	first := bfs(marks[0], fortress)
	second := bfs(marks[1], fortress)
	attack := bfs(fortress, cell{-1, -1}) // moves are symmetric, so this is the way back
	// the earlier army waits at the meeting place, then both march together
	best := inf
	for r := 0; r < n; r++ {
		for c := 0; c < m; c++ {
			if (cell{r, c}) == fortress {
				continue
			}
			meet := first[r][c]
			if second[r][c] > meet {
				meet = second[r][c]
			}
			if meet+attack[r][c] < best {
				best = meet + attack[r][c]
			}
		}
	}
	if best >= inf {
		fmt.Println("Impossible")
	} else {
		fmt.Println(best)
	}
}
