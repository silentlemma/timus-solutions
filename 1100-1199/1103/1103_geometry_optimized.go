package main

import (
	"math/bits"
	"os"
	"sort"
	"strconv"
)

const inputSize = 4096
const outputSize = 128

type input struct {
	bytes            [inputSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = os.Stdin.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}

func (in *input) number() int64 {
	c := in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	sign := int64(1)
	if c == '-' {
		sign = -1
		c = in.next()
	}
	value := int64(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = in.next()
	}
	return sign * value
}

type entry struct {
	x, y, dot int64
	area      uint64
}

func cross(o, a, b entry) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func angleBefore(a, b entry) bool {
	if a.dot < 0 && b.dot >= 0 {
		return false
	}
	if a.dot >= 0 && b.dot < 0 {
		return true
	}
	ad, bd := a.dot, b.dot
	negative := ad < 0
	if negative {
		ad = -ad
		bd = -bd
	}
	// Products can exceed64 bits; exact signed comparison needs two unsigned limbs.
	ah, al := bits.Mul64(uint64(ad), b.area)
	bh, bl := bits.Mul64(uint64(bd), a.area)
	if negative {
		return ah < bh || ah == bh && al < bl
	}
	return ah > bh || ah == bh && al > bl
}

type entries []entry

func (values entries) Len() int           { return len(values) }
func (values entries) Less(i, j int) bool { return angleBefore(values[i], values[j]) }
func (values entries) Swap(i, j int)      { values[i], values[j] = values[j], values[i] }

func selectMedian(values []entry, target int) entry {
	left, right := 0, len(values)-1
	depth := 2 * bits.Len(uint(len(values)))
	for left < right {
		if depth == 0 {
			sort.Sort(entries(values[left : right+1]))
			return values[target]
		}
		depth--
		a, b, c := values[left], values[(left+right)/2], values[right]
		if angleBefore(b, a) {
			a, b = b, a
		}
		if angleBefore(c, b) {
			b = c
		}
		if angleBefore(b, a) {
			b = a
		}
		pivot := b
		i, j := left, right
		for i <= j {
			for i <= right && angleBefore(values[i], pivot) {
				i++
			}
			for j >= left && angleBefore(pivot, values[j]) {
				j--
			}
			if i <= j {
				values[i], values[j] = values[j], values[i]
				i++
				j--
			}
		}
		if target <= j {
			right = j
		} else if target >= i {
			left = i
		} else {
			return values[target]
		}
	}
	return values[target]
}

func main() {
	var in input
	n := int(in.number())
	points := make([]entry, n)
	lowest := 0
	for i := range points {
		points[i].x, points[i].y = in.number(), in.number()
		if points[i].y < points[lowest].y ||
			points[i].y == points[lowest].y && points[i].x < points[lowest].x {
			lowest = i
		}
	}
	points[0], points[lowest] = points[lowest], points[0]
	a := points[0]
	next := 1
	for i := 2; i < n; i++ {
		if cross(a, points[next], points[i]) < 0 {
			next = i
		}
	}
	points[1], points[next] = points[next], points[1]
	b := points[1]
	others := points[2:]
	for i := range others {
		p := &others[i]
		p.dot = (a.x-p.x)*(b.x-p.x) + (a.y-p.y)*(b.y-p.y)
		p.area = uint64(cross(*p, a, b))
	}
	// The median angle has exactly half the remaining points on either side of its circle.
	c := selectMedian(others, len(others)/2)
	var buffer [outputSize]byte
	output := buffer[:0]
	for _, p := range []entry{a, b, c} {
		output = strconv.AppendInt(output, p.x, 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, p.y, 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
