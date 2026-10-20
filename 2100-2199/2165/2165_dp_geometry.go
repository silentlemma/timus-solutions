package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const coordinateLimit int64 = 100000000
const areaBoundFactor int64 = 8
const infinity int64 = areaBoundFactor * coordinateLimit * coordinateLimit
const wholeSuffix = ".0"
const halfSuffix = ".5"

type scanner struct {
	data []byte
	pos  int
}

func (in *scanner) nextInt() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := int64(1)
	if in.data[in.pos] == '-' {
		sign = -1
		in.pos++
	}
	value := int64(0)
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int64(in.data[in.pos]-'0')
		in.pos++
	}
	return value * sign
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n := int(in.nextInt())
	x := make([]int64, n)
	y := make([]int64, n)
	for i := 0; i < n; i++ {
		x[i] = in.nextInt()
		y[i] = in.nextInt()
	}

	dp := make([][]int64, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int64, n)
		if i+1 < n {
			dp[i][i+1] = infinity
		}
	}
	for width := 2; width < n; width++ {
		for left := 0; left+width < n; left++ {
			right := left + width
			best := int64(0)
			dx := x[right] - x[left]
			dy := y[right] - y[left]
			for middle := left + 1; middle < right; middle++ {
				candidate := dp[left][middle]
				if dp[middle][right] < candidate {
					candidate = dp[middle][right]
				}
				if candidate <= best {
					continue
				}
				area := (x[middle]-x[left])*dy - (y[middle]-y[left])*dx
				if area < candidate {
					candidate = area
				}
				if candidate > best {
					best = candidate
				}
			}
			dp[left][right] = best
		}
	}
	answer := dp[0][n-1]
	suffix := wholeSuffix
	if answer%2 != 0 {
		suffix = halfSuffix
	}
	fmt.Printf("%d%s\n", answer/2, suffix)
}
