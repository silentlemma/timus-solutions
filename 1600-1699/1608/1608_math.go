package main

import (
	"fmt"
	"strconv"
)

const (
	digits = 10
	pair   = digits * (digits - 1) // two free mirrored digits that differ
)

// complete counts lucky numbers of this length that start with these digits.
func complete(prefix []int, length int) int64 {
	ways := int64(1)
	fixed := len(prefix)
	for i := 0; i < (length+1)/2; i++ {
		j := length - 1 - i
		switch {
		case i == j:
			if i >= fixed {
				ways *= digits
			}
		case j < fixed:
			if prefix[i] == prefix[j] {
				return 0
			}
		case i < fixed:
			ways *= digits - 1 // the partner must differ from the fixed digit
		default:
			ways *= pair
		}
	}
	return ways
}

// luckyUpTo counts the lucky tickets numbered 1 .. n.
func luckyUpTo(n int64) int64 {
	if n <= 0 {
		return 0
	}
	s := strconv.FormatInt(n, 10)
	length := len(s)
	ds := make([]int, length)
	for i := range s {
		ds[i] = int(s[i] - '0')
	}
	total := int64(0)
	// all shorter numbers, by their first digit
	for k := 1; k < length; k++ {
		for d := 1; d < digits; d++ {
			total += complete([]int{d}, k)
		}
	}
	// same length: the first position where the number drops below n
	for k := 0; k < length; k++ {
		prefix := append(append([]int(nil), ds[:k]...), 0)
		start := 0
		if k == 0 {
			start = 1
		}
		for d := start; d < ds[k]; d++ {
			prefix[k] = d
			total += complete(prefix, length)
		}
	}
	return total + complete(ds, length)
}

func main() {
	var a, b int64
	if _, err := fmt.Scan(&a, &b); err != nil {
		return
	}
	fmt.Println(luckyUpTo(b) - luckyUpTo(a-1))
}
