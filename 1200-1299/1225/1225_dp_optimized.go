package main

import (
	"io/ioutil"
	"os"
	"strconv"
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
	n := integer(data, &index)
	// a row ends in white or red; it comes from a row one shorter ending in
	// the other of the two, or from one two shorter followed by blue
	prev, cur := int64(2), int64(2)
	for i := 2; i < n; i++ {
		prev, cur = cur, prev+cur
	}
	result := strconv.AppendInt(make([]byte, 0, 24), int64(cur), 10)
	result = append(result, '\n')
	os.Stdout.Write(result)
}
