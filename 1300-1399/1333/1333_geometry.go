package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	strips  = 20000
	percent = 100
	middle  = 0.5 // where in its strip the line is taken
)

type piece struct{ low, high float64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	cx, cy, r := make([]float64, n), make([]float64, n), make([]float64, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &cx[i], &cy[i], &r[i])
	}
	// the area is the sum over thin vertical strips of the covered part of
	// the line through the middle of each strip
	covered := 0.0
	for k := 0; k < strips; k++ {
		x := (float64(k) + middle) / strips
		var pieces []piece
		for i := 0; i < n; i++ {
			if math.Abs(x-cx[i]) < r[i] {
				half := math.Sqrt(r[i]*r[i] - (x-cx[i])*(x-cx[i]))
				low, high := math.Max(0, cy[i]-half), math.Min(1, cy[i]+half)
				if low < high {
					pieces = append(pieces, piece{low, high})
				}
			}
		}
		sort.Slice(pieces, func(a, b int) bool { return pieces[a].low < pieces[b].low })
		end := 0.0
		for _, p := range pieces {
			if p.high > end {
				covered += p.high - math.Max(p.low, end)
				end = p.high
			}
		}
	}
	fmt.Printf("%.6f\n", covered/strips*percent)
}
