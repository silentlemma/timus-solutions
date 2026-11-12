package main

import "syscall"

const (
	base          = 10
	eleven        = 11
	maxDigits     = 10
	maxCandidates = 2 * maxDigits
	inputSize     = 64
	outputSize    = 1024
)

var input [inputSize]byte
var position, available int

func readByte() byte {
	for position == available {
		count, err := syscall.Read(syscall.Stdin, input[:])
		if count > 0 {
			position, available = 0, count
			break
		}
		if err != syscall.EINTR {
			return 0
		}
	}
	c := input[position]
	position++
	return c
}

func readNumber() int64 {
	c := readByte()
	for c != 0 && c <= ' ' {
		c = readByte()
	}
	var n int64
	for c >= '0' && c <= '9' {
		n = n*base + int64(c-'0')
		c = readByte()
	}
	return n
}

func appendNumber(output []byte, n int64) []byte {
	var digits [maxDigits]byte
	start := len(digits)
	for {
		start--
		digits[start] = '0' + byte(n%base)
		n /= base
		if n == 0 {
			break
		}
	}
	return append(output, digits[start:]...)
}

func main() {
	n := readNumber()
	var found [maxCandidates]int64
	count := 0
	for power := int64(1); power <= n; power *= base {
		for carry := int64(0); carry < 2; carry++ {
			twice := n%power + carry*power
			if twice%2 != 0 || twice/2 >= power {
				continue
			}
			tail, q := twice/2, (n-twice)/power
			prefix, digit := q/eleven, q%eleven
			x := (prefix*base+digit)*power + tail
			if digit >= base || x < base || prefix == 0 && digit == 0 {
				continue
			}
			position := 0
			for position < count && found[position] < x {
				position++
			}
			if position < count && found[position] == x {
				continue
			}
			// At most two candidates per decimal place.
			copy(found[position+1:count+1], found[position:count])
			found[position] = x
			count++
		}
	}

	var buffer [outputSize]byte
	output := appendNumber(buffer[:0], int64(count))
	output = append(output, '\n')
	for _, x := range found[:count] {
		output = appendNumber(output, x)
		output = append(output, " + "...)
		width := 0
		for value := x / base; value > 0; value /= base {
			width++
		}
		y := n - x
		var digits [maxDigits]byte
		for i := width - 1; i >= 0; i-- {
			digits[i] = '0' + byte(y%base)
			y /= base
		}
		output = append(output, digits[:width]...)
		output = append(output, " = "...)
		output = appendNumber(output, n)
		output = append(output, '\n')
	}
	for len(output) > 0 {
		count, err := syscall.Write(syscall.Stdout, output)
		if count > 0 {
			output = output[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			break
		}
	}
}
