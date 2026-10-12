package main

import (
	"fmt"
	"math"
)

const MAX_ROPE = 30000

func main() {
	var ax, ay, bx, by, cx, cy, rope float64
	var token string
	fmt.Scan(&ax, &ay, &bx, &by, &cx, &cy, &token)
	for _, digit := range token {
		if digit < '0' || digit > '9' {
			continue
		}
		rope = math.Min(MAX_ROPE, rope*10+float64(digit-'0'))
		if rope == MAX_ROPE {
			break
		}
	}
	dx, dy := bx-ax, by-ay
	// the nearest point of the bed: C projected onto AB, kept inside it
	t, length := 0.0, dx*dx+dy*dy
	if length != 0 {
		t = math.Max(0, math.Min(1, ((cx-ax)*dx+(cy-ay)*dy)/length))
	}
	nearest := math.Hypot(ax+t*dx-cx, ay+t*dy-cy)
	farthest := math.Max(math.Hypot(ax-cx, ay-cy), math.Hypot(bx-cx, by-cy))
	fmt.Printf("%.2f\n%.2f\n", math.Max(0, nearest-rope), math.Max(0, farthest-rope))
}
