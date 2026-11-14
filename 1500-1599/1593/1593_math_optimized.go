package main

import (
	"fmt"
	"math"
	"math/bits"
)

var bases = [...]uint64{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

const batch = 64
const maxCycle = 1 << 16

func multiply(a, b, n uint64) uint64 {
	high, low := bits.Mul64(a, b)
	_, rest := bits.Div64(high, low, n)
	return rest
}

func prime(n uint64) bool {
	for _, p := range bases {
		if n%p == 0 {
			return n == p
		}
	}
	twos := bits.TrailingZeros64(n - 1)
	odd := (n - 1) >> twos
	for _, a := range bases {
		value := uint64(1)
		for exponent := odd; exponent != 0; exponent >>= 1 {
			if exponent&1 != 0 {
				value = multiply(value, a, n)
			}
			a = multiply(a, a, n)
		}
		if value == 1 {
			continue
		}
		for i := 1; i < twos && value != n-1; i++ {
			value = multiply(value, value, n)
		}
		if value != n-1 {
			return false
		}
	}
	return true
}

func gcd(a, b uint64) uint64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func distance(a, b uint64) uint64 {
	if a < b {
		return b - a
	}
	return a - b
}

func divisor(n uint64) uint64 {
	for c := uint64(1); ; c++ {
		step := func(a uint64) uint64 { return (multiply(a, a, n) + c) % n }
		x, y, saved, factor := uint64(0), uint64(2), uint64(0), uint64(1)
		for size := 1; size <= maxCycle && factor == 1; size *= 2 {
			x = y
			for i := 0; i < size; i++ {
				y = step(y)
			}
			for start := 0; start < size && factor == 1; start += batch {
				saved = y
				product := uint64(1)
				for i := start; i < size && i < start+batch; i++ {
					y = step(y)
					product = multiply(product, distance(x, y), n)
				}
				factor = gcd(product, n)
			}
		}
		if factor == n {
			factor = 1
			for factor == 1 {
				saved = step(saved)
				factor = gcd(distance(x, saved), n)
			}
		}
		if factor > 1 && factor < n {
			return factor
		}
	}
}

func square(n uint64) bool {
	root := uint64(math.Sqrt(float64(n)))
	return root*root == n || (root+1)*(root+1) == n
}

const POWER_OF_FOUR = 4
const LEGENDRE_MODULUS = 8
const LEGENDRE_RESIDUE = 7
const TWO_SQUARE_OBSTRUCTION = 3
const THREE_SQUARES = 3
const FOUR_SQUARES = 4

func collect(n uint64, odd map[uint64]bool) {
	if square(n) {
		return
	}
	if prime(n) {
		if n%POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION {
			if odd[n] {
				delete(odd, n)
			} else {
				odd[n] = true
			}
		}
		return
	}
	part := divisor(n)
	collect(part, odd)
	collect(n/part, odd)
}

func solve(n uint64) int {
	if square(n) {
		return 1
	}
	for n%POWER_OF_FOUR == 0 {
		n /= POWER_OF_FOUR
	}
	if n%LEGENDRE_MODULUS == LEGENDRE_RESIDUE {
		return FOUR_SQUARES
	}
	if n%2 == 0 {
		n /= 2
	}
	if n%POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION {
		return THREE_SQUARES
	}
	for _, p := range bases {
		odd := false
		for n%p == 0 {
			n /= p
			odd = !odd
		}
		if odd && p%POWER_OF_FOUR == TWO_SQUARE_OBSTRUCTION {
			return THREE_SQUARES
		}
	}
	odd := make(map[uint64]bool)
	collect(n, odd)
	if len(odd) != 0 {
		return THREE_SQUARES
	}
	return 2
}

func main() {
	var n uint64
	if _, err := fmt.Scan(&n); err == nil {
		fmt.Println(solve(n))
	}
}
