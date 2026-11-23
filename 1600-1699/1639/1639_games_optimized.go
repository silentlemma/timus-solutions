package main

import (
	"io/ioutil"
	"os"
)

// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer(data []byte, index *int) int {
	for *index < len(data) && data[*index] <= ' ' {
		*index += 1
	}
	value := 0
	for *index < len(data) && data[*index] >= '0' && data[*index] <= '9' {
		value = value*10 + int(data[*index]-'0')
		*index += 1
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	index := 0
	m, n := integer(data, &index), integer(data, &index)
	// every break adds one piece, so the game always lasts m * n - 1 moves
	if (m*n-1)%2 == 1 {
		os.Stdout.WriteString("[:=[first]\n")
	} else {
		os.Stdout.WriteString("[second]=:]\n")
	}
}
