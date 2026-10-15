package main

import (
	"bufio"
	"fmt"
	"os"
)

type point struct{ x, y float64 }

func cross(a, b, c point) float64 {
	return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)
}

// clip keeps the part of a convex polygon on the given side (sign of the
// cross product) of the line through a and b.
func clip(poly []point, a, b point, sign float64) []point {
	var out []point
	for i := range poly {
		p, q := poly[i], poly[(i+1)%len(poly)]
		sp, sq := cross(a, b, p)*sign, cross(a, b, q)*sign
		if sp >= 0 {
			out = append(out, p)
		}
		if (sp > 0 && sq < 0) || (sp < 0 && sq > 0) {
			t := sp / (sp - sq)
			out = append(out, point{p.x + (q.x-p.x)*t, p.y + (q.y-p.y)*t})
		}
	}
	return out
}

func area(poly []point) float64 {
	total := 0.0
	for i := range poly {
		a, b := poly[(i+len(poly)-1)%len(poly)], poly[i]
		total += a.x*b.y - b.x*a.y
	}
	return total / 2
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	pts := make([]point, n)
	for i := range pts {
		fmt.Fscan(in, &pts[i].x, &pts[i].y)
	}
	if n-k < k {
		k = n - k
	}
	if k == 1 {
		// every rope lies along the fence: the rabbit cannot get in at all
		fmt.Printf("%.9f\n", 1.0)
		return
	}
	whole, reachable := area(pts), 0.0
	for i := 0; i < n; i++ {
		// the face next to side i is on the side's side of every rope; only
		// the ropes from vertices i + 1 - k, ..., i pass over that side
		next := pts[(i+1)%n]
		mid := point{(pts[i].x + next.x) / 2, (pts[i].y + next.y) / 2}
		ropes := []int{i + 1 - k, i}
		for j := i + 2 - k; j < i; j++ {
			ropes = append(ropes, j)
		}
		face := pts
		for _, j := range ropes {
			a, b := pts[(j%n+n)%n], pts[(j+k)%n]
			sign := -1.0
			if cross(a, b, mid) > 0 {
				sign = 1
			}
			face = clip(face, a, b, sign)
			if len(face) == 0 {
				break
			}
		}
		reachable += area(face)
	}
	fmt.Printf("%.9f\n", (whole-reachable)/whole)
}
