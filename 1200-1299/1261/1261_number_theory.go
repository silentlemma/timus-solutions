package main

import "fmt"

const base = 3

func main() {
	var n int64
	fmt.Scan(&n)
	// balanced ternary: digits 1 go into the payment, digits -1 into the tip
	var pay, tip int64
	for power := int64(1); n > 0; power *= base {
		switch n % base {
		case 1:
			pay += power
			n--
		case base - 1:
			tip += power
			n++
		}
		n /= base
	}
	// no tip yet: add the smallest bill the payment lacks to both
	for power := int64(1); tip == 0; power *= base {
		if pay/power%base == 0 {
			pay += power
			tip = power
		}
	}
	fmt.Println(pay, tip)
}
