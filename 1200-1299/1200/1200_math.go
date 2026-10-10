package main

import (
	"fmt"
	"math"
)

const (
	cents = 100
	peak  = 2 * cents
)

func main() {
	var fa, fb float64
	var k int64
	fmt.Scan(&fa, &fb, &k)
	a, b := int64(math.Round(fa*cents)), int64(math.Round(fb*cents))
	// everything is in kopecks: x horns earn a * x - 100 * x^2
	best, bestX, bestY := int64(-1), int64(0), int64(0)
	yPeak := int64(0)
	if b > 0 {
		yPeak = b / peak
	}
	min := func(p, q int64) int64 {
		if p < q {
			return p
		}
		return q
	}
	for x := int64(0); x <= k; x++ {
		room, gainX := k-x, a*x-cents*x*x
		// the hoof profit is concave in y, so the best y is next to its peak
		for _, y := range []int64{min(yPeak, room), min(yPeak+1, room)} {
			total := gainX + b*y - cents*y*y
			if total > best {
				best, bestX, bestY = total, x, y
			}
		}
	}
	fmt.Printf("%d.%02d\n%d %d\n", best/cents, best%cents, bestX, bestY)
}
