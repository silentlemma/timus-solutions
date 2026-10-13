package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const points = 4
const pad = 1.0 // width given to a rectangle squeezed onto one line

var px, py [points]int64

// frame: the bounding box with sides along (dx, dy) if every point is on its border.
func frame(dx, dy int64) (string, bool) {
	var us, vs [points]int64
	for i := 0; i < points; i++ {
		us[i] = px[i]*dx + py[i]*dy // exact integers in the turned frame
		vs[i] = py[i]*dx - px[i]*dy
	}
	loU, hiU, loV, hiV := us[0], us[0], vs[0], vs[0]
	for i := 1; i < points; i++ {
		loU, hiU = min64(loU, us[i]), max64(hiU, us[i])
		loV, hiV = min64(loV, vs[i]), max64(hiV, vs[i])
	}
	for i := 0; i < points; i++ {
		if us[i] != loU && us[i] != hiU && vs[i] != loV && vs[i] != hiV {
			return "", false
		}
	}
	norm := math.Hypot(float64(dx), float64(dy))
	// back to real lengths; a flat box gets some width, still holding every point on a side
	lu, hu := float64(loU)/norm, float64(hiU)/norm
	lv, hv := float64(loV)/norm, float64(hiV)/norm
	if hiU == loU {
		hu += pad
	}
	if hiV == loV {
		hv += pad
	}
	ex, ey := float64(dx)/norm, float64(dy)/norm
	cu := [points]float64{lu, hu, hu, lu}
	cv := [points]float64{lv, lv, hv, hv}
	out := "+"
	for i := 0; i < points; i++ {
		out += fmt.Sprintf(" %.9f %.9f", cu[i]*ex-cv[i]*ey, cu[i]*ey+cv[i]*ex)
	}
	return out, true
}

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max64(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	for k := 0; k < n; k++ {
		for i := 0; i < points; i++ {
			fmt.Fscan(in, &px[i], &py[i])
		}
		// the valid turns form a closed set whose ends make two points tie,
		// so the directions between points are enough to try
		var dirs [][2]int64
		for i := 0; i < points; i++ {
			for j := i + 1; j < points; j++ {
				if px[i] != px[j] || py[i] != py[j] {
					dirs = append(dirs, [2]int64{px[j] - px[i], py[j] - py[i]})
				}
			}
		}
		if len(dirs) == 0 {
			dirs = append(dirs, [2]int64{1, 0})
		}
		line := "-"
		for _, d := range dirs {
			if s, ok := frame(d[0], d[1]); ok {
				line = s
				break
			}
		}
		fmt.Fprintln(out, line)
	}
}
