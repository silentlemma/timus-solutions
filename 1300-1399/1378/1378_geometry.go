package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

// from the centre, r1 reaches the farthest point and r2 reaches across it:
// area / (pi r1 r2) is 1 for any oval and 2 / pi for a square, and
// area / (pi r1^2) is 2 / pi for a square, at most 0.41 for a triangle
const (
	oval       = 0.8
	square     = 0.5
	half       = 0.5 // a pixel reaches half a pixel beyond its centre
	bufferSize = 1 << 16
)

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	var w, h int
	fmt.Fscan(in, &w, &h)
	var ends [][2]float64 // the first and last pixel of each row
	var count, sx, sy float64
	for y := 0; y < h; y++ {
		first, last := -1, -1
		for x := 0; x < w; x++ {
			ch, _ := in.ReadByte()
			for ch != '0' && ch != '1' {
				ch, _ = in.ReadByte()
			}
			if ch == '1' {
				if first < 0 {
					first = x
				}
				last = x
				count++
				sx += float64(x)
				sy += float64(y)
			}
		}
		if first >= 0 {
			ends = append(ends, [2]float64{float64(first), float64(y)})
			ends = append(ends, [2]float64{float64(last), float64(y)})
		}
	}
	cx, cy := sx/count, sy/count
	far := ends[0]
	for _, p := range ends {
		if math.Hypot(p[0]-cx, p[1]-cy) > math.Hypot(far[0]-cx, far[1]-cy) {
			far = p
		}
	}
	r1 := math.Hypot(far[0]-cx, far[1]-cy)
	ux, uy, r2 := (far[0]-cx)/r1, (far[1]-cy)/r1, 0.0
	for _, p := range ends {
		r2 = math.Max(r2, math.Abs((p[1]-cy)*ux-(p[0]-cx)*uy))
	}
	switch {
	case count/(math.Pi*(r1+half)*(r2+half)) > oval:
		fmt.Println("circle")
	case count/(math.Pi*(r1+half)*(r1+half)) > square:
		fmt.Println("square")
	default:
		fmt.Println("triangle")
	}
}
