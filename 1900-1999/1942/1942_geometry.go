package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	scale          = 1000
	fractionDigits = 3
)

type point struct{ x, y int }
type answer struct{ count, norm int }

func scaled(token string) int {
	sign, whole, fraction, digits := 1, 0, 0, 0
	afterPoint := false
	for _, symbol := range token {
		switch {
		case symbol == '-':
			sign = -1
		case symbol == '+':
			continue
		case symbol == '.':
			afterPoint = true
		case afterPoint:
			fraction = fraction*10 + int(symbol-'0')
			digits++
		default:
			whole = whole*10 + int(symbol-'0')
		}
	}
	for digits < fractionDigits {
		fraction *= 10
		digits++
	}
	return sign * (whole*scale + fraction)
}

func bestGroup(points []point) answer {
	counts := make([]int32, scale*scale)
	best := answer{}
	for _, p := range points {
		rx, ry := (p.x%scale+scale)%scale, (p.y%scale+scale)%scale
		code := rx*scale + ry
		counts[code]++
		count := int(counts[code])
		dx, dy := rx, ry
		if dx > scale-dx {
			dx = scale - dx
		}
		if dy > scale-dy {
			dy = scale - dy
		}
		norm := dx*dx + dy*dy
		if count > best.count || count == best.count && norm < best.norm {
			best = answer{count, norm}
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var size int
	fmt.Fscan(in, &size)
	points := make([]point, size)
	for index := range points {
		var x, y string
		fmt.Fscan(in, &x, &y)
		points[index] = point{scaled(x), scaled(y)}
	}
	best := bestGroup(points)
	fmt.Printf("%d %.9f\n", best.count, math.Sqrt(float64(best.norm))/scale)
}
