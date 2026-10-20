package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

const decimalScale int64 = 1000000000000
const precision = 12

type scanner struct {
	data  []byte
	index int
}

func (s *scanner) nextInt() int64 {
	for s.index < len(s.data) && s.data[s.index] <= ' ' {
		s.index++
	}
	negative := s.data[s.index] == '-'
	if negative {
		s.index++
	}
	var value int64
	for s.index < len(s.data) && s.data[s.index] >= '0' && s.data[s.index] <= '9' {
		value = value*10 + int64(s.data[s.index]-'0')
		s.index++
	}
	if negative {
		return -value
	}
	return value
}

type line struct {
	dx int64
	dy int64
	c  int64
}

func abs(value int64) int64 {
	if value < 0 {
		return -value
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	count := int(input.nextInt())
	lines := make([]line, count)
	for i := range lines {
		x1, y1 := input.nextInt(), input.nextInt()
		x2, y2 := input.nextInt(), input.nextInt()
		dx, dy := x2-x1, y2-y1
		if dx < 0 || dx == 0 && dy < 0 {
			dx, dy = -dx, -dy
		}
		lines[i] = line{dx: dx, dy: dy, c: dy*x1 - dx*y1}
	}

	sort.Slice(lines, func(i, j int) bool {
		return lines[i].dy*lines[j].dx < lines[j].dy*lines[i].dx
	})

	var bestNum int64
	bestDen := int64(1)
	// A farthest intersection belongs to neighboring directions in cyclic order.
	for i, a := range lines {
		b := lines[(i+1)%count]
		num := abs(a.dx*b.c-a.c*b.dx) + abs(a.dy*b.c-a.c*b.dy)
		den := abs(a.dx*b.dy - a.dy*b.dx)
		if num*bestDen > bestNum*den {
			bestNum, bestDen = num, den
		}
	}

	rounded := ((bestNum%bestDen)*decimalScale + bestDen/2) / bestDen
	answer := strconv.FormatInt(bestNum/bestDen+rounded/decimalScale, 10)
	remainder := rounded % decimalScale
	if remainder != 0 {
		fractional := strconv.FormatInt(remainder, 10)
		fractional = strings.Repeat("0", precision-len(fractional)) + fractional
		answer += "." + strings.TrimRight(fractional, "0")
	}
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, answer)
	output.Flush()
}
