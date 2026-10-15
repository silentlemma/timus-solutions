package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	corners = 3
	inner   = 0.5       // inner points go this share of the way from the centre to a vertex
	outer   = 1 + inner // outer points go this far the opposite way
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var x, y [corners]float64
	gx, gy := 0.0, 0.0
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
		gx += x[i] / corners
		gy += y[i] / corners
	}
	for _, k := range []float64{inner, -outer} {
		for i := range x {
			fmt.Fprintf(out, "%.10f %.10f\n", gx+(x[i]-gx)*k, gy+(y[i]-gy)*k)
		}
	}
}
