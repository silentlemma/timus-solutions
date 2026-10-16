package main

import (
	"fmt"
	"math/bits"
)

const (
	corners = 3
	points  = 5
)

func abs(v int64) uint64 {
	if v < 0 {
		return uint64(-v)
	}
	return uint64(v)
}

// lessOrEqual reports whether a * b <= c * d for non-negative values, using the
// full 128-bit products
func lessOrEqual(a, b, c, d uint64) bool {
	hi1, lo1 := bits.Mul64(a, b)
	hi2, lo2 := bits.Mul64(c, d)
	return hi1 < hi2 || hi1 == hi2 && lo1 <= lo2
}

func main() {
	var mana, h, top int64
	if _, err := fmt.Scan(&mana, &h, &top); err != nil {
		return
	}
	var x, y [points]int64
	for i := 0; i < points; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	// after flying up, mana - h is left for the radius, and the field must
	// reach the nearest of the floor and the three walls
	spare := mana - h
	ok := spare >= h
	for i := 1; i <= corners && spare >= 0; i++ {
		j := i%corners + 1
		ux, uy := x[j]-x[i], y[j]-y[i]
		wx, wy, wz := x[corners+1]-x[i], y[corners+1]-y[i], top
		nx, ny, nz := uy*wz, -ux*wz, ux*wy-uy*wx
		reach := abs(nx*(x[0]-x[i]) + ny*(y[0]-y[i]) + nz*h)
		// the distance to the wall is reach / |normal|, compared exactly
		length := uint64(nx*nx + ny*ny + nz*nz)
		if lessOrEqual(reach, reach, uint64(spare*spare), length) {
			ok = true
		}
	}
	if ok && spare >= 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
