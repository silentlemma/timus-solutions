package main

import (
	"os"
)

const vertexCount = 4

type point struct{ x, y int64 }

func boundaryCount(points [vertexCount]point) int {
	var boundary [2 * vertexCount]point
	used := 0
	insert := func(p point) {
		for _, old := range boundary[:used] {
			if old == p {
				return
			}
		}
		boundary[used] = p
		used++
	}
	for shift := 0; shift < vertexCount; shift++ {
		var a, b point
		if shift%2 == 0 {
			first := shift / 2
			opposite := (first + 2) % vertexCount
			a = point{2 * points[first].x, 2 * points[first].y}
			b = point{2 * points[opposite].x, 2 * points[opposite].y}
		} else {
			a = point{points[0].x + points[shift].x, points[0].y + points[shift].y}
			remaining := [2]int{}
			count := 0
			for i := 0; i < vertexCount; i++ {
				if i != 0 && i != shift {
					remaining[count] = i
					count++
				}
			}
			p, q := points[remaining[0]], points[remaining[1]]
			b = point{p.x + q.x, p.y + q.y}
		}
		dx, dy := b.x-a.x, b.y-a.y
		if dx == 0 && dy == 0 {
			continue
		}
		valid := true
		for i, p := range points {
			q := points[(shift-i+vertexCount)%vertexCount]
			if (p.x+q.x-a.x)*dy != (p.y+q.y-a.y)*dx || (p.x-q.x)*dx+(p.y-q.y)*dy != 0 {
				valid = false
				break
			}
		}
		if valid {
			insert(a)
			insert(b)
		}
	}
	return used
}

func main() {
	var points [vertexCount]point
	for i := range points {
		points[i] = point{int64(integer()), int64(integer())}
	}
	writeInteger(boundaryCount(points))
}

const inputBufferBytes = 256

var inputBuffer [inputBufferBytes]byte
var inputPosition, inputLength int

// Keep only a bounded refill buffer and the current token; Read may return partial data.
// Refill a fixed byte buffer; EOF is separate from every possible input byte.
func nextByte() int {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(inputBuffer[:])
		inputPosition = 0
		if inputLength == 0 {
			return -1
		}
	}
	ch := inputBuffer[inputPosition]
	inputPosition++
	return int(ch)
}

// Read the single input stream once and convert tokens without fmt reflection.
// Parse decimal input directly to avoid fmt's reflection and token allocations.
func integer() int {
	position, length := inputPosition, inputLength
	read := func() int {
		if position == length {
			inputPosition = position
			ch := nextByte()
			position, length = inputPosition, inputLength
			return ch
		}
		ch := int(inputBuffer[position])
		position++
		return ch
	}
	ch := read()
	for ch >= 0 && ch <= ' ' {
		ch = read()
	}
	negative := ch == '-'
	if negative || ch == '+' {
		ch = read()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		if negative {
			value = value*10 - (ch - '0')
		} else {
			value = value*10 + ch - '0'
		}
		ch = read()
	}
	if ch >= 0 {
		position--
	}
	inputPosition = position
	return value
}

// Reuse one output buffer; io.Writer cannot retain it after Write returns.
func writeBytes(data []byte) {
	for len(data) > 0 {
		count, err := os.Stdout.Write(data)
		if count > 0 {
			data = data[count:]
		}
		if err != nil || count == 0 {
			return
		}
	}
}
func appendInteger(out []byte, value int64) []byte {
	var buffer [24]byte
	at := len(buffer)
	negative := value < 0
	var magnitude uint64
	if negative {
		magnitude = uint64(-(value + 1)) + 1
	} else {
		magnitude = uint64(value)
	}
	for {
		at--
		buffer[at] = byte('0' + magnitude%10)
		magnitude /= 10
		if magnitude == 0 {
			break
		}
	}
	if negative {
		at--
		buffer[at] = '-'
	}
	return append(out, buffer[at:]...)
}
func writeInteger(value int) {
	var bytes [24]byte
	out := appendInteger(bytes[:0], int64(value))
	out = append(out, '\n')
	writeBytes(out)
}
