package main

import (
	"fmt"
	"math"
	"math/bits"
)

const quarters = 4

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

// atLeast tells whether p*q >= r*s for nonnegative 64-bit values
func atLeast(p, q, r, s int64) bool {
	hi1, lo1 := bits.Mul64(uint64(p), uint64(q))
	hi2, lo2 := bits.Mul64(uint64(r), uint64(s))
	return hi1 > hi2 || hi1 == hi2 && lo1 >= lo2
}

// columnSum is the sum of isqrt(n - x*x) over x = 0 .. m, where
// 2*m*m <= n, found by walking from m to the left along the upper hull
// of the lattice points in the disk.
func columnSum(n, m int64) int64 {
	inside := func(px, py int64) bool { return px >= 0 && px*px+py*py <= n }
	x, y := m, isqrt(n-m*m)
	total := y
	// a vector (a, b) moves a columns left and b rows up
	stack := [][2]int64{{1, 0}, {1, 1}}
	for x > 0 {
		a1, b1 := stack[len(stack)-1][0], stack[len(stack)-1][1]
		stack = stack[:len(stack)-1]
		for inside(x-a1, y+b1) {
			// the columns x - a1 .. x - 1 lie under this hull edge
			total += a1*y + (a1-1)*(b1-1)/2 + b1
			x -= a1
			y += b1
		}
		if x-a1 < 0 {
			break
		}
		a2, b2 := a1, b1
		for {
			a1, b1 = stack[len(stack)-1][0], stack[len(stack)-1][1]
			if inside(x-a1, y+b1) {
				break
			}
			a2, b2 = a1, b1
			stack = stack[:len(stack)-1]
		}
		for {
			a12, b12 := a1+a2, b1+b2
			nx := x - a12
			if nx < 0 {
				break
			}
			if inside(nx, y+b12) {
				stack = append(stack, [2]int64{a12, b12})
				a1, b1 = a12, b12
			} else {
				// from the outside point nx, steps of (a1, b1) rise at
				// least as fast as the circle, so no inside point lies
				// between
				if atLeast(b1*b1, n-nx*nx, a1*a1, nx*nx) {
					break
				}
				a2, b2 = a12, b12
			}
		}
	}
	for column := int64(0); column < x; column++ {
		total += isqrt(n - column*column)
	}
	return total
}

func main() {
	var radius int64
	if _, err := fmt.Scan(&radius); err != nil {
		return
	}
	// slab (x, y) of the first quarter burns when its nearest corner is
	// strictly inside the circle: x*x + y*y <= radius^2 - 1
	n := radius*radius - 1
	m := isqrt(n / 2)
	total := columnSum(n, m)
	// points with x < y twice, then the diagonal once
	quarter := 2*(total-m*(m+1)/2) + m + 1
	fmt.Println(quarters * quarter)
}
