package main

import "syscall"

const maxPoints = 200
const inputSize = 512
const decimal = 10

type point struct{ x, y int16 }
type segment struct {
	left, right point
	low, high   int16
}

var input [inputSize]byte
var offset, length int
var points [maxPoints]point
var segments [maxPoints]segment
var endpoint [maxPoints]bool

func nextByte() byte {
	if offset == length {
		for {
			size, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if size <= 0 || err != nil {
				return 0
			}
			length = size
			break
		}
		offset = 0
	}
	value := input[offset]
	offset++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign, c = -1, nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = decimal*value + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

func (s segment) side(p point) int64 {
	dx := int64(s.right.x) - int64(s.left.x)
	dy := int64(s.right.y) - int64(s.left.y)
	return dx*(int64(p.y)-int64(s.left.y)) - dy*(int64(p.x)-int64(s.left.x))
}

func (s segment) spans(t segment) bool {
	a, b := s.side(t.left), s.side(t.right)
	return a <= 0 && b >= 0 || b <= 0 && a >= 0
}

func (s segment) meets(t segment) bool {
	return s.left.x <= t.right.x && t.left.x <= s.right.x &&
		s.low <= t.high && t.low <= s.high && s.spans(t) && t.spans(s)
}

func onNetwork(p point, tracks []segment) bool {
	for _, s := range tracks {
		if s.left.x <= p.x && p.x <= s.right.x && s.low <= p.y && p.y <= s.high && s.side(p) == 0 {
			return true
		}
	}
	return false
}

func connected(n, m int) bool {
	for i, p := range points[:n] {
		if !endpoint[i] && !onNetwork(p, segments[:m]) {
			return false
		}
	}
	// The prefix holds segments reached by BFS. Move newly discovered
	// segments into it, so no later search compares two reached segments.
	reached := 1
	for head := 0; head < reached && reached < m; head++ {
		for i := reached; i < m; i++ {
			if segments[head].meets(segments[i]) {
				segments[i], segments[reached] = segments[reached], segments[i]
				reached++
			}
		}
	}
	return reached == m
}

func main() {
	n, m := number(), number()
	for i := range points[:n] {
		points[i] = point{int16(number()), int16(number())}
	}
	for i := range segments[:m] {
		a, b := number()-1, number()-1
		endpoint[a], endpoint[b] = true, true
		left, right := points[a], points[b]
		if left.x > right.x {
			left, right = right, left
		}
		low, high := left.y, right.y
		if low > high {
			low, high = high, low
		}
		segments[i] = segment{left, right, low, high}
	}
	if connected(n, m) {
		writeOutput("YES\n")
	} else {
		writeOutput("NO\n")
	}
}

func writeOutput(text string) {
	data := []byte(text)
	for len(data) != 0 {
		written, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if written <= 0 || err != nil {
			return
		}
		data = data[written:]
	}
}
