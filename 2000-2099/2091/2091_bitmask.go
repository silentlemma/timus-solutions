package main

import (
	"math/bits"
	"syscall"
)

const rawInputSize = 256
const rawOutputSize = 128
const decimalSize = 32
const radix = 10

var rawInput [rawInputSize]byte
var rawPosition, rawLength int
var rawOutput [rawOutputSize]byte
var rawUsed int

func byteIn() byte {
	if rawPosition == rawLength {
		// Global arrays stay live and never move across the raw system call.
		n, failure := syscall.Read(syscall.Stdin, rawInput[:])
		if failure != nil || n == 0 {
			return 0
		}
		rawPosition, rawLength = 0, int(n)
	}
	ch := rawInput[rawPosition]
	rawPosition++
	return ch
}
func nextInt() int {
	ch := byteIn()
	for ch != 0 && ch <= ' ' {
		ch = byteIn()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*radix + int(ch-'0')
		ch = byteIn()
	}
	return value
}
func flush() {
	at := 0
	for at < rawUsed {
		n, failure := syscall.Write(syscall.Stdout, rawOutput[at:rawUsed])
		if failure != nil || n == 0 {
			break
		}
		at += int(n)
	}
	rawUsed = 0
}
func byteOut(ch byte) {
	if rawUsed == len(rawOutput) {
		flush()
	}
	rawOutput[rawUsed] = ch
	rawUsed++
}
func numberOut(value int64) {
	var digits [decimalSize]byte
	at := len(digits)
	for {
		at--
		digits[at] = byte(value%radix) + '0'
		value /= radix
		if value == 0 {
			break
		}
	}
	for ; at < len(digits); at++ {
		byteOut(digits[at])
	}
}

const maxCourses = 100
const wordBits = 64
const groups = 4

var low, high [maxCourses]uint64
var counts [maxCourses]int

func emit(best, first, second int) {
	numberOut(int64(best))
	byteOut('\n')
	numberOut(int64(first + 1))
	byteOut(' ')
	numberOut(int64(second + 1))
	byteOut('\n')
	flush()
}
func main() {
	n, m := nextInt(), nextInt()
	for row := 0; row < n; row++ {
		for course := 0; course < m; course++ {
			if nextInt() != 0 {
				counts[course]++
				if row < wordBits {
					low[course] |= uint64(1) << uint(row)
				} else {
					high[course] |= uint64(1) << uint(row-wordBits)
				}
			}
		}
	}
	best, first, second := n+1, 0, 1
	for a := 0; a < m; a++ {
		for b := a + 1; b < m; b++ {
			both := bits.OnesCount64(low[a]&low[b]) + bits.OnesCount64(high[a]&high[b])
			score := both
			if value := counts[a] - both; value > score {
				score = value
			}
			if value := counts[b] - both; value > score {
				score = value
			}
			if value := n - counts[a] - counts[b] + both; value > score {
				score = value
			}
			if score < best {
				best, first, second = score, a, b
			}
			if best == (n+groups-1)/groups {
				emit(best, first, second)
				return
			}
		}
	}
	emit(best, first, second)
}
