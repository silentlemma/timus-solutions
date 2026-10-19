package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const gravity int64 = 10
const halfGravity = gravity / 2
const quadraticFactor int64 = 4
const margin = 1e-6
const (
	distanceIndex = iota
	heightIndex
	thicknessIndex
	diameterIndex
	vxIndex
	vyIndex
	uxIndex
	uyIndex
	inputFields
)

type interval struct{ lo, hi float64 }
type polynomial struct{ a, b, c int64 }
type piece struct {
	left, right  float64
	coefficients polynomial
}

func roots(p polynomial) (interval, bool) {
	delta := p.b*p.b + quadraticFactor*p.a*p.c
	if delta < 0 {
		return interval{}, false
	}
	if delta == 0 {
		value := float64(p.b) / float64(2*p.a)
		return interval{value, value}, true
	}
	q := (float64(p.b) + math.Copysign(math.Sqrt(float64(delta)), float64(p.b))) / 2
	x, y := q/float64(p.a), -float64(p.c)/q
	return interval{math.Min(x, y), math.Max(x, y)}, true
}

func feasible(data [inputFields]int64) []interval {
	distance, height := data[distanceIndex], data[heightIndex]
	thickness, diameter := data[thicknessIndex], data[diameterIndex]
	vx, vy, ux, uy := data[vxIndex], data[vyIndex], data[uxIndex], data[uyIndex]
	lo, hi := 0.0, math.Min(2*float64(vy)/float64(gravity), float64(distance)/float64(vx))
	face := func(x, level int64) polynomial {
		return polynomial{halfGravity * (ux*ux + vx*vx),
			vy*ux*ux - uy*vx*ux + gravity*x*vx,
			uy*x*ux - halfGravity*x*x - level*ux*ux}
	}
	for _, x := range []int64{distance, distance + thickness} {
		pair, ok := roots(face(x, height))
		if !ok {
			return nil
		}
		lo, hi = math.Max(lo, pair.lo), math.Min(hi, pair.hi)
		if lo >= hi {
			return nil
		}
	}
	ceiling := height + diameter
	before := float64(gravity*distance-ux*uy) / float64(gravity*vx)
	after := float64(gravity*(distance+thickness)-ux*uy) / float64(gravity*vx)
	pieces := []piece{
		{lo, math.Min(hi, before), face(distance, ceiling)},
		{math.Max(lo, before), math.Min(hi, after),
			polynomial{gravity * gravity, 2 * gravity * vy, uy*uy - 2*gravity*ceiling}},
		{math.Max(lo, after), hi, face(distance+thickness, ceiling)},
	}
	found, badLo, badHi := false, hi, lo
	for _, part := range pieces {
		if part.left > part.right {
			continue
		}
		pair, ok := roots(part.coefficients)
		if !ok {
			continue
		}
		a, b := math.Max(part.left, pair.lo), math.Min(part.right, pair.hi)
		if a <= b {
			found = true
			badLo = math.Min(badLo, a)
			badHi = math.Max(badHi, b)
		}
	}
	if !found {
		return []interval{{lo, hi}}
	}
	answer := make([]interval, 0, 2)
	if lo < badLo {
		answer = append(answer, interval{lo, badLo})
	}
	if badHi < hi {
		answer = append(answer, interval{badHi, hi})
	}
	return answer
}

func solve(data [inputFields]int64) float64 {
	bestWidth, answer := 2*margin, -1.0
	for _, segment := range feasible(data) {
		if segment.hi-segment.lo > bestWidth {
			bestWidth = segment.hi - segment.lo
			answer = (segment.lo + segment.hi) / 2
		}
	}
	return answer
}

func run(in *bufio.Reader, out *bufio.Writer) {
	var data [inputFields]int64
	for i := range data {
		fmt.Fscan(in, &data[i])
	}
	fmt.Fprintln(out, solve(data))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	run(in, out)
}
