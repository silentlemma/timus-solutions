package main

import "os"

const (
	maxFactor     = 178
	firstOddPrime = 3
	maxQueries    = 2000
	inputSize     = 512
	outputSize    = maxQueries * 6
	maxDigits     = 5
)

var (
	input         [inputSize]byte
	inputPosition int
	inputLength   int
	output        [outputSize]byte
	outputLength  int
)

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength, _ = os.Stdin.Read(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func nextInt() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return value
}

func writeNumber(value int) {
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
	output[outputLength] = '\n'
	outputLength++
}

func inverse(e, phi int) int {
	a, b := e, phi
	x, y := 1, 0
	for b != 0 {
		q := a / b
		a, b = b, a-q*b
		x, y = y, x-q*y
	}
	return (x + phi) % phi
}

func power(base, exponent, mod int) int {
	value := 1
	for base %= mod; exponent != 0; exponent >>= 1 {
		if exponent&1 != 0 {
			value = value * base % mod
		}
		base = base * base % mod
	}
	return value
}

func main() {
	var composite [maxFactor + 1]bool
	var primes [maxFactor / 2]uint16
	count := 0
	for p := firstOddPrime; p <= maxFactor; p += 2 {
		if composite[p] {
			continue
		}
		primes[count] = uint16(p)
		count++
		for q := p * p; q <= maxFactor; q += 2 * p {
			composite[q] = true
		}
	}
	for queries := nextInt(); queries > 0; queries-- {
		e, n, c := nextInt(), nextInt(), nextInt()
		for _, prime := range primes[:count] {
			p := int(prime)
			if n%p != 0 {
				continue
			}
			phi := (p - 1) * (n/p - 1)
			writeNumber(power(c, inverse(e, phi), n))
			break
		}
	}
	os.Stdout.Write(output[:outputLength])
}
