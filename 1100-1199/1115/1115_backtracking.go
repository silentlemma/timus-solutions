package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// no row is longer than all the ships together: 99 * 100
const (
	searchLimit = 256
	attempts    = 128
	rngMod      = 65536
	maxSum      = 10000
	bits        = 64
	words       = (maxSum + bits - 1) / bits
)

type sums [words]uint64

func (s *sums) has(v int) bool { return s[v/bits]>>(uint(v)%bits)&1 == 1 }

// shiftOr returns s | s << by
func (s *sums) shiftOr(by int) sums {
	out := *s
	w, b := by/bits, uint(by)%bits
	for i := words - 1; i >= w; i-- {
		v := s[i-w] << b
		if b > 0 && i-w-1 >= 0 {
			v |= s[i-w-1] >> (bits - b)
		}
		out[i] |= v
	}
	return out
}

var (
	n, m               int
	ships, rows, order []int
	owner              []int
	calls              int
	limited            bool
)

func pick(pos int, free []int, reach []sums, k, need int) bool {
	if limited {
		calls++
		if calls > searchLimit {
			return false
		}
	}
	if need == 0 {
		return fill(pos + 1)
	}
	if !reach[k].has(need) {
		return false
	}
	last := -1
	for j := k; j < len(free); j++ {
		length := ships[free[j]]
		// equal ships are interchangeable: try each length once per place
		if length == last || length > need || !reach[j+1].has(need-length) {
			continue
		}
		last = length
		owner[free[j]] = order[pos]
		if pick(pos, free, reach, j+1, need-length) {
			return true
		}
		owner[free[j]] = -1
		if limited && calls > searchLimit {
			return false
		}
	}
	return false
}

func fill(pos int) bool {
	var free []int
	for i := 0; i < n; i++ {
		if owner[i] < 0 {
			free = append(free, i)
		}
	}
	if pos == m-1 {
		// the last row takes every ship that is left
		sum := 0
		for _, i := range free {
			sum += ships[i]
		}
		if sum != rows[order[pos]] {
			return false
		}
		for _, i := range free {
			owner[i] = order[pos]
		}
		return true
	}
	// reach[k]: the sums that the free ships from k on can make
	reach := make([]sums, len(free)+1)
	reach[len(free)][0] = 1
	for k := len(free) - 1; k >= 0; k-- {
		reach[k] = reach[k+1].shiftOr(ships[free[k]])
	}
	for q := pos; q < m; q++ {
		if !reach[0].has(rows[order[q]]) {
			return false
		}
	}
	return pick(pos, free, reach, 0, rows[order[pos]])
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n, &m)
	ships = make([]int, n)
	rows = make([]int, m)
	for i := range ships {
		fmt.Fscan(in, &ships[i])
	}
	for i := range rows {
		fmt.Fscan(in, &rows[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(ships)))
	// try the shortest rows first as a heuristic
	order = make([]int, m)
	for r := range order {
		order[r] = r
	}
	sort.Slice(order, func(a, b int) bool {
		if rows[order[a]] != rows[order[b]] {
			return rows[order[a]] < rows[order[b]]
		}
		return order[a] < order[b]
	})
	owner = make([]int, n)
	for i := range owner {
		owner[i] = -1
	}
	state := 1
	// restart costly searches in a reproducible order; the final search is complete
	for attempt := 0; attempt <= attempts; attempt++ {
		calls = 0
		limited = attempt < attempts
		if fill(0) {
			break
		}
		for i := m - 1; i > 0; i-- {
			state = (state*97 + 1) % rngMod
			j := state % (i + 1)
			order[i], order[j] = order[j], order[i]
		}
		rank := make([]int, 101)
		for i := range rank {
			rank[i] = i
		}
		for i := 100; i > 1; i-- {
			state = (state*97 + 1) % rngMod
			j := 1 + state%i
			rank[i], rank[j] = rank[j], rank[i]
		}
		sort.Slice(ships, func(a, b int) bool { return rank[ships[a]] < rank[ships[b]] })
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for r := 0; r < m; r++ {
		var row []string
		for i := 0; i < n; i++ {
			if owner[i] == r {
				row = append(row, strconv.Itoa(ships[i]))
			}
		}
		fmt.Fprintln(out, len(row))
		fmt.Fprintln(out, strings.Join(row, " "))
	}
}
