package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"os"
)

const (
	fullTurn        = 360000
	quarterTurn     = 90000
	octant          = 45000
	halfTurn        = 180000.0
	pi              = 3.141592653589793
	boundaryEpsilon = 1e-11
	microScale      = 1000000
	fractionDigits  = 6
	half            = 0.5
)

var sineCoefficients = [...]float64{
	2.8114572543455206e-15, -7.647163731819816e-13, 1.6059043836821613e-10,
	-2.505210838544172e-08, 2.7557319223985893e-06, -0.0001984126984126984,
	0.008333333333333333, -0.16666666666666666, 1,
}

var cosineCoefficients = [...]float64{
	-1.5619206968586225e-16, 4.779477332387385e-14, -1.1470745597729725e-11,
	2.08767569878681e-09, -2.755731922398589e-07, 2.48015873015873e-05,
	-0.001388888888888889, 0.041666666666666664, -half, 1,
}

type point struct {
	x, y int64
}

type scanner struct {
	data []byte
	pos  int
}

func (in *scanner) next() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := int64(1)
	if in.data[in.pos] == '-' {
		sign = -1
		in.pos++
	}
	value := int64(0)
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		ch := in.data[in.pos]
		if ch != '.' {
			value = value*10 + int64(ch-'0')
		}
		in.pos++
	}
	return sign * value
}

func cross(a, b point) int64 {
	return a.x*b.y - a.y*b.x
}

func sinCos(angle int64) (float64, float64) {
	a := angle % fullTurn
	if a < 0 {
		a += fullTurn
	}
	quadrant, r := a/quarterTurn, a%quarterTurn
	mirror := r > octant
	if mirror {
		r = quarterTurn - r
	}
	radiansPerUnit := float64(pi)
	radiansPerUnit /= halfTurn
	x := float64(r) * radiansPerUnit
	z := x * x
	s, c := 0.0, 0.0
	for _, coefficient := range sineCoefficients {
		s = s*z + coefficient
	}
	for _, coefficient := range cosineCoefficients {
		c = c*z + coefficient
	}
	s = x * s
	if r == octant {
		s = c
	}
	if mirror {
		s, c = c, s
	}
	switch quadrant {
	case 0:
		return s, c
	case 1:
		return c, -s
	case 2:
		return -s, -c
	default:
		return -c, s
	}
}

func height(p point, sine, cosine float64) float64 {
	return float64(p.x)*sine + float64(p.y)*cosine
}

func capacity(points []point, prefix []int64, angle int64) float64 {
	sine, cosine := sinCos(angle)
	first := height(points[0], sine, cosine)
	total := prefix[len(points)-1]
	if first == 0 {
		if cosine*float64(points[0].x)-sine*float64(points[0].y) < 0 {
			return float64(total)
		}
		return 0
	}
	negative := first < 0
	lo, hi := 0, len(points)-1
	for hi-lo > 1 {
		mid := (lo + hi) / 2
		if (height(points[mid], sine, cosine) < 0) == negative {
			lo = mid
		} else {
			hi = mid
		}
	}
	left := height(points[lo], sine, cosine)
	right := height(points[hi], sine, cosine)
	t := left / (left - right)
	if t < 0 {
		t = 0
	}
	if t > 1 {
		t = 1
	}
	triangle := float64(prefix[hi] - prefix[lo])
	if negative {
		return float64(prefix[lo]) + t*triangle
	}
	return float64(total-prefix[hi]) + (1-t)*triangle
}

func printArea(out *bufio.Writer, area float64) {
	units := int64(area*half + half)
	fmt.Fprintf(out, "%d.%0*d000\n", units/microScale, fractionDigits, units%microScale)
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n := int(in.next())
	vertices := make([]point, n)
	for i := range vertices {
		vertices[i] = point{in.next(), in.next()}
	}
	hole := point{in.next(), in.next()}
	for i := range vertices {
		vertices[i].x -= hole.x
		vertices[i].y -= hole.y
	}
	edge := 0
	for i, a := range vertices {
		b := vertices[(i+1)%n]
		if cross(a, b) == 0 && a.x*b.x+a.y*b.y < 0 {
			edge = i
			break
		}
	}
	points := make([]point, n)
	for i := range points {
		points[i] = vertices[(edge+1+i)%n]
	}
	prefix := make([]int64, n)
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] + cross(points[i-1], points[i])
	}
	first := points[0]
	degreesPerRadian := float64(halfTurn)
	degreesPerRadian /= pi
	zero := -math.Atan2(float64(first.y), float64(first.x)) * degreesPerRadian
	lower, upper := zero, zero+fullTurn
	if zero > 0 {
		lower, upper = zero-fullTurn, zero
	}
	drained := first.y == 0 && first.x > 0
	remaining := capacity(points, prefix, 0)
	if drained {
		remaining = 0
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	printArea(out, remaining)
	q := int(in.next())
	angle := int64(0)
	for i := 0; i < q; i++ {
		angle += in.next()
		if float64(angle) <= lower+boundaryEpsilon || float64(angle) >= upper-boundaryEpsilon {
			drained = true
		}
		if drained {
			remaining = 0
		} else {
			current := capacity(points, prefix, angle)
			if current < remaining {
				remaining = current
			}
		}
		printArea(out, remaining)
	}
}
