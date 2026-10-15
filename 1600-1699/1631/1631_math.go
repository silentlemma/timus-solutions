package main

import (
	"fmt"
	"math"
)

func main() {
	var m, n int
	if _, err := fmt.Scan(&m, &n); err != nil {
		return
	}
	// m * n moves close the tour; m + n + 1 of them are diagonal
	diagonal := m + n + 1
	fmt.Printf("%.12f\n", float64(m*n)+float64(diagonal)*(math.Sqrt2-1))
}
