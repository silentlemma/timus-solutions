package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	base = 10
	inf  = 1 << 30
)

// digit returns digit i of s from the lowest, zero past its length.
func digit(s string, i int) int {
	if i < len(s) {
		return int(s[len(s)-1-i] - '0')
	}
	return 0
}

// least is the lowest digit position i may take: the first digit may not
// become zero.
func least(s string, i int) int {
	if i == len(s)-1 {
		return 1
	}
	return 0
}

// most is the highest: past its own length a number has only the digit 0.
func most(s string, i int) int {
	if i < len(s) {
		return base - 1
	}
	return 0
}

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b, c string
	fmt.Fscan(in, &a, &b, &c)
	width := len(c)
	if len(a) > width || len(b) > width {
		fmt.Println(-1) // the sum would be longer than C
		return
	}
	// cost[carry]: the cheapest fix of the lower positions that carries this
	cost := [2]int{0, inf}
	for i := 0; i < width; i++ {
		next := [2]int{inf, inf}
		for carry := 0; carry < 2; carry++ {
			if cost[carry] == inf {
				continue
			}
			for x := least(a, i); x <= most(a, i); x++ {
				for y := least(b, i); y <= most(b, i); y++ {
					total := x + y + carry
					z := total % base
					if z < least(c, i) {
						continue
					}
					v := cost[carry] + abs(x-digit(a, i)) + abs(y-digit(b, i)) + abs(z-digit(c, i))
					if v < next[total/base] {
						next[total/base] = v
					}
				}
			}
		}
		cost = next
	}
	if cost[0] < inf {
		fmt.Println(cost[0])
	} else {
		fmt.Println(-1)
	}
}
