package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const outputReservePerQuery = 16

type fastInput struct {
	data     []byte
	position int
}

func (input *fastInput) readInt() int {
	for input.position < len(input.data) && input.data[input.position] <= ' ' {
		input.position++
	}
	negative := input.data[input.position] == '-'
	if negative {
		input.position++
	}
	value := 0
	for input.position < len(input.data) {
		ch := input.data[input.position]
		if ch < '0' || ch > '9' {
			break
		}
		value = value*10 + int(ch-'0')
		input.position++
	}
	if negative {
		return -value
	}
	return value
}

type removedRange struct {
	left   int
	right  int
	center int
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := fastInput{data: data}
	n := input.readInt()
	q := input.readInt()
	steps := make([]int, n)
	for index := range steps {
		steps[index] = input.readInt()
	}
	queries := make([]int, q)
	maximum := 0
	for index := range queries {
		query := input.readInt()
		queries[index] = query
		magnitude := query
		if query < 0 {
			magnitude = -query - 1
		}
		if magnitude > maximum {
			maximum = magnitude
		}
	}

	left, right := 0, maximum+1
	offset := int64(0)
	removed := make([]removedRange, 0)
	for _, step := range steps {
		if int64(left)+offset < 0 {
			offset += int64(step)
		} else {
			offset -= int64(step)
		}
		cut := -offset
		if int64(left) < cut && cut < int64(right) {
			middle := int(cut)
			center := 2*middle - 1
			// Opposite values stay related by x -> -x - 1 after every later step.
			if middle-left <= right-middle {
				removed = append(removed, removedRange{left, middle, center})
				left = middle
			} else {
				removed = append(removed, removedRange{middle, right, center})
				right = middle
			}
		}
	}

	answer := make([]int64, maximum+1)
	for index := left; index < right; index++ {
		answer[index] = int64(index) + offset
	}
	for block := len(removed) - 1; block >= 0; block-- {
		current := removed[block]
		for index := current.left; index < current.right; index++ {
			answer[index] = -answer[current.center-index] - 1
		}
	}

	output := make([]byte, 0, q*outputReservePerQuery)
	for _, query := range queries {
		var value int64
		if query < 0 {
			value = -answer[-query-1] - 1
		} else {
			value = answer[query]
		}
		output = strconv.AppendInt(output, value, 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
