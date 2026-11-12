package main

import "syscall"

func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

const inputSize = 32

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 64

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	used += copy(output[used:], digits[first:])
}

const mod uint32 = 1000000007
const byteBits = 8

func main() {
	n := number()
	fib := make([]uint32, n+1)
	fib[1] = 1
	for i := 2; i <= n; i++ {
		value := fib[i-1] + fib[i-2]
		if value >= mod {
			value -= mod
		}
		fib[i] = value
	}
	composite := make([]byte, (n/2+byteBits)/byteBits)
	answer := uint64(1)
	for p := 2; p <= n; {
		odd := p / 2
		if p == 2 || composite[odd/byteBits]>>uint(odd%byteBits)&1 == 0 {
			if p != 2 && p <= n/p {
				for multiple := p * p; multiple <= n; multiple += 2 * p {
					index := multiple / 2
					composite[index/byteBits] |= byte(1) << uint(index%byteBits)
				}
			}
			exponent := uint64(0)
			for power := p; power <= n; {
				for k := power; k <= n; k += power {
					exponent += uint64(fib[n-k+1])
				}
				if power > n/p {
					break
				}
				power *= p
			}
			answer = answer * (exponent%uint64(mod) + 1) % uint64(mod)
		}
		if p == 2 {
			p++
		} else {
			p += 2
		}
	}
	writeNumber(int(answer))
	output[used] = '\n'
	used++
	writeAll(output[:used])
}
