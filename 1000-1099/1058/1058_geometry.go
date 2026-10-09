package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

// samples per smooth piece and golden-section steps around the best samples
const (
	samples = 64
	steps   = 60
	eps     = 1e-12
)

var (
	n           int
	vx, vy, pre []float64
	half        float64
	// the step of the golden-section search
	golden = (math.Sqrt(5) - 1) / 2
)

func at(u float64) (float64, float64, int) {
	i := int(u)
	t := u - float64(i)
	return vx[i] + t*(vx[i+1]-vx[i]), vy[i] + t*(vy[i+1]-vy[i]), i
}

// partner is the position w in (u, u + n) of the other end of the halving cut
func partner(u float64) float64 {
	px, py, i := at(u)
	// twice the area of P, V[i+1], ..., V[j]
	fan := func(j int) float64 {
		return px*vy[i+1] - vx[i+1]*py + pre[j] - pre[i+1] + vx[j]*py - px*vy[j]
	}
	lo, hi := i+1, i+n
	for hi-lo > 1 {
		mid := (lo + hi) / 2
		if fan(mid) <= half {
			lo = mid
		} else {
			hi = mid
		}
	}
	j := lo
	// on the edge V[j] -> V[j+1] the area grows linearly with the position
	ex, ey := vx[j+1]-vx[j], vy[j+1]-vy[j]
	slope := vx[j]*ey - ex*vy[j] + ex*py - px*ey
	s := 0.0
	if slope > 0 {
		s = (half - fan(j)) / slope
	}
	return float64(j) + math.Min(math.Max(s, 0), 1)
}

func length(u float64) float64 {
	px, py, _ := at(u)
	qx, qy, _ := at(partner(u))
	return math.Hypot(qx-px, qy-py)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	fmt.Fscan(in, &n)
	xs := make([]float64, n)
	ys := make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &xs[i], &ys[i])
	}
	// the walk below needs counterclockwise order, whatever order is given
	twice := 0.0
	for i := 0; i < n; i++ {
		j := (i + n - 1) % n
		twice += xs[j]*ys[i] - xs[i]*ys[j]
	}
	if twice < 0 {
		for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
			xs[i], xs[j] = xs[j], xs[i]
			ys[i], ys[j] = ys[j], ys[i]
		}
	}
	// vertices repeated twice so that a walk along the boundary never wraps
	for k := 0; k <= 2*n; k++ {
		vx = append(vx, xs[k%n])
		vy = append(vy, ys[k%n])
	}
	// pre[k]: twice the signed area swept by the edges 0 .. k-1 from the origin
	pre = []float64{0}
	for k := 0; k < 2*n; k++ {
		pre = append(pre, pre[k]+vx[k]*vy[k+1]-vx[k+1]*vy[k])
	}
	half = pre[n] / 2
	// the cut length is smooth between the vertices and the partners of the
	// vertices; sample every piece and refine around its local minima
	var breaks []float64
	for k := 0; k <= n; k++ {
		breaks = append(breaks, float64(k))
		if k < n {
			breaks = append(breaks, math.Mod(partner(float64(k)), float64(n)))
		}
	}
	sort.Float64s(breaks)
	best := length(0)
	for b := 0; b+1 < len(breaks); b++ {
		from, to := breaks[b], breaks[b+1]
		if to-from < eps {
			continue
		}
		us := make([]float64, samples+1)
		vals := make([]float64, samples+1)
		for k := 0; k <= samples; k++ {
			us[k] = from + (to-from)*float64(k)/samples
			vals[k] = length(us[k])
			best = math.Min(best, vals[k])
		}
		for k := 0; k <= samples; k++ {
			// a local minimum among the samples, the piece ends included
			left, right := k-1, k+1
			if left < 0 {
				left = 0
			}
			if right > samples {
				right = samples
			}
			if vals[k] > vals[left] || vals[k] > vals[right] {
				continue
			}
			lo, hi := us[left], us[right]
			for step := 0; step < steps; step++ {
				m1, m2 := hi-golden*(hi-lo), lo+golden*(hi-lo)
				if length(m1) < length(m2) {
					hi = m2
				} else {
					lo = m1
				}
			}
			best = math.Min(best, length((lo+hi)/2))
		}
	}
	fmt.Printf("%.6f\n", best)
}
