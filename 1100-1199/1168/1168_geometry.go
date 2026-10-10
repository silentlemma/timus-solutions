package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	// eps: R is a real number; all other lengths are integers, so a squared
	// distance is an integer and only the integer part of R*R matters
	eps = 1e-6
	// sky is above every altitude a station allows: 32000 plus 100000
	sky = 1000000
)

func isqrt(v int64) int64 {
	s := int64(math.Sqrt(float64(v)))
	for s*s > v {
		s--
	}
	for (s+1)*(s+1) <= v {
		s++
	}
	return s
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var m, n, k int
	fmt.Fscan(in, &m, &n, &k)
	h := make([]int64, m*n)
	for c := range h {
		fmt.Fscan(in, &h[c])
	}
	si, sj := make([]int64, k), make([]int64, k)
	z, reach := make([]int64, k), make([]int64, k)
	taken := make([]bool, m*n)
	for t := 0; t < k; t++ {
		var r float64
		fmt.Fscan(in, &si[t], &sj[t], &r)
		si[t]--
		sj[t]--
		c := si[t]*int64(n) + sj[t]
		z[t] = h[c]
		reach[t] = int64(r*r + eps)
		taken[c] = true
	}
	var total int64
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if taken[i*n+j] {
				continue
			}
			// the receiver at altitude a hears a station at height z when
			// (a - z)^2 <= R^2 - (horizontal distance)^2
			low, high := h[i*n+j], int64(sky)
			for t := 0; t < k && low <= high; t++ {
				di, dj := int64(i)-si[t], int64(j)-sj[t]
				rest := reach[t] - di*di - dj*dj
				if rest < 0 {
					high = -1
					break
				}
				s := isqrt(rest)
				if z[t]-s > low {
					low = z[t] - s
				}
				if z[t]+s < high {
					high = z[t] + s
				}
			}
			if low <= high {
				total += high - low + 1
			}
		}
	}
	fmt.Println(total)
}
