package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	prime    = 1000000007 // independence is decided exactly, modulo this prime
	zeroBand = 5e-6       // values that print as 0.00000, kept without a minus
)

func power(base, exp int64) int64 {
	result := int64(1)
	for base %= prime; exp > 0; exp >>= 1 {
		if exp&1 == 1 {
			result = result * base % prime
		}
		base = base * base % prime
	}
	return result
}

type reduced struct {
	pivot int
	row   []int64
}

// independent finds a maximal linearly independent subset by Gaussian
// elimination modulo prime, so no rounding decides the rank.
func independent(vectors [][]int64) []int {
	var basis []reduced
	var chosen []int
	for k, vec := range vectors {
		row := make([]int64, len(vec))
		for i, x := range vec {
			row[i] = (x%prime + prime) % prime
		}
		for _, b := range basis {
			if f := row[b.pivot]; f != 0 {
				for i := range row {
					row[i] = ((row[i]-f*b.row[i])%prime + prime) % prime
				}
			}
		}
		pivot := -1
		for i, x := range row {
			if x != 0 {
				pivot = i
				break
			}
		}
		if pivot < 0 {
			continue
		}
		inv := power(row[pivot], prime-2)
		for i := range row {
			row[i] = row[i] * inv % prime
		}
		basis = append(basis, reduced{pivot, row})
		chosen = append(chosen, k)
	}
	return chosen
}

func dot(u, v []float64) float64 {
	s := 0.0
	for i := range u {
		s += u[i] * v[i]
	}
	return s
}

// qr gives Q and R (by columns) of independent columns: Gram-Schmidt with
// every projection done twice, which keeps Q orthonormal to rounding error.
func qr(columns [][]float64) ([][]float64, [][]float64) {
	var q, r [][]float64
	for _, col := range columns {
		v := append([]float64(nil), col...)
		coef := make([]float64, len(q))
		for pass := 0; pass < 2; pass++ {
			for k, u := range q {
				c := dot(u, v)
				coef[k] += c
				for i := range v {
					v[i] -= c * u[i]
				}
			}
		}
		norm := math.Sqrt(dot(v, v))
		for i := range v {
			v[i] /= norm
		}
		q = append(q, v)
		r = append(r, append(coef, norm))
	}
	return q, r
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	// engine i pushes along row i; the thrust is the sum of X_i times row i.
	// The shortest best X lies in the span of the columns c_j = (row i at j)_i
	cols := make([][]int64, n)
	real := make([][]float64, n)
	for j := range cols {
		cols[j] = make([]int64, m)
		real[j] = make([]float64, m)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(in, &cols[j][i])
			real[j][i] = float64(cols[j][i])
		}
	}
	b := make([]float64, n)
	for j := range b {
		fmt.Fscan(in, &b[j])
	}
	var picked [][]float64
	for _, j := range independent(cols) {
		picked = append(picked, real[j])
	}
	basis, _ := qr(picked)
	// with X = sum of w_k basis[k], the thrust is K w for K[j][k] = c_j . q_k,
	// and K has full column rank: least squares by QR of K
	size := len(basis)
	kCols := make([][]float64, size)
	for k, u := range basis {
		kCols[k] = make([]float64, n)
		for j := range real {
			kCols[k][j] = dot(real[j], u)
		}
	}
	q2, upper := qr(kCols)
	w := make([]float64, size)
	for i := size - 1; i >= 0; i-- {
		s := dot(q2[i], b)
		for k := i + 1; k < size; k++ {
			s -= upper[k][i] * w[k]
		}
		w[i] = s / upper[i][i]
	}
	for i := 0; i < m; i++ {
		x := 0.0
		for k := range basis {
			x += w[k] * basis[k][i]
		}
		if math.Abs(x) < zeroBand {
			x = 0
		}
		if i > 0 {
			out.WriteString(" ")
		}
		fmt.Fprintf(out, "%.5f", x)
	}
	out.WriteString("\n")
}
