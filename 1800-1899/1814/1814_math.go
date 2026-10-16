package main

import (
	"fmt"
	"math"
)

const mod = 1000000007

// matrix holds a 2 x 2 matrix rows first: a b / c d
type matrix struct{ a, b, c, d int64 }

func mul(x, y matrix) matrix {
	return matrix{(x.a*y.a + x.b*y.c) % mod, (x.a*y.b + x.b*y.d) % mod,
		(x.c*y.a + x.d*y.c) % mod, (x.c*y.b + x.d*y.d) % mod}
}

// term is the factor [a 1; 1 0] by which [p_k p_(k-1); q_k q_(k-1)] grows
func term(a int64) matrix { return matrix{a % mod, 1, 1, 0} }

func main() {
	var x, k int64
	if _, err := fmt.Scan(&x, &k); err != nil {
		return
	}
	a0 := int64(math.Sqrt(float64(x)))
	for a0*a0 > x {
		a0--
	}
	for (a0+1)*(a0+1) <= x {
		a0++
	}
	// the partial quotients of sqrt(x) repeat with a period that ends at
	// the first term equal to 2 a0
	var period []int64
	m, d, a := int64(0), int64(1), a0
	for a != 2*a0 {
		m = d*a - m
		d = (x - m*m) / d
		a = (a0 + m) / d
		period = append(period, a)
	}
	cycle := matrix{1, 0, 0, 1}
	for _, v := range period {
		cycle = mul(cycle, term(v))
	}
	result, power := term(a0), cycle
	length := int64(len(period))
	for full := k / length; full > 0; full >>= 1 {
		if full&1 == 1 {
			result = mul(result, power)
		}
		power = mul(power, power)
	}
	for i := int64(0); i < k%length; i++ {
		result = mul(result, term(period[i]))
	}
	// convergents are always in lowest terms
	fmt.Printf("%d/%d\n", result.a, result.c)
}
