package main

import (
	"fmt"
	"math"
)

const turn = 2 * math.Pi

func main() {
	var x0, y0, eps float64
	fmt.Scan(&x0, &y0, &eps)
	across := math.Asin(math.Max(-1, math.Min(1, x0)))
	up := math.Acos(math.Max(-1, math.Min(1, y0)))
	// take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
	// t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
	s0 := across + turn*(math.Ceil(1/eps)+1)
	t0 := s0 * s0
	t := up + turn*math.Round((t0-up)/turn)
	fmt.Printf("%.6f\n", t)
}
