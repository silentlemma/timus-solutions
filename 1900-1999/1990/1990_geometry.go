package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"sort"
)

type point struct{ x, y int64 }
type reader struct {
	data     []byte
	position int
}

func (r *reader) number() int64 {
	for r.position < len(r.data) && r.data[r.position] <= ' ' {
		r.position++
	}
	sign := int64(1)
	if r.data[r.position] == '-' {
		sign = -1
		r.position++
	}
	value := int64(0)
	for r.position < len(r.data) && r.data[r.position] > ' ' {
		value = value*10 + int64(r.data[r.position]-'0')
		r.position++
	}
	return sign * value
}
func vertexClearance(vertices, other []point, sign int64) float64 {
	result := math.Inf(1)
	index := 0
	for _, p := range vertices {
		for index+1 < len(other) && other[index+1].y <= p.y {
			index++
		}
		var gap float64
		if index+1 == len(other) {
			gap = float64(sign * (other[index].x - p.x))
		} else {
			a, b := other[index], other[index+1]
			numerator := (a.x-p.x)*(b.y-p.y) + (b.x-p.x)*(p.y-a.y)
			gap = float64(sign*numerator) / float64(b.y-a.y)
		}
		if gap < result {
			result = gap
		}
	}
	return result
}
func fractionAt(vertices []point, index int, y int64) (int64, int64, int) {
	for index+1 < len(vertices) && vertices[index+1].y <= y {
		index++
	}
	if index+1 == len(vertices) {
		return vertices[index].x, 1, index
	}
	a, b := vertices[index], vertices[index+1]
	return a.x*(b.y-y) + b.x*(y-a.y), b.y - a.y, index
}
func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := reader{data: data}
	readWall := func() []point {
		count := int(input.number())
		wall := make([]point, count)
		for i := range wall {
			wall[i] = point{input.number(), input.number()}
		}
		return wall
	}
	left, right := readWall(), readWall()
	answer := math.Min(vertexClearance(left, right, 1), vertexClearance(right, left, -1))
	first, second := 0, 0
	group := make([]int64, 0)
	process := func(y int64) {
		if y < left[0].y || y > left[len(left)-1].y {
			return
		}
		var ln, ld, rn, rd int64
		ln, ld, first = fractionAt(left, first, y)
		rn, rd, second = fractionAt(right, second, y)
		sort.Slice(group, func(i, j int) bool { return group[i] < group[j] })
		found := false
		previous := int64(0)
		best := 0.0
		for _, x := range group {
			if x*ld < ln || x*rd > rn {
				continue
			}
			gap := float64(x - previous)
			if !found {
				gap = float64(x*ld-ln) / float64(ld)
			}
			if gap > best {
				best = gap
			}
			previous = x
			found = true
		}
		if found {
			gap := float64(rn-previous*rd) / float64(rd)
			if gap > best {
				best = gap
			}
			if best < answer {
				answer = best
			}
		}
	}
	count := int(input.number())
	currentY := int64(0)
	for i := 0; i < count; i++ {
		x, y := input.number(), input.number()
		if len(group) > 0 && y != currentY {
			process(currentY)
			group = group[:0]
		}
		currentY = y
		group = append(group, x)
	}
	if len(group) > 0 {
		process(currentY)
	}
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(output, "%.12f\n", answer)
	output.Flush()
}
