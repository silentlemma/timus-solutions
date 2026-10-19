package main

import (
	"os"
)

const maxInput = 5000000 + 16

func main() {
	// one fixed buffer: the word, and then the answer in its place
	data := make([]byte, maxInput)
	total := 0
	for total < len(data) {
		k, err := os.Stdin.Read(data[total:])
		total += k
		if err != nil || k == 0 {
			break
		}
	}
	data = data[:total]
	start := 0
	for start < len(data) && (data[start] < 'a' || data[start] > 'z') {
		start++
	}
	end := start
	for end < len(data) && data[end] >= 'a' && data[end] <= 'z' {
		end++
	}
	word := data[start:end]
	n := len(word)
	// node 0 is the imaginary root of length -1, node 1 the empty string
	length := make([]int32, n+2)
	link := make([]int32, n+2)
	next := [2][]int32{make([]int32, n+2), make([]int32, n+2)}
	length[0] = -1
	// bit 4 is clear in 'a' and 'b'; it marks the positions that add a palindrome
	const mark = 4
	var last, used int32 = 1, 2
	for pos := 0; pos < n; pos++ {
		c := word[pos]
		letter := c - 'a'
		parent := last
		for {
			before := pos - 1 - int(length[parent])
			if before >= 0 && word[before]&^mark == c {
				break
			}
			parent = link[parent]
		}
		current := next[letter][parent]
		if current == 0 {
			current = used
			used++
			length[current] = length[parent] + 2
			next[letter][parent] = current
			if length[current] == 1 {
				link[current] = 1
			} else {
				candidate := link[parent]
				for {
					before := pos - 1 - int(length[candidate])
					if before >= 0 && word[before]&^mark == c {
						break
					}
					candidate = link[candidate]
				}
				link[current] = next[letter][candidate]
			}
			word[pos] |= mark
		}
		last = current
	}
	for i := range word {
		if word[i]&mark != 0 {
			word[i] = '1'
		} else {
			word[i] = '0'
		}
	}
	if end < len(data) {
		data[end] = '\n'
		os.Stdout.Write(data[start : end+1])
	} else {
		os.Stdout.Write(word)
		os.Stdout.Write([]byte{'\n'})
	}
}
