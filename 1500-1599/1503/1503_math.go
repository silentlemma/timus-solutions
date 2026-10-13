package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	steps   = 200 // halvings of the search interval: far below the 1e-6 asked
	quartic = 4
)

func value(poly []float64, x float64) float64 {
	s := 0.0
	for _, c := range poly {
		s = s*x + c
	}
	return s
}

func sign(v float64) int {
	switch {
	case v > 0:
		return 1
	case v < 0:
		return -1
	}
	return 0
}

// signRoots finds the points where poly changes sign inside (lo, hi); between
// neighbouring sign changes of the derivative the polynomial is monotone.
func signRoots(poly []float64, lo, hi float64) []float64 {
	if len(poly) < 2 {
		return nil
	}
	n := len(poly) - 1
	deriv := make([]float64, n)
	for i := range deriv {
		deriv[i] = poly[i] * float64(n-i)
	}
	cuts := append([]float64{lo}, signRoots(deriv, lo, hi)...)
	cuts = append(cuts, hi)
	var found []float64
	for k := 0; k+1 < len(cuts); k++ {
		a, b := cuts[k], cuts[k+1]
		sa, sb := sign(value(poly, a)), sign(value(poly, b))
		if sa == 0 || sb == 0 || sa == sb {
			continue
		}
		for it := 0; it < steps; it++ {
			mid := (a + b) / 2
			if sign(value(poly, mid)) == sa {
				a = mid
			} else {
				b = mid
			}
		}
		found = append(found, (a+b)/2)
	}
	return found
}

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

// rationalRoot returns a root p/q of poly, or ok = false.
func rationalRoot(poly []int64) (p, q int64, ok bool) {
	lead, last := abs(poly[0]), abs(poly[len(poly)-1])
	for q = 1; q <= lead; q++ {
		if lead%q != 0 {
			continue
		}
		for pa := int64(1); pa <= last; pa++ {
			if last%pa != 0 {
				continue
			}
			for _, p = range []int64{pa, -pa} {
				// q^n f(p/q), exact in integers
				s, qp := int64(0), int64(1)
				for _, c := range poly {
					s = s*p + c*qp
					qp *= q
				}
				if s == 0 {
					return p, q, true
				}
			}
		}
	}
	return 0, 0, false
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	poly := make([]int64, n+1) // the leading coefficient first
	for i := range poly {
		fmt.Fscan(in, &poly[i])
	}
	var roots []float64
	// rational roots p/q, with p dividing the constant term and q the
	// leading one; dividing by (q x - p) keeps integer coefficients
	for len(poly) > 1 && poly[len(poly)-1] == 0 {
		roots = append(roots, 0)
		poly = poly[:len(poly)-1]
	}
	for len(poly) > 1 {
		p, q, ok := rationalRoot(poly)
		if !ok {
			break
		}
		out := []int64{poly[0] / q}
		for i := 1; i+1 < len(poly); i++ {
			out = append(out, (poly[i]+p*out[len(out)-1])/q)
		}
		poly = out
		roots = append(roots, float64(p)/float64(q))
	}
	// what is left has no rational roots; a repeated irrational root would
	// need its quadratic twice, so only a0 (x^2 + b x + d)^2 can repeat
	if len(poly) == quartic+1 {
		a0, c3, c2, c1, c0 := poly[0], poly[1], poly[2], poly[quartic-1], poly[quartic]
		u := quartic * a0
		e := u*c2 - c3*c3 // then b = 2 c3 / u, d = 2 e / u^2
		if 2*c3*e == c1*u*u && e*e == c0*u*u*u {
			if w := c3*c3 - 2*e; w > 0 { // the roots are (-c3 +- sqrt(w)) / u
				for _, sq := range []float64{-math.Sqrt(float64(w)), math.Sqrt(float64(w))} {
					r := (float64(-c3) + sq) / float64(u)
					roots = append(roots, r, r)
				}
			}
			poly = []int64{1}
		}
	}
	rest := make([]float64, len(poly))
	for i, c := range poly {
		rest[i] = float64(c)
	}
	bound := 1.0
	for _, c := range rest[1:] {
		bound = math.Max(bound, 1+math.Abs(c/rest[0]))
	}
	roots = append(roots, signRoots(rest, -bound, bound)...)
	sort.Float64s(roots)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, r := range roots {
		fmt.Fprintf(out, "%.10f\n", r)
	}
}
