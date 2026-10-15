package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

const (
	quartic      = 5 // coefficients of a degree-4 polynomial
	discriminant = 4 // t^2 - at + e has discriminant a^2 - 4e
)

// divisors gives the positive and negative divisors of v != 0.
func divisors(v int64) []int64 {
	if v < 0 {
		v = -v
	}
	var out []int64
	for d := int64(1); d*d <= v; d++ {
		if v%d == 0 {
			out = append(out, d, -d, v/d, -(v / d))
		}
	}
	return out
}

func value(poly []int64, x int64) int64 {
	result := int64(0)
	for _, c := range poly {
		result = result*x + c
	}
	return result
}

// root finds an integer root of a monic polynomial: it divides the
// constant term.
func root(poly []int64) (int64, bool) {
	if poly[len(poly)-1] == 0 {
		return 0, true
	}
	for _, d := range divisors(poly[len(poly)-1]) {
		if value(poly, d) == 0 {
			return d, true
		}
	}
	return 0, false
}

func exactRoot(v int64) int64 {
	s := int64(math.Sqrt(float64(v)))
	for s*s > v {
		s--
	}
	for (s+1)*(s+1) <= v {
		s++
	}
	return s
}

// quadratics splits the quartic as (x^2 + px + q)(x^2 + rx + s) with
// qs = d, p + r = a, q + s + pr = b, ps + qr = c.
func quadratics(poly []int64) ([]int64, []int64, bool) {
	a, b, c, d := poly[1], poly[2], poly[quartic-2], poly[quartic-1]
	for _, q := range divisors(d) {
		s := d / q
		var p int64
		if q != s {
			if (c-a*q)%(s-q) != 0 {
				continue
			}
			p = (c - a*q) / (s - q)
		} else {
			// then p and r are the roots of t^2 - at + (b - 2q)
			disc := a*a - discriminant*(b-2*q)
			if disc < 0 {
				continue
			}
			root := exactRoot(disc)
			if root*root != disc || (a+root)%2 != 0 {
				continue
			}
			p = (a + root) / 2
		}
		r := a - p
		if q+s+p*r == b && p*s+q*r == c {
			return []int64{1, p, q}, []int64{1, r, s}, true
		}
	}
	return nil, nil, false
}

func show(poly []int64) string {
	deg := len(poly) - 1
	var out strings.Builder
	for i, c := range poly {
		if c == 0 {
			continue
		}
		power := deg - i
		if c < 0 {
			out.WriteString("-")
		} else if out.Len() > 0 {
			out.WriteString("+")
		}
		size := c
		if size < 0 {
			size = -size
		}
		if size != 1 || power == 0 {
			out.WriteString(strconv.FormatInt(size, 10))
		}
		if power > 0 {
			out.WriteString("x")
		}
		if power > 1 {
			out.WriteString(strconv.Itoa(power))
		}
	}
	return "(" + out.String() + ")"
}

func main() {
	poly := make([]int64, quartic)
	poly[0] = 1
	for i := 1; i < quartic; i++ {
		fmt.Scan(&poly[i])
	}
	var factors [][]int64
	for len(poly) > 2 {
		r, ok := root(poly)
		if !ok {
			break
		}
		factors = append(factors, []int64{1, -r})
		quotient := []int64{1}
		for _, coef := range poly[1 : len(poly)-1] {
			quotient = append(quotient, coef+r*quotient[len(quotient)-1])
		}
		poly = quotient
	}
	if len(poly) == quartic {
		first, second, ok := quadratics(poly)
		if !ok {
			fmt.Println("Irreducible")
			return
		}
		factors = append(factors, first, second)
	} else if len(poly) > 1 {
		factors = append(factors, poly)
	}
	var out strings.Builder
	for _, f := range factors {
		out.WriteString(show(f))
	}
	fmt.Println(out.String())
}
