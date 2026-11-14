package main

import "os"

const (
	maxDigits   = 2000
	blockDigits = 6
	maxBlocks   = (maxDigits + blockDigits - 1) / blockDigits
	decimal     = 10
	base        = 1000000
	firstBlock  = 890625
	inverse     = 218751 // Inverse of 1 - 2*firstBlock modulo base.
	oneDigit    = 3
	ioSize      = 32
)

func countSolutions(n int) int {
	var blocks [maxBlocks]uint64
	blocks[0] = firstBlock
	carry := uint64(firstBlock * firstBlock / base)
	count := oneDigit
	place := 0
	digits := uint64(firstBlock / decimal)
	available := blockDigits - 1
	for remaining := n - 1; remaining > 0; remaining-- {
		if available == 0 {
			place++
			known := carry
			for left, right := 1, place-1; left < right; left, right = left+1, right-1 {
				known += 2 * blocks[left] * blocks[right]
			}
			if place%2 == 0 {
				middle := blocks[place/2]
				known += middle * middle
			}
			// A new block adds 2*firstBlock*digits to its column of the square.
			// Solve the resulting linear congruence for that block.
			digits = (known % base) * inverse % base
			blocks[place] = digits
			carry = (known + 2*firstBlock*digits) / base
			available = blockDigits
		}
		digit := digits % decimal
		if digit != 0 {
			count++
		}
		if digit != decimal-1 {
			count++
		}
		digits /= decimal
		available--
	}
	return count
}
func main() {
	var data [ioSize]byte
	n := 0
reading:
	for {
		size, _ := os.Stdin.Read(data[:])
		if size == 0 {
			break
		}
		for _, ch := range data[:size] {
			if ch >= '0' && ch <= '9' {
				n = n*decimal + int(ch-'0')
			} else if n != 0 {
				break reading
			}
		}
	}
	answer := countSolutions(n)
	start := len(data) - 1
	data[start] = '\n'
	for answer != 0 {
		start--
		data[start] = byte(answer%decimal) + '0'
		answer /= decimal
	}
	os.Stdout.Write(data[start:])
}
