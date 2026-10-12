package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	halfTurn = 180.0
	most     = 4.0 // the longest squared chord, between opposite points
	bits     = 64
)

type point struct{ x, y, z float64 }

// the point on the unit sphere
func unit(latitude, longitude float64) point {
	a, b := latitude*math.Pi/halfTurn, longitude*math.Pi/halfTurn
	return point{math.Cos(a) * math.Cos(b), math.Cos(a) * math.Sin(b), math.Sin(a)}
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() float64 {
		sc.Scan()
		v, _ := strconv.ParseFloat(sc.Text(), bits)
		return v
	}
	n, m, r := int(next()), int(next()), next()
	pads := make([]point, m)
	for i := range pads {
		w := next()
		pads[i] = unit(w, next())
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < n; i++ {
		w := next()
		q := unit(w, next())
		// the nearest pad has the shortest chord through the planet
		best := most
		for _, p := range pads {
			dx, dy, dz := q.x-p.x, q.y-p.y, q.z-p.z
			if chord := dx*dx + dy*dy + dz*dz; chord < best {
				best = chord
			}
		}
		half := math.Min(1, math.Sqrt(best)/2)
		fmt.Fprintf(out, "%.2f\n", 2*r*math.Asin(half))
	}
}
