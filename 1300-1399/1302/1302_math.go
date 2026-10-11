package main

import (
	"fmt"
	"math"
)

const axes = 3 // the row and the two diagonal strips

// strips gives the row of cell n and its two diagonal strips, from the
// left and from the right; one step across an edge changes exactly one
func strips(n int64) [axes]int64 {
	row := int64(math.Sqrt(float64(n - 1)))
	for row*row > n-1 {
		row--
	}
	for (row+1)*(row+1) <= n-1 {
		row++
	}
	row++
	place := n - (row-1)*(row-1) // 1 .. 2 row - 1 within the row
	return [axes]int64{row, (place + 1) / 2, (2*row - place + 1) / 2}
}

func main() {
	var m, n int64
	fmt.Scan(&m, &n)
	a, b := strips(m), strips(n)
	total := int64(0)
	for i := range a {
		d := a[i] - b[i]
		if d < 0 {
			d = -d
		}
		total += d
	}
	fmt.Println(total)
}
