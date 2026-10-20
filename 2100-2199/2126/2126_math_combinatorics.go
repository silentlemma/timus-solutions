package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const CHOICES int64 = 3

func modPow(base, exponent, modulus int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent%2 == 1 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent /= 2
	}
	return result
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, p int64
	fmt.Fscan(in, &n, &p)

	half := (p - 1) / 2
	exponent := int64(0)
	digits := make([]int64, 0)
	for remaining := n; remaining > 0; remaining /= p {
		digit := remaining % p
		// Reflect upper digits to keep the recurrence below half the modulus.
		if digit > half {
			digit = p - 1 - digit
			exponent += half - digit
		}
		digits = append(digits, digit)
	}
	sort.Slice(digits, func(i, j int) bool { return digits[i] < digits[j] })

	index, previous, current, factorial := int64(0), int64(1), int64(1), int64(1)
	numerator, denominator := int64(1), int64(1)
	for _, digit := range digits {
		for index < digit {
			index++
			// Scaling the central coefficient by index! avoids modular division.
			next := ((2*index-1)*current + CHOICES*(index-1)*(index-1)*previous) % p
			previous, current = current, next
			factorial = factorial * index % p
		}
		numerator = numerator * current % p
		denominator = denominator * factorial % p
	}

	draws := numerator * modPow(denominator, p-2, p) % p
	draws = draws * modPow(p-CHOICES, exponent, p) % p
	answer := (modPow(CHOICES, n, p) - draws + p) % p
	answer = answer * ((p + 1) / 2) % p
	fmt.Println(answer)
}
