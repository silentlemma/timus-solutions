package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	area    = 100 // the cross-section of the bar, 10 by 10 cm
	length  = 100
	piece   = 500   // grams, at one gram per cubic centimetre
	microns = 10000 // in a centimetre
	steps   = 100
	capped  = 3 // a cap of height h has volume pi h^2 (3 r - h) / 3
	half    = 0.5
)

type hole struct{ centre, r float64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	holes := make([]hole, n)
	for i := range holes {
		var x, z float64
		fmt.Fscan(in, &x, &holes[i].centre, &z, &holes[i].r)
	}
	// cheese is the weight of the bar from its start to the mark at (in cm):
	// the full volume minus the part of every hole below the mark, a spherical
	// cap of height h with volume pi h^2 (3 r - h) / 3
	cheese := func(at float64) float64 {
		weight := area * at
		for _, h := range holes {
			c := math.Min(math.Max(at-(h.centre-h.r), 0), 2*h.r)
			weight -= math.Pi * c * c * (capped*h.r - c) / capped
		}
		return weight
	}
	var cuts []int64
	start := int64(0)
	for cheese(length)-cheese(float64(start)/microns) >= piece {
		// the mark where the next piece reaches 500 grams, then rounded to the
		// micrometre grid; the next piece starts at the cut actually made
		base := cheese(float64(start) / microns)
		lo, hi := float64(start)/microns, float64(length)
		for i := 0; i < steps; i++ {
			mid := (lo + hi) / 2
			if cheese(mid)-base < piece {
				lo = mid
			} else {
				hi = mid
			}
		}
		start = int64(math.Floor(hi*microns + half))
		if start >= length*microns {
			break
		}
		cuts = append(cuts, start)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(cuts))
	for _, c := range cuts {
		fmt.Fprintln(out, c)
	}
}
