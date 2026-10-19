package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
)

func palindromeCounts(word []byte) ([]int, []int) {
	n := len(word)
	radii, ending, starting := make([]int, n), make([]int, n+1), make([]int, n+1)
	left, right := 0, -1
	for center := 0; center < n; center++ {
		radius := 1
		if center <= right {
			radius = radii[left+right-center]
			if radius > right-center+1 {
				radius = right - center + 1
			}
		}
		for center-radius >= 0 && center+radius < n && word[center-radius] == word[center+radius] {
			radius++
		}
		radii[center] = radius
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
			radius = radii[left+right-center+1]
			if radius > right-center+1 {
				radius = right - center + 1
			}
		}
		for center-radius-1 >= 0 && center+radius < n && word[center-radius-1] == word[center+radius] {
			radius++
		}
		radii[center] = radius
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
	countEnding, countStarting := 0, 0
	for i := 0; i < n; i++ {
		countEnding += ending[i]
		countStarting += starting[i]
		ending[i], starting[i] = countEnding, countStarting
	}
	return ending, starting
}

func solve(word []byte) int64 {
	ending, starting := palindromeCounts(word)
	answer := int64(0)
	for cut := 0; cut+1 < len(word); cut++ {
		answer += int64(ending[cut]) * int64(starting[cut+1])
	}
	return answer
}

func main() {
	raw, _ := ioutil.ReadAll(os.Stdin)
	fmt.Println(solve(bytes.TrimSpace(raw)))
}
