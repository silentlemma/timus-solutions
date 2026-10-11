package main

import (
	"fmt"
	"math"
)

const (
	rolls = 70
	dirs  = 6
	turn  = 60.0 // degrees between neighbouring directions
	off   = 80   // coordinates stay within rolls of the origin
	size  = 2*off + 1
)

const degree = math.Pi / 180

// ua and ub are the six directions of a hexagonal lattice, as integer
// combinations of the first two of them
var ua = [dirs]int{1, 0, -1, -1, 0, 1}
var ub = [dirs]int{0, 1, 1, 0, -1, -1}

// classes holds the starting edges at 0 and 180, or at 90 and 270 degrees
var classes = []float64{0, 90}

type state struct{ a, b, d int }

func main() {
	var tx, ty float64
	fmt.Scan(&tx, &ty)
	// a jump through the base in half steps: (1 + sqrt 3) / 2 = 1/2 + sin 60
	side := (1 + 2*math.Sin(turn*degree)) / 2
	best := math.Hypot(tx, ty) // no rolls at all
	for _, start := range classes {
		var wx, wy [dirs]float64
		for k := 0; k < dirs; k++ {
			angle := (start + turn*float64(k)) * degree
			wx[k], wy[k] = math.Cos(angle), math.Sin(angle)
		}
		// a state is a triangle lying on the table: twice its apex position
		// (in steps of the base jump) and the direction from the apex to the
		// base edge; it costs one roll to reach from the start
		var cost [size][size][dirs]int
		for a := range cost {
			for b := range cost[a] {
				for d := range cost[a][b] {
					cost[a][b][d] = rolls
				}
			}
		}
		buckets := make([][]state, rolls+1)
		for _, u := range []int{0, dirs / 2} {
			s := state{ua[u], ub[u], (u + dirs/2) % dirs}
			cost[s.a+off][s.b+off][s.d] = 1
			buckets[1] = append(buckets[1], s)
		}
		for c := 1; c < rolls; c++ {
			for i := 0; i < len(buckets[c]); i++ {
				s := buckets[c][i]
				if cost[s.a+off][s.b+off][s.d] != c {
					continue
				}
				// roll onto the base: its centre is half a step beyond the apex
				ea, eb := float64(s.a+ua[s.d]), float64(s.b+ub[s.d])
				x := side * (ea*wx[0] + eb*wx[1])
				y := side * (ea*wy[0] + eb*wy[1])
				best = math.Min(best, math.Hypot(x-tx, y-ty))
				next := []state{
					{s.a, s.b, (s.d + 1) % dirs},
					{s.a, s.b, (s.d + dirs - 1) % dirs},
					{s.a + 2*ua[s.d], s.b + 2*ub[s.d], (s.d + dirs/2) % dirs},
				}
				add := []int{1, 1, 2} // a side face is one roll, the base two
				for k, n := range next {
					nc := c + add[k]
					if nc < rolls && cost[n.a+off][n.b+off][n.d] > nc {
						cost[n.a+off][n.b+off][n.d] = nc
						buckets[nc] = append(buckets[nc], n)
					}
				}
			}
		}
	}
	fmt.Printf("%.4f\n", best)
}
