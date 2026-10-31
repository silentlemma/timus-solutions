package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const maxSum = 1800
const limbDigits = 9
const base int64 = 1000000000

func main() {
	var n, k int
	fmt.Scan(&n, &k)
	// the answer is below 10^n and n < 1800, so fixed limb arrays suffice.
	var zero, other [maxSum/limbDigits + 1]int64
	// numbers of valid prefixes ending with a zero and with another digit,
	// where the first digit is not zero.
	other[0] = int64(k - 1)
	used := 1
	for i := 1; i < n; i++ {
		carry := int64(0)
		for j := 0; j < used; j++ {
			// k <= 10 keeps the intermediate below 18 * base, within int64.
			next := (zero[j]+other[j])*int64(k-1) + carry
			zero[j] = other[j]
			other[j] = next % base
			carry = next / base
		}
		if carry != 0 {
			other[used] = carry
			used++
		}
	}
	carry := int64(0)
	for j := 0; j < used; j++ {
		next := zero[j] + other[j] + carry
		other[j] = next % base
		carry = next / base
	}
	if carry != 0 {
		other[used] = carry
		used++
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.FormatInt(other[used-1], 10))
	for j := used - 2; j >= 0; j-- {
		limb := strconv.FormatInt(other[j], 10)
		for pad := len(limb); pad < limbDigits; pad++ {
			out.WriteByte('0')
		}
		out.WriteString(limb)
	}
	out.WriteByte('\n')
}
