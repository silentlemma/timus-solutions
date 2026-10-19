package main

import (
	"fmt"
	"math"
)

const quad = 4 // the discriminant of a t^2 + b t + c is b^2 - 4 a c

// signSqrtVs compares sign * sqrt(disc) with the integer k exactly: -1, 0 or 1
func signSqrtVs(sign int, disc, k int64) int {
	cmp := func(a, b int64) int {
		if a > b {
			return 1
		}
		if a < b {
			return -1
		}
		return 0
	}
	if sign > 0 {
		if k < 0 {
			return 1
		}
		return cmp(disc, k*k)
	}
	if k > 0 {
		return -1
	}
	return cmp(k*k, disc)
}

type root struct {
	t       float64
	atDenis bool // Eugene is at Denis's place
}

func main() {
	var x, y, z, vx, vy, ex, ey int64
	fmt.Scan(&x, &y, &z, &vx, &vy, &ex, &ey)
	// Stewart: the point at fraction t of the way from Denis to the hall is at
	// squared distance (1 - t) X^2 + t Y^2 - t (1 - t) Z^2 from Vanya; Eugene is
	// at d^2, so t solves z2 t^2 + b t + c = 0 with integer coefficients
	d2 := (ex-vx)*(ex-vx) + (ey-vy)*(ey-vy)
	z2 := z * z
	b, c := y*y-x*x-z2, x*x-d2
	disc := b*b - quad*z2*c
	var found []root
	if disc >= 0 {
		for _, s := range []int{1, -1} {
			if s < 0 && disc == 0 {
				break
			}
			// t = (-b + s sqrt(disc)) / (2 z2) must lie in [0, 1]
			if signSqrtVs(s, disc, b) < 0 || signSqrtVs(s, disc, 2*z2+b) > 0 {
				continue
			}
			t := (float64(-b) + float64(s)*math.Sqrt(float64(disc))) / float64(2*z2)
			found = append(found, root{t, c == 0 && signSqrtVs(s, disc, b) == 0})
		}
	}
	// a model triangle: Vanya at 0, Denis on the x axis, the hall above it
	fx, fy := float64(x), float64(y)
	cosV := float64(x*x+y*y-z2) / (2 * fx * fy)
	hx, hy := fy*cosV, fy*math.Sqrt(math.Max(0, 1-cosV*cosV))
	ux, uy := float64(ex-vx), float64(ey-vy)
	var points [][2]float64
	for _, r := range found {
		px, py := fx+r.t*(hx-fx), r.t*hy
		for _, mirror := range []float64{1, -1} {
			if mirror < 0 && r.atDenis {
				break
			}
			// rotate (and maybe reflect) the model so that its point lands on Eugene
			qx, qy := px, mirror*py
			norm := qx*qx + qy*qy
			cosR, sinR := (qx*ux+qy*uy)/norm, (qx*uy-qy*ux)/norm
			points = append(points, [2]float64{float64(vx) + cosR*fx, float64(vy) + sinR*fx})
		}
	}
	fmt.Println(len(points))
	for _, p := range points {
		fmt.Printf("%.12f %.12f\n", p[0], p[1])
	}
}
