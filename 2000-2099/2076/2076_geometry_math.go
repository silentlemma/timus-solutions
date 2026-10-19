package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const (
	scale   = 4 // N is the distance of Q from the vertex times 4 |A|^3
)

func mul(a, b *big.Int) *big.Int { return new(big.Int).Mul(a, b) }
func add(a, b *big.Int) *big.Int { return new(big.Int).Add(a, b) }
func sub(a, b *big.Int) *big.Int { return new(big.Int).Sub(a, b) }
func small(k int64) *big.Int     { return big.NewInt(k) }

func cross(ux, uy, vx, vy *big.Int) *big.Int { return sub(mul(ux, vy), mul(uy, vx)) }

func answer(a, b, c, d, e, f, px, py, r *big.Int) string {
	// the curve is C + B t + A t^2 with A = (a, d), B = (b, e), C = (c, f)
	wx, wy := sub(px, c), sub(py, f) // P relative to C
	r2 := mul(r, r)
	if a.Sign() == 0 && d.Sign() == 0 {
		if b.Sign() == 0 && e.Sign() == 0 {
			// a single point: every line through it is an axis, and Q runs over the
			// circle with diameter CP, from C itself to P
			if add(mul(wx, wx), mul(wy, wy)).Cmp(r2) <= 0 {
				return "YES"
			}
			return "MAYBE"
		}
		// a line: the line itself is an axis (Q lies on it), and so is every
		// perpendicular, with Q at the distance of P from the line
		dist := cross(wx, wy, b, e)
		if mul(dist, dist).Cmp(mul(r2, add(mul(b, b), mul(e, e)))) <= 0 {
			return "YES"
		}
		return "MAYBE"
	}
	// one axis along A; along it, P lies at N / (4 |A|^3) from the vertex
	a2 := add(mul(a, a), mul(d, d))
	ab := add(mul(a, b), mul(d, e))
	n := add(mul(mul(small(scale), a2), add(mul(wx, a), mul(wy, d))), mul(ab, ab))
	k := cross(a, d, b, e)
	k2 := mul(k, k) // zero for a ray, otherwise the parabola width
	a6 := mul(mul(a2, a2), a2)
	inside := false
	if n.Cmp(mul(small(2), k2)) <= 0 {
		// the nearest point of the curve is its vertex (the end of a ray)
		inside = mul(n, n).Cmp(mul(mul(small(scale*scale), r2), a6)) <= 0
	} else {
		// Q far enough inside: squared distance k2 (N - k2) / (4 |A|^6), zero on a ray
		inside = mul(k2, sub(n, k2)).Cmp(mul(mul(small(scale), r2), a6)) <= 0
	}
	if inside {
		return "YES"
	}
	return "NO"
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		read := func() *big.Int {
			x := new(big.Int)
			fmt.Fscan(in, x)
			return x
		}
		// assignments evaluate their operands from left to right
		a, b, c, d, e, f := read(), read(), read(), read(), read(), read()
		px, py, r := read(), read(), read()
		fmt.Fprintln(out, answer(a, b, c, d, e, f, px, py, r))
	}
}
