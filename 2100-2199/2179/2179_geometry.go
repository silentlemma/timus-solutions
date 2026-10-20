package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const TRIANGLE_SIDES = 3

type point struct {
	x, y int64
}

type scanner struct {
	data []byte
	pos  int
}

func (s *scanner) nextInt() int64 {
	for s.pos < len(s.data) && s.data[s.pos] <= ' ' {
		s.pos++
	}
	sign := int64(1)
	if s.data[s.pos] == '-' {
		sign = -1
		s.pos++
	}
	value := int64(0)
	for s.pos < len(s.data) && s.data[s.pos] >= '0' && s.data[s.pos] <= '9' {
		value = value*10 + int64(s.data[s.pos]-'0')
		s.pos++
	}
	return sign * value
}

func cross(a, b, c point) int64 {
	return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
}

func chainLength(points []point, reverse bool) int {
	chain := make([]point, 0, len(points))
	for step := range points {
		index := step
		if reverse {
			index = len(points) - 1 - step
		}
		current := points[index]
		for len(chain) >= 2 && cross(chain[len(chain)-2], chain[len(chain)-1], current) < 0 {
			chain = chain[:len(chain)-1]
		}
		chain = append(chain, current)
	}
	return len(chain)
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	n := int(input.nextInt())
	points := make([]point, n)
	for i := range points {
		points[i] = point{input.nextInt(), input.nextInt()}
	}
	sort.Slice(points, func(i, j int) bool {
		return points[i].x < points[j].x ||
			(points[i].x == points[j].x && points[i].y < points[j].y)
	})

	// Keeping collinear points also gives the correct count for a single line.
	boundary := chainLength(points, false) + chainLength(points, true) - 2
	fmt.Println(TRIANGLE_SIDES*n - TRIANGLE_SIDES - boundary)
}
