package main

import (
	"bufio"
	"os"
	"strconv"
)

const maxRoute = 2000
const maxBuses = 1000

type bus struct {
	front, back, next uint16
}

func number(input *bufio.Reader) uint16 {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	var value uint16
	for err == nil && ch >= '0' && ch <= '9' {
		value = 10*value + uint16(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	count := number(input)
	var first [maxRoute + 1]uint16
	var buses [maxBuses + 1]bus
	for id := uint16(1); id <= count; id++ {
		front, back := number(input), number(input)
		buses[id] = bus{front, back, first[front]}
		first[front] = id
	}
	target, left, right := number(input), number(input), number(input)
	var predecessor [maxRoute + 1]uint16
	var seen [maxRoute + 1]bool
	var queue [maxRoute]uint16
	tail := 1
	queue[0], seen[left], seen[right] = left, true, true
	if left != right {
		queue[tail] = right
		tail++
	}
	// A swap makes the back route available using one more exchange.
	for head := 0; head < tail && !seen[target]; head++ {
		for id := first[queue[head]]; id != 0; id = buses[id].next {
			back := buses[id].back
			if !seen[back] {
				seen[back], predecessor[back] = true, id
				queue[tail] = back
				tail++
			}
		}
	}
	if !seen[target] {
		os.Stdout.WriteString("IMPOSSIBLE\n")
		return
	}
	var path [maxBuses]uint16
	length := 0
	for id := predecessor[target]; id != 0; id = predecessor[buses[id].front] {
		path[length] = id
		length++
	}
	out := bufio.NewWriter(os.Stdout)
	out.WriteString(strconv.Itoa(length))
	out.WriteByte('\n')
	for i := length - 1; i >= 0; i-- {
		out.WriteString(strconv.Itoa(int(path[i])))
		out.WriteByte('\n')
	}
	out.Flush()
}
