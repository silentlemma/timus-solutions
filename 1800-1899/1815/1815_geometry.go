package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	cities = 3
	eps    = 1e-9 // a tie at the edge gives the same cost either way
)

var x, y, w [cities]float64

func cost(mx, my float64) float64 {
	total := 0.0
	for i := 0; i < cities; i++ {
		total += w[i] * math.Hypot(x[i]-mx, y[i]-my)
	}
	return total
}

func solve() float64 {
	// a city is the best place when the pull of the others, the weighted
	// unit vectors towards them, is no stronger than the weight standing
	// on that very spot
	for v := 0; v < cities; v++ {
		here, px, py := 0.0, 0.0, 0.0
		for i := 0; i < cities; i++ {
			d := math.Hypot(x[i]-x[v], y[i]-y[v])
			if d == 0 {
				here += w[i]
			} else {
				px += w[i] * (x[i] - x[v]) / d
				py += w[i] * (y[i] - y[v]) / d
			}
		}
		if math.Hypot(px, py) <= here+eps {
			return cost(x[v], y[v])
		}
	}
	// otherwise the best point is inside: by Ptolemy's inequality
	// w2 |MB| + w3 |MC| >= w1 |MQ| for the point Q beyond BC with
	// |BQ| : |CQ| : |BC| = w3 : w2 : w1, so the answer is w1 |AQ|
	base := math.Hypot(x[2]-x[1], y[2]-y[1])
	fromB, fromC := base*w[2]/w[0], base*w[1]/w[0]
	along := (fromB*fromB - fromC*fromC + base*base) / (2 * base)
	height := math.Sqrt(math.Max(0, fromB*fromB-along*along))
	ex, ey := (x[2]-x[1])/base, (y[2]-y[1])/base
	nx, ny := -ey, ex
	// Q lies on the other side of BC from A
	if (x[0]-x[1])*nx+(y[0]-y[1])*ny > 0 {
		nx, ny = -nx, -ny
	}
	qx, qy := x[1]+along*ex+height*nx, y[1]+along*ey+height*ny
	return w[0] * math.Hypot(x[0]-qx, y[0]-qy)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var t int
	if _, err := fmt.Fscan(reader, &t); err != nil {
		return
	}
	for ; t > 0; t-- {
		for i := 0; i < cities; i++ {
			fmt.Fscan(reader, &x[i], &y[i])
		}
		for i := 0; i < cities; i++ {
			fmt.Fscan(reader, &w[i])
		}
		fmt.Fprintf(writer, "%.10f\n", solve())
	}
}
