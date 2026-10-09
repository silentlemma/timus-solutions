package main

import "fmt"

const positions = 32

var binom [positions + 1][positions + 1]int64

// countUpto counts the numbers in [0, n] that are sums of exactly k different
// powers of b, that is, have only digits 0 and 1 in base b with k ones
func countUpto(n int64, k, b int) int64 {
	var digits []int
	for ; n > 0; n /= int64(b) {
		digits = append(digits, int(n%int64(b)))
	}
	// a digit above 1 lets every smaller number with 0/1 digits through: it
	// and all digits after it may as well be 1
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] > 1 {
			for j := i; j >= 0; j-- {
				digits[j] = 1
			}
			break
		}
	}
	// count 0/1 strings with k ones not above the digits, from the top
	var total int64
	ones := 0
	for i := len(digits) - 1; i >= 0 && ones <= k; i-- {
		if digits[i] == 1 {
			if k-ones <= i {
				total += binom[i][k-ones]
			}
			ones++
		}
	}
	if ones == k {
		total++
	}
	return total
}

func main() {
	for i := 0; i <= positions; i++ {
		binom[i][0] = 1
		for j := 1; j <= i; j++ {
			binom[i][j] = binom[i-1][j-1]
			if j < i {
				binom[i][j] += binom[i-1][j]
			}
		}
	}
	var x, y int64
	var k, b int
	fmt.Scan(&x, &y, &k, &b)
	fmt.Println(countUpto(y, k, b) - countUpto(x-1, k, b))
}
