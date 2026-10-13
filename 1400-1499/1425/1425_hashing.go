package main

import "fmt"

const bits = 21 // the answer stays below 900 000 cells, a table of 2^21 is enough
const word = 64
const slots = 1 << bits
const mix = 0x9E3779B97F4A7C15

// an open-addressing set of cell numbers; 0 marks an empty slot, so numbers are stored + 1
var table = make([]uint64, slots)
var distinct = 0

func add(cell int64) {
	key := uint64(cell) + 1
	h := (key * mix) >> (word - bits)
	for table[h] != 0 && table[h] != key {
		h = (h + 1) & (slots - 1)
	}
	if table[h] == 0 {
		table[h] = key
		distinct++
	}
}

var n, s int

// room: how many steps fit on the board from cell in direction v.
func room(cell, v []int) int {
	r := s
	for i := 0; i < n; i++ {
		if v[i] > 0 && s-1-cell[i] < r {
			r = s - 1 - cell[i]
		} else if v[i] < 0 && cell[i] < r {
			r = cell[i]
		}
	}
	return r
}

func key(v []int) string { return fmt.Sprint(v) }

func main() {
	fmt.Scan(&n, &s)
	start := make([]int, n)
	for i := range start {
		fmt.Scan(&start[i])
		start[i]--
	}
	// a cell is the number with digits x_i in base S
	weight := make([]int64, n)
	weight[0] = 1
	for i := 1; i < n; i++ {
		weight[i] = weight[i-1] * int64(s)
	}
	// rook directions along each axis, bishop directions along all axes at once
	var dirs [][]int
	seen := map[string]bool{}
	addDir := func(v []int) {
		if !seen[key(v)] { // in one dimension they coincide
			seen[key(v)] = true
			dirs = append(dirs, v)
		}
	}
	for i := 0; i < n; i++ {
		for _, sign := range []int{1, -1} {
			v := make([]int, n)
			v[i] = sign
			addDir(v)
		}
	}
	for mask := 0; mask < 1<<n; mask++ {
		v := make([]int, n)
		for i := range v {
			v[i] = 1
			if mask>>i&1 == 1 {
				v[i] = -1
			}
		}
		addDir(v)
	}
	var first [][]int
	seenCell := map[string]bool{}
	for _, v := range dirs {
		r := room(start, v)
		for k := 1; k <= r; k++ {
			cell := make([]int, n)
			for i := range cell {
				cell[i] = start[i] + k*v[i]
			}
			if !seenCell[key(cell)] {
				seenCell[key(cell)] = true
				first = append(first, cell)
			}
		}
	}
	for _, cell := range first {
		var here int64
		for i := 0; i < n; i++ {
			here += int64(cell[i]) * weight[i]
		}
		for _, v := range dirs {
			var step int64
			for i := 0; i < n; i++ {
				step += int64(v[i]) * weight[i]
			}
			// every cell on the ray after the first move
			r := room(cell, v)
			for k := 1; k <= r; k++ {
				add(here + int64(k)*step)
			}
		}
	}
	fmt.Println(distinct)
}
