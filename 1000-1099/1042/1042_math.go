package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const wordBits = 64

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// equation v over GF(2): the chosen technicians turn valve v an odd number
	// of times; bit n of an equation is its right-hand side
	words := n/wordBits + 1
	eq := make([][]uint64, n)
	for v := range eq {
		eq[v] = make([]uint64, words)
		eq[v][n/wordBits] |= 1 << uint(n%wordBits)
	}
	get := func(row []uint64, c int) bool { return row[c/wordBits]>>uint(c%wordBits)&1 == 1 }
	for t := 0; t < n; t++ {
		for {
			var v int
			fmt.Fscan(in, &v)
			if v == -1 {
				break
			}
			eq[v-1][t/wordBits] |= 1 << uint(t%wordBits)
		}
	}
	// Gauss-Jordan elimination: column c ends with a single 1, in its pivot row
	pivotOf := make([]int, n)
	rank := 0
	for c := 0; c < n; c++ {
		pivotOf[c] = -1
		r := rank
		for r < n && !get(eq[r], c) {
			r++
		}
		if r == n {
			continue
		}
		eq[r], eq[rank] = eq[rank], eq[r]
		for i := 0; i < n; i++ {
			if i != rank && get(eq[i], c) {
				for k := range eq[i] {
					eq[i][k] ^= eq[rank][k]
				}
			}
		}
		pivotOf[c] = rank
		rank++
	}
	for r := rank; r < n; r++ {
		if get(eq[r], n) {
			fmt.Println("No solution")
			return
		}
	}
	// independent technicians make the solution unique, so it is also the shortest
	var chosen []string
	for c := 0; c < n; c++ {
		if pivotOf[c] >= 0 && get(eq[pivotOf[c]], n) {
			chosen = append(chosen, strconv.Itoa(c+1))
		}
	}
	fmt.Println(strings.Join(chosen, " "))
}
