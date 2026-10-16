package main

import (
	"fmt"
	"math"
)

const (
	gravity     = 9.81
	centimetres = 100
	seconds     = 60
	steps       = 100
	turn        = 4
)

func main() {
	var length, height, turns float64
	if _, err := fmt.Scan(&length, &height, &turns); err != nil {
		return
	}
	half := length / centimetres / 2
	top := height / centimetres
	omega := turns * 2 * math.Pi / seconds
	quarter := math.Pi / 2 / omega
	// the height of the lowest end of the toast at time t
	gap := func(t float64) float64 {
		return top - gravity*t*t/2 - half*math.Abs(math.Sin(omega*t))
	}
	// d gap / dt in quarter k, where the angle within the half turn is
	// omega*t - (k / 2)*pi
	slope := func(t float64, k int) float64 {
		return -gravity*t - half*omega*math.Cos(omega*t-float64(k/2)*math.Pi)
	}
	// d slope / dt, falling through an odd quarter
	bend := func(t float64, k int) float64 {
		return -gravity + half*omega*omega*math.Sin(omega*t-float64(k/2)*math.Pi)
	}
	k := 0
	for {
		a, b := float64(k)*quarter, float64(k+1)*quarter
		lowest := gap(b)
		if k%2 == 1 {
			// the end rises again here: the slope of the gap is concave, so
			// find its peak; where it turns positive, the gap has a minimum
			lo, hi := a, b
			for i := 0; i < steps; i++ {
				mid := (lo + hi) / 2
				if bend(mid, k) > 0 {
					lo = mid
				} else {
					hi = mid
				}
			}
			if slope(lo, k) > 0 {
				lo, hi = a, lo
				for i := 0; i < steps; i++ {
					mid := (lo + hi) / 2
					if slope(mid, k) < 0 {
						lo = mid
					} else {
						hi = mid
					}
				}
				lowest = math.Min(lowest, gap(lo))
			}
		}
		if lowest <= 0 {
			break
		}
		k++
	}
	// in quarters 0 and 3 of a turn the butter faces down
	if inTurn := k % turn; inTurn == 0 || inTurn == turn-1 {
		fmt.Println("butter")
	} else {
		fmt.Println("bread")
	}
}
