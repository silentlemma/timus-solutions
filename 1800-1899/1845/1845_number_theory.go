package main

import (
	"bufio"
	"fmt"
	"os"
)

type gauss struct {
	re, im int64
}

func sub(a, b gauss) gauss { return gauss{a.re - b.re, a.im - b.im} }

func mul(a, b gauss) gauss {
	return gauss{a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re}
}

func norm(a gauss) int64 { return a.re*a.re + a.im*a.im }

func floorDiv(a, b int64) int64 {
	q := a / b
	if a%b != 0 && (a < 0) != (b < 0) {
		q--
	}
	return q
}

// quotient returns x / y rounded to the nearest Gaussian integer in both parts
func quotient(x, y gauss) gauss {
	n := norm(y)
	re, im := x.re*y.re+x.im*y.im, x.im*y.re-x.re*y.im
	return gauss{floorDiv(2*re+n, 2*n), floorDiv(2*im+n, 2*n)}
}

// remainder returns what is left of x after taking away the nearest
// multiple of p: its norm is at most half the norm of p
func remainder(x, p gauss) gauss { return sub(x, mul(p, quotient(x, p))) }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	a := make([][]gauss, n)
	for i := range a {
		a[i] = make([]gauss, n)
		for j := range a[i] {
			fmt.Fscan(in, &a[i][j].re, &a[i][j].im)
		}
	}
	var p gauss
	fmt.Fscan(in, &p.re, &p.im)
	for i := range a {
		for j := range a[i] {
			a[i][j] = remainder(a[i][j], p)
		}
	}
	// elimination modulo p: the Euclidean algorithm on the Gaussian
	// integers clears each column below the diagonal with row operations,
	// which keep the determinant; the entries of the column only shrink
	det := gauss{1, 0}
	for k := 0; k < n; k++ {
		for i := k + 1; i < n; i++ {
			for a[i][k] != (gauss{}) {
				q := quotient(a[k][k], a[i][k])
				a[k][k] = sub(a[k][k], mul(q, a[i][k]))
				for j := k + 1; j < n; j++ {
					a[k][j] = remainder(sub(a[k][j], mul(q, a[i][j])), p)
				}
				a[k], a[i] = a[i], a[k]
				det = gauss{-det.re, -det.im}
			}
		}
		det = remainder(mul(det, a[k][k]), p)
	}
	fmt.Println(det.re, det.im)
}
