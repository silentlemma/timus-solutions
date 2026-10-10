package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	// peg: a cost is pegs * peg + inches cut, fewer pegs first, then less
	// cutting
	peg  = 1000000
	none = -1
)

type shelf struct{ y, left, length, a, b int }

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// clear is the cheapest way to get a shelf out of the open strip (lo, hi) of
// the tome, keeping its plank inside the niche [0, width]
func clear(s shelf, lo, hi, width int) int {
	if s.left+s.length <= lo || s.left >= hi {
		return 0
	}
	best := 2*peg + s.length
	for _, side := range [][2]int{{0, lo}, {hi, width}} {
		start, end := side[0], side[1]
		// pegs stay: a plank of length t in [start, end] over both pegs with
		// its middle between them exists for b - a <= t <= this bound
		if start <= s.a && s.b <= end {
			longest := min(min(s.length, 2*(s.b-start)), min(end-start, 2*(end-s.a)))
			if longest >= s.b-s.a {
				best = min(best, s.length-longest)
			}
		}
		// one peg moves anywhere, so only the kept peg and the room matter
		kept := (start <= s.a && s.a <= end) || (start <= s.b && s.b <= end)
		if end > start && kept {
			best = min(best, peg+max(0, s.length-(end-start)))
		}
	}
	return best
}

// carry is the cost of making a shelf hold the tome over [x, x + tome]
func carry(s shelf, x, tome, width int) int {
	if s.length < tome {
		return none
	}
	// pegs stay: limits on the new left end, doubled to stay in integers
	low := max(max(0, 2*(s.b-s.length)), max(2*s.a-s.length, 2*(x+tome-s.length)))
	high := min(min(2*s.a, 2*x), min(2*s.b-s.length, 2*(width-s.length)))
	if low <= high {
		return 0
	}
	// one peg moves: the plank only has to reach over the tome and the peg
	// that stays
	for _, p := range []int{s.a, s.b} {
		if max(x+tome, p)-min(x, p) <= s.length {
			return peg
		}
	}
	return none
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var width, height, tomeW, tomeH, n int
	fmt.Fscan(in, &width, &height, &tomeW, &tomeH, &n)
	shelves := make([]shelf, n)
	for i := range shelves {
		var x1, x2 int
		s := &shelves[i]
		fmt.Fscan(in, &s.y, &s.left, &s.length, &x1, &x2)
		s.a, s.b = s.left+x1, s.left+x2
	}
	sort.Slice(shelves, func(i, j int) bool { return shelves[i].y < shelves[j].y })
	spots := width - tomeW + 1
	// prefix[k][x]: total cost of clearing the strip at x from the k lowest
	// shelves
	prefix := make([][]int, n+1)
	prefix[0] = make([]int, spots)
	for k, s := range shelves {
		prefix[k+1] = make([]int, spots)
		for x := 0; x < spots; x++ {
			prefix[k+1][x] = prefix[k][x] + clear(s, x, x+tomeW, width)
		}
	}
	best := none
	for i, s := range shelves {
		if s.y+tomeH > height {
			continue
		}
		// the shelves strictly between the tome bottom and top are in the way
		top := i + 1
		for top < n && shelves[top].y < s.y+tomeH {
			top++
		}
		for x := 0; x < spots; x++ {
			if base := carry(s, x, tomeW, width); base != none {
				total := base + prefix[top][x] - prefix[i+1][x]
				if best == none || total < best {
					best = total
				}
			}
		}
	}
	fmt.Println(best/peg, best%peg)
}
