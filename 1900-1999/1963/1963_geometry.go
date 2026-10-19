package main

import (
	"bufio"
	"fmt"
	"os"
)

const vertexCount = 4

type point struct{ x, y int64 }

func boundaryCount(points [vertexCount]point) int {
	boundary := make(map[point]bool)
	for shift := 0; shift < vertexCount; shift++ {
		var a, b point
		if shift%2 == 0 {
			first := shift / 2
			opposite := (first + 2) % vertexCount
			a = point{2 * points[first].x, 2 * points[first].y}
			b = point{2 * points[opposite].x, 2 * points[opposite].y}
		} else {
			a = point{points[0].x + points[shift].x, points[0].y + points[shift].y}
			remaining := [2]int{}
			count := 0
			for i := 0; i < vertexCount; i++ {
				if i != 0 && i != shift {
					remaining[count] = i
					count++
				}
			}
			p, q := points[remaining[0]], points[remaining[1]]
			b = point{p.x + q.x, p.y + q.y}
		}
		dx, dy := b.x-a.x, b.y-a.y
		if dx == 0 && dy == 0 {
			continue
		}
		valid := true
		for i, p := range points {
			q := points[(shift-i+vertexCount)%vertexCount]
			if (p.x+q.x-a.x)*dy != (p.y+q.y-a.y)*dx || (p.x-q.x)*dx+(p.y-q.y)*dy != 0 {
				valid = false
				break
			}
		}
		if valid {
			boundary[a] = true
			boundary[b] = true
		}
	}
	return len(boundary)
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var points [vertexCount]point
	for i := range points {
		fmt.Fscan(input, &points[i].x, &points[i].y)
	}
	fmt.Println(boundaryCount(points))
}
