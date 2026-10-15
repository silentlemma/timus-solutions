package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	dim   = 3 // coordinates of the sniper
	area  = 3 // corners of a polygon with an inside
	sides = 4 // the wall constraints come first
)

// the fields of a building
const (
	lx = iota
	ly
	rx
	ry
	height
	fields
)

type line struct{ p, q, c int64 } // the closed half-plane p u + q v >= c

type corner struct{ u, v, den int64 } // the point (u / den, v / den), den > 0

type gap struct{ loN, loD, hiN, hiD int64 } // the open interval of t

// blockedInterval finds the open interval of t for which the shot from S to
// A + t (B - A) passes through the inside of the box: a point of the shot
// is S + u (A - S) + v (B - A) with v = u t, a convex polygon in (u, v).
func blockedInterval(s, a, b, box []int64) (gap, bool) {
	ax, ay, dx, dy := a[0]-s[0], a[1]-s[1], b[0]-a[0], b[1]-a[1]
	cons := []line{{ax, dx, box[lx] - s[0]}, {-ax, -dx, s[0] - box[rx]},
		{ay, dy, box[ly] - s[1]}, {-ay, -dy, s[1] - box[ry]},
		{1, 0, 0}, {-1, 0, -1}, // 0 <= u <= 1
		{1, 1, 0}, {2, -1, 0}} // -1 <= t <= 2 keeps the polygon bounded
	for _, w := range cons[:sides] {
		if w.p == 0 && w.q == 0 && w.c >= 0 {
			return gap{}, false // the plane of the shots holds a wall or misses the box
		}
	}
	if s[2] > 0 {
		cons = append(cons, line{s[2], 0, s[2] - box[height]}) // below the roof
	}
	var corners []corner
	for i := range cons {
		for j := i + 1; j < len(cons); j++ {
			f, g := cons[i], cons[j]
			den := f.p*g.q - g.p*f.q
			if den == 0 {
				continue
			}
			u, v := f.c*g.q-g.c*f.q, f.p*g.c-g.p*f.c
			if den < 0 {
				den, u, v = -den, -u, -v
			}
			fits := true
			for _, h := range cons {
				fits = fits && h.p*u+h.q*v >= h.c*den
			}
			for _, k := range corners {
				fits = fits && !(u*k.den == k.u*den && v*k.den == k.v*den)
			}
			if fits {
				corners = append(corners, corner{u, v, den})
			}
		}
	}
	// the polygon has an inside exactly when it has three different corners
	if len(corners) < area {
		return gap{}, false
	}
	// t = v / u, and u > 0 at every corner, as S is outside the box
	r := gap{corners[0].v, corners[0].u, corners[0].v, corners[0].u}
	for _, k := range corners {
		if k.v*r.loD < r.loN*k.u {
			r.loN, r.loD = k.v, k.u
		}
		if k.v*r.hiD > r.hiN*k.u {
			r.hiN, r.hiD = k.v, k.u
		}
	}
	return r, true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	s, a, b := make([]int64, dim), make([]int64, 2), make([]int64, 2)
	var n int
	fmt.Fscan(in, &s[0], &s[1], &s[2], &a[0], &a[1], &b[0], &b[1], &n)
	var gaps []gap
	for i := 0; i < n; i++ {
		box := make([]int64, fields)
		for j := range box {
			fmt.Fscan(in, &box[j])
		}
		if g, ok := blockedInterval(s, a, b, box); ok {
			gaps = append(gaps, g)
		}
	}
	// the free times form a closed set whose first point is 0 or the right
	// end of some blocked interval
	candidates := [][2]int64{{0, 1}}
	for _, g := range gaps {
		if 0 <= g.hiN && g.hiN <= g.hiD {
			candidates = append(candidates, [2]int64{g.hiN, g.hiD})
		}
	}
	sort.Slice(candidates, func(i, j int) bool {
		return candidates[i][0]*candidates[j][1] < candidates[j][0]*candidates[i][1]
	})
	for _, c := range candidates {
		tn, td := c[0], c[1]
		free := true
		for _, g := range gaps {
			free = free && !(g.loN*td < tn*g.loD && tn*g.hiD < g.hiN*td)
		}
		if free {
			t := float64(tn) / float64(td)
			fmt.Printf("%.10f %.10f\n", float64(a[0])+float64(b[0]-a[0])*t,
				float64(a[1])+float64(b[1]-a[1])*t)
			return
		}
	}
	fmt.Println("Impossible")
}
