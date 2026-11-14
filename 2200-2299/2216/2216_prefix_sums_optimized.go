package main

import (
	"bufio"
	"os"
	"strconv"
)

func number(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && ch >= '0' && ch <= '9' {
		value = value*10 + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	floors, elevators := number(input), number(input)
	if floors == 1 {
		os.Stdout.WriteString("-1\n")
		return
	}
	difference := make([]int32, floors)
	for i := 0; i < elevators; i++ {
		left, right := number(input), number(input)
		difference[left-1]++
		difference[right-1]--
	}
	// The final difference is beyond the last gap.
	load, best := int32(0), int32(elevators)
	for _, delta := range difference[:floors-1] {
		load += delta
		if load < best {
			best = load
		}
	}
	os.Stdout.WriteString(strconv.Itoa(int(best)) + "\n")
}
