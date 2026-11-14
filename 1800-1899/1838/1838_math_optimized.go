package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const decimal = 10

func next(input *bufio.Reader) int32 {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	var value int32
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*decimal + int32(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func safeLength(length int32, supports []int32) int32 {
	minCut := 2 * supports[0]
	maxCut := 2*supports[len(supports)-1] - length
	if minCut >= maxCut {
		return 0
	}
	start := sort.Search(len(supports), func(i int) bool { return supports[i] > minCut })
	var safe int32
	for i := start; i < len(supports); i++ {
		left, right := supports[i-1], supports[i]
		if left >= maxCut {
			break
		}
		lo, hi := left, right
		// Clip the gap by the extreme supports and the two centers of mass.
		if lo < minCut {
			lo = minCut
		}
		if lo < 2*right-length {
			lo = 2*right - length
		}
		if hi > maxCut {
			hi = maxCut
		}
		if hi > 2*left {
			hi = 2 * left
		}
		if hi > lo {
			safe += hi - lo
		}
	}
	return safe
}

func main() {
	input := bufio.NewReader(os.Stdin)
	length, count := next(input), next(input)
	supports := make([]int32, count)
	for i := range supports {
		supports[i] = next(input)
	}
	unsafe := length - safeLength(length, supports)
	os.Stdout.WriteString(strconv.FormatInt(int64(unsafe), decimal) + "\n")
}
