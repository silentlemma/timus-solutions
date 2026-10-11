package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
)

const eps = 1e-9

// float turns an exact big integer into the nearest float64
func float(x *big.Int) float64 {
	f, _ := new(big.Float).SetInt(x).Float64()
	return f
}

func mul(a, b int64) *big.Int {
	return new(big.Int).Mul(big.NewInt(a), big.NewInt(b))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	x, y, z, r := make([]int64, n), make([]int64, n), make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &x[i], &y[i], &z[i], &r[i])
	}
	// a ray along d touches ghost i when d.C_i >= L_i |d|, where L_i is the
	// length of a tangent from the gun: L_i^2 = |C_i|^2 - R_i^2
	norm, tan2, tan := make([]int64, n), make([]int64, n), make([]float64, n)
	dot := make([][]int64, n)
	for i := 0; i < n; i++ {
		norm[i] = x[i]*x[i] + y[i]*y[i] + z[i]*z[i]
		tan2[i] = norm[i] - r[i]*r[i]
		tan[i] = math.Sqrt(float64(tan2[i]))
		dot[i] = make([]int64, n)
	}
	for i := 0; i < n; i++ {
		for k := 0; k < n; k++ {
			dot[i][k] = x[i]*x[k] + y[i]*y[k] + z[i]*z[k]
		}
	}
	var best []int
	// the ray through the centre of ghost i, tested exactly in integers
	for i := 0; i < n; i++ {
		var hit []int
		for k := 0; k < n; k++ {
			if dot[i][k]*dot[i][k] >= tan2[k]*norm[i] {
				hit = append(hit, k)
			}
		}
		if len(hit) > len(best) {
			best = hit
		}
	}
	// rays touching two ghosts i and j: d = (a C_i + b C_j + c C_i x C_j) / det
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			g := dot[i][j]
			det := norm[i]*norm[j] - g*g
			if det == 0 {
				continue
			}
			// 1 - |a C_i + b C_j|^2 = Q / det with Q = base + 2 g L_i L_j
			base := norm[i]*norm[j] - g*g - tan2[i]*norm[j] - tan2[j]*norm[i]
			p := tan2[i] * tan2[j]
			gap := new(big.Int).Mul(mul(2*g, 2*g), big.NewInt(p))
			gap.Sub(gap, mul(base, base))
			if base < 0 && gap.Sign() < 0 {
				continue // the two outlines do not meet
			}
			root := math.Sqrt(float64(p))
			var q float64
			if base >= 0 {
				q = float64(base) + 2*float64(g)*root
			} else {
				q = float(gap) / (2*float64(g)*root - float64(base))
			}
			// a det and b det, rationalised to avoid cancellation
			na := new(big.Int).Sub(new(big.Int).Mul(mul(tan2[i], norm[j]), big.NewInt(norm[j])),
				new(big.Int).Mul(mul(tan2[j], g), big.NewInt(g)))
			nb := new(big.Int).Sub(new(big.Int).Mul(mul(tan2[j], norm[i]), big.NewInt(norm[i])),
				new(big.Int).Mul(mul(tan2[i], g), big.NewInt(g)))
			ad := float(na) / (tan[i]*float64(norm[j]) + tan[j]*float64(g))
			bd := float(nb) / (tan[j]*float64(norm[i]) + tan[i]*float64(g))
			cx := y[i]*z[j] - z[i]*y[j]
			cy := z[i]*x[j] - x[i]*z[j]
			cz := x[i]*y[j] - y[i]*x[j]
			signs := []float64{1, -1}
			if q == 0 {
				signs = signs[:1]
			}
			for _, sign := range signs {
				s := sign * math.Sqrt(q)
				var hit []int
				for k := 0; k < n; k++ {
					t := float64(cx*x[k] + cy*y[k] + cz*z[k])
					v := ad*float64(dot[i][k]) + bd*float64(dot[j][k]) + s*t
					if k == i || k == j || v >= float64(det)*tan[k]*(1-eps) {
						hit = append(hit, k)
					}
				}
				if len(hit) > len(best) {
					best = hit
				}
			}
		}
	}
	fmt.Fprintln(out, len(best))
	for i, k := range best {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, k+1)
	}
	fmt.Fprintln(out)
}
