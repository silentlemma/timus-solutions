package main

import (
	"math"
	"os"
	"sort"
	"strconv"
)

const (
	maxPoints  = 1000
	origin     = 10000
	fieldBits  = 15
	fieldMask  = 1<<fieldBits - 1
	inputSize  = 4096
	outputSize = 16
	decimal    = 10
)

type point uint32
type points []point

func (p point) x() int { return int(p >> fieldBits) }
func (p point) y() int { return int(p & fieldMask) }

func (p points) Len() int           { return len(p) }
func (p points) Less(i, j int) bool { return p[i] < p[j] }
func (p points) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

var input [inputSize]byte
var position, available int
var vertices, stack [maxPoints]point

func nextByte() byte {
	if position == available {
		available, _ = os.Stdin.Read(input[:])
		position = 0
		if available == 0 {
			return 0
		}
	}
	ch := input[position]
	position++
	return ch
}

func nextInt() int {
	ch := nextByte()
	for ch != 0 && ch <= ' ' {
		ch = nextByte()
	}
	sign := 1
	if ch == '-' {
		sign, ch = -1, nextByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = decimal*value + int(ch-'0')
		ch = nextByte()
	}
	return sign * value
}

func turn(a, b, c point) int {
	return (b.x()-a.x())*(c.y()-a.y()) - (b.y()-a.y())*(c.x()-a.x())
}

func chainLength(start, stop, step int) float64 {
	count := 0
	for i := start; i != stop; i += step {
		p := vertices[i]
		for count >= 2 && turn(stack[count-2], stack[count-1], p) <= 0 {
			count--
		}
		stack[count] = p
		count++
	}
	length := 0.0
	for i := 1; i < count; i++ {
		dx := stack[i].x() - stack[i-1].x()
		dy := stack[i].y() - stack[i-1].y()
		length += math.Sqrt(float64(dx*dx + dy*dy))
	}
	return length
}

func main() {
	size, gap := nextInt(), nextInt()
	for i := 0; i < size; i++ {
		x, y := nextInt()+origin, nextInt()+origin
		vertices[i] = point(x<<fieldBits | y)
	}
	sort.Sort(points(vertices[:size]))
	length := chainLength(0, size, 1) + chainLength(size-1, -1, -1) + 2*math.Pi*float64(gap)
	var output [outputSize]byte
	line := strconv.AppendInt(output[:0], int64(math.Round(length)), decimal)
	os.Stdout.Write(append(line, '\n'))
}
