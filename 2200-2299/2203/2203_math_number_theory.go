package main

import (
	"bufio"
	"fmt"
	"os"
)

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func inverse(value, modulus int64) int64 {
	if modulus == 1 {
		return 0
	}
	oldR, r := value, modulus
	oldCoefficient, coefficient := int64(1), int64(0)
	for r != 0 {
		quotient := oldR / r
		oldR, r = r, oldR-quotient*r
		oldCoefficient, coefficient = coefficient, oldCoefficient-quotient*coefficient
	}
	result := oldCoefficient % modulus
	if result < 0 {
		result += modulus
	}
	return result
}

func visits(a, b, x, y, n int64) int64 {
	if x <= a || y <= b {
		return n
	}
	breadDivisor, sausageDivisor := gcd(x, a), gcd(y, b)
	breadPeriod, breadCount := x/breadDivisor, a/breadDivisor
	sausagePeriod, sausageCount := y/sausageDivisor, b/sausageDivisor
	commonDivisor := gcd(breadPeriod, sausagePeriod)
	modulus := sausagePeriod / commonDivisor
	coefficient := inverse(breadPeriod/commonDivisor, modulus)
	period := breadPeriod * modulus
	answer := (n*a+x-1)/x + (n*b+y-1)/y

	// Each ingredient has a few purchase residues in its repeating period.
	for i := int64(0); i < breadCount; i++ {
		breadResidue := i * breadPeriod / breadCount
		for j := int64(0); j < sausageCount; j++ {
			sausageResidue := j * sausagePeriod / sausageCount
			difference := sausageResidue - breadResidue
			if difference%commonDivisor != 0 {
				continue
			}
			// CRT gives the first simultaneous purchase for this residue pair.
			step := difference / commonDivisor * coefficient % modulus
			if step < 0 {
				step += modulus
			}
			first := breadResidue + breadPeriod*step
			if first < n {
				answer -= 1 + (n-1-first)/period
			}
		}
	}
	return answer
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var a, b, x, y, n int64
	fmt.Fscan(reader, &a, &b, &x, &y, &n)
	fmt.Println(visits(a, b, x, y, n))
}
