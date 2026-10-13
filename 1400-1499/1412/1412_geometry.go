package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const turn = 2 * math.Pi

// cut: the signed area of the unit disk at the origin inside the triangle (origin, a, b).
func cut(ax, ay, bx, by float64) float64 {
	dx, dy := bx-ax, by-ay
	qa, qb, qc := dx*dx+dy*dy, ax*dx+ay*dy, ax*ax+ay*ay-1
	marks := []float64{0, 1}
	if disc := qb*qb - qa*qc; disc > 0 {
		root := math.Sqrt(disc)
		for _, t := range []float64{(-qb - root) / qa, (-qb + root) / qa} {
			if t > 0 && t < 1 {
				marks = append(marks, t)
			}
		}
	}
	sort.Float64s(marks)
	area := 0.0
	for i := 0; i+1 < len(marks); i++ {
		s, t := marks[i], marks[i+1]
		px, py, qx, qy := ax+dx*s, ay+dy*s, ax+dx*t, ay+dy*t
		mx, my := (px+qx)/2, (py+qy)/2
		cross := px*qy - py*qx
		// a piece inside the disk adds its triangle, one outside adds its sector
		if mx*mx+my*my < 1 {
			area += cross / 2
		} else {
			area += math.Atan2(cross, px*qx+py*qy) / 2
		}
	}
	return area
}

// change: the water that one umbrella moves off or onto the field.
func change(x, y, width, length float64) float64 {
	cx := []float64{-x, length - x, length - x, -x}
	cy := []float64{-y, -y, width - y, width - y}
	covered := 0.0
	for i := range cx {
		j := (i + len(cx) - 1) % len(cx)
		covered += cut(cx[j], cy[j], cx[i], cy[i])
	}
	// the rim splits into arcs at the field's border lines
	angles := []float64{0, turn}
	for _, d := range []float64{-x, length - x} {
		if math.Abs(d) <= 1 {
			angles = append(angles, math.Acos(d), turn-math.Acos(d))
		}
	}
	for _, d := range []float64{-y, width - y} {
		if math.Abs(d) <= 1 {
			angles = append(angles, math.Mod(math.Asin(d)+turn, turn), math.Pi-math.Asin(d))
		}
	}
	sort.Float64s(angles)
	inside := 0.0
	for i := 0; i+1 < len(angles); i++ {
		m := (angles[i] + angles[i+1]) / 2
		px, py := x+math.Cos(m), y+math.Sin(m)
		if px >= 0 && px <= length && py >= 0 && py <= width {
			inside += angles[i+1] - angles[i]
		}
	}
	// rain caught over the whole disk leaves from the rim evenly by angle
	return math.Pi*inside/turn - covered
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var width, length, n int
	fmt.Fscan(in, &width, &length, &n)
	total := float64(width) * float64(length)
	for i := 0; i < n; i++ {
		var x, y float64
		fmt.Fscan(in, &x, &y)
		total += change(x, y, float64(width), float64(length))
	}
	fmt.Printf("%.3f\n", total)
}
