package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

const scale = 100 // coordinates come with two decimals: work in hundredths

func hundredths(s string) int64 {
	whole, part := s, ""
	if i := strings.IndexByte(s, '.'); i >= 0 {
		whole, part = s[:i], s[i+1:]
	}
	part = (part + "00")[:2]
	w, _ := strconv.Atoi(whole)
	p, _ := strconv.Atoi(part)
	if strings.HasPrefix(s, "-") {
		p = -p
	}
	return int64(w)*scale + int64(p)
}

type point struct{ x, y, z int64 }

// fold puts a point of the net on the box: the face A x B in the middle of
// the column lies at z = 0 with its corner (c, b + c) at the origin
func fold(a, b, c, x, y int64) point {
	switch {
	case x < c:
		return point{0, y - b - c, c - x}
	case x > c+a:
		return point{a, y - b - c, x - c - a}
	case y < b:
		return point{x - c, b - y, c}
	case y < b+c:
		return point{x - c, 0, b + c - y}
	case y <= 2*b+c:
		return point{x - c, y - b - c, 0}
	}
	return point{x - c, b, y - 2*b - c}
}

func main() {
	var a, b, c int64
	var x1, y1, x2, y2 string
	fmt.Scan(&a, &b, &c, &x1, &y1, &x2, &y2)
	a, b, c = a*scale, b*scale, c*scale
	p := fold(a, b, c, hundredths(x1), hundredths(y1))
	q := fold(a, b, c, hundredths(x2), hundredths(y2))
	dx, dy, dz := p.x-q.x, p.y-q.y, p.z-q.z
	fmt.Printf("%.10f\n", math.Sqrt(float64(dx*dx+dy*dy+dz*dz))/scale)
}
