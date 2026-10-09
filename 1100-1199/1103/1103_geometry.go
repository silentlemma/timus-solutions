package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"sort"
)

type point struct{ x, y int64 }

func cross(o, a, b point) int64 {
	return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	pts := make([]point, n)
	for i := range pts {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}
	// A is the lowest point and B the next one on the hull, so every other
	// point lies on the left of AB and sees it under an angle below 180
	a := pts[0]
	for _, p := range pts {
		if p.y < a.y || (p.y == a.y && p.x < a.x) {
			a = p
		}
	}
	var rest []point
	for _, p := range pts {
		if p != a {
			rest = append(rest, p)
		}
	}
	b := rest[0]
	for _, p := range rest {
		if cross(a, b, p) < 0 {
			b = p
		}
	}
	type entry struct {
		p          point
		dot, cross *big.Int
	}
	var others []entry
	for _, p := range rest {
		if p != b {
			dot := (a.x-p.x)*(b.x-p.x) + (a.y-p.y)*(b.y-p.y)
			others = append(others, entry{p, big.NewInt(dot), big.NewInt(cross(p, a, b))})
		}
	}
	// the angle APB grows as its cotangent dot / cross falls; the products
	// reach 10^33, so they are compared as big integers
	var l, r big.Int
	sort.Slice(others, func(i, j int) bool {
		l.Mul(others[i].dot, others[j].cross)
		r.Mul(others[j].dot, others[i].cross)
		return l.Cmp(&r) > 0
	})
	// points seeing AB under a larger angle than C lie inside the circle ABC
	c := others[len(others)/2].p
	fmt.Printf("%d %d\n%d %d\n%d %d\n", a.x, a.y, b.x, b.y, c.x, c.y)
}
