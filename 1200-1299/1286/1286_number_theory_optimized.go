package main

import "syscall"

const inputBufferSize = 64

var input [inputBufferSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		for {
			count, err := syscall.Read(syscall.Stdin, input[:])
			if count > 0 {
				position, length = 0, count
				break
			}
			if err != syscall.EINTR {
				return 0
			}
		}
	}
	c := input[position]
	position++
	return c
}

func number() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	negative := c == '-'
	if negative || c == '+' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	if negative {
		return -value
	}
	return value
}

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

func reachable(p, q, dx, dy int64) bool {
	step := gcd(p, q)
	if step == 0 {
		return dx == 0 && dy == 0
	}
	if dx%step != 0 || dy%step != 0 {
		return false
	}
	parityStep := 2 * step
	return (p+q)%parityStep != 0 || (dx+dy)%parityStep == 0
}

func main() {
	p, q, x, y := number(), number(), number(), number()
	answer := []byte("NO\n")
	if reachable(p, q, number()-x, number()-y) {
		answer = []byte("YES\n")
	}
	for len(answer) > 0 {
		count, err := syscall.Write(syscall.Stdout, answer)
		if count > 0 {
			answer = answer[count:]
		}
		if count <= 0 && err != syscall.EINTR {
			break
		}
	}
}
