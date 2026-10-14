package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	eps      = 1e-12 // events closer than this in angle happen together
	percent  = 100
	half     = 0.5
	mostHits = 5 // an arrow stops after the fifth cow
	enter    = 0 // at one angle, rays start touching before they stop
	leave    = 1
)

var tau = 2 * math.Pi

type event struct {
	angle float64
	kind  int
}

// norm returns the angle in [0, 2 pi); a tiny negative angle may round up to 2 pi
func norm(a float64) float64 {
	a = math.Mod(a, tau)
	if a < 0 {
		a += tau
	}
	if a >= tau {
		return 0
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	number := func() float64 {
		var v float64
		fmt.Fscan(in, &v)
		return v
	}
	n, k, p := int(number()), int(number()), int64(number())
	r, vx, vy := number(), number(), number()
	// expected hits of an arrow whose ray meets m cows, kept exact as integers
	// in units of 1 / 100^4: each further cow adds p / 100 of the last addition
	scale := int64(1)
	for m := 1; m < mostHits; m++ {
		scale *= percent
	}
	gain := make([]int64, n+1)
	term := scale
	for m := 1; m <= n; m++ {
		gain[m] = gain[m-1]
		if m <= mostHits {
			gain[m] += term
		}
		if m < mostHits {
			term = term / percent * p
		}
	}
	turn := make([]float64, k)
	for i := range turn {
		turn[i] = norm(math.Atan(float64(i)/float64(k-1) - half))
	}
	// the angle a seen by arrow i: the events of one arrow come in this order
	turned := func(a float64, i int) float64 {
		if a >= turn[i] {
			return a - turn[i]
		}
		return a - turn[i] + tau
	}
	// rays meet a cow at angles within asin(R / d) of its centre, and
	// each arrow sees the same angular intervals turned back by its offset
	base := make([]event, 2*n)
	count := make([]int, k)
	for j := 0; j < n; j++ {
		x, y := number()-vx, number()-vy
		centre, width := math.Atan2(y, x), math.Asin(math.Min(1, r/math.Hypot(x, y)))
		base[2*j] = event{norm(centre - width), enter}
		base[2*j+1] = event{norm(centre + width), leave}
		// the intervals that wrap hold the angle 0 of the arrow
		for i := 0; i < k; i++ {
			if turned(base[2*j].angle, i) > turned(base[2*j+1].angle, i) {
				count[i]++
			}
		}
	}
	sort.Slice(base, func(a, b int) bool {
		if base[a].angle != base[b].angle {
			return base[a].angle < base[b].angle
		}
		return base[a].kind < base[b].kind
	})
	size := 2 * n
	// arrow i takes the sorted events from cut[i] on, wrapping around once
	cut, used := make([]int, k), make([]int, k)
	for i := range cut {
		cut[i] = sort.Search(size, func(e int) bool { return base[e].angle >= turn[i] })
	}
	at := func(i int) event { return base[(cut[i]+used[i])%size] }
	// the arrow whose next event comes first, or -1 when all are done
	pick := func() int {
		choice, angle, kind := -1, 0.0, 0
		for i := 0; i < k; i++ {
			if used[i] == size {
				continue
			}
			e := at(i)
			a := turned(e.angle, i)
			if choice < 0 || a < angle || (a == angle && e.kind < kind) {
				choice, angle, kind = i, a, e.kind
			}
		}
		return choice
	}
	best, total, bestAngle := int64(-1), int64(0), 0.0
	for i := 0; i < k; i++ {
		total += gain[count[i]]
	}
	var leaving []int
	next := pick()
	first := turned(at(next).angle, next)
	for next >= 0 {
		x := turned(at(next).angle, next)
		leaving = leaving[:0]
		for next >= 0 && turned(at(next).angle, next)-x <= eps {
			if at(next).kind == enter {
				total += gain[count[next]+1] - gain[count[next]]
				count[next]++
			} else {
				leaving = append(leaving, next)
			}
			used[next]++
			next = pick()
		}
		// at the angle itself, touching counts: new cows join, none leave yet
		point := total
		for _, i := range leaving {
			count[i]--
			total -= gain[count[i]+1] - gain[count[i]]
		}
		// after the last event the stretch runs on past 2 pi to the first one
		following := tau + first
		if next >= 0 {
			following = turned(at(next).angle, next)
		}
		// an open stretch is safer than a single tangent angle, so it wins ties
		if following-x > eps && total >= best {
			best, bestAngle = total, (x+following)/2
		}
		if point > best {
			best, bestAngle = point, x
		}
	}
	fmt.Printf("The best shot at (%.10f;%.10f) gives Vasya %.4f average hits.\n",
		math.Cos(bestAngle), math.Sin(bestAngle), float64(best)/float64(scale))
}
