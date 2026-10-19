package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

// stretch gives the length of the trace while the source a and the
// receiver b move along the directions ua and ub for the time span
func stretch(ax, ay, bx, by, uax, uay, ubx, uby, span float64) float64 {
	dx, dy, vx, vy := bx-ax, by-ay, ubx-uax, uby-uay
	a := vx*vx + vy*vy
	m := dx*vy - dy*vx // constant cross product of d(t) = b - a and v
	if a == 0 || m <= 0 {
		return 0
	}
	// the trace point is a + lam(t) d(t), lam linear; its speed is
	// |r(t)| / sqrt(q(t)) for q(t) = |d(t)|^2 and a quadratic r(t)
	lam0, lam1 := (uax*dy-uay*dx)/m, (uax*vy-uay*vx)/m
	h, c := dx*vx+dy*vy, dx*dx+dy*dy
	b := 2 * h
	r2 := 2 * lam1 * a
	r1 := uax*vx + uay*vy + lam1*(b+h) + lam0*a
	r0 := uax*dx + uay*dy + lam1*c + lam0*h
	// r = alpha q + beta q' + gamma, integrated term by term
	alpha := 2 * lam1
	beta := (r1 - alpha*b) / (2 * a)
	gamma := r0 - alpha*c - beta*b
	rootA, tail := math.Sqrt(a), alpha*m*m/(2*a)+gamma
	primitive := func(t float64) float64 {
		q, slope := math.Max(a*t*t+b*t+c, 0), 2*a*t+b
		return (lam1*slope/(2*a)+2*beta)*math.Sqrt(q) + tail*math.Asinh(slope/(2*m))/rootA
	}
	// the speed changes sign at the roots of r: the trace has a cusp there
	var roots []float64
	if r2 != 0 {
		half := r1 / 2
		if disc := half*half - r2*r0; disc > 0 {
			s := math.Sqrt(disc)
			roots = []float64{(-half - s) / r2, (-half + s) / r2}
			sort.Float64s(roots)
		}
	} else if r1 != 0 {
		roots = []float64{-r0 / r1}
	}
	cuts := []float64{0}
	for _, t := range roots {
		if t > 0 && t < span {
			cuts = append(cuts, t)
		}
	}
	cuts = append(cuts, span)
	total := 0.0
	for k := 0; k+1 < len(cuts); k++ {
		lo, hi := cuts[k], cuts[k+1]
		mid := (lo + hi) / 2
		part := primitive(hi) - primitive(lo)
		if r2*mid*mid+r1*mid+r0 >= 0 {
			total += part
		} else {
			total -= part
		}
	}
	return total
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	xs, ys := make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	var d float64
	fmt.Fscan(in, &d)
	size, ux, uy := make([]float64, n), make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		k := (i + 1) % n
		size[i] = math.Hypot(xs[k]-xs[i], ys[k]-ys[i])
		ux[i], uy[i] = (xs[k]-xs[i])/size[i], (ys[k]-ys[i])/size[i]
	}
	// the source starts at vertex 0; the receiver d further along the border
	j, left := 0, d
	for left >= size[j] {
		left -= size[j]
		j++
	}
	bx, by := xs[j]+ux[j]*left, ys[j]+uy[j]*left
	ahead := size[j] - left // what is left of the receiver's edge
	i, ax, ay, behind, total := 0, xs[0], ys[0], size[0], 0.0
	// walk from one corner event to the next, one of the two at a vertex
	for i < n {
		total += stretch(ax, ay, bx, by, ux[i], uy[i], ux[j], uy[j], math.Min(behind, ahead))
		if behind <= ahead {
			ahead -= behind
			bx, by = bx+ux[j]*behind, by+uy[j]*behind
			i++
			if i < n {
				ax, ay, behind = xs[i], ys[i], size[i]
			}
			if ahead <= 0 {
				j = (j + 1) % n
				bx, by, ahead = xs[j], ys[j], size[j]
			}
		} else {
			behind -= ahead
			ax, ay = ax+ux[i]*ahead, ay+uy[i]*ahead
			j = (j + 1) % n
			bx, by, ahead = xs[j], ys[j], size[j]
		}
	}
	fmt.Printf("%.10f\n", total)
}
