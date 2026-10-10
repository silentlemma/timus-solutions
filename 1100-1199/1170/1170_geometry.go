package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

// dir is a direction (y, x) through a corner, kept in lowest terms
type dir [2]int64

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

var events = map[dir][2]int64{}

func term(start, end dir, dp, dq int64) {
	for k, d := range []dir{start, end} {
		g := gcd(d[0], d[1])
		key := dir{d[0] / g, d[1] / g}
		sign := int64(1 - 2*k)
		e := events[key]
		events[key] = [2]int64{e[0] + sign*dp, e[1] + sign*dq}
	}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	type rect struct{ x1, y1, x2, y2, c int64 }
	rects := make([]rect, n)
	for i := range rects {
		r := &rects[i]
		fmt.Fscan(in, &r.x1, &r.y1, &r.x2, &r.y2, &r.c)
	}
	var c0, length int64
	fmt.Fscan(in, &c0, &length)
	// walking at angle t, a vertical line x = a is crossed after a/cos t and a
	// horizontal one y = b after b/sin t; a rectangle adds (c - c0) times
	// (exit - entry), a sum of such terms, each valid between two corners
	for _, r := range rects {
		w := r.c - c0
		// out through the right side or the top, in through the left or the bottom
		term(dir{r.y1, r.x2}, dir{r.y2, r.x2}, w*r.x2, 0)
		term(dir{r.y2, r.x2}, dir{r.y2, r.x1}, 0, w*r.y2)
		term(dir{r.y1, r.x1}, dir{r.y2, r.x1}, -w*r.x1, 0)
		term(dir{r.y1, r.x2}, dir{r.y1, r.x1}, 0, -w*r.y1)
	}
	order := make([]dir, 0, len(events))
	for d := range events {
		order = append(order, d)
	}
	sort.Slice(order, func(i, j int) bool {
		return order[i][0]*order[j][1] < order[j][0]*order[i][1]
	})
	// below the lowest corner no rectangle is met at all
	bestCost := float64(c0 * length)
	bestT := math.Atan2(float64(order[0][0]), float64(order[0][1])) / 2
	// between corners the time is c0*L + p/cos t + q/sin t: with p, q > 0 it
	// is above c0*L, otherwise monotone or concave, so corners are enough
	var p, q int64
	for _, d := range order {
		t := math.Atan2(float64(d[0]), float64(d[1]))
		cost := float64(c0*length) + float64(p)/math.Cos(t) + float64(q)/math.Sin(t)
		if cost < bestCost {
			bestCost, bestT = cost, t
		}
		p += events[d][0]
		q += events[d][1]
	}
	l := float64(length)
	fmt.Printf("%.6f\n%.6f %.6f\n", bestCost, l*math.Cos(bestT), l*math.Sin(bestT))
}
