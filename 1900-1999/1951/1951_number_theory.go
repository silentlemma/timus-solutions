package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	sieveLimit   = 10000
	lowerModulus = 5000
	modulusCount = 510
)

type complexPair struct {
	real, imaginary int64
}

func primeModuli() []int64 {
	prime := make([]bool, sieveLimit+1)
	for index := 2; index <= sieveLimit; index++ {
		prime[index] = true
	}
	for value := 2; value*value <= sieveLimit; value++ {
		if prime[value] {
			for multiple := value * value; multiple <= sieveLimit; multiple += value {
				prime[multiple] = false
			}
		}
	}
	result := make([]int64, 0, modulusCount)
	for value := lowerModulus; value <= sieveLimit && len(result) < modulusCount; value++ {
		if prime[value] {
			result = append(result, int64(value))
		}
	}
	return result
}

var moduli = primeModuli()

func normalize(value, modulus int64) int64 {
	remainder := value % modulus
	if remainder < 0 {
		remainder += modulus
	}
	return remainder
}

func multiply(first, second complexPair, modulus int64) complexPair {
	return complexPair{
		normalize(first.real*second.real-first.imaginary*second.imaginary, modulus),
		normalize(first.real*second.imaginary+first.imaginary*second.real, modulus),
	}
}

func power(real, imaginary int64, exponent int, modulus int64) complexPair {
	base := complexPair{normalize(real, modulus), normalize(imaginary, modulus)}
	result := complexPair{1, 0}
	for exponent > 0 {
		if exponent&1 != 0 {
			result = multiply(result, base, modulus)
		}
		base = multiply(base, base, modulus)
		exponent >>= 1
	}
	return result
}

func gcd(first, second int) int {
	for second != 0 {
		first, second = second, first%second
	}
	return first
}

func countRoots(a, b int64, n int, c, d int64, m int) int {
	common := gcd(n, m)
	for _, modulus := range moduli {
		if power(a, b, m/common, modulus) != power(c, d, n/common, modulus) {
			return 0
		}
	}
	return common
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var a, b, c, d int64
	var n, m int
	fmt.Fscan(in, &a, &b, &n, &c, &d, &m)
	fmt.Println(countRoots(a, b, n, c, d, m))
}
