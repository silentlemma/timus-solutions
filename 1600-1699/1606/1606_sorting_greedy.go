package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const start = 100000
const decimalDigits = 5

func number(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && ch >= '0' && ch <= '9' {
		value = 10*value + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n := number(input)
	x := make([]int32, n+1)
	height := make([]uint16, start+1)
	for id := 1; id <= n; id++ {
		x[id] = int32(number(input))
		height[number(input)] = uint16(id)
	}
	path := make([]uint16, 0, n)
	right := false
	for y := start; y >= 0; y-- {
		id := height[y]
		if id == 0 {
			continue
		}
		count := len(path)
		if count == 0 {
			path = append(path, id)
			continue
		}
		step := x[id] > x[path[count-1]]
		// A step in the same direction moves the endpoint to the new extreme.
		if count == 1 || step != right {
			path = append(path, id)
		} else {
			path[count-1] = id
		}
		right = step
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, len(path))
	var digits [decimalDigits]byte
	for i, id := range path {
		if i != 0 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendUint(digits[:0], uint64(id), 10))
	}
	output.WriteByte('\n')
}
