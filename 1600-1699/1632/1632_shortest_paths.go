package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	limit = 1e6
	tight = 1e-7 // a smaller slack counts as an equality
)

type edge struct {
	lo, hi int
	lift   float64
}

func minMax(z []float64) (float64, float64) {
	lo, hi := z[0], z[0]
	for _, h := range z {
		if h < lo {
			lo = h
		}
		if h > hi {
			hi = h
		}
	}
	return lo, hi
}

func main() {
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	type laser struct{ x, y, u, v, w int64 }
	lasers := make([]laser, n)
	for i := range lasers {
		l := &lasers[i]
		fmt.Fscan(in, &l.x, &l.y, &l.u, &l.v, &l.w)
	}
	var m int
	fmt.Fscan(in, &m)
	// z[hi] - z[lo] must exceed lift: the gap of the beams where they cross
	edges := make([]edge, m)
	out := make([][]int, n)
	for k := 0; k < m; k++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		a--
		b--
		la, lb := lasers[a], lasers[b]
		det := la.u*lb.v - la.v*lb.u
		dx, dy := lb.x-la.x, lb.y-la.y
		top := lb.w*(la.v*dx-la.u*dy) - la.w*(dx*lb.v-dy*lb.u)
		edges[k] = edge{b, a, float64(top) / float64(det)}
		out[b] = append(out[b], k)
	}
	// longest paths from an imaginary source tied to every laser by 0.
	// Only lasers raised in the last round can raise others.
	z := make([]float64, n)
	active := make([]int, n)
	for i := range active {
		active[i] = i
	}
	mark := make([]bool, n)
	for round := 0; round < n && len(active) > 0; round++ {
		var raised []int
		for _, lo := range active {
			for _, k := range out[lo] {
				e := edges[k]
				if z[lo]+e.lift > z[e.hi] {
					z[e.hi] = z[lo] + e.lift
					if !mark[e.hi] {
						mark[e.hi] = true
						raised = append(raised, e.hi)
					}
				}
			}
		}
		for _, h := range raised {
			mark[h] = false
		}
		active = raised
	}
	// equalities form an acyclic graph; a step per level of it makes them
	// strict, small enough to keep the other constraints and the bounds
	next := make([][]int, n)
	indegree, level := make([]int, n), make([]int, n)
	slackMin := -1.0
	for _, e := range edges {
		slack := z[e.hi] - z[e.lo] - e.lift
		if slack < tight {
			next[e.lo] = append(next[e.lo], e.hi)
			indegree[e.hi]++
		} else if slackMin < 0 || slack < slackMin {
			slackMin = slack
		}
	}
	var queue []int
	for i := 0; i < n; i++ {
		if indegree[i] == 0 {
			queue = append(queue, i)
		}
	}
	for head := 0; head < len(queue); head++ {
		at := queue[head]
		for _, to := range next[at] {
			if level[at]+1 > level[to] {
				level[to] = level[at] + 1
			}
			indegree[to]--
			if indegree[to] == 0 {
				queue = append(queue, to)
			}
		}
	}
	levels := 0
	for _, l := range level {
		if l > levels {
			levels = l
		}
	}
	step := 0.0
	if levels > 0 {
		lo, hi := minMax(z)
		room := 2*limit - (hi - lo)
		if slackMin >= 0 && slackMin < room {
			room = slackMin
		}
		step = room / float64(2*levels+2)
	}
	for i := range z {
		z[i] += step * float64(level[i])
	}
	lo, hi := minMax(z)
	middle := (lo + hi) / 2
	for _, h := range z {
		fmt.Fprintf(w, "%.10f\n", h-middle)
	}
}
