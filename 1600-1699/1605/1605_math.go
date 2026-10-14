package main

import (
	"fmt"
	"math"
)

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		return
	}
	// x_n = 2/3 - (-1)^n (2/3) 2^-n: an even n leaves k sixes while
	// 10^k <= 2^n, an odd n while 2 10^k < 2^n, that is 10^k <= 2^(n-1)
	m := n
	if n%2 == 1 {
		m = n - 1
	}
	fmt.Println(int64(math.Floor(float64(m) * math.Log10(2))))
}
