package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const (
	limit         = 1 << 16
	maxFactors    = 6
	firstOddPrime = 3
	outputDigits  = 6
)

func power(base uint32, exponent int, modulus uint32) uint32 {
	result := uint32(1)
	for exponent != 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent >>= 1
	}
	return result
}

func largestRoot(prime int, factors []uint8) uint16 {
	order := prime - 1
	odd := order >> uint(bits.TrailingZeros(uint(order)))
	var storage [maxFactors]int
	powers := append(storage[:0], order/2)
	for odd > 1 {
		factor := int(factors[odd/2])
		if factor == 0 {
			factor = odd
		}
		powers = append(powers, order/factor)
		for odd%factor == 0 {
			odd /= factor
		}
	}
	for g := order; g >= 2; g-- {
		generator := true
		for _, exponent := range powers {
			if power(uint32(g), exponent, uint32(prime)) == 1 {
				generator = false
				break
			}
		}
		if generator {
			return uint16(g)
		}
	}
	return 0
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	next := func() int {
		input.Scan()
		value, _ := strconv.Atoi(input.Text())
		return value
	}
	count := next()
	factors := make([]uint8, limit/2)
	for p := firstOddPrime; p*p < limit; p += 2 {
		if factors[p/2] == 0 {
			for i := p * p / 2; i < len(factors); i += p {
				if factors[i] == 0 {
					factors[i] = uint8(p)
				}
			}
		}
	}

	known := make([]uint16, limit/2)
	output := bufio.NewWriter(os.Stdout)
	var digits [outputDigits]byte
	for i := 0; i < count; i++ {
		prime := next()
		if known[prime/2] == 0 {
			known[prime/2] = largestRoot(prime, factors)
		}
		line := strconv.AppendUint(digits[:0], uint64(known[prime/2]), 10)
		output.Write(append(line, '\n'))
	}
	output.Flush()
}
