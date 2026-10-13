package main

import (
	"fmt"
	"math"
)

func angle(px, ax, ay, bx, by float64) float64 {
	ux, uy, vx, vy := ax-px, ay, bx-px, by
	return math.Atan2(math.Abs(ux*vy-uy*vx), ux*vx+uy*vy)
}

func main() {
	var x1, y1, x2, y2 int64
	fmt.Scan(&x1, &y1, &x2, &y2)
	var best float64
	switch {
	case y1*y2 < 0 || (y1*y2 == 0 && x1 != x2):
		best = math.Pi // stand on the billboard itself
	case y1*y2 == 0:
		best = math.Pi / 2 // a vertical billboard standing on the road
	default:
		if y1 < 0 {
			y1, y2 = -y1, -y2
		}
		var spots []float64
		if y1 == y2 {
			spots = []float64{float64(x1+x2) / 2}
		} else {
			// the best spot is where a circle through both ends touches the road:
			// its distance from where the billboard's line meets the road is sqrt(QA * QB)
			qx := float64(x1) - float64(y1*(x2-x1))/float64(y2-y1)
			qa := math.Hypot(float64(x1)-qx, float64(y1))
			qb := math.Hypot(float64(x2)-qx, float64(y2))
			reach := math.Sqrt(qa * qb)
			spots = []float64{qx - reach, qx + reach}
		}
		for _, p := range spots {
			best = math.Max(best, angle(p, float64(x1), float64(y1), float64(x2), float64(y2)))
		}
	}
	fmt.Printf("%.6f\n", best)
}
