package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

const (
	small = 8   // pieces up to this size are checked triple by triple
	half  = 0.5 // a better triangle has every side shorter than half its perimeter
)

var (
	xs, ys []float64
	order  []int
	best   = math.Inf(1)
	answer = []int{0, 1, 2}
)

func dist(a, b int) float64 { return math.Hypot(xs[a]-xs[b], ys[a]-ys[b]) }

// triples tries every triple of pts, sorted by y, that fits within reach
// vertically.
func triples(pts []int, reach float64) {
	for i, a := range pts {
		top := ys[a] + reach
		for j := i + 1; j < len(pts) && ys[pts[j]] < top; j++ {
			for k := j + 1; k < len(pts) && ys[pts[k]] < top; k++ {
				b, c := pts[j], pts[k]
				if p := dist(a, b) + dist(b, c) + dist(c, a); p < best {
					best = p
					answer = []int{a, b, c}
					top = ys[a] + best*half
				}
			}
		}
	}
}

func byY(pts []int) {
	sort.Slice(pts, func(i, j int) bool { return ys[pts[i]] < ys[pts[j]] })
}

// solve handles the points order[lo:hi].
func solve(lo, hi int) {
	if hi-lo <= small {
		pts := append([]int(nil), order[lo:hi]...)
		byY(pts)
		triples(pts, math.Inf(1))
		return
	}
	mid := (lo + hi) / 2
	split := xs[order[mid]]
	solve(lo, mid)
	solve(mid, hi)
	// a better triangle across the split lies in a strip around it
	reach := best * half
	var strip []int
	for _, p := range order[lo:hi] {
		if math.Abs(xs[p]-split) < reach {
			strip = append(strip, p)
		}
	}
	byY(strip)
	triples(strip, reach)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n := next()
	xs, ys, order = make([]float64, n), make([]float64, n), make([]int, n)
	for i := 0; i < n; i++ {
		xs[i], ys[i] = float64(next()), float64(next())
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		a, b := order[i], order[j]
		if xs[a] != xs[b] {
			return xs[a] < xs[b]
		}
		return ys[a] < ys[b]
	})
	solve(0, n)
	fmt.Printf("%.6f\n%d %d %d\n", best, answer[0]+1, answer[1]+1, answer[2]+1)
}
