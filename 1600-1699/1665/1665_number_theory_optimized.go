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

const inputSize = 8192

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

const maxTests = 100
const rootBound = 1 << 12
const firstOddPrime = 3

var composite [rootBound + 1]bool
var primes [rootBound / 2]uint16
var primeCount int

func preparePrimes() {
	for prime := firstOddPrime; prime*prime <= rootBound; prime += 2 {
		if !composite[prime] {
			for multiple := prime * prime; multiple <= rootBound; multiple += 2 * prime {
				composite[multiple] = true
			}
		}
	}
	for prime := firstOddPrime; prime <= rootBound; prime += 2 {
		if !composite[prime] {
			primes[primeCount] = uint16(prime)
			primeCount++
		}
	}
}

func eligible(value int) bool {
	twos := 0
	for value%2 == 0 {
		value /= 2
		twos++
	}
	if value == 1 {
		return twos%2 == 1
	}
	if twos%2 == 0 {
		return true
	}
	// Here a factor two was removed, so the odd residual is below 2^24 and its root below 4096.
	for _, small := range primes[:primeCount] {
		prime := int(small)
		if prime*prime > value {
			break
		}
		if value%prime == 0 {
			return true
		}
	}
	return false
}

func main() {
	tests := number()
	preparePrimes()
	var output [len("YES\n") * maxTests]byte
	used := 0
	for i := 0; i < tests; i++ {
		answer := "NO\n"
		if eligible(number()) {
			answer = "YES\n"
		}
		used += copy(output[used:], answer)
	}
	writeAll(output[:used])
}
