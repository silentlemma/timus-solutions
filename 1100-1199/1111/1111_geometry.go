package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
	"sort"
	"strconv"
	"strings"
)

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const (
	pointDen  = 4
	squareDen = 8
)

type fraction struct{ num, den uint64 }

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

func max0(v int64) int64 {
	if v < 0 {
		return 0
	}
	return v
}

// distance is the squared distance from P to the square with diagonal
// (x1, y1)-(x2, y2)
func distance(x1, y1, x2, y2, px, py int64) fraction {
	// doubled coordinates of P relative to the centre, and the diagonal
	qx, qy := 2*px-x1-x2, 2*py-y1-y2
	dx, dy := x2-x1, y2-y1
	h := dx*dx + dy*dy
	if h == 0 {
		return fraction{uint64(qx*qx + qy*qy), pointDen}
	}
	// projections on the two side directions, the diagonal turned by +-45
	// degrees; inside the square both stay within h
	s1 := abs(qx*(dx-dy) + qy*(dy+dx))
	s2 := abs(qx*(dx+dy) + qy*(dy-dx))
	a, b := max0(s1-h), max0(s2-h)
	return fraction{uint64(a*a + b*b), uint64(squareDen * h)}
}

// less compares two fractions through 128-bit cross products
func less(p, q fraction) bool {
	hi1, lo1 := bits.Mul64(p.num, q.den)
	hi2, lo2 := bits.Mul64(q.num, p.den)
	return hi1 < hi2 || (hi1 == hi2 && lo1 < lo2)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	type square struct{ x1, y1, x2, y2 int64 }
	sq := make([]square, n)
	for i := range sq {
		fmt.Fscan(in, &sq[i].x1, &sq[i].y1, &sq[i].x2, &sq[i].y2)
	}
	var px, py int64
	fmt.Fscan(in, &px, &py)
	dist := make([]fraction, n)
	order := make([]int, n)
	for i, s := range sq {
		dist[i] = distance(s.x1, s.y1, s.x2, s.y2, px, py)
		order[i] = i
	}
	sort.SliceStable(order, func(a, b int) bool { return less(dist[order[a]], dist[order[b]]) })
	out := make([]string, n)
	for i, v := range order {
		out[i] = strconv.Itoa(v + 1)
	}
	fmt.Println(strings.Join(out, " "))
}
