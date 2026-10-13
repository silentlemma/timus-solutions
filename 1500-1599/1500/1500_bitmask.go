package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"strings"
)

const half = 10 // categories are split into a low and a high half of the mask

func main() {
	reader := bufio.NewReader(os.Stdin)
	var k, n, m int
	fmt.Fscan(reader, &k, &n, &m)
	// byCategory[u][c]: the crossings next to u along roads of category c
	byCategory := make([][]uint32, n)
	for u := range byCategory {
		byCategory[u] = make([]uint32, k)
	}
	for i := 0; i < m; i++ {
		var a, b, c int
		fmt.Fscan(reader, &a, &b, &c)
		byCategory[a][c] |= 1 << uint(b)
		byCategory[b][c] |= 1 << uint(a)
	}
	lowSize := k
	if lowSize > half {
		lowSize = half
	}
	highSize := k - lowSize
	low := make([][]uint32, n)
	high := make([][]uint32, n)
	for u := 0; u < n; u++ {
		low[u] = make([]uint32, 1<<uint(lowSize))
		high[u] = make([]uint32, 1<<uint(highSize))
		for s := 1; s < 1<<uint(lowSize); s++ {
			low[u][s] = low[u][s&(s-1)] | byCategory[u][bits.TrailingZeros(uint(s))]
		}
		for s := 1; s < 1<<uint(highSize); s++ {
			high[u][s] = high[u][s&(s-1)] | byCategory[u][lowSize+bits.TrailingZeros(uint(s))]
		}
	}
	lowMask := 1<<uint(lowSize) - 1
	// connects tells whether the roads of the categories in s lead from 0 to 1
	connects := func(s int) bool {
		lo, hi := s&lowMask, s>>uint(lowSize)
		reach, todo := uint32(1), uint32(1)
		for todo != 0 {
			u := bits.TrailingZeros32(todo)
			todo &= todo - 1
			fresh := (low[u][lo] | high[u][hi]) &^ reach
			reach |= fresh
			todo |= fresh
			if reach&2 != 0 {
				return true
			}
		}
		return false
	}
	// fewer permits first
	for size := 1; size <= k; size++ {
		for s := 0; s < 1<<uint(k); s++ {
			if bits.OnesCount(uint(s)) == size && connects(s) {
				var chosen []string
				for c := 0; c < k; c++ {
					if s>>uint(c)&1 == 1 {
						chosen = append(chosen, fmt.Sprint(c))
					}
				}
				fmt.Println(size)
				fmt.Println(strings.Join(chosen, " "))
				return
			}
		}
	}
}
