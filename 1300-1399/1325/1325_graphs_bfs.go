package main

import (
	"bufio"
	"os"
	"strconv"
)

const kindMask byte = 3
const visited byte = 4
const directions = 8
const decimalBase = 10
const outputReserve = 32
const unreachable = ^uint32(0)

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func answer(length int, changes uint32) {
	output := make([]byte, 0, outputReserve)
	output = strconv.AppendInt(output, int64(length), decimalBase)
	output = append(output, ' ')
	output = strconv.AppendUint(output, uint64(changes), decimalBase)
	output = append(output, '\n')
	os.Stdout.Write(output)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	n, m := number(in), number(in)
	sr, sc, tr, tc := number(in), number(in), number(in), number(in)
	width := m + 2
	field := make([]byte, (n+2)*width)
	for row := 1; row <= n; row++ {
		for col := 1; col <= m; col++ {
			c, _ := in.ReadByte()
			for c < '0' || c > '2' {
				c, _ = in.ReadByte()
			}
			field[row*width+col] = c - '0'
		}
	}
	start, target := sr*width+sc, tr*width+tc
	if start == target {
		answer(1, 0)
		return
	}
	moves := [directions]int{-width - 1, -width, -width + 1, -1, 1, width - 1, width, width + 1}
	distance := make([]uint32, len(field))
	for cell := range distance {
		distance[cell] = unreachable
	}
	distance[start] = 0
	queue := make([]uint32, 2*n*m+1)
	first, last := 0, 1
	queue[0] = uint32(start)
	for first != last {
		cell := int(queue[first])
		first++
		if first == len(queue) {
			first = 0
		}
		if field[cell]&visited != 0 {
			continue
		}
		kind := field[cell] & kindMask
		field[cell] |= visited
		for _, move := range moves {
			near := cell + move
			object := field[near]
			if object == 0 || object&visited != 0 {
				continue
			}
			cost := uint32(0)
			if object != kind {
				cost = 1
			}
			value := distance[cell] + cost
			if value >= distance[near] {
				continue
			}
			distance[near] = value
			if cost == 0 {
				if first == 0 {
					first = len(queue)
				}
				first--
				queue[first] = uint32(near)
			} else {
				queue[last] = uint32(near)
				last++
				if last == len(queue) {
					last = 0
				}
			}
		}
	}
	if distance[target] == unreachable {
		answer(0, 0)
		return
	}
	for cell := range field {
		field[cell] &= kindMask
	}
	queue[0] = uint32(start)
	field[start] |= visited
	head, tail, length := 0, 1, 1
	for head < tail {
		end := tail
		for head < end {
			cell := int(queue[head])
			head++
			if cell == target {
				answer(length, distance[target])
				return
			}
			kind := field[cell] & kindMask
			for _, move := range moves {
				near := cell + move
				object := field[near]
				if object == 0 || object&visited != 0 {
					continue
				}
				cost := uint32(0)
				if object != kind {
					cost = 1
				}
				if distance[near] == distance[cell]+cost {
					field[near] |= visited
					queue[tail] = uint32(near)
					tail++
				}
			}
		}
		length++
	}
}
