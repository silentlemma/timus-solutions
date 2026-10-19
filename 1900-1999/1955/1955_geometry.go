package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

type point struct{ x, y int64 }
type edge struct{ x, y, constant int64 }
type interval struct{ left, right float64 }
type span struct {
	length  float64
	visible bool
}
type lineKey struct{ x, y, constant int64 }

func minInteger(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
func maxInteger(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}
func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	if a < 0 {
		return -a
	}
	return a
}

func lineSpan(points []point, edges []edge, px, py, dx, dy int64) span {
	n := len(points)
	offset, squared := dx*py-dy*px, dx*dx+dy*dy
	heights := make([]int64, n)
	for i, p := range points {
		heights[i] = dx*p.y - dy*p.x - offset
	}
	hits := make([]float64, 0, n)
	intervals := make([]interval, 0, 2*n)
	previous := heights[n-1]
	for i, height := range heights {
		if (previous > 0) != (height > 0) {
			e := edges[i]
			hits = append(hits, float64(e.constant-px*e.y+py*e.x)/float64(height-previous))
		} else if height == 0 && previous == 0 {
			a, b := points[(i+n-1)%n], points[i]
			first := float64((a.x-px)*dx+(a.y-py)*dy) / float64(squared)
			second := float64((b.x-px)*dx+(b.y-py)*dy) / float64(squared)
			intervals = append(intervals, interval{math.Min(first, second), math.Max(first, second)})
		}
		previous = height
	}
	sort.Float64s(hits)
	for i := 0; i < len(hits); i += 2 {
		intervals = append(intervals, interval{hits[i], hits[i+1]})
	}
	if len(intervals) == 0 {
		return span{}
	}
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].left != intervals[j].left {
			return intervals[i].left < intervals[j].left
		}
		return intervals[i].right < intervals[j].right
	})
	left, right, best, visible := intervals[0].left, intervals[0].right, 0.0, false
	for _, part := range intervals[1:] {
		if part.left <= right {
			right = math.Max(right, part.right)
		} else {
			best = math.Max(best, right-left)
			visible = visible || (left <= 0 && right >= 1)
			left, right = part.left, part.right
		}
	}
	return span{math.Max(best, right-left), visible || (left <= 0 && right >= 1)}
}

func longestSegment(points []point) float64 {
	n := len(points)
	edges := make([]edge, n)
	var lower, diameter int64
	minX, maxX, minY, maxY := points[0].x, points[0].x, points[0].y, points[0].y
	var endpoint, direction point
	for i, p := range points {
		a := points[(i+n-1)%n]
		edges[i] = edge{p.x - a.x, p.y - a.y, a.x*p.y - a.y*p.x}
		lower = maxInteger(lower, edges[i].x*edges[i].x+edges[i].y*edges[i].y)
		minX, maxX = minInteger(minX, p.x), maxInteger(maxX, p.x)
		minY, maxY = minInteger(minY, p.y), maxInteger(maxY, p.y)
		for j := 0; j < i; j++ {
			dx, dy := points[j].x-p.x, points[j].y-p.y
			squared := dx*dx + dy*dy
			if squared > diameter {
				diameter = squared
				endpoint = p
				direction = point{dx, dy}
			}
		}
	}
	initial := lineSpan(points, edges, endpoint.x, endpoint.y, direction.x, direction.y)
	if initial.visible {
		return math.Sqrt(float64(diameter))
	}
	best := math.Max(float64(lower), initial.length*initial.length*float64(diameter))
	widthSquared, heightSquared := (maxX-minX)*(maxX-minX), (maxY-minY)*(maxY-minY)
	seen := make(map[lineKey]struct{})
	for i, p := range points {
		for j := 0; j < i; j++ {
			dx, dy := points[j].x-p.x, points[j].y-p.y
			squared := dx*dx + dy*dy
			if widthSquared*squared < lower*dx*dx || heightSquared*squared < lower*dy*dy {
				continue
			}
			divisor := gcd(dx, dy)
			nx, ny := dx/divisor, dy/divisor
			if nx < 0 || (nx == 0 && ny < 0) {
				nx, ny = -nx, -ny
			}
			key := lineKey{nx, ny, nx*p.y - ny*p.x}
			if _, ok := seen[key]; ok {
				continue
			}
			seen[key] = struct{}{}
			current := lineSpan(points, edges, p.x, p.y, dx, dy)
			if current.visible {
				lower = maxInteger(lower, squared)
				if lower == diameter {
					return math.Sqrt(float64(diameter))
				}
			}
			best = math.Max(best, math.Max(current.length*current.length*float64(squared), float64(lower)))
		}
	}
	return math.Sqrt(best)
}
func main() {
	input := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(input, &n)
	points := make([]point, n)
	for i := range points {
		fmt.Fscan(input, &points[i].x, &points[i].y)
	}
	fmt.Printf("%.12f\n", longestSegment(points))
}
