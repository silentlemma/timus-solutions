package main

import (
	"fmt"
	"math/bits"
	"os"
)

const bufferSize = 4096
const wordBits = 64

var input [bufferSize]byte
var position, available int

func read() int {
	if position == available {
		available, _ = os.Stdin.Read(input[:])
		position = 0
		if available == 0 {
			return -1
		}
	}
	value := input[position]
	position++
	return int(value)
}

func nextInt() int {
	c := read()
	for c <= ' ' {
		c = read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + c - '0'
		c = read()
	}
	return value
}

func main() {
	m, n, edges := nextInt(), nextInt(), nextInt()
	left, right := m, n
	if left > right {
		left, right = right, left
	}
	words := (right + wordBits - 1) / wordBits
	adjacent, free := make([]uint64, left*words), make([]uint64, words)
	for b := range free {
		free[b] = ^uint64(0)
	}
	for i := 0; i < edges; i++ {
		a, b := nextInt()-1, nextInt()-1
		if m > n {
			a, b = b, a
		}
		adjacent[a*words+b/wordBits] |= uint64(1) << uint(b%wordBits)
	}
	matchL, matchR := make([]int, left), make([]int, right)
	parent, queue := make([]int, right), make([]int, left)
	for v := range matchL {
		matchL[v] = -1
	}
	for u := range matchR {
		matchR[u] = -1
	}
	size := 0
	for root := 0; root < left; root++ {
		seen := make([]uint64, words)
		head, tail, target := 0, 1, -1
		queue[0] = root
		for head < tail && target < 0 {
			v := queue[head]
			head++
			for b := 0; b < words; b++ {
				available := adjacent[v*words+b] & free[b]
				if available != 0 {
					target = b*wordBits + bits.TrailingZeros64(available)
					parent[target] = v
					break
				}
			}
			if target >= 0 {
				break
			}
			// Each unseen right vertex has one matched partner, enqueued once.
			for b := 0; b < words; b++ {
				options := adjacent[v*words+b] &^ seen[b]
				seen[b] |= options
				for options != 0 {
					u := b*wordBits + bits.TrailingZeros64(options)
					parent[u] = v
					queue[tail] = matchR[u]
					tail++
					options &= options - 1
				}
			}
		}
		if target >= 0 {
			free[target/wordBits] &^= uint64(1) << uint(target%wordBits)
			// Reverse old matching edges along the BFS parent chain.
			for target >= 0 {
				v := parent[target]
				old := matchL[v]
				matchL[v], matchR[target] = target, v
				target = old
			}
			size++
		}
	}
	fmt.Println(m + n - size)
}
