package main

import (
	"fmt"
	"math"
)

func main() {
	var h, t, v, x float64
	fmt.Scan(&h, &t, &v, &x)
	// the least time climbs at x as long as possible and at full speed in
	// the remaining seconds; the most climbs just faster than x, or during
	// all t seconds when that is too slow to reach h
	least := math.Max(0, h-t*x) / (v - x)
	most := math.Min(t, h/x)
	fmt.Printf("%.6f %.6f\n", least, most)
}
