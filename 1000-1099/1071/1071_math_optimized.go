package main

import (
	"math"
	"syscall"
)

const (
	decimal    = 10
	bufferSize = 32
)

func fits(x, y, base int) bool {
	// Match the subsequence starting with the least significant digit.
	wanted := y % base
	for x > y {
		digit := x % base
		x /= base
		if digit == wanted {
			y /= base
			if y == 0 {
				return true
			}
			wanted = y % base
		}
	}
	return x == y
}

func smallBase(x, y, last int) int {
	// If x >= y², x always has more digits throughout this range.
	if y <= x/y {
		for base := 2; base <= last; base++ {
			if fits(x, y, base) {
				return base
			}
		}
		return 0
	}
	for base := 2; base <= last; {
		highX, highY := x, y
		exponent := 0
		for highY >= base {
			highX /= base
			highY /= base
			exponent++
		}
		if highX < base {
			// Equal digit counts cannot match by deletion. The count for x
			// cannot increase, so skip until y needs one fewer digit.
			base = afterPower(base+1, last+1, exponent, y)
		} else if fits(x, y, base) {
			return base
		} else {
			base++
		}
	}
	return 0
}

func answer(x, y int) int {
	last := int(math.Sqrt(float64(x)))
	if base := smallBase(x, y, last); base != 0 {
		return base
	}
	base := max(2, last+1)
	best := x + 1
	low := max(base, x/(y+1)+1)
	if low <= x/y {
		best = low
	}
	difference := x - y
	// Larger divisors of the complement correspond to smaller bases.
	for d := difference / max(base, y+1); d > 0; d-- {
		if difference%d == 0 {
			if candidate := difference / d; candidate < best {
				best = candidate
			}
			break
		}
	}
	if best <= x {
		return best
	}
	return 0
}

// Find the first base in [low, high) whose exponent-th power exceeds value.
// If every base satisfies the old digit bound, return the exclusive limit.
func afterPower(low, high, exponent, value int) int {
	for low < high {
		mid := low + (high-low)/2
		power := 1
		for i := 0; i < exponent && power <= value; i++ {
			power *= mid
		}
		if power > value {
			high = mid
		} else {
			low = mid + 1
		}
	}
	return low
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func readPair() (int, int) {
	var values [2]int
	var buffer [bufferSize]byte
	index, reading := 0, false
	for {
		size, err := syscall.Read(syscall.Stdin, buffer[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return values[0], values[1]
		}
		for _, c := range buffer[:size] {
			if c >= '0' && c <= '9' {
				values[index] = values[index]*decimal + int(c-'0')
				reading = true
			} else if reading {
				index++
				if index == len(values) {
					return values[0], values[1]
				}
				reading = false
			}
		}
		if err != nil {
			return values[0], values[1]
		}
	}
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func main() {
	x, y := readPair()
	if x <= y || y <= 0 {
		return
	}
	best := answer(x, y)
	if best == 0 {
		write([]byte("No solution\n"))
		return
	}
	var buffer [bufferSize]byte
	pos := len(buffer) - 1
	buffer[pos] = '\n'
	for best > 0 {
		pos--
		buffer[pos] = '0' + byte(best%decimal)
		best /= decimal
	}
	write(buffer[pos:])
}
