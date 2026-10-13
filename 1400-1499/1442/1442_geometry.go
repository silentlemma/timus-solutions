package main

import (
	"fmt"
	"math"
)

const (
	eps        = 1e-9
	depthLimit = 50
	cone       = 1.0 / 3 // a cone holds a third of its cylinder
	richardson = 15      // error estimate of the Simpson rule on halves
)

// weights of the ends and the middle
var simpson = [...]float64{1.0 / 6, 4.0 / 6, 1.0 / 6}

var r, d, h, k float64

// the powder lost in the slice at x, parallel to the slit x = d: the cone
// surface k (r - rho) drops to k |x - d| wherever rho < a = r - |x - d|
func lost(x float64) float64 {
	a := r - math.Abs(x-d)
	if a <= math.Abs(x) {
		return 0
	}
	y := math.Sqrt(a*a - x*x)
	tail := 0.0
	if x != 0 {
		tail = x * x * math.Log((a+y)/math.Abs(x))
	}
	return k * (a*y - tail)
}

func rule(lo, hi, flo, fmid, fhi float64) float64 {
	return (hi - lo) * (simpson[0]*flo + simpson[1]*fmid + simpson[2]*fhi)
}

func adaptive(lo, hi, flo, fmid, fhi, whole, e float64, depth int) float64 {
	mid := (lo + hi) / 2
	fl, fr := lost((lo+mid)/2), lost((mid+hi)/2)
	left, right := rule(lo, mid, flo, fl, fmid), rule(mid, hi, fmid, fr, fhi)
	delta := left + right - whole
	if depth == 0 || math.Abs(delta) <= richardson*e {
		return left + right + delta/richardson
	}
	return adaptive(lo, mid, flo, fl, fmid, left, e/2, depth-1) +
		adaptive(mid, hi, fmid, fr, fhi, right, e/2, depth-1)
}

func integral(lo, hi float64) float64 {
	if hi <= lo {
		return 0
	}
	flo, fmid, fhi := lost(lo), lost((lo+hi)/2), lost(hi)
	return adaptive(lo, hi, flo, fmid, fhi, rule(lo, hi, flo, fmid, fhi), eps, depthLimit)
}

func main() {
	fmt.Scan(&r, &d, &h)
	k = h / r // the slope of the powder
	volume := math.Pi * r * r * h * cone
	if d < r { // the slit cuts the base between (d - r) / 2 and (d + r) / 2, kinks at 0 and d
		volume -= integral((d-r)/2, 0) + integral(0, d) + integral(d, (d+r)/2)
	}
	fmt.Printf("%.6f\n", volume)
}
