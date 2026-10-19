package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math/bits"
	"os"
)

const wordBits = 64
const decimal = 10

type Matrix [][]uint64

func matrix(n, m int) Matrix {
	rows := make(Matrix, n)
	for u := range rows {
		rows[u] = make([]uint64, (m+wordBits-1)/wordBits)
	}
	return rows
}
func maximumMatching(rows Matrix, m int) ([]int, []int) {
	n := len(rows)
	words := (m + wordBits - 1) / wordBits
	remaining := m
	left, right := make([]int, n), make([]int, m)
	for u := range left {
		left[u] = -1
	}
	for v := range right {
		right[v] = -1
	}
	free := make([]uint64, words)
	for w := range free {
		free[w] = ^uint64(0)
	}
	if m%wordBits != 0 {
		free[words-1] = (uint64(1) << uint(m%wordBits)) - 1
	}
	for start := 0; start < n && remaining > 0; start++ {
		direct := -1
		for w := 0; w < words; w++ {
			mask := rows[start][w] & free[w]
			if mask != 0 {
				direct = w*wordBits + bits.TrailingZeros64(mask)
				break
			}
		}
		if direct >= 0 {
			left[start] = direct
			right[direct] = start
			free[direct/wordBits] &^= uint64(1) << uint(direct%wordBits)
			remaining--
			continue
		}
		queue := make([]int, 1, n)
		queue[0] = start
		parent := make([]int, m)
		for v := range parent {
			parent[v] = -1
		}
		seen := make([]uint64, words)
		finish := -1
		for at := 0; at < len(queue) && finish < 0; at++ {
			u := queue[at]
			for w := 0; w < words && finish < 0; w++ {
				mask := rows[u][w] &^ seen[w]
				for mask != 0 {
					bit := mask & (^mask + 1)
					mask &= mask - 1
					seen[w] |= bit
					v := w*wordBits + bits.TrailingZeros64(bit)
					parent[v] = u
					if right[v] < 0 {
						finish = v
						break
					}
					queue = append(queue, right[v])
				}
			}
		}
		if finish >= 0 {
			free[finish/wordBits] &^= uint64(1) << uint(finish%wordBits)
			remaining--
			for finish >= 0 {
				u := parent[finish]
				old := left[u]
				left[u] = finish
				right[finish] = u
				finish = old
			}
		}
	}
	return left, right
}
func reach(rows Matrix, opposite, ownMatch []int) ([]bool, []bool) {
	own, other := make([]bool, len(rows)), make([]bool, len(opposite))
	queue := make([]int, 0, len(rows))
	for u, matched := range ownMatch {
		if matched < 0 {
			own[u] = true
			queue = append(queue, u)
		}
	}
	words := (len(opposite) + wordBits - 1) / wordBits
	seen := make([]uint64, words)
	for at := 0; at < len(queue); at++ {
		u := queue[at]
		for w := 0; w < words; w++ {
			mask := rows[u][w] &^ seen[w]
			for mask != 0 {
				bit := mask & (^mask + 1)
				mask &= mask - 1
				seen[w] |= bit
				v := w*wordBits + bits.TrailingZeros64(bit)
				partner := opposite[v]
				other[v] = true
				if partner >= 0 && !own[partner] {
					own[partner] = true
					queue = append(queue, partner)
				}
			}
		}
	}
	return own, other
}
func solve(rows, reverse Matrix) (string, string) {
	left, right := maximumMatching(rows, len(reverse))
	neverLeft, alwaysRight := reach(rows, right, left)
	neverRight, alwaysLeft := reach(reverse, left, right)
	a, b := make([]byte, len(rows)), make([]byte, len(reverse))
	for u := range a {
		a[u] = 'E'
		if neverLeft[u] {
			a[u] = 'N'
		} else if alwaysLeft[u] {
			a[u] = 'A'
		}
	}
	for v := range b {
		b[v] = 'E'
		if neverRight[v] {
			b[v] = 'N'
		} else if alwaysRight[v] {
			b[v] = 'A'
		}
	}
	return string(a), string(b)
}

type Input struct {
	data []byte
	at   int
}

func (in *Input) next() int {
	for in.at < len(in.data) && in.data[in.at] <= ' ' {
		in.at++
	}
	value := 0
	for in.at < len(in.data) && in.data[in.at] > ' ' {
		value = value*decimal + int(in.data[in.at]-'0')
		in.at++
	}
	return value
}
func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err != nil {
		return
	}
	in := Input{data: data}
	n, m, k := in.next(), in.next(), in.next()
	rows, reverse := matrix(n, m), matrix(m, n)
	for i := 0; i < k; i++ {
		u, v := in.next()-1, in.next()-1
		rows[u][v/wordBits] |= uint64(1) << uint(v%wordBits)
		reverse[v][u/wordBits] |= uint64(1) << uint(u%wordBits)
	}
	a, b := solve(rows, reverse)
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, a)
	fmt.Fprintln(out, b)
	out.Flush()
}
