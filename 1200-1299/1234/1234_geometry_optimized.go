package main

import "syscall"

const decimal = 10
const inputBufferSize = 128

type byteInput struct {
	data      [inputBufferSize]byte
	next, end int
}

func (input *byteInput) readByte() byte {
	for input.next == input.end {
		size, err := syscall.Read(syscall.Stdin, input.data[:])
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return 0
		}
		input.next, input.end = 0, size
	}
	value := input.data[input.next]
	input.next++
	return value
}

func tenths(input *byteInput) int64 {
	ch := input.readByte()
	for ch != 0 && ch <= ' ' {
		ch = input.readByte()
	}
	var whole int64
	for ch >= '0' && ch <= '9' {
		whole = whole*decimal + int64(ch-'0')
		ch = input.readByte()
	}
	if ch == '.' {
		fraction := input.readByte()
		if fraction >= '0' && fraction <= '9' {
			return whole*decimal + int64(fraction-'0')
		}
	}
	return whole * decimal
}

func square(x int64) int64 { return x * x }

func fits(q, p, b, a int64) bool {
	if q > b {
		return false
	}
	if p <= a {
		return true
	}
	sum, difference := square(p+q), square(p-q)
	return square(a+b)*difference+square(a-b)*sum >= 2*sum*difference
}

func main() {
	input := &byteInput{}
	q, p, third := tenths(input), tenths(input), tenths(input)
	if q > p {
		q, p = p, q
	}
	if third < q {
		q, p = third, q
	} else if third < p {
		p = third
	}
	b, a := tenths(input), tenths(input)
	if b > a {
		b, a = a, b
	}
	answer := []byte("NO\n")
	if fits(q, p, b, a) {
		answer = []byte("YES\n")
	}
	for len(answer) > 0 {
		size, err := syscall.Write(syscall.Stdout, answer)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		answer = answer[size:]
	}
}
