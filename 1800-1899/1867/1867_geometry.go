package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	n      int
	d      [][]int64
	xs, ys []int64
)

func isqrt(v int64) int64 {
	r := int64(math.Sqrt(float64(v)))
	for r*r > v {
		r--
	}
	for (r+1)*(r+1) <= v {
		r++
	}
	return r
}

// place puts atom 0 at the origin and atom p at (a, b); every other atom
// follows from its distances to these two up to a reflection in the line
// through them, and the first atom off that line picks the side by flip
func place(p int, a, b int64, flip bool) bool {
	big := a*a + b*b
	signs := []int64{1, -1}
	if flip {
		signs = []int64{-1, 1}
	}
	xs, ys = make([]int64, n), make([]int64, n)
	for i := 1; i < n; i++ {
		twice := d[0][i] - d[p][i] + big // twice the dot product with (a, b)
		if twice%2 != 0 {
			return false
		}
		dot := twice / 2
		square := big*d[0][i] - dot*dot // the cross product, squared
		if square < 0 {
			return false
		}
		cross := isqrt(square)
		if cross*cross != square {
			return false
		}
		done := false
		for _, sign := range signs {
			nx, ny := a*dot+b*sign*cross, b*dot-a*sign*cross
			if nx%big != 0 || ny%big != 0 {
				continue
			}
			x, y := nx/big, ny/big
			fits := true
			for j := 0; j < i && fits; j++ {
				fits = (x-xs[j])*(x-xs[j])+(y-ys[j])*(y-ys[j]) == d[i][j]
			}
			if fits {
				xs[i], ys[i] = x, y
				done = true
				break
			}
		}
		if !done {
			return false
		}
	}
	return true
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fscan(reader, &n)
	d = make([][]int64, n)
	for i := range d {
		d[i] = make([]int64, n)
		for j := range d[i] {
			fmt.Fscan(reader, &d[i][j])
		}
	}
	p := 0
	for i := 1; i < n && p == 0; i++ {
		if d[0][i] != 0 {
			p = i
		}
	}
	if p == 0 {
		// everything sits at the origin
		for _, row := range d {
			for _, v := range row {
				if v != 0 {
					fmt.Fprintln(writer, "Impossible")
					return
				}
			}
		}
		for i := 0; i < n; i++ {
			fmt.Fprintln(writer, "0 0")
		}
		return
	}
	big := d[0][p]
	// the symmetries of the grid bring atom p to (a, b) with 0 <= a <= b
	for a := int64(0); 2*a*a <= big; a++ {
		b := isqrt(big - a*a)
		if a*a+b*b != big {
			continue
		}
		for _, flip := range []bool{false, true} {
			if place(p, a, b, flip) {
				for i := 0; i < n; i++ {
					fmt.Fprintln(writer, xs[i], ys[i])
				}
				return
			}
		}
	}
	fmt.Fprintln(writer, "Impossible")
}
