package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const stages = 3

// line is a*x + b*y + c, shifted by a tiny eps: a*x + b*y + c + eps < 0 is the
// half-plane kept
type line struct{ a, b, c int64 }

func mul(x, y int64) *big.Int {
	return new(big.Int).Mul(big.NewInt(x), big.NewInt(y))
}

// side is -1, 0 or 1: where the corner of lines p and q lies against line l,
// all shifted by eps; the values reach 3 * 10^37, past 64 bits
func side(p, q, l line) int {
	det := new(big.Int).Sub(mul(p.a, q.b), mul(q.a, p.b))
	x0 := new(big.Int).Sub(mul(q.c, p.b), mul(p.c, q.b))
	y0 := new(big.Int).Sub(mul(p.c, q.a), mul(q.c, p.a))
	t0 := new(big.Int).Mul(big.NewInt(l.a), x0)
	t0.Add(t0, new(big.Int).Mul(big.NewInt(l.b), y0))
	t0.Add(t0, new(big.Int).Mul(big.NewInt(l.c), det))
	t1 := new(big.Int).Add(mul(l.a, p.b-q.b), mul(l.b, q.a-p.a))
	t1.Add(t1, det)
	sign := t0.Sign()
	if sign == 0 {
		sign = t1.Sign()
	}
	if det.Sign() < 0 {
		sign = -sign
	}
	return sign
}

// clip cuts the polygon, given by its lines in boundary order, by the line
func clip(edges []line, l line) []line {
	m := len(edges)
	sides := make([]int, m)
	for k := range edges {
		sides[k] = side(edges[(k+m-1)%m], edges[k], l)
	}
	// edge k runs from corner k to corner k + 1; it stays if part of it is inside
	keep := make([]bool, m)
	start := -1
	for k := range edges {
		keep[k] = sides[k] < 0 || sides[(k+1)%m] < 0
		if keep[k] && start < 0 {
			start = k
		}
	}
	if start < 0 {
		return nil
	}
	var out []line
	for step := 0; step < m; step++ {
		k := (start + step) % m
		next := (k + 1) % m
		if !keep[k] {
			continue
		}
		out = append(out, edges[k])
		// the boundary leaves the half-plane before the next kept edge
		if !keep[next] || sides[next] > 0 {
			out = append(out, l)
		}
	}
	if len(out) < stages {
		return nil
	}
	return out
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	s := make([][stages]int64, n)
	for i := range s {
		for k := 0; k < stages; k++ {
			fmt.Fscan(in, &s[i][k])
		}
	}
	// the sides of the triangle x > 0, y > 0, x + y < 1, in boundary order
	triangle := []line{{0, -1, 0}, {1, 1, -1}, {-1, 0, 0}}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < n; i++ {
		edges := triangle
		for j := 0; j < n && edges != nil; j++ {
			if j == i {
				continue
			}
			// with u_k = length_k / s_ik > 0, i beats j when
			// sum (s_jk - s_ik) / s_jk * u_k < 0; times s_j1 s_j2 s_j3 the
			// coefficients are integers below 10^12
			var g [stages]int64
			for k := 0; k < stages; k++ {
				others := s[j][(k+1)%stages] * s[j][(k+2)%stages]
				g[k] = (s[j][k] - s[i][k]) * others
			}
			// u_3 = 1 - x - y on the triangle
			l := line{g[0] - g[2], g[1] - g[2], g[2]}
			if l.a == 0 && l.b == 0 {
				if l.c >= 0 {
					edges = nil
				}
				continue
			}
			edges = clip(edges, l)
		}
		if edges == nil {
			out.WriteString("No\n")
		} else {
			out.WriteString("Yes\n")
		}
	}
}
