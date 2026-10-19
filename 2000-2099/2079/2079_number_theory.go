package main

import (
	"fmt"
	"math"
	"sort"
	"strconv"
	"strings"
)

const (
	small = 50 // small primes: walk the whole sequence
	five  = 5
	quad  = 4 // the discriminant of a y^2 + b y + c is b^2 - 4 a c
)

var p int64

// elem is a t + b in F_p[t] / (t^2 - t - 1)
type elem struct{ a, b int64 }

func power(b, e int64) int64 {
	r := int64(1)
	for b %= p; e > 0; e >>= 1 {
		if e&1 == 1 {
			r = r * b % p
		}
		b = b * b % p
	}
	return r
}

// sqrtMod is a square root of a modulo the odd prime p, or -1 (Tonelli-Shanks)
func sqrtMod(a int64) int64 {
	a %= p
	if a == 0 {
		return 0
	}
	if power(a, (p-1)/2) != 1 {
		return -1
	}
	q, s := p-1, int64(0)
	for q%2 == 0 {
		q /= 2
		s++
	}
	z := int64(2)
	for power(z, (p-1)/2) != p-1 {
		z++
	}
	m, c, t, r := s, power(z, q), power(a, q), power(a, (q+1)/2)
	for t != 1 {
		i, t2 := int64(0), t
		for t2 != 1 {
			t2 = t2 * t2 % p
			i++
		}
		b := power(c, int64(1)<<uint(m-i-1))
		m, c = i, b*b%p
		t, r = t*c%p, r*b%p
	}
	return r
}

// mul is (a t + b)(c t + d) with t^2 = t + 1
func mul(u, v elem) elem {
	ac := u.a * v.a % p
	cross := (u.a*v.b + u.b*v.a) % p
	return elem{(ac + cross) % p, (ac + u.b*v.b) % p}
}

func main() {
	var x int64
	fmt.Scan(&p, &x)
	found := map[int64]bool{}
	if p <= small {
		// the pairs (F(k), F(k + 1)) repeat with a period of at most 4p + 4
		a, b := int64(0), int64(1)
		for {
			if a == x {
				found[b] = true
			}
			a, b = b, (a+b)%p
			if a == 0 && b == 1 {
				break
			}
		}
	} else {
		// t^k = F(k) t + F(k - 1), and Cassini's identity
		// F(k + 1)^2 - F(k + 1) F(k) - F(k)^2 = (-1)^k limits y = F(k + 1)
		// to the roots of y^2 - x y - x^2 - s = 0, s = 1 or -1
		candidates := map[int64]bool{}
		half := (p + 1) / 2
		for _, s := range []int64{1, -1} {
			root := sqrtMod(((x*x+quad*(x*x+s))%p + p) % p)
			if root < 0 {
				continue
			}
			candidates[(x+root)%p*half%p] = true
			candidates[(x-root+p)%p*half%p] = true
		}
		// a pair is a power of t when the discrete logarithm exists: baby steps
		// t^j, giant steps by t^-m; the period divides p - 1 or 2 (p + 1)
		bound := 2 * (p + 1)
		if p%five == 1 || p%five == five-1 {
			bound = p - 1
		}
		m := int64(math.Sqrt(float64(bound))) + 1
		baby := make(map[elem]bool, m)
		e := elem{0, 1}
		for j := int64(0); j < m; j++ {
			baby[e] = true
			e = mul(e, elem{1, 0})
		}
		back, inverse := elem{0, 1}, elem{1, p - 1} // t^-m = (t - 1)^m
		for k := m; k > 0; k >>= 1 {
			if k&1 == 1 {
				back = mul(back, inverse)
			}
			inverse = mul(inverse, inverse)
		}
		for y := range candidates {
			e = elem{x, (y - x + p) % p}
			for i := int64(0); i <= m; i++ {
				if baby[e] {
					found[y] = true
					break
				}
				e = mul(e, back)
			}
		}
	}
	values := make([]int64, 0, len(found))
	for y := range found {
		values = append(values, y)
	}
	sort.Slice(values, func(i, j int) bool { return values[i] < values[j] })
	fmt.Println(len(values))
	if len(values) > 0 {
		parts := make([]string, len(values))
		for i, y := range values {
			parts[i] = strconv.FormatInt(y, 10)
		}
		fmt.Println(strings.Join(parts, " "))
	}
}
