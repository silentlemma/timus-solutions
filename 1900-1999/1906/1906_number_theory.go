package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const maxValue int64 = 1000000000

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

func extendedGCD(a, b int64) (int64, int64, int64) {
	x, nextX, y, nextY := int64(1), int64(0), int64(0), int64(1)
	for b != 0 {
		quotient := a / b
		a, b = b, a-quotient*b
		x, nextX = nextX, x-quotient*nextX
		y, nextY = nextY, y-quotient*nextY
	}
	return a, x, y
}

func largestModulus(d, e, constraint int64) int64 {
	if e%gcd(d, constraint) == 0 {
		return constraint
	}
	common := gcd(constraint, e)
	remaining, forbidden := constraint/common, d/gcd(d, e)
	for {
		divisor := gcd(remaining, forbidden)
		if divisor == 1 {
			return common * remaining
		}
		remaining /= divisor
	}
}

func witness(length int, d, e, constraint int64) (int, int64, int64) {
	modulus := d*maxValue + 1
	if constraint != 0 {
		modulus = largestModulus(d, e, constraint)
	}
	common := gcd(d, modulus)
	reduced := modulus / common
	multiplier := int64(0)
	if reduced != 1 {
		mod := big.NewInt(reduced)
		inverse := new(big.Int).ModInverse(big.NewInt(d/common), mod)
		product := new(big.Int).Mul(big.NewInt(e/common), inverse)
		multiplier = product.Mod(product, mod).Int64()
	}
	return length, modulus, multiplier
}

func solve(values []int64) (int, int64, int64) {
	n := len(values)
	if values[0] == 0 {
		length := 0
		for length < n && values[length] == 0 {
			length++
		}
		return length, 1, 0
	}
	if n == 1 {
		return 1, values[0] + 1, 0
	}
	d, e, constraint := values[0], values[1], int64(0)
	largest := d
	if e > largest {
		largest = e
	}
	length := 2
	for index := 1; index < n-1; index++ {
		a, b := values[index], values[index+1]
		if a == 0 {
			if b != 0 {
				break
			}
			length = index + 2
			continue
		}
		divisor := gcd(d, a)
		nextE := big.NewInt(e)
		if divisor != d {
			_, x, y := extendedGCD(d, a)
			nextE.Mul(big.NewInt(x), big.NewInt(e))
			nextE.Add(nextE, new(big.Int).Mul(big.NewInt(y), big.NewInt(b)))
		}
		// The determinant can exceed signed 64-bit range before taking its gcd.
		determinant := new(big.Int).Mul(big.NewInt(d/divisor), big.NewInt(b))
		determinant.Sub(determinant, new(big.Int).Mul(big.NewInt(a/divisor), big.NewInt(e)))
		nextConstraint := new(big.Int).GCD(nil, nil, big.NewInt(constraint), determinant).Int64()
		if nextConstraint != 0 {
			nextE.Mod(nextE, big.NewInt(nextConstraint))
		}
		nextValue, nextLargest := nextE.Int64(), largest
		if b > nextLargest {
			nextLargest = b
		}
		if nextConstraint != 0 && largestModulus(divisor, nextValue, nextConstraint) <= nextLargest {
			break
		}
		d, e, constraint = divisor, nextValue, nextConstraint
		largest, length = nextLargest, index+2
	}
	return witness(length, d, e, constraint)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(in, &count)
	values := make([]int64, count)
	for i := range values {
		fmt.Fscan(in, &values[i])
	}
	length, modulus, multiplier := solve(values)
	fmt.Println(length, modulus, multiplier)
}
