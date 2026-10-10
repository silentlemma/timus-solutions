package main

import (
	"fmt"
	"math"
	"sort"
)

const (
	// reach: a draught is hit when its centre is this close to the path of
	// the centre of the moving one, two radii of 0.4
	reach  = 0.8
	eps    = 1e-9
	side   = 8
	pieces = 2 * side
)

var kills [pieces][]int
var memo []int8 // -1 unknown, else whether the player to move wins

// wins tells whether the player to move, red (0) or white (1), wins
func wins(alive, turn int) bool {
	key := alive<<1 | turn
	if memo[key] >= 0 {
		return memo[key] == 1
	}
	mask := 1<<side - 1
	if turn == 1 {
		mask <<= side
	}
	own := alive & mask
	result := false
	for p := 0; p < pieces && !result; p++ {
		if own>>p&1 == 1 {
			for _, s := range kills[p] {
				if !wins(alive&^s, 1-turn) {
					result = true
					break
				}
			}
		}
	}
	memo[key] = 0
	if result {
		memo[key] = 1
	}
	return result
}

func main() {
	var x, y [pieces]float64
	for k := 0; k < pieces; k++ {
		fmt.Scan(&x[k], &y[k])
	}
	// every direction kills the draughts within reach of its ray; the set
	// changes only where the ray becomes tangent to some draught, so the
	// tangent directions and the gaps between them give every possible set
	for p := 0; p < pieces; p++ {
		var angles []float64
		for q := 0; q < pieces; q++ {
			if q != p {
				d := math.Hypot(x[q]-x[p], y[q]-y[p])
				centre := math.Atan2(y[q]-y[p], x[q]-x[p])
				half := math.Asin(math.Min(1, reach/d))
				for _, a := range []float64{centre - half, centre + half} {
					angles = append(angles, math.Mod(a+2*math.Pi, 2*math.Pi))
				}
			}
		}
		sort.Float64s(angles)
		tries := append([]float64{}, angles...)
		for k := range angles {
			next := angles[0] + 2*math.Pi
			if k+1 < len(angles) {
				next = angles[k+1]
			}
			tries = append(tries, (angles[k]+next)/2)
		}
		seen := map[int]bool{}
		for _, t := range tries {
			ux, uy := math.Cos(t), math.Sin(t)
			mask := 1 << p
			for q := 0; q < pieces; q++ {
				dx, dy := x[q]-x[p], y[q]-y[p]
				if q != p && dx*ux+dy*uy >= 0 && math.Abs(dx*uy-dy*ux) <= reach+eps {
					mask |= 1 << q
				}
			}
			if !seen[mask] {
				seen[mask] = true
				kills[p] = append(kills[p], mask)
			}
		}
		sort.Ints(kills[p])
	}
	memo = make([]int8, 1<<(pieces+1))
	for k := range memo {
		memo[k] = -1
	}
	if wins(1<<pieces-1, 0) {
		fmt.Println("RED")
	} else {
		fmt.Println("WHITE")
	}
}
