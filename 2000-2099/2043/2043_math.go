package main

import (
	"bufio"
	"fmt"
	"os"
)

const mod int64 = 1000000007

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func columns(n, m, k int64) int64 {
	end, total := n*m-1, int64(0)
	for c := int64(0); c < n; c++ {
		lower := c * m
		upper := lower + m
		first, last := lower/k+1, min(upper, end)/k
		if last < first {
			continue
		}
		count := last - first + 1
		var a, b int64
		if c%2 == 0 {
			a, b = first*k-lower, last*k-lower
		} else {
			a, b = upper-first*k, upper-last*k
			if b == 0 {
				total++
			}
		}
		pair := a + b
		if count%2 == 0 {
			count /= 2
		} else {
			pair /= 2
		}
		total += (count % mod) * (pair % mod) % mod
		if total >= mod {
			total -= mod
		}
	}
	return total
}

func residues(n, m, k int64) int64 {
	period := 2 * m
	g := gcd(k, period)
	length := period / g
	refills := (n*m - 1) / k
	remainder := refills % length
	reverse := length - remainder - 1
	work := min(remainder, reverse)
	half := length / 2
	cycle := (g%mod*(half%mod)%mod*((length-half)%mod) + 1) % mod
	at, step, prefix := int64(0), k%period, int64(0)
	for i := int64(0); i < work; i++ {
		at += step
		if at >= period {
			at -= period
		}
		prefix += min(at, period-at)
	}
	prefix %= mod
	if reverse < remainder {
		prefix = (cycle - 1 - prefix + mod) % mod
	}
	return ((refills/length%mod)*cycle%mod + prefix) % mod
}

func solve(n, m, k int64) int64 {
	base := n*m - 1
	if k > base {
		return base % mod
	}
	length := 2 * m / gcd(k, 2*m)
	remainder := base / k % length
	work := min(remainder, length-remainder-1)
	var extra int64
	if n < work {
		extra = columns(n, m, k)
	} else {
		extra = residues(n, m, k)
	}
	return (base%mod + 2*extra) % mod
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var tests int
	fmt.Fscan(in, &tests)
	for ; tests > 0; tests-- {
		var n, m, k int64
		fmt.Fscan(in, &n, &m, &k)
		fmt.Fprintln(out, solve(n, m, k))
	}
}
