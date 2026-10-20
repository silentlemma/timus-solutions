package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	padding        = 2
	directionCount = 4
	walk           = 0
	jump           = 1
	drop           = 2
	climb          = 3
)

type inputReader struct {
	data []byte
	pos  int
}

func (in *inputReader) next() []byte {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	start := in.pos
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		in.pos++
	}
	return in.data[start:in.pos]
}

func (in *inputReader) number() int {
	value := 0
	for _, digit := range in.next() {
		value = value*10 + int(digit-'0')
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := inputReader{data: data}
	a, b, h := in.number(), in.number(), in.number()
	width := b + 2*padding
	rows := a + 2*padding
	plane := width * rows
	total := plane * (h + 2)
	air := make([]bool, total)
	for z := 1; z <= h; z++ {
		for x := 1; x <= a; x++ {
			row := in.next()
			base := z*plane + (x+1)*width + padding
			for y, cell := range row {
				air[base+y] = cell == '.'
			}
		}
	}
	readPosition := func() int {
		x, y, z := in.number(), in.number(), in.number()
		return z*plane + (x+1)*width + y + 1
	}
	start, goal := readPosition(), readPosition()
	stand := make([]bool, total)
	for id := plane; id < total; id++ {
		stand[id] = air[id] && !air[id-plane]
	}
	parent := make([]int, total)
	for id := range parent {
		parent[id] = -1
	}
	action := make([]byte, total)
	queue := make([]int, 1, total)
	queue[0] = start
	parent[start] = start
	deltas := [directionCount]int{-width, 1, width, -1}
	for head := 0; head < len(queue) && parent[goal] < 0; head++ {
		current := queue[head]
		for direction, delta := range deltas {
			near := current + delta
			if stand[near] && parent[near] < 0 {
				parent[near] = current
				action[near] = byte(walk*directionCount + direction)
				queue = append(queue, near)
			}
			target := near + delta
			if air[near] && air[near-plane] && stand[target] && parent[target] < 0 {
				parent[target] = current
				action[target] = byte(jump*directionCount + direction)
				queue = append(queue, target)
			}
			target = near - plane
			if air[near] && stand[target] && parent[target] < 0 {
				parent[target] = current
				action[target] = byte(drop*directionCount + direction)
				queue = append(queue, target)
			}
			target = near + plane
			if air[current+plane] && stand[target] && parent[target] < 0 {
				parent[target] = current
				action[target] = byte(climb*directionCount + direction)
				queue = append(queue, target)
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if parent[goal] < 0 {
		fmt.Fprintln(out, "NO")
		return
	}
	path := make([]byte, 0)
	for id := goal; id != start; id = parent[id] {
		path = append(path, action[id])
	}
	fmt.Fprintln(out, "YES")
	fmt.Fprintln(out, len(path))
	moves := []string{"walk", "jump", "drop", "climb"}
	directions := []string{"north", "east", "south", "west"}
	for index := len(path) - 1; index >= 0; index-- {
		code := int(path[index])
		fmt.Fprintln(out, moves[code/directionCount], directions[code%directionCount])
	}
}
