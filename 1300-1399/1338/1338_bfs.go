package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	south, north, west, east = 0, 1, 2, 3 // also the order cars prefer
	sides                    = 4
	buffer                   = 1 << 20
)

func main() {
	in := bufio.NewReaderSize(os.Stdin, buffer)
	readLine := func() string {
		s, _ := in.ReadString('\n')
		return strings.TrimRight(s, "\r\n")
	}
	head := strings.Fields(readLine())
	w, _ := strconv.Atoi(head[0])
	h, _ := strconv.Atoi(head[1])
	width := w + 2
	// the plan with a frame of buildings, as one flat array
	rows := make([]string, h)
	road := make([]bool, width*(h+2))
	for r := range rows {
		row := readLine()
		if len(row) < w {
			row += strings.Repeat(".", w-len(row))
		}
		rows[r] = row[:w]
		for c := 0; c < w; c++ {
			road[(r+1)*width+c+1] = rows[r][c] == '#' || rows[r][c] == 'o'
		}
	}
	// control points numbered from the bottom row up, left to right
	var points []int
	for r := h - 1; r >= 0; r-- {
		for c := 0; c < w; c++ {
			if rows[r][c] == 'o' {
				points = append(points, (r+1)*width+c+1)
			}
		}
	}
	steps := [sides]int{width, -width, -1, 1} // south, north, west, east
	var rest []string
	for {
		line, err := in.ReadString('\n')
		rest = append(rest, strings.Fields(line)...)
		if err != nil {
			break
		}
	}
	m := 0
	if len(rest) > 0 {
		m, _ = strconv.Atoi(rest[0])
	}
	dist, side := make([]int, len(road)), make([]int, len(road))
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for number := 1; number <= m; number++ {
		target, _ := strconv.Atoi(rest[number])
		goal := points[target-1]
		for i := range dist {
			dist[i] = -1
		}
		dist[goal] = 0
		order := []int{goal}
		for i := 0; i < len(order); i++ {
			cell := order[i]
			for _, step := range steps {
				near := cell + step
				if road[near] && dist[near] < 0 {
					dist[near] = dist[cell] + 1
					order = append(order, near)
				}
			}
		}
		// every cell inherits the side its car arrives from from the cell it
		// moves to; cells one step away arrive straight from their own side
		for _, cell := range order[1:] {
			for k, step := range steps {
				near := cell + step
				if dist[near] == dist[cell]-1 {
					if near == goal {
						side[cell] = k ^ 1 // the opposite side of the step onto the goal
					} else {
						side[cell] = side[near]
					}
					break
				}
			}
		}
		var counts [sides]int
		for _, p := range points {
			if p != goal && dist[p] > 0 {
				counts[side[p]]++
			}
		}
		fmt.Fprintf(out, "Experiment #%d: North: %d, South: %d, East: %d, West: %d\n",
			number, counts[north], counts[south], counts[east], counts[west])
	}
}
