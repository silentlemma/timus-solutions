package main

import (
	"fmt"
	"math"
)

const halfTurn = 180.0

type point struct{ x, y int64 }

var w, h, bx, by int64

func abs(v int) int {
	if v < 0 {
		return -v
	}
	return v
}

// the mirror images of B that a straight line from A reaches after the
// given number of bounces: i walls across, j walls up
func image(i, j int) point {
	x, y := int64(i)*w+bx, int64(j)*h+by
	if abs(i)%2 == 1 {
		x = int64(i)*w + w - bx
	}
	if abs(j)%2 == 1 {
		y = int64(j)*h + h - by
	}
	return point{x, y}
}

func images(bounces int) []point {
	var found []point
	for i := -bounces; i <= bounces; i++ {
		rest := bounces - abs(i)
		found = append(found, image(i, rest))
		if rest != 0 {
			found = append(found, image(i, -rest))
		}
	}
	return found
}

func main() {
	var n int
	var ax, ay int64
	fmt.Scan(&w, &h, &n, &ax, &ay, &bx, &by)
	found := false
	var bestLength int64
	var bestAngle float64
	for _, p := range images(n) {
		dx, dy := p.x-ax, p.y-ay
		length := dx*dx + dy*dy
		angle := math.Atan2(float64(dy), float64(dx)) * halfTurn / math.Pi
		if angle < 0 {
			angle += 2 * halfTurn
		}
		if !found || length < bestLength || (length == bestLength && angle < bestAngle) {
			found, bestLength, bestAngle = true, length, angle
		}
	}
	fmt.Printf("%.2f\n", bestAngle)
}
