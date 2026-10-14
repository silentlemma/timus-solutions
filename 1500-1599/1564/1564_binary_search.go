package main

import "fmt"

const (
	base = 10
	top  = 1000000000000000000 // more than 10^18 ones are counted below this floor
)

// ones counts the digits 1 in the numbers from 1 to x: at each place p, every
// full block of 10 p numbers holds p ones there, and the last part adds p,
// the rest past the 1, or nothing, as its digit is above, at or below 1
func ones(x int64) int64 {
	total := int64(0)
	// x is at least 1; p stops before p * 10 could pass 10^19
	for p := int64(1); ; p *= base {
		high, digit, low := x/p/base, x/p%base, x%p
		total += high * p
		if digit > 1 {
			total += p
		} else if digit == 1 {
			total += low + 1
		}
		if p > x/base {
			break
		}
	}
	return total
}

func main() {
	var k int64
	fmt.Scan(&k)
	// the floor where the k-th one was counted is the first x with ones(x) >= k
	lo, hi := int64(1), int64(top)
	for lo < hi {
		mid := lo + (hi-lo)/2
		if ones(mid) >= k {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	if ones(lo) == k {
		fmt.Println(lo)
	} else {
		fmt.Println("Petr lies")
	}
}
