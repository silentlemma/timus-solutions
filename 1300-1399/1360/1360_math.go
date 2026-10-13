package main

import (
	"fmt"
	"math"
	"strconv"
)

const turn = 2 * math.Pi
const scale = 1000000

func main() {
	var x0, y0 float64
	var radius string
	fmt.Scan(&x0, &y0, &radius)
	eps, _ := strconv.ParseFloat(radius, 64)
	eps = math.Min(eps, 1)
	across := math.Asin(math.Max(-1, math.Min(1, x0)))
	up := math.Acos(math.Max(-1, math.Min(1, y0)))
	// take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
	// t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
	s0 := across + turn*(math.Ceil(1/eps)+1)
	t0 := s0 * s0
	t := up + turn*math.Floor((t0-up)/turn+0.5)
	ticks := int64(math.Floor(t*scale + 0.5))
	fmt.Printf("%d.%06d\n", ticks/scale, ticks%scale)
}
