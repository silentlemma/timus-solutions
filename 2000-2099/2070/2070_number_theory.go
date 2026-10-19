package main

import "fmt"

const limit = 1000000 // square root of the largest R

func main() {
	var l, r int64
	fmt.Scan(&l, &r)
	composite := make([]bool, limit+1)
	composite[0], composite[1] = true, true
	for i := 2; i*i <= limit; i++ {
		if !composite[i] {
			for j := i * i; j <= limit; j += i {
				composite[j] = true
			}
		}
	}
	// the only unsatisfying numbers are p^k, k >= 2, with k + 1 divisors and k + 1 prime
	bad := int64(0)
	for p := int64(2); p*p <= r; p++ {
		if composite[p] {
			continue
		}
		power := p * p
		for k := 2; ; k++ {
			if power >= l && !composite[k+1] {
				bad++
			}
			if power > r/p {
				break
			}
			power *= p
		}
	}
	fmt.Println(r - l + 1 - bad)
}
