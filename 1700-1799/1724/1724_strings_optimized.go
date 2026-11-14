package main

import (
	"bufio"
	"os"
	"strconv"
)

func states(text []byte) []uint32 {
	state := make([]uint32, len(text)+1)
	var current uint32
	for i, letter := range text {
		// The prefix immediately before an opener stores its parent state.
		if letter >= 'a' && current != 0 && text[current-1] == letter-'a'+'A' {
			current = state[current-1]
		} else {
			current = uint32(i + 1)
		}
		state[i+1] = current
	}
	return state
}

func number(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	const maxTextLength = 100000
	input := bufio.NewScanner(os.Stdin)
	input.Buffer(nil, maxTextLength+1)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	state := states(input.Bytes())
	queries := number(input)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	for i := 0; i < queries; i++ {
		left, right := number(input), number(input)
		answer := byte('0')
		if state[left-1] == state[right] {
			answer = '1'
		}
		output.WriteByte(answer)
	}
	output.WriteByte('\n')
}
