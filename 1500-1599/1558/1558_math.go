package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// digitsOf returns the digits of the line, without the brackets
func digitsOf(line string) string {
	var b strings.Builder
	for _, c := range line {
		if c >= '0' && c <= '9' {
			b.WriteRune(c)
		}
	}
	return b.String()
}

// lowFirst returns x as k digits, the least significant first
func lowFirst(x int64, k int) string {
	b := make([]byte, k)
	for i := range b {
		b[i] = byte('0' + x%10)
		x /= 10
	}
	return string(b)
}

func reversed(s string) string {
	b := []byte(s)
	for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
		b[i], b[j] = b[j], b[i]
	}
	return string(b)
}

func main() {
	sc := bufio.NewScanner(os.Stdin)
	var nums []string
	for len(nums) < 2 && sc.Scan() {
		if s := digitsOf(sc.Text()); s != "" {
			nums = append(nums, s)
		}
	}
	k := len(nums[0])
	top := int64(1)
	for i := 0; i < k; i++ {
		top *= 10
	}
	a, _ := strconv.Atoi(nums[0])
	b, _ := strconv.Atoi(nums[1])
	total := int64(a) + int64(b)
	// without a carry every block is the plain sum; with one, the lowest block
	// sends a carry on, and every block above it gets the carry and sends one
	var p, digits string
	if total < top {
		p = lowFirst(total, k)
		digits = p
	} else {
		p = lowFirst(total+1-top, k)
		digits = lowFirst(total-top, k) + p
	}
	// the shortest period of the repeated block, then the shortest tail after
	// which every digit repeats the digit that period further up
	d := 1
	for k%d != 0 || p != p[d:]+p[:d] {
		d++
	}
	digits += p + p
	start := len(digits) - 2*k
	for start > 0 && digits[start-1] == digits[start-1+d] {
		start--
	}
	fmt.Println("(" + reversed(digits[start:start+d]) + ")" + reversed(digits[:start]))
}
