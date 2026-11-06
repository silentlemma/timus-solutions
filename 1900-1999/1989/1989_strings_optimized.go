package main

import (
	"bufio"
	"bytes"
	"os"
)

const (
	maxWord    = 100000
	bufferSize = 4096
	decimal    = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value := 0
	for _, digit := range input.Bytes() {
		value = value*decimal + int(digit-'0')
	}
	return value
}

func different(a, b byte) int {
	if a != b {
		return 1
	}
	return 0
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], maxWord+1)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	word := append([]byte(nil), input.Bytes()...)
	size := len(word)
	reversed := make([]byte, size)
	changes := 0
	for i, value := range word {
		reversed[size-1-i] = value
		if i > 0 {
			changes += different(word[i-1], value)
		}
	}
	output := bufio.NewWriter(os.Stdout)
	for count := nextInt(input); count > 0; count-- {
		input.Scan()
		update := input.Bytes()[0] == 'c'
		left := nextInt(input) - 1
		if update {
			input.Scan()
			value := input.Bytes()[0]
			if left > 0 {
				changes += different(word[left-1], value) - different(word[left-1], word[left])
			}
			if left+1 < size {
				changes += different(word[left+1], value) - different(word[left+1], word[left])
			}
			word[left], reversed[size-1-left] = value, value
		} else {
			end := nextInt(input)
			half := (end - left) / 2
			if changes == 0 || bytes.Equal(word[left:left+half], reversed[size-end:size-end+half]) {
				output.WriteString("Yes\n")
			} else {
				output.WriteString("No\n")
			}
		}
	}
	output.Flush()
}
