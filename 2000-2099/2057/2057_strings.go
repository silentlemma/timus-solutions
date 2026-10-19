package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
)

type Palindromes struct{ odd, even []int }

func buildRadii(word []byte) *Palindromes {
	size := len(word)
	result := &Palindromes{make([]int, size), make([]int, size)}
	left, right := 0, -1
	for center := 0; center < size; center++ {
		radius := 1
		if center <= right {
			radius = result.odd[left+right-center]
			if right-center+1 < radius {
				radius = right - center + 1
			}
		}
		for center >= radius && center+radius < size && word[center-radius] == word[center+radius] {
			radius++
		}
		result.odd[center] = radius
		if center+radius-1 > right {
			left, right = center-radius+1, center+radius-1
		}
	}
	left, right = 0, -1
	for center := 0; center < size; center++ {
		radius := 0
		if center <= right {
			radius = result.even[left+right-center+1]
			if right-center+1 < radius {
				radius = right - center + 1
			}
		}
		for center > radius && center+radius < size && word[center-radius-1] == word[center+radius] {
			radius++
		}
		result.even[center] = radius
		if center+radius-1 > right {
			left, right = center-radius, center+radius-1
		}
	}
	return result
}
func (radii *Palindromes) palindrome(start, end int) bool {
	length, center := end-start, (start+end)/2
	if length%2 != 0 {
		return radii.odd[center] >= length/2+1
	}
	return radii.even[center] >= length/2
}
func negativeArray(size int) []int {
	result := make([]int, size)
	for i := range result {
		result[i] = -1
	}
	return result
}
func solve(word []byte) (int, int) {
	size := len(word)
	radii := buildRadii(word)
	maximum := negativeArray(size + 1)
	first, last := negativeArray(size/2+1), negativeArray(size/2+1)
	maximum[0] = 0
	highest := -1
	for end := 1; end <= size; end++ {
		position := end - 2
		if position >= 0 && maximum[position] >= 0 {
			value := maximum[position]
			if first[value] < 0 {
				first[value] = position
			}
			last[value] = position
			if value > highest {
				highest = value
			}
		}
		for value := highest; value >= 0 && value >= highest-1; value-- {
			if first[value] >= 0 &&
				(!radii.palindrome(first[value], end) || !radii.palindrome(last[value], end)) {
				maximum[end] = value + 1
				break
			}
		}
	}
	if maximum[size] < 0 {
		return -1, -1
	}
	minimum := 1
	if radii.palindrome(0, size) {
		minimum = 2
	}
	return minimum, maximum[size]
}
func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	word := bytes.Fields(input)[0]
	minimum, maximum := solve(word)
	if minimum < 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(minimum, maximum)
	}
}
