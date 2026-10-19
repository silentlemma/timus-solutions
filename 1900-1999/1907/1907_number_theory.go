package main

import (
	"bufio"
	"fmt"
	"os"
)

const firstOddPrime int64 = 3

func coprimeCount(bound int64, index int, primes []int64, oddOnly bool) int64 {
	if bound == 0 {
		return 0
	}
	if index == len(primes) {
		if oddOnly {
			return (bound + 1) / 2
		}
		return bound
	}
	return coprimeCount(bound, index+1, primes, oddOnly) -
		coprimeCount(bound/primes[index], index+1, primes, oddOnly)
}

func countSizes(first, limit int64) int64 {
	oddPart := first
	for oddPart%2 == 0 {
		oddPart /= 2
	}
	var primes []int64
	for divisor := firstOddPrime; divisor*divisor <= oddPart; divisor += 2 {
		if oddPart%divisor == 0 {
			primes = append(primes, divisor)
			for oddPart%divisor == 0 {
				oddPart /= divisor
			}
		}
	}
	if oddPart > 1 {
		primes = append(primes, oddPart)
	}
	oddOnly := first%2 == 0
	bound := limit
	if !oddOnly {
		bound /= 2
	}
	return limit - coprimeCount(bound, 0, primes, oddOnly)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var first, limit int64
	fmt.Fscan(in, &first, &limit)
	fmt.Fprintln(out, countSizes(first, limit))
}
