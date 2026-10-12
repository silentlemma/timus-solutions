package main

import (
	"fmt"
	"math"
)

const (
	turn            = 2 * math.Pi
	halfTurn        = 180.0
	fullTurnDegrees = 360.0
	roundOff        = 1e-15
)

// an arc angle in [0, 2 pi)
func ahead(angle float64) float64 {
	angle = math.Mod(angle, turn)
	if angle < 0 {
		angle += turn
	}
	return angle
}

// the second-circle centers, using power = d squared minus r squared
// to test whether the circles meet
func circleCross(r, cy, kx, ky, power float64) [][2]float64 {
	if power < 0 || power > 8*r*r {
		return nil
	}
	d := math.Hypot(kx, ky-cy)
	along := (4*r*r + power) / (2 * d)
	side := math.Sqrt(math.Max(0, power*(8*r*r-power))) / (2 * d)
	ux, uy := kx/d, (ky-cy)/d
	mx, my := ux*along, cy+uy*along
	return [][2]float64{{mx - uy*side, my + ux*side}, {mx + uy*side, my - ux*side}}
}

func shortest(x, y, heading, r, kx, ky float64) float64 {
	dx, dy := kx-x, ky-y
	if r*r == 0 || (dx == 0 && dy == 0) {
		return math.Hypot(dx, dy)
	}
	heading = math.Mod(heading, fullTurnDegrees)
	if heading < 0 {
		heading += fullTurnDegrees
	}
	quadrant := int(math.Floor(heading/90 + 0.5))
	heading = (heading - float64(quadrant)*90) * math.Pi / halfTurn
	kx = dx*math.Cos(heading) + dy*math.Sin(heading)
	ky = -dx*math.Sin(heading) + dy*math.Cos(heading)
	for i := 0; i < quadrant%4; i++ {
		kx, ky = ky, -kx
	}
	best := math.Inf(1)
	// sign 1 turns left (counter-clockwise), sign -1 turns right
	for _, sign := range []float64{1, -1} {
		cy := sign * r
		power := dx*dx + dy*dy - 2*cy*ky
		if power < 0 && power >= -roundOff*(dx*dx+dy*dy) {
			power = 0
		}
		// an arc, then straight along the tangent to the crumb
		if power >= 0 {
			run := math.Sqrt(power)
			leave := math.Atan2(kx, r-sign*ky) - math.Atan2(run, r)
			best = math.Min(best, r*ahead(leave)+run)
		}
		// an arc, then an arc the other way around a circle 2r further out
		// that passes through the crumb
		for _, o := range circleCross(r, cy, kx, ky, power) {
			first := ahead(math.Atan2(o[0], r-sign*o[1]))
			vx, vy := -o[0], cy-o[1] // the switch radius, doubled
			ex, ey := kx-o[0], ky-o[1]
			last := math.Atan2(-sign*(vx*ey-vy*ex), vx*ex+vy*ey)
			best = math.Min(best, r*(first+ahead(last)))
		}
	}
	return best
}

func main() {
	var x, y, a, r, kx, ky float64
	fmt.Scan(&x, &y, &a, &r, &kx, &ky)
	fmt.Printf("%.4f\n", shortest(x, y, a, math.Abs(r), kx, ky))
}
