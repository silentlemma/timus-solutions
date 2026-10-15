package main

import "fmt"

const (
	base = 10
	five = 5 // the last digit of one of the two endless solutions of x^2 = x
)

func main() {
	var n int
	fmt.Scan(&n)
	// x^2 ends with x exactly when x^2 = x mod 10^d for its d digits; besides
	// 0 and 1 the solutions are the endings of two 10-adic numbers, ...0625
	// and ...9376, whose digits other than the last add up to 9 place by place

	digits := []int{five}       // the 5-adic one, lowest digit first
	carry := five * five / base // carry into position d of the square so far
	for d := 1; d < n; d++ {
		// digit d of x^2: the products x_i x_j with i + j = d, plus the carry, and
		// a new digit c adds 2 * 5 * c, a multiple of 10: c is forced
		total := carry
		for i := 1; i < d; i++ {
			total += digits[i] * digits[d-i]
		}
		c := total % base
		digits = append(digits, c)
		carry = (total + 2*five*c) / base
	}
	count := 1 + 2 // the numbers 1, 5 and 6
	for d := 1; d < n; d++ {
		// a d + 1 digit number needs a nonzero leading digit
		if digits[d] != 0 {
			count++
		}
		if digits[d] != base-1 {
			count++
		}
	}
	fmt.Println(count)
}
