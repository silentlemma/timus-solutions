package main

import (
	"fmt"
	"math"
)

const (
	outer, middle, total = 5.0, 8.0, 9.0 // three-point Gauss-Legendre weights, as 5/9 and 8/9
	tolerance            = 1e-13
	depth                = 50
	limit                = 20.0 // sinh(20) is about 2.4e8, beyond which the tails are negligible
)

var (
	node               = math.Sqrt(0.6) // the outer nodes on [-1, 1]
	a0, a1, a2, a3, a4 float64
)

// f is the integrand after x = sinh t, dx = cosh t dt.
func f(t float64) float64 {
	x := math.Sinh(t)
	return math.Cosh(t) / ((((a4*x+a3)*x+a2)*x+a1)*x + a0)
}

func gauss(lo, hi float64) float64 {
	mid, half := (lo+hi)/2, (hi-lo)/2
	return half * (outer*f(mid-half*node) + middle*f(mid) + outer*f(mid+half*node)) / total
}

// integrate splits while the halves disagree with the whole.
func integrate(lo, hi, whole float64, left int) float64 {
	mid := (lo + hi) / 2
	l, r := gauss(lo, mid), gauss(mid, hi)
	both := l + r
	if left == 0 || math.Abs(both-whole) <= tolerance*(1+math.Abs(both)) {
		return both
	}
	return integrate(lo, mid, l, left-1) + integrate(mid, hi, r, left-1)
}

func main() {
	if _, err := fmt.Scan(&a0, &a1, &a2, &a3, &a4); err != nil {
		return
	}
	fmt.Printf("%.10f\n", integrate(-limit, limit, gauss(-limit, limit), depth))
}
