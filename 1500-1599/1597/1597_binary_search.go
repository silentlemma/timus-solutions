package main

import (
	"bufio"
	"fmt"
	"os"
)

const mostDrops = 2000000000 // two eggs already cover 10^18 floors with this many

// covered is the number of floors t drops with k eggs can settle, the sum
// of C(t, i) over i = 1..k, or n + 1 if that is more.
func covered(t, k, n int64) int64 {
	total, term := int64(0), int64(1)
	for i := int64(1); i <= k && i <= t; i++ {
		// term * (t - i + 1) / i without overflow: split term by i
		q, r, f := term/i, term%i, t-i+1
		if q > n/f {
			return n + 1
		}
		term = q*f + r*f/i
		total += term
		if total > n {
			return n + 1
		}
	}
	return total
}

func drops(k, n int64) int64 {
	if k == 1 {
		return n
	}
	lo, hi := int64(1), int64(mostDrops)
	for lo < hi {
		mid := (lo + hi) / 2
		if covered(mid, k, n) >= n {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for {
		var k, n int64
		if _, err := fmt.Fscan(in, &k, &n); err != nil || (k == 0 && n == 0) {
			return
		}
		fmt.Fprintln(out, drops(k, n))
	}
}
