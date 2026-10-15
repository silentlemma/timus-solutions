package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const small = 100 // below this the first candidates are simply tried in turn

const wordBits = 64

func isqrt(v int64) int64 {
	root := int64(math.Sqrt(float64(v)))
	for root*root > v {
		root--
	}
	for (root+1)*(root+1) <= v {
		root++
	}
	return root
}

func ceilSqrt(v int64) int64 {
	root := isqrt(v)
	if root*root == v {
		return root
	}
	return root + 1
}

func fits(n, k int64) bool {
	return n/k == n/(k+1)
}

func least(n int64) int64 {
	// the shares agree exactly when n mod k >= n div k, which needs k > s,
	// s = isqrt(n); with k = s + x and e = n - s^2 the quotient is s - x or
	// s - x + 1, and each case gives the least x in closed form
	if n < small {
		k := int64(1)
		for !fits(n, k) {
			k++
		}
		return k
	}
	s := isqrt(n)
	e := n - s*s
	var xs []int64
	gap := s - e
	if gap >= 1 {
		// quotient s - x: the least x with x^2 + x >= gap (then x^2 - x < gap)
		x := isqrt(gap)
		for x*x+x < gap {
			x++
		}
		for x > 1 && (x-1)*(x-1)+(x-1) >= gap {
			x--
		}
		xs = append(xs, x)
	}
	// quotient s - x + 1: x^2 >= 2s - e + 1 > (x - 1)^2
	xs = append(xs, ceilSqrt(2*s-e+1))
	best := int64(-1)
	for _, x := range xs {
		for d := int64(-1); d <= 1; d++ {
			k := s + x + d
			if x+d >= 1 && fits(n, k) && (best < 0 || k < best) {
				best = k
			}
		}
	}
	return best
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())
	for i := 0; i < t; i++ {
		scanner.Scan()
		n, _ := strconv.ParseInt(scanner.Text(), 10, wordBits)
		writer.WriteString(strconv.FormatInt(least(n), 10))
		writer.WriteString("\n")
	}
}
