package main

import (
	"fmt"
	"math"
)

const (
	corners = 3
	wide    = 2 * math.Pi / 3 // 120 degrees
)

func main() {
	var x, y, angle, side [corners]float64
	for i := 0; i < corners; i++ {
		fmt.Scan(&x[i], &y[i])
	}
	for i := 0; i < corners; i++ {
		b, c := (i+1)%corners, (i+2)%corners
		ux, uy, wx, wy := x[b]-x[i], y[b]-y[i], x[c]-x[i], y[c]-y[i]
		angle[i] = math.Atan2(math.Abs(ux*wy-uy*wx), ux*wx+uy*wy)
		side[i] = math.Hypot(x[c]-x[b], y[c]-y[b])
	}
	for i := 0; i < corners; i++ {
		if angle[i] >= wide {
			// a corner of at least 120 degrees is the best place itself
			fmt.Printf("%.8f %.8f\n", x[i], y[i])
			return
		}
	}
	// otherwise the Fermat point: every side is seen at 120 degrees, and its
	// barycentric weights are a / sin(A + 60 degrees) and so on
	total, fx, fy := 0.0, 0.0, 0.0
	for i := 0; i < corners; i++ {
		w := side[i] / math.Sin(angle[i]+math.Pi/corners)
		total += w
		fx += w * x[i]
		fy += w * y[i]
	}
	fmt.Printf("%.8f %.8f\n", fx/total, fy/total)
}
