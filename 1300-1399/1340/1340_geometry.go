package main

import (
	"fmt"
	"math"
)

const (
	turn     = 2 * math.Pi
	eps      = 1e-9
	halfTurn = 180.0
)

// an arc angle in [0, 2 pi), with angles a hair below a full turn taken
// as no turn at all
func ahead(angle float64) float64 {
	angle = math.Mod(angle, turn)
	if angle < 0 {
		angle += turn
	}
	if angle > turn-eps {
		return 0
	}
	return angle
}

// the points where the circles around a and b of radii ra and rb meet
func circleCross(ax, ay, ra, bx, by, rb float64) [][2]float64 {
	d := math.Hypot(bx-ax, by-ay)
	if d == 0 || d > ra+rb+eps || d < math.Abs(ra-rb)-eps {
		return nil
	}
	along := (ra*ra - rb*rb + d*d) / (2 * d)
	side := math.Sqrt(math.Max(0, ra*ra-along*along))
	ux, uy := (bx-ax)/d, (by-ay)/d
	mx, my := ax+ux*along, ay+uy*along
	return [][2]float64{{mx - uy*side, my + ux*side}, {mx + uy*side, my - ux*side}}
}

func shortest(x, y, heading, r, kx, ky float64) float64 {
	if r == 0 {
		return math.Hypot(kx-x, ky-y)
	}
	best := math.Inf(1)
	// sign 1 turns left (counter-clockwise), sign -1 turns right
	for _, sign := range []float64{1, -1} {
		cx, cy := x-sign*r*math.Sin(heading), y+sign*r*math.Cos(heading)
		start := math.Atan2(y-cy, x-cx) // where the cockroach is on the circle
		// an arc, then straight along the tangent to the crumb
		if d := math.Hypot(kx-cx, ky-cy); d >= r-eps {
			run := math.Sqrt(math.Max(0, d*d-r*r))
			leave := math.Atan2(ky-cy, kx-cx) - sign*math.Acos(math.Min(1, r/d))
			best = math.Min(best, r*ahead(sign*(leave-start))+run)
		}
		// an arc, then an arc the other way around a circle 2r further out
		// that passes through the crumb
		for _, o := range circleCross(cx, cy, 2*r, kx, ky, r) {
			sw := math.Atan2(o[1]-cy, o[0]-cx)
			first := ahead(sign * (sw - start))
			back := sw + math.Pi // the switch point seen from the new center
			end := math.Atan2(ky-o[1], kx-o[0])
			best = math.Min(best, r*(first+ahead(-sign*(end-back))))
		}
	}
	return best
}

func main() {
	var x, y, a, r, kx, ky float64
	fmt.Scan(&x, &y, &a, &r, &kx, &ky)
	fmt.Printf("%.4f\n", shortest(x, y, a*math.Pi/halfTurn, math.Abs(r), kx, ky))
}
