package main

import (
	"io/ioutil"
	"os"
	"strconv"
)

const firstOddPrime = 3

func smallestFactors(limit int) []uint16 {
	factors := make([]uint16, (limit+1)/2)
	for prime := firstOddPrime; prime <= limit/prime; prime += 2 {
		if factors[prime/2] != 0 {
			continue
		}
		for value := prime * prime; value <= limit; value += 2 * prime {
			if factors[value/2] == 0 {
				factors[value/2] = uint16(prime)
			}
		}
	}
	return factors
}

func largestFactor(value int, factors []uint16) int {
	if value%2 == 0 {
		value /= value & -value
		if value == 1 {
			return 2
		}
	}
	for factors[value/2] != 0 {
		value /= int(factors[value/2])
	}
	return value
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	nextInt := func() int {
		for position < len(data) && data[position] <= ' ' {
			position++
		}
		value := 0
		for position < len(data) && data[position] >= '0' && data[position] <= '9' {
			value = value*10 + int(data[position]-'0')
			position++
		}
		return value
	}
	count := nextInt()
	queries := make([][2]int, count)
	limit := 1
	for i := range queries {
		queries[i] = [2]int{nextInt(), nextInt()}
		for _, value := range queries[i] {
			if value > limit {
				limit = value
			}
		}
	}
	factors := smallestFactors(limit)
	var output []byte
	for _, pair := range queries {
		a, b := pair[0], pair[1]
		common := gcd(a, b)
		if common != 1 && a != b {
			// Shared factors survive exactly when they are at least this threshold.
			threshold := largestFactor(a/common, factors)
			other := largestFactor(b/common, factors)
			if other > threshold {
				threshold = other
			}
			if threshold > 2 {
				common /= common & -common
			}
			for common > 1 {
				prime := 2
				if common%2 != 0 {
					prime = int(factors[common/2])
					if prime == 0 {
						prime = common
					}
				}
				if prime >= threshold {
					break
				}
				common /= prime
			}
		}
		output = strconv.AppendInt(output, int64(common), 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
