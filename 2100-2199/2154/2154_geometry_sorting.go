package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"sort"
)

const (
	space = ' '
	minus = '-'
	zero  = '0'
)

type point struct {
	x, y   int64
	nx, ny int64
}

type input struct {
	data []byte
	pos  int
}

func (in *input) nextInt() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= space {
		in.pos++
	}
	sign := int64(1)
	if in.data[in.pos] == minus {
		sign = -1
		in.pos++
	}
	value := int64(0)
	for in.pos < len(in.data) && in.data[in.pos] > space {
		value = value*10 + int64(in.data[in.pos]-zero)
		in.pos++
	}
	return value * sign
}

func distance(a, b point) float64 {
	area := a.x*b.y - a.y*b.x
	if area < 0 {
		area = -area
	}
	dx, dy := a.x-b.x, a.y-b.y
	return float64(area) / math.Sqrt(float64(dx*dx+dy*dy))
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n := int(in.nextInt())
	points := make([]point, n)
	hasOrigin := false
	for i := range points {
		x, y := in.nextInt(), in.nextInt()
		nx, ny := x, y
		if ny < 0 || ny == 0 && nx < 0 {
			nx, ny = -nx, -ny
		}
		points[i] = point{x: x, y: y, nx: nx, ny: ny}
		hasOrigin = hasOrigin || x == 0 && y == 0
	}
	answer := 0.0
	if !hasOrigin {
		// Opposite rays have the same direction modulo a half turn.
		sort.Slice(points, func(i, j int) bool {
			a, b := points[i], points[j]
			return a.nx*b.ny-a.ny*b.nx > 0
		})
		answer = math.Inf(1)
		for i := range points {
			value := distance(points[i], points[(i+1)%n])
			if value < answer {
				answer = value
			}
		}
	}
	fmt.Printf("%.10f\n", answer)
}
