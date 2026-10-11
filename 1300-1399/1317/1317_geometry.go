package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const eps = 1e-9

// side holds an outward normal and an offset: inside the lot nx x + ny y <= c
type side struct{ nx, ny, c float64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var h float64
	fmt.Fscan(in, &n, &h)
	xs, ys := make([]float64, n), make([]float64, n)
	for i := range xs {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	var d, lx, ly float64
	fmt.Fscan(in, &d, &lx, &ly)
	area := 0.0
	for i := 0; i < n; i++ {
		area += xs[i]*ys[(i+1)%n] - xs[(i+1)%n]*ys[i]
	}
	if area < 0 {
		for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
			xs[i], xs[j] = xs[j], xs[i]
			ys[i], ys[j] = ys[j], ys[i]
		}
	}
	sides := make([]side, n)
	for i := range sides {
		j := (i + 1) % n
		nx, ny := ys[j]-ys[i], xs[i]-xs[j]
		sides[i] = side{nx, ny, nx*xs[i] + ny*ys[i]}
	}
	var k int
	fmt.Fscan(in, &k)
	shot := 0
	for s := 0; s < k; s++ {
		var px, py float64
		fmt.Fscan(in, &px, &py)
		r := math.Hypot(px-lx, py-ly)
		inside := true
		for _, e := range sides {
			if e.nx*px+e.ny*py > e.c+eps*math.Hypot(e.nx, e.ny)*(r+1) {
				inside = false
			}
		}
		if inside {
			shot++ // over the lot the laser always reaches it in time
			continue
		}
		// the beam leaves the lot at horizontal distance a and must clear
		// the fence there, so it meets the stone no lower than h r / a
		ux, uy, a := (px-lx)/r, (py-ly)/r, math.Inf(1)
		for _, e := range sides {
			if toward := e.nx*ux + e.ny*uy; toward > 0 {
				a = math.Min(a, (e.c-e.nx*lx-e.ny*ly)/toward)
			}
		}
		if r*r*(a*a+h*h) <= d*d*a*a*(1+eps) {
			shot++
		}
	}
	fmt.Println(shot)
}
