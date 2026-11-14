package main

import (
	"bufio"
	"math"
	"os"
	"sort"
	"strconv"
)

const (
	centimetres = 100
	minRope     = centimetres
	maxRope     = 50 * centimetres
	minDistance = 2 * minRope
	precision   = 4
	floatBits   = 64
	maxTrees    = 1000
	outputSize  = 24
)

type point struct{ x, y int16 }

func squared(a, b point) int32 {
	dx, dy := int32(a.x)-int32(b.x), int32(a.y)-int32(b.y)
	return dx*dx + dy*dy
}

type tree struct {
	point
	bound int32
}

func nearest(points []point, i, direction int, bound int32) int32 {
	a := points[i]
	for j := i + direction; j >= 0 && j < len(points); j += direction {
		dx := int32(a.x) - int32(points[j].x)
		if dx*dx >= bound {
			break
		}
		if distance := squared(a, points[j]); distance < bound {
			bound = distance
		}
	}
	return bound
}

func largest(points []point) float64 {
	sort.Slice(points, func(i, j int) bool { return points[i].x < points[j].x })
	var storage [maxTrees]tree
	trees := storage[:0]
	for i, p := range points {
		// The horizontal distance bounds every subsequent candidate on this side.
		bound := nearest(points, i, -1, maxRope*maxRope)
		bound = nearest(points, i, 1, bound)
		if bound >= minRope*minRope {
			trees = append(trees, tree{p, bound})
		}
	}
	sort.Slice(trees, func(i, j int) bool { return trees[i].bound > trees[j].bound })
	best := 0.0
	for i, a := range trees {
		limitA := math.Sqrt(float64(a.bound))
		for _, b := range trees[i+1:] {
			upper := float64(a.bound + b.bound)
			if upper <= best {
				break
			}
			pair := squared(a.point, b.point)
			if pair < minDistance*minDistance {
				continue
			}
			limitB := math.Sqrt(float64(b.bound))
			distance := math.Sqrt(float64(pair))
			if distance >= limitA+limitB {
				best = upper
				break
			}
			// The convex objective on the tight boundary is maximized at an endpoint.
			longA := math.Min(limitA, distance-minRope)
			longB := math.Min(limitB, distance-minRope)
			shortA, shortB := distance-longB, distance-longA
			best = math.Max(best, math.Max(longA*longA+shortB*shortB, shortA*shortA+longB*longB))
		}
	}
	return best
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	n, _ := strconv.Atoi(input.Text())
	coordinate := func() int16 {
		input.Scan()
		value, _ := strconv.ParseFloat(input.Text(), floatBits)
		return int16(math.Round(value * centimetres))
	}
	var points [maxTrees]point
	for i := 0; i < n; i++ {
		points[i] = point{coordinate(), coordinate()}
	}
	area := math.Pi * largest(points[:n]) / (centimetres * centimetres)
	var output [outputSize]byte
	line := strconv.AppendFloat(output[:0], area, 'f', precision, floatBits)
	os.Stdout.Write(append(line, '\n'))
}
