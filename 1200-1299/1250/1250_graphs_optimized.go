package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const (
	sea     byte = 0
	land    byte = 1
	outside byte = 2
	barrier byte = 4
	decimal      = 10
	padding      = 4
)

func number(data []byte, cursor *int) int {
	pos := *cursor
	for pos < len(data) && data[pos] <= ' ' {
		pos++
	}
	value := 0
	for pos < len(data) && data[pos] >= '0' && data[pos] <= '9' {
		value = decimal*value + int(data[pos]-'0')
		pos++
	}
	*cursor = pos
	return value
}

func flood(cells []byte, stack []uint32, start int, steps []int, mask, want, mark byte) []uint32 {
	stack = append(stack[:0], uint32(start))
	cells[start] = mark
	for len(stack) > 0 {
		pos := int(stack[len(stack)-1])
		stack = stack[:len(stack)-1]
		for _, step := range steps {
			next := pos + step
			if cells[next]&mask == want {
				cells[next] = mark
				stack = append(stack, uint32(next))
			}
		}
	}
	return stack
}

func countIslands(data []byte) int {
	pos := 0
	width, height := number(data, &pos), number(data, &pos)
	x, y := number(data, &pos), number(data, &pos)
	// One ring is the exterior starting region and the other guards every step.
	stride := width + padding
	cells := make([]byte, stride*(height+padding))
	for col := 0; col < stride; col++ {
		cells[col] = barrier
		cells[len(cells)-stride+col] = barrier
	}
	for row := 1; row <= height+2; row++ {
		left := row * stride
		cells[left], cells[left+stride-1] = barrier, barrier
		cells[left+1], cells[left+stride-2] = outside, outside
	}
	for col := 1; col <= width+2; col++ {
		cells[stride+col], cells[len(cells)-2*stride+col] = outside, outside
	}
	for row := 2; row < height+2; row++ {
		for col := 2; col < width+2; col++ {
			for data[pos] != '#' && data[pos] != '.' {
				pos++
			}
			if data[pos] == '#' {
				cells[row*stride+col] = land
			}
			pos++
		}
	}
	four := [...]int{1, -1, stride, -stride}
	eight := [...]int{1, -1, stride, -stride, stride + 1, stride - 1, -stride + 1, -stride - 1}
	var stack []uint32
	start := (y+1)*stride + x + 1
	if cells[start] == sea {
		stack = flood(cells, stack, start, eight[:], land|outside|barrier, sea, barrier)
	}
	// The interior ring is now passable during the exterior flood.
	for i, cell := range cells {
		if cell == outside {
			cells[i] = sea
		}
	}
	stack = flood(cells, stack, stride+1, four[:], outside|barrier, sea, outside)
	count := 0
	for i, cell := range cells {
		if cell == land {
			count++
			stack = flood(cells, stack, i, four[:], land, land, barrier)
		}
	}
	return count
}

func main() {
	data, err := ioutil.ReadAll(os.Stdin)
	if err == nil {
		os.Stdout.WriteString(strconv.Itoa(countIslands(data)) + "\n")
	}
}
