package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

type FastInput struct {
	data []byte
	pos  int
}

func (in *FastInput) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

type Entry struct {
	index int
	value int
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := FastInput{data: data}
	rows, width := in.nextInt(), in.nextInt()
	height, santaWidth := in.nextInt(), in.nextInt()
	left := make([]Entry, rows)
	right := make([]Entry, rows)
	leftHead, leftTail := 0, 0
	rightHead, rightTail := 0, 0
	best := 0

	for index := 0; index < rows; index++ {
		leftValue, rightValue := in.nextInt(), in.nextInt()
		first := index - height
		for leftHead < leftTail && left[leftHead].index < first {
			leftHead++
		}
		for rightHead < rightTail && right[rightHead].index < first {
			rightHead++
		}
		for leftHead < leftTail && left[leftTail-1].value <= leftValue {
			leftTail--
		}
		for rightHead < rightTail && right[rightTail-1].value <= rightValue {
			rightTail--
		}
		left[leftTail] = Entry{index: index, value: leftValue}
		leftTail++
		right[rightTail] = Entry{index: index, value: rightValue}
		rightTail++
		current := left[leftHead].value + right[rightHead].value
		if current > best {
			best = current
		}
	}

	answer := width - santaWidth + 1 - best
	if answer < 0 {
		answer = 0
	}
	fmt.Println(answer)
}
