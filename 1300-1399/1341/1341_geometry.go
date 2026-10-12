package main

import (
	"fmt"
	"math"
)

const (
	radius   = 6400.0
	halfTurn = 180.0
	shownAt  = 0.0005 // values that print as 0.000
)

// three decimals, without a minus sign on zero
func show(value float64) {
	if math.Abs(value) < shownAt {
		value = 0
	}
	fmt.Printf("%.3f\n", value)
}

func main() {
	var w, lon, side float64
	fmt.Scan(&w, &lon, &side)
	arc := side / radius // the angle of one side seen from the center
	south := w * math.Pi / halfTurn
	north := south + arc
	// north and south along meridians cancel; east runs along the northern
	// parallel and west along the southern one, at different speeds
	lon += (arc/math.Cos(north) - arc/math.Cos(south)) * halfTurn / math.Pi
	lon = math.Mod(lon, 2*halfTurn)
	if lon > halfTurn {
		lon -= 2 * halfTurn
	} else if lon <= -halfTurn {
		lon += 2 * halfTurn
	}
	show(w)
	show(lon)
}
