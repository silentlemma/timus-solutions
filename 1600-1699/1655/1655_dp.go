package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	full    = 360.0
	minutes = 60.0
	eps     = 1e-9
)

type ship struct {
	angle, due float64
	id         int
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var a, w float64
	var n int
	if _, err := fmt.Fscan(in, &a, &w, &n); err != nil {
		return
	}
	var first []int // ships right in front of the gun, shot at once
	var ships []ship
	for k := 1; k <= n; k++ {
		var b, d, v float64
		fmt.Fscan(in, &b, &d, &v)
		deadline := (d - 1) / v * minutes // when the ship reaches one mile
		turn := math.Mod(math.Mod(b-a, full)+full, full)
		if turn <= eps || full-turn <= eps {
			first = append(first, k)
		} else {
			ships = append(ships, ship{turn, deadline, k})
		}
	}
	sort.Slice(ships, func(x, y int) bool { return ships[x].angle < ships[y].angle })
	m := len(ships)
	size := m + 1
	speed := full * w // degrees a minute
	inf := math.Inf(1)
	// the shot ships always form an arc around the start: i of them taken
	// turning left (from the end of the sorted list), j turning right; left
	// and right hold the earliest time with the gun at that end
	left, right := make([]float64, size*size), make([]float64, size*size)
	cameLeft, cameRight := make([]int, size*size), make([]int, size*size) // the side before
	for k := range left {
		left[k], right[k] = inf, inf
	}
	left[0], right[0] = 0, 0
	for i := 0; i < size; i++ {
		for j := 0; i+j < m; j++ {
			here := i*size + j
			tl, tr := left[here], right[here]
			if math.IsInf(tl, 1) && math.IsInf(tr, 1) {
				continue
			}
			atLeft, atRight := 0.0, 0.0
			if i > 0 {
				atLeft = full - ships[m-i].angle
			}
			if j > 0 {
				atRight = ships[j-1].angle
			}
			next := ships[j].angle // the next ship turning right
			there := here + 1
			for _, mv := range [][2]float64{{tr + (next-atRight)/speed, 1}, {tl + (atLeft+next)/speed, 0}} {
				if mv[0] <= ships[j].due+eps && mv[0]+eps < right[there] {
					right[there], cameRight[there] = mv[0], int(mv[1])
				}
			}
			next = full - ships[m-i-1].angle // the next ship turning left
			there = here + size
			for _, mv := range [][2]float64{{tl + (next-atLeft)/speed, 0}, {tr + (atRight+next)/speed, 1}} {
				if mv[0] <= ships[m-i-1].due+eps && mv[0]+eps < left[there] {
					left[there], cameLeft[there] = mv[0], int(mv[1])
				}
			}
		}
	}
	// ending at the left end wins ties, then the fewest ships taken leftwards
	best, side := inf, 0
	for s, at := range [][]float64{left, right} {
		for i := 0; i < size; i++ {
			if at[i*size+m-i] < best {
				best, side = at[i*size+m-i], s
			}
		}
	}
	if math.IsInf(best, 1) {
		fmt.Fprintln(out, "Impossible")
		return
	}
	at := left
	if side == 1 {
		at = right
	}
	i := 0
	for math.Abs(at[i*size+m-i]-best) > eps {
		i++
	}
	j := m - i
	var order []int
	for i > 0 || j > 0 {
		here := i*size + j
		if side == 1 {
			order = append(order, ships[j-1].id)
			side, j = cameRight[here], j-1
		} else {
			order = append(order, ships[m-i].id)
			side, i = cameLeft[here], i-1
		}
	}
	fmt.Fprintf(out, "%.3f\n", best)
	for _, k := range first {
		fmt.Fprintln(out, k)
	}
	for k := len(order) - 1; k >= 0; k-- {
		fmt.Fprintln(out, order[k])
	}
}
