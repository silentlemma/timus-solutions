package main

import (
	"bufio"
	"fmt"
	"os"
)

const buffer = 1 << 16

var reader = bufio.NewReaderSize(os.Stdin, buffer)

func readInt() int64 {
	c, _ := reader.ReadByte()
	for c == ' ' || c == '\n' || c == '\r' {
		c, _ = reader.ReadByte()
	}
	sign := int64(1)
	if c == '-' {
		sign = -1
		c, _ = reader.ReadByte()
	}
	v := int64(0)
	for c >= '0' && c <= '9' {
		v = v*10 + int64(c-'0')
		c, _ = reader.ReadByte()
	}
	return sign * v
}

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

func main() {
	n := int(readInt())
	y, vertical := int64(1), int64(0)
	var low, high, right int64
	blocked := false
	for i := 0; i < n; i++ {
		readInt()
		y1, x2, y2 := readInt(), readInt(), readInt()
		if i > 0 && !blocked {
			// the rectangles form a chain from left to right, so the
			// horizontal part is fixed; only the height at each border varies
			lo, hi := low+1, high-1
			if y1 > low {
				lo = y1 + 1
			}
			if y2 < high {
				hi = y2 - 1
			}
			if lo > hi {
				blocked = true
			} else {
				// moving only when forced is optimal: clamp into the crossing
				target := y
				if target < lo {
					target = lo
				}
				if target > hi {
					target = hi
				}
				vertical += abs(target - y)
				y = target
			}
		}
		low, high, right = y1, y2, x2
	}
	if blocked {
		fmt.Println(-1)
	} else {
		fmt.Println(right - 2 + vertical + abs(high-1-y))
	}
}
