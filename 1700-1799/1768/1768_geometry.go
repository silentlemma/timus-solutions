package main

import (
	"bufio"
	"fmt"
	"math"
	"math/cmplx"
	"os"
)

// eps: a wrong set must move by 1e-5 to become right, so one turn misses by
// more than 1e-5 / n, while right sets given to 1e-10 miss by far less
const eps = 1e-8

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	z := make([]complex128, n)
	var centre complex128
	for i := 0; i < n; i++ {
		var x, y float64
		fmt.Fscan(reader, &x, &y)
		z[i] = complex(x, y)
		centre += z[i]
	}
	centre /= complex(float64(n), 0)
	for i := range z {
		z[i] -= centre
	}
	// the vertices of a regular polygon in order turn into each other by a
	// rotation of 2 pi / n about the centre, one way or the other
	ok := false
	if cmplx.Abs(z[0]) > eps {
		for _, way := range []float64{1, -1} {
			turn := cmplx.Rect(1, way*2*math.Pi/float64(n))
			all := true
			for i := 0; i < n; i++ {
				if cmplx.Abs(z[(i+1)%n]-turn*z[i]) > eps {
					all = false
				}
			}
			if all {
				ok = true
			}
		}
	}
	if ok {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
