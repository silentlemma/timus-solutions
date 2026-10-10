package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	side      = 4
	rooms     = side * side
	maxLevels = 16
	none      = -(int64(1) << 62)
)

// plan is the part of a trip on one level: start, end and rooms
type plan struct{ s, e, k int }

// moves inside a level: name, row step, column step
var (
	names  = "NESW"
	dr     = [4]int{-1, 0, 1, 0}
	dc     = [4]int{0, 1, 0, -1}
	n      int
	food   [maxLevels][rooms]int
	door   [maxLevels][rooms]int
	best   [maxLevels][rooms][rooms][rooms + 1]int
	start  int
	choice [maxLevels][rooms]plan
)

func step(u, d int) int {
	r, c := u/side+dr[d], u%side+dc[d]
	if r >= 0 && r < side && c >= 0 && c < side {
		return r*side + c
	}
	return -1
}

// walk records in best[lv][s] the most food on paths of each length and end
func walk(lv, s, u, mask, k, total int) {
	if total > best[lv][s][u][k] {
		best[lv][s][u][k] = total
	}
	for d := range dr {
		if v := step(u, d); v >= 0 && mask>>v&1 == 0 {
			walk(lv, s, v, mask|1<<v, k+1, total+food[lv][v])
		}
	}
}

// findMoves appends a path of left rooms from u to e with exactly rest food
func findMoves(lv, u, e, mask, left, rest int, path *[]byte) bool {
	if left == 1 {
		return u == e && rest == food[lv][u]
	}
	for d := range dr {
		if v := step(u, d); v >= 0 && mask>>v&1 == 0 {
			*path = append(*path, names[d])
			if findMoves(lv, v, e, mask|1<<v, left-1, rest-food[lv][u], path) {
				return true
			}
			*path = (*path)[:len(*path)-1]
		}
	}
	return false
}

// bestPath maximises den * food - num * rooms and returns the per-level
// choices with their food and room count
func bestPath(num, den int64) ([]plan, int64, int64) {
	after := make([]int64, rooms)
	for lv := n - 1; lv >= 0; lv-- {
		here := make([]int64, rooms)
		for s := range here {
			here[s] = none
			for e := 0; e < rooms; e++ {
				if (lv < n-1 && door[lv][e] == 0) || after[e] == none {
					continue
				}
				for k := 1; k <= rooms; k++ {
					w := best[lv][s][e][k]
					v := den*int64(w) - num*int64(k) + after[e]
					if w >= 0 && v > here[s] {
						here[s] = v
						choice[lv][s] = plan{s, e, k}
					}
				}
			}
		}
		after = here
	}
	var trip []plan
	var total, count int64
	s := start
	for lv := 0; lv < n; lv++ {
		p := choice[lv][s]
		trip = append(trip, p)
		total += int64(best[lv][s][p.e][p.k])
		count += int64(p.k)
		s = p.e
	}
	return trip, total, count
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n)
	for lv := 0; lv < n; lv++ {
		for u := 0; u < rooms; u++ {
			fmt.Fscan(in, &food[lv][u])
		}
		for u := 0; u < rooms; u++ {
			fmt.Fscan(in, &door[lv][u])
		}
	}
	var r, c int
	fmt.Fscan(in, &r, &c)
	start = (r-1)*side + c - 1
	for lv := 0; lv < n; lv++ {
		for s := 0; s < rooms; s++ {
			for e := 0; e < rooms; e++ {
				for k := range best[lv][s][e] {
					best[lv][s][e][k] = -1
				}
			}
			walk(lv, s, s, 1<<s, 1, food[lv][s])
		}
	}
	// Dinkelbach: move to the better ratio until no path beats the current
	num, den := int64(0), int64(1)
	var chosen []plan
	for {
		trip, total, count := bestPath(num, den)
		if total*den <= num*count {
			break
		}
		num, den, chosen = total, count, trip
	}
	var moves []byte
	for lv, p := range chosen {
		if lv > 0 {
			moves = append(moves, 'D')
		}
		findMoves(lv, p.s, p.e, 1<<p.s, p.k, best[lv][p.s][p.e][p.k], &moves)
	}
	fmt.Printf("%.4f\n%d\n", float64(num)/float64(den), len(moves))
	if len(moves) > 0 {
		fmt.Println(string(moves))
	}
}
