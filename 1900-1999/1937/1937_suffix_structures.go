package main

import (
	"bufio"
	"fmt"
	"os"
)

const alphabetSize = 26

func palindromeRadii(text string, odd bool) []int32 {
	radius := make([]int32, len(text))
	left, right := 0, -1
	if odd {
		for center := range text {
			current := 0
			if center <= right {
				current = int(radius[left+right-center])
				if current > right-center {
					current = right - center
				}
			}
			for center-current-1 >= 0 && center+current+1 < len(text) &&
				text[center-current-1] == text[center+current+1] {
				current++
			}
			radius[center] = int32(current)
			if center+current > right {
				left, right = center-current, center+current
			}
		}
	} else {
		for center := range text {
			current := 0
			if center <= right {
				current = int(radius[left+right-center+1])
				if current > right-center+1 {
					current = right - center + 1
				}
			}
			for center-current-1 >= 0 && center+current < len(text) &&
				text[center-current-1] == text[center+current] {
				current++
			}
			radius[center] = int32(current)
			if center+current-1 > right {
				left, right = center-current, center+current-1
			}
		}
	}
	return radius
}

type suffixAutomaton struct {
	transitions, length, link, firstEnd []int32
}

func newSuffixAutomaton(pattern string) *suffixAutomaton {
	capacity := 2 * len(pattern)
	automaton := &suffixAutomaton{
		transitions: make([]int32, capacity*alphabetSize),
		length:      make([]int32, capacity),
		link:        make([]int32, capacity),
		firstEnd:    make([]int32, capacity),
	}
	for index := range automaton.transitions {
		automaton.transitions[index] = -1
	}
	for index := range automaton.link {
		automaton.link[index], automaton.firstEnd[index] = -1, -1
	}
	states, last := int32(1), int32(0)
	for position := range pattern {
		symbol := int32(pattern[position] - 'a')
		current := states
		states++
		automaton.length[current] = automaton.length[last] + 1
		automaton.firstEnd[current] = int32(position)
		previous := last
		for previous >= 0 && automaton.transitions[previous*alphabetSize+symbol] < 0 {
			automaton.transitions[previous*alphabetSize+symbol] = current
			previous = automaton.link[previous]
		}
		if previous < 0 {
			automaton.link[current] = 0
		} else {
			following := automaton.transitions[previous*alphabetSize+symbol]
			if automaton.length[previous]+1 == automaton.length[following] {
				automaton.link[current] = following
			} else {
				clone := states
				states++
				automaton.length[clone] = automaton.length[previous] + 1
				automaton.link[clone] = automaton.link[following]
				automaton.firstEnd[clone] = automaton.firstEnd[following]
				copy(automaton.transitions[clone*alphabetSize:(clone+1)*alphabetSize],
					automaton.transitions[following*alphabetSize:(following+1)*alphabetSize])
				for previous >= 0 && automaton.transitions[previous*alphabetSize+symbol] == following {
					automaton.transitions[previous*alphabetSize+symbol] = clone
					previous = automaton.link[previous]
				}
				automaton.link[following], automaton.link[current] = clone, clone
			}
		}
		last = current
	}
	return automaton
}

func findRotations(first, second string) (int, int) {
	firstSize, secondSize := len(first), len(second)
	middleSize := firstSize - secondSize
	doubled := first + first
	radius := palindromeRadii(doubled, middleSize%2 != 0)
	half := middleSize / 2
	centerOffset := secondSize + half
	candidateExists := false
	for start := 0; start < firstSize; start++ {
		if int(radius[start+centerOffset]) >= half {
			candidateExists = true
			break
		}
	}
	if !candidateExists {
		return -1, -1
	}
	reversed := []byte(second)
	for left, right := 0, len(reversed)-1; left < right; left, right = left+1, right-1 {
		reversed[left], reversed[right] = reversed[right], reversed[left]
	}
	reversedSecond := string(reversed)
	pattern := reversedSecond + reversedSecond[:secondSize-1]
	automaton := newSuffixAutomaton(pattern)
	state, matched := int32(0), 0
	for position := 0; position < firstSize+secondSize-1; position++ {
		symbol := int32(doubled[position] - 'a')
		for state != 0 && automaton.transitions[state*alphabetSize+symbol] < 0 {
			state = automaton.link[state]
			matched = int(automaton.length[state])
		}
		following := automaton.transitions[state*alphabetSize+symbol]
		if following >= 0 {
			state = following
			matched++
		} else {
			state, matched = 0, 0
		}
		start := position - secondSize + 1
		if start >= 0 && matched >= secondSize && int(radius[start+centerOffset]) >= half {
			reversedStart := int(automaton.firstEnd[state]) - secondSize + 1
			return start, (secondSize - reversedStart) % secondSize
		}
	}
	return -1, -1
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var first, second string
	fmt.Fscan(input, &first, &second)
	left, right := findRotations(first, second)
	if left < 0 {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
		fmt.Println(left+1, right+1)
	}
}
