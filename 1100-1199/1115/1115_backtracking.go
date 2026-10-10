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
	maxSum = 10000
	bits   = 64
	words  = (maxSum + bits - 1) / bits
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
)

func pick(pos int, free []int, reach []sums, k, need int) bool {
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
	// the shortest rows first: they have the fewest ways to be filled
	order = make([]int, m)
	for r := range order {
		order[r] = r
	}
	sort.Slice(order, func(a, b int) bool { return rows[order[a]] < rows[order[b]] })
	owner = make([]int, n)
	for i := range owner {
		owner[i] = -1
	}
	fill(0)
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
