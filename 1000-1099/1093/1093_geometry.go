package main

import (
	"fmt"
	"math"
)

const (
	halfG = 5.0
	// tiny: coefficients this small count as zero
	tiny = 1e-12
	// eps: tolerance for times and for being strictly inside the rim
	eps = 1e-9
)

func main() {
	var cx, cy, cz, nx, ny, nz, r, sx, sy, sz, vx, vy, vz float64
	fmt.Scan(&cx, &cy, &cz, &nx, &ny, &nz, &r, &sx, &sy, &sz, &vx, &vy, &vz)
	dx, dy, dz := sx-cx, sy-cy, sz-cz
	// inside: the dart at time t, if that time has come, is strictly inside
	// the rim
	inside := func(t float64) bool {
		if t < -eps {
			return false
		}
		t = math.Max(t, 0)
		px, py, pz := dx+vx*t, dy+vy*t, dz+vz*t-halfG*t*t
		return px*px+py*py+pz*pz < r*r-eps
	}
	// the distance to the plane, times |N|, is a t^2 + 2 h t + c; a flight that
	// never crosses the plane, even one lying in it, misses
	a := -halfG * nz
	h := (nx*vx + ny*vy + nz*vz) / 2
	c := nx*dx + ny*dy + nz*dz
	hit := false
	if math.Abs(a) < tiny {
		hit = math.Abs(h) >= tiny && inside(-c/(2*h))
	} else if d := h*h - a*c; d >= -tiny {
		root := math.Sqrt(math.Max(d, 0))
		hit = inside((-h-root)/a) || inside((-h+root)/a)
	}
	if hit {
		fmt.Println("HIT")
	} else {
		fmt.Println("MISSED")
	}
}
