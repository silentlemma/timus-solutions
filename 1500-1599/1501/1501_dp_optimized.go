package main

import (
	"bytes"
	"io/ioutil"
	"os"
)

const maxLength = 1000

var first, second [maxLength + 1]int16
var forward, backward [maxLength + 1]bool
var moves [2*maxLength + 1]byte
var used int

func frontier(row *[maxLength + 1]bool, a0, a1, b0, b1, step int) bool {
	width := (b1 - b0) * step
	for t := 0; t <= width; t++ {
		row[t] = false
	}
	row[0] = true
	for i := a0; ; i += step {
		any := false
		for t := 0; t <= width; t++ {
			sum := first[i] + second[b0+step*t]
			row[t] = sum >= -1 && sum <= 1 && (row[t] || (t > 0 && row[t-1]))
			any = any || row[t]
		}
		if !any {
			return false
		}
		if i == a1 {
			break
		}
	}
	return true
}
func appendMoves(move byte, count int) {
	for ; count > 0; count-- {
		moves[used] = move
		used++
	}
}
func recover(a0, a1, b0, b1 int) bool {
	if a0 == a1 || b0 == b1 {
		for i := a0; i <= a1; i++ {
			for j := b0; j <= b1; j++ {
				sum := first[i] + second[j]
				if sum < -1 || sum > 1 {
					return false
				}
			}
		}
		if a0 == a1 {
			appendMoves('2', b1-b0)
		} else {
			appendMoves('1', a1-a0)
		}
		return true
	}
	middle := (a0 + a1) / 2
	single := a1-a0 == 1
	upper, lower := middle, middle
	if single {
		upper, lower = a0, a1
	}
	if !frontier(&forward, a0, upper, b0, b1, 1) || !frontier(&backward, a1, lower, b1, b0, -1) {
		return false
	}
	width, split := b1-b0, -1
	for t := 0; t <= width; t++ {
		if forward[t] && backward[width-t] {
			split = t
			break
		}
	}
	if split < 0 {
		return false
	}
	// Height1 joins two horizontal paths with the single first-pile move.
	if single {
		appendMoves('2', split)
		appendMoves('1', 1)
		appendMoves('2', width-split)
		return true
	}
	// No parent frontier remains live: child calls reuse the same arrays.
	return recover(a0, middle, b0, b0+split) && recover(middle, a1, b0+split, b1)
}
func main() {
	raw, _ := ioutil.ReadAll(os.Stdin)
	parts := bytes.Fields(raw)
	a, b := parts[1], parts[2]
	n := len(a)
	for i := 0; i < n; i++ {
		delta := int16(-1)
		if a[i] == '1' {
			delta = 1
		}
		first[i+1] = first[i] + delta
		delta = -1
		if b[i] == '1' {
			delta = 1
		}
		second[i+1] = second[i] + delta
	}
	if recover(0, n, 0, n) {
		moves[used] = '\n'
		os.Stdout.Write(moves[:used+1])
	} else {
		os.Stdout.WriteString("Impossible\n")
	}
}
