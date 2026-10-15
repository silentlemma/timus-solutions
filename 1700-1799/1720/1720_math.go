package main

import "fmt"

// covered counts the numbers 1 .. t that are sums of contests: k contests
// give [kx, ky]; once k (y - x) >= x - 1 the next interval touches this one,
// so from the first such k on everything is covered, before it they are apart
func covered(t, x, y int64) int64 {
	if t < x {
		return 0
	}
	if y == x {
		return t / x
	}
	joined := (x - 1 + (y - x) - 1) / (y - x)
	if joined < 1 {
		joined = 1
	}
	full := t / y // the intervals that end by t
	if joined-1 < full {
		full = joined - 1
	}
	count := (y-x)*(full*(full+1)/2) + full
	k := full + 1
	if k <= joined-1 && k <= t/x {
		count += t - k*x + 1
	}
	if joined <= t/x {
		count += t - joined*x + 1
	}
	return count
}

func main() {
	var x, y, low, high int64
	fmt.Scan(&x, &y, &low, &high)
	fmt.Println(covered(high, x, y) - covered(low-1, x, y))
}
