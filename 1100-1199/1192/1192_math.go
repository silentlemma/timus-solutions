package main

import (
	"fmt"
	"math"
)

const (
	gravity  = 10.0
	pi       = 3.1415926535 // the value the statement fixes
	halfTurn = 180.0
)

func main() {
	var v, a, k float64
	fmt.Scan(&v, &a, &k)
	// one flight covers v^2 sin(2a) / g; every bounce keeps the angle and
	// divides v^2 by k, so the flights form a geometric series with ratio 1/k
	flight := v * v * math.Sin(2*a*pi/halfTurn) / gravity
	fmt.Printf("%.2f\n", flight*k/(k-1))
}
