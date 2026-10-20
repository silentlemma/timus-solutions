package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"sort"
)

const (
	maxCoordinate   = 10000
	columnCount     = 2*maxCoordinate + 1
	gravity         = 10
	halfGravity     = gravity / 2
	outputPrecision = 9
)

type point struct {
	x, y, wait int
	best       float64
}

type input struct {
	data []byte
	pos  int
}

func (in *input) nextInt() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	sign := 1
	if in.data[in.pos] == '-' {
		sign = -1
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value * sign
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n := in.nextInt()
	startX, startY := in.nextInt(), in.nextInt()
	points := make([]point, n+1)
	for i := 0; i < n; i++ {
		points[i] = point{x: in.nextInt(), y: in.nextInt(), wait: in.nextInt()}
	}
	points[n] = point{x: startX, y: startY}
	sort.Slice(points, func(i, j int) bool {
		return points[i].y < points[j].y
	})
	columns := make([][]int, columnCount)
	for i := 0; i < n; i++ {
		column := points[i].x + maxCoordinate
		columns[column] = append(columns[column], i)
	}
	fall := make([]float64, startY+1)
	for drop := 0; drop <= startY; drop++ {
		fall[drop] = math.Sqrt(float64(drop) / float64(halfGravity))
	}
	for i := range points {
		p := &points[i]
		best := fall[p.y]
		radius := int(math.Sqrt(float64((p.y - 1) / halfGravity)))
		left, right := p.x-radius, p.x+radius
		if left < -maxCoordinate {
			left = -maxCoordinate
		}
		if right > maxCoordinate {
			right = maxCoordinate
		}
		for x := left; x <= right; x++ {
			dx := x - p.x
			drop := halfGravity * dx * dx
			if drop < 1 {
				drop = 1
			}
			height := p.y - drop
			column := columns[x+maxCoordinate]
			lo, hi := 0, len(column)
			for lo < hi {
				mid := (lo + hi) / 2
				if points[column[mid]].y <= height {
					lo = mid + 1
				} else {
					hi = mid
				}
			}
			// A higher reachable cloud dominates all lower clouds in its column.
			if lo > 0 {
				target := &points[column[lo-1]]
				candidate := fall[p.y-target.y] + target.best
				if candidate > best {
					best = candidate
				}
			}
		}
		p.best = float64(p.wait) + best
	}
	fmt.Printf("%.*f\n", outputPrecision, points[n].best)
}
