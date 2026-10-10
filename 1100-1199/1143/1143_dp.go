package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	x := make([]float64, n)
	y := make([]float64, n)
	for k := 0; k < n; k++ {
		fmt.Fscan(in, &x[k], &y[k])
	}
	dist := func(a, b int) float64 { return math.Hypot(x[a]-x[b], y[a]-y[b]) }
	// a shortest path never crosses itself, so on a convex polygon the visited
	// camps form an arc and the path ends at one of its ends; at[i] and
	// atEnd[i] are the best paths over the arc from camp i, ending at either end
	at := make([]float64, n)
	atEnd := make([]float64, n)
	for length := 1; length < n; length++ {
		grow := make([]float64, n)
		growEnd := make([]float64, n)
		for i := range grow {
			grow[i], growEnd[i] = math.Inf(1), math.Inf(1)
		}
		for i := 0; i < n; i++ {
			j, before, after := (i+length-1)%n, (i+n-1)%n, (i+length)%n
			relax := func(cost float64, here int) {
				grow[before] = math.Min(grow[before], cost+dist(here, before))
				growEnd[i] = math.Min(growEnd[i], cost+dist(here, after))
			}
			relax(at[i], i)
			relax(atEnd[i], j)
		}
		at, atEnd = grow, growEnd
	}
	best := math.Inf(1)
	for i := 0; i < n; i++ {
		best = math.Min(best, math.Min(at[i], atEnd[i]))
	}
	fmt.Printf("%.3f\n", best)
}
