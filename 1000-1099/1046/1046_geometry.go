package main

import (
	"bufio"
	"fmt"
	"math"
	"math/cmplx"
	"os"
)

const (
	halfTurn = 180
	rounding = 0.005
)

// clean prints a value that would print as -0.00 as 0.00
func clean(v float64) float64 {
	if math.Abs(v) < rounding {
		return 0
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	apex := make([]complex128, n)
	turn := make([]complex128, n)
	for i := range apex {
		var x, y float64
		fmt.Fscan(in, &x, &y)
		apex[i] = complex(x, y)
	}
	for i := range turn {
		var degrees float64
		fmt.Fscan(in, &degrees)
		turn[i] = cmplx.Rect(1, degrees*math.Pi/halfTurn)
	}
	// a step turns z around M[i] by its angle, z -> w z + (1 - w) M[i], and going
	// around the polygon composes the steps into z -> a z + b that fixes A[0]
	a, b := complex(1, 0), complex(0, 0)
	for i := 0; i < n; i++ {
		a = turn[i] * a
		b = turn[i]*b + (1-turn[i])*apex[i]
	}
	// the angles never add up to a multiple of 360, so a != 1
	z := b / (1 - a)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for i := 0; i < n; i++ {
		fmt.Fprintf(w, "%.2f %.2f\n", clean(real(z)), clean(imag(z)))
		z = apex[i] + turn[i]*(z-apex[i])
	}
}
