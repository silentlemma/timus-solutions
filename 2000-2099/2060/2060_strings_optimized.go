package main

import (
	"bytes"
	"io"
	"os"
	"strconv"
)

const (
	maxLength = 300000
	decimal   = 10
)

func solve(word []byte) int64 {
	n := len(word)
	radii, ending, starting := make([]int32, n), make([]int32, n+1), make([]int32, n+1)
	left, right := 0, -1
	for center := 0; center < n; center++ {
		radius := 1
		if center <= right {
			radius = int(radii[left+right-center])
			if radius > right-center+1 {
				radius = right - center + 1
			}
		}
		for center-radius >= 0 && center+radius < n && word[center-radius] == word[center+radius] {
			radius++
		}
		radii[center] = int32(radius)
		if center+radius-1 > right {
			left, right = center-radius+1, center+radius-1
		}
		ending[center]++
		ending[center+radius]--
		starting[center-radius+1]++
		starting[center+1]--
	}
	left, right = 0, -1
	for center := 0; center < n; center++ {
		radius := 0
		if center <= right {
			radius = int(radii[left+right-center+1])
			if radius > right-center+1 {
				radius = right - center + 1
			}
		}
		for center-radius-1 >= 0 && center+radius < n && word[center-radius-1] == word[center+radius] {
			radius++
		}
		radii[center] = int32(radius)
		if center+radius-1 > right {
			left, right = center-radius, center+radius-1
		}
		if radius != 0 {
			ending[center]++
			ending[center+radius]--
			starting[center-radius]++
			starting[center]--
		}
	}
	// The product uses ending at the cut and starting immediately after it.
	var countEnding, countStarting int32 = 0, starting[0]
	var answer int64
	for cut := 0; cut+1 < n; cut++ {
		countEnding += ending[cut]
		countStarting += starting[cut+1]
		answer += int64(countEnding) * int64(countStarting)
	}
	return answer
}

func main() {
	var input [maxLength + 2]byte
	count, _ := io.ReadFull(os.Stdin, input[:])
	word := bytes.TrimSpace(input[:count])
	os.Stdout.WriteString(strconv.FormatInt(solve(word), decimal) + "\n")
}
