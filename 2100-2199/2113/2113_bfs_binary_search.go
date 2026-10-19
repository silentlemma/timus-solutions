package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const (
	blocked        = -1
	maximumHeight  = 100000
	directionCount = 2 * 2
)

type scanner struct {
	data     []byte
	position int
}

func (input *scanner) nextInt() int {
	for input.position < len(input.data) && input.data[input.position] <= ' ' {
		input.position++
	}
	value := 0
	for input.position < len(input.data) && input.data[input.position] >= '0' {
		value = value*10 + int(input.data[input.position]-'0')
		input.position++
	}
	return value
}

func canEscape(height, water []int, offsets [directionCount]int, start, jump, infinity int) bool {
	if water[start] == infinity {
		return true
	}
	distance := make([]int, len(height))
	for index := range distance {
		distance[index] = blocked
	}
	queue := make([]int, len(height))
	head, tail := 0, 1
	queue[0] = start
	distance[start] = 0
	for head < tail {
		current := queue[head]
		head++
		arrival := distance[current] + 1
		for _, offset := range offsets {
			next := current + offset
			if height[next] == blocked || distance[next] != blocked ||
				height[next]-height[current] > jump || arrival >= water[next] {
				continue
			}
			if water[next] == infinity {
				return true
			}
			distance[next] = arrival
			queue[tail] = next
			tail++
		}
	}
	return false
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	rows, columns := input.nextInt(), input.nextInt()
	stride := columns + 2
	size := (rows + 2) * stride
	infinity := size + 1
	height := make([]int, size)
	for index := range height {
		height[index] = blocked
	}
	for row := 1; row <= rows; row++ {
		for column := 1; column <= columns; column++ {
			height[row*stride+column] = input.nextInt()
		}
	}
	row, column := input.nextInt(), input.nextInt()
	start := row*stride + column
	row, column = input.nextInt(), input.nextInt()
	source := row*stride + column
	offsets := [directionCount]int{-stride, -1, 1, stride}
	water := make([]int, size)
	for index := range water {
		water[index] = infinity
	}
	queue := make([]int, size)
	head, tail := 0, 1
	queue[0] = source
	water[source] = 0
	for head < tail {
		current := queue[head]
		head++
		for _, offset := range offsets {
			next := current + offset
			if height[next] == blocked || height[next] > height[current] ||
				water[next] != infinity {
				continue
			}
			water[next] = water[current] + 1
			queue[tail] = next
			tail++
		}
	}
	if !canEscape(height, water, offsets, start, maximumHeight, infinity) {
		fmt.Println(-1)
		return
	}
	low, high := 0, maximumHeight
	for low < high {
		middle := low + (high-low)/2
		if canEscape(height, water, offsets, start, middle, infinity) {
			high = middle
		} else {
			low = middle + 1
		}
	}
	fmt.Println(low)
}
