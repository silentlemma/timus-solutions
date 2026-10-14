package main

import (
	"fmt"
	"math/big"
	"strconv"
	"strings"
)

const (
	total    = 1000
	maxOdd   = 100
	outcomes = 3
)

func decimal(token string) (*big.Int, int) {
	parts := strings.Split(strings.ToLower(token), "e")
	mantissa := parts[0]
	exponent := 0
	if len(parts) == 2 {
		exponent, _ = strconv.Atoi(parts[1])
	}
	scale := 0
	if point := strings.IndexByte(mantissa, '.'); point >= 0 {
		scale = len(mantissa) - point - 1
	}
	scale -= exponent
	value, _ := new(big.Int).SetString(strings.ReplaceAll(mantissa, ".", ""), 10)
	if scale < 0 {
		value.Mul(value, power(-scale))
		scale = 0
	}
	return value, scale
}

func power(scale int) *big.Int {
	return new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(scale)), nil)
}

func main() {
	numerator := big.NewInt(1)
	denominator := big.NewInt(0)
	for i := 0; i < outcomes; i++ {
		var token string
		fmt.Scan(&token)
		value, scale := decimal(token)
		denominator.Mul(denominator, value)
		denominator.Add(denominator, new(big.Int).Mul(numerator, power(scale)))
		numerator.Mul(numerator, value)
	}
	numerator.Mul(numerator, big.NewInt(total))
	// betting in proportion to 1 / k on every outcome pays the same whatever
	// happens, and any other split pays less on some outcome
	low, high := 0, total*maxOdd/outcomes+1
	for low+1 < high {
		middle := (low + high) / 2
		left := new(big.Int).Mul(numerator, big.NewInt(2))
		right := new(big.Int).Mul(denominator, big.NewInt(int64(2*middle-1)))
		if left.Cmp(right) >= 0 {
			low = middle
		} else {
			high = middle
		}
	}
	fmt.Println(low)
}
