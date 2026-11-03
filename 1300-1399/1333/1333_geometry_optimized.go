package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const maxBombs = 10
const strips = 4096
const percent = 100
const middle = 0.5

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	var cx, cy, rr, low, high [maxBombs]float64
	for i := 0; i < n; i++ {
		var radius float64
		fmt.Fscan(in, &cx[i], &cy[i], &radius)
		rr[i] = radius * radius
	}
	covered := 0.0
	// Midpoint error<=2*sum(r)/strips, below0.005 for at most10 discs.
	// Reuse bounded interval arrays instead of allocating every slice.
	for k := 0; k < strips; k++ {
		x := (float64(k) + middle) / strips
		count := 0
		for i := 0; i < n; i++ {
			dx := x - cx[i]
			square := rr[i] - dx*dx
			if square <= 0 {
				continue
			}
			half := math.Sqrt(square)
			a, b := math.Max(0, cy[i]-half), math.Min(1, cy[i]+half)
			if a >= b {
				continue
			}
			j := count
			count++
			for j > 0 && low[j-1] > a {
				low[j], high[j] = low[j-1], high[j-1]
				j--
			}
			low[j], high[j] = a, b
		}
		end := 0.0
		for i := 0; i < count; i++ {
			if high[i] > end {
				covered += high[i] - math.Max(low[i], end)
				end = high[i]
			}
		}
	}
	fmt.Printf("%.6f\n", covered/strips*percent)
}
