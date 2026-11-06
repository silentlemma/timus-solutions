package main

import "syscall"

const (
	inputSize     = 64
	outputSize    = 1024
	maxDigits     = 10
	firstOddPrime = 3
)

var (
	bases         = [...]int64{2, 3, 5, 7}
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
)

// Use standard handles directly; retry interrupts and finish short writes.
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

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func nextInt() int64 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value int64
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func writeNumber(value int64) {
	var digits [maxDigits]byte
	position := len(digits)
	for {
		position--
		digits[position] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	for ; position < len(digits); position++ {
		output[outputLength] = digits[position]
		outputLength++
	}
}

func writeByte(value byte) {
	output[outputLength] = value
	outputLength++
}

func power(b, e, m int64) int64 {
	r := int64(1)
	b %= m
	for ; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % m
		}
		b = b * b % m
	}
	return r
}

func isPrime(n int64) bool {
	if n < 2 {
		return false
	}
	for _, b := range bases {
		if n%b == 0 {
			return n == b
		}
	}
	d, s := n-1, 0
	for d%2 == 0 {
		d /= 2
		s++
	}
	for _, b := range bases {
		x := power(b, d, n)
		if x == 1 || x == n-1 {
			continue
		}
		composite := true
		for i := 1; i < s && composite; i++ {
			x = x * x % n
			composite = x != n-1
		}
		if composite {
			return false
		}
	}
	return true
}

func twoPrimes(n int64) (int64, int64) {
	if n == 4 {
		return 2, 2
	}
	for p := int64(firstOddPrime); ; p += 2 {
		if isPrime(p) && isPrime(n-p) {
			return p, n - p
		}
	}
}

func split(n int64) (int64, int64, int64) {
	if isPrime(n) {
		return n, 0, 0
	}
	if n%2 == 0 {
		a, b := twoPrimes(n)
		return a, b, 0
	}
	if isPrime(n - 2) {
		return 2, n - 2, 0
	}
	// Fixing three leaves an even remainder for the final two primes.
	a, b := twoPrimes(n - firstOddPrime)
	return firstOddPrime, a, b
}

func main() {
	for queries := nextInt(); queries > 0; queries-- {
		a, b, c := split(nextInt())
		writeNumber(a)
		if b != 0 {
			writeByte(' ')
			writeNumber(b)
		}
		if c != 0 {
			writeByte(' ')
			writeNumber(c)
		}
		writeByte('\n')
	}
	writeAll(output[:outputLength])
}
