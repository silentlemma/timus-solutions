package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const eps = 1e-9

type point struct{ x, z float64 }

var h, d, tg, sn, cs float64

// minDrop is the smallest drop of one move from a point on the cone wall at
// depth t below the station: the move goes across to the opposite wall, or
// is almost level once the cone there is at least d wide
func minDrop(t float64) float64 {
	w := 2 * t * tg
	if w >= d {
		return 0
	}
	return (math.Sqrt(d*d*(1+tg*tg)-w*w) - w*tg) / (1 + tg*tg)
}

// path makes n moves in the plane y = 0: first slides moves down the wall,
// then crosses the cone at full tilt each time, and as soon as one move can
// drop exactly the extra height, makes it and goes straight down
func path(n, slides int) []point {
	var pts []point
	t, x, side := 0.0, 0.0, 1.0
	for left := n; left >= 1; left-- {
		extra := h - t - float64(left-1)*d
		if drop := minDrop(t); extra >= drop-eps {
			x += side * math.Sqrt(math.Max(0, d*d-extra*extra))
			t += extra
			pts = append(pts, point{x, h - t})
			for k := left - 1; k >= 1; k-- {
				pts = append(pts, point{x, float64(k-1) * d})
			}
			pts[len(pts)-1].z = 0
			return pts
		} else if left == 1 {
			return nil
		} else if n-left < slides {
			x -= side * d * sn
			t += d * cs
		} else {
			t += drop
			x = side * t * tg
			side = -side
		}
		pts = append(pts, point{x, h - t})
	}
	return nil
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var alpha float64
	fmt.Fscan(in, &h, &d, &alpha)
	tg, sn, cs = math.Tan(alpha/2), math.Sin(alpha/2), math.Cos(alpha/2)
	n := int(math.Ceil(h/d - eps))
	for slides := 0; slides <= n; slides++ {
		if pts := path(n, slides); pts != nil {
			fmt.Fprintln(out, n)
			for _, p := range pts {
				fmt.Fprintf(out, "%.6f 0 %.6f\n", p.x, p.z)
			}
			return
		}
	}
	fmt.Fprintln(out, -1)
}
