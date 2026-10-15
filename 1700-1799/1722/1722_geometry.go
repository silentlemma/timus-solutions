package main

import (
	"fmt"
	"math"
)

const percent = 100

func cross(ax, ay, bx, by float64) float64 {
	return ax*by - ay*bx
}

// signed area, positive for a counterclockwise triangle
func triangle(ax, ay, bx, by, cx, cy float64) float64 {
	return cross(bx-ax, by-ay, cx-ax, cy-ay) / 2
}

func main() {
	var big, small, near, x, y float64
	fmt.Scan(&big, &small, &near, &x, &y)
	d := math.Hypot(x, y)
	ux, uy := x/d, y/d
	// the outer common tangents touch both buildings at n * radius from
	// each center, n making cos = -k with the direction to the new one
	k := (near - small) / d
	s := math.Sqrt(1 - k*k)
	var tx, ty, ex, ey [2]float64
	for i, side := range []float64{-1, 1} {
		nx := -k*ux - side*s*uy
		ny := -k*uy + side*s*ux
		tx[i], ty[i] = x+near*nx, y+near*ny
		// the line runs away from the old building through the tangent
		// point, and leaves the city where |T + t D| = R
		dx, dy := x+(near-small)*nx, y+(near-small)*ny
		a := dx*dx + dy*dy
		b := tx[i]*dx + ty[i]*dy
		c := tx[i]*tx[i] + ty[i]*ty[i] - big*big
		t := (-b + math.Sqrt(b*b-a*c)) / a
		ex[i], ey[i] = tx[i]+t*dx, ty[i]+t*dy
	}
	// go around the hidden part counterclockwise: the arc of the new
	// building that faces the old one, the first tangent out to the city
	// border, along the border, the second tangent back
	area := math.Acos(k) * near * near
	area += triangle(x, y, tx[0], ty[0], ex[0], ey[0])
	area += triangle(x, y, ex[1], ey[1], tx[1], ty[1])
	turn := math.Atan2(cross(ex[0], ey[0], ex[1], ey[1]), ex[0]*ex[1]+ey[0]*ey[1])
	if turn < 0 {
		turn += 2 * math.Pi
	}
	// the border arc seen from the new center: a triangle plus the piece
	// of the city cut off by the chord
	area += triangle(x, y, ex[0], ey[0], ex[1], ey[1])
	area += turn*big*big/2 - triangle(0, 0, ex[0], ey[0], ex[1], ey[1])
	fmt.Printf("%.10f\n", percent*area/(math.Pi*big*big))
}
