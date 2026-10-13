package main

import "fmt"

func main() {
	var a, b, n int64
	fmt.Scan(&a, &b, &n)
	swapped := a < b
	if swapped {
		a, b = b, a
	}
	// b items of price a can always become a items of price b, so x below b is enough,
	// with a >= b either b or n / a is at most sqrt(n)
	top := n / a
	if b-1 < top {
		top = b - 1
	}
	spent, bx, by := int64(-1), int64(0), int64(0)
	for x := int64(0); x <= top && spent != n; x++ {
		y := (n - x*a) / b
		if x*a+y*b > spent {
			spent, bx, by = x*a+y*b, x, y
		}
	}
	if swapped {
		bx, by = by, bx
	}
	fmt.Println(bx, by)
}
