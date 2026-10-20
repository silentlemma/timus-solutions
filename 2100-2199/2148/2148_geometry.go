package main

import (
	"fmt"
	"math"
)

func main() {
	var cx, cy, r, ax, ay, bx, by int64
	fmt.Scan(&cx, &cy, &r, &ax, &ay, &bx, &by)
	// The players are equally far from the centre, so the mirror point lies on
	// the bisector of the angle between them, in the direction w = A + B - 2C.
	wx, wy := ax+bx-2*cx, ay+by-2*cy
	// Both shots stay outside the tank exactly when each player is strictly
	// beyond the tangent line at that point: (A - C) . w > r |w|.
	dot := (ax-cx)*wx + (ay-cy)*wy
	norm := wx*wx + wy*wy
	if dot <= 0 || dot*dot <= r*r*norm {
		fmt.Println("No way")
		return
	}
	scale := float64(r) / math.Sqrt(float64(norm))
	fmt.Printf("%.9f %.9f\n", float64(cx)+float64(wx)*scale, float64(cy)+float64(wy)*scale)
}
