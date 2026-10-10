package main

import "fmt"

const digits = 10

func main() {
	var n int64
	fmt.Scan(&n)
	var count [digits]int64
	for p := int64(1); p <= n; p *= digits {
		// at this position the numbers up to n split into the part above, the
		// digit itself and the part below; every smaller upper part repeats
		// each digit p times here
		high, cur, low := n/(p*digits), n/p%digits, n%p
		for d := int64(1); d < digits; d++ {
			count[d] += high * p
			if d < cur {
				count[d] += p
			} else if d == cur {
				count[d] += low + 1
			}
		}
		// a zero needs a nonzero digit above it, so the upper part 0 is skipped
		if high > 0 {
			count[0] += (high - 1) * p
			if cur > 0 {
				count[0] += p
			} else {
				count[0] += low + 1
			}
		}
	}
	for _, c := range count {
		fmt.Println(c)
	}
}
