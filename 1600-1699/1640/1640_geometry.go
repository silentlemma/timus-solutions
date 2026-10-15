package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	// Sandro's own spot holds no demon: stay there and reach the farthest one
	farthest := 0.0
	for i := 0; i < n; i++ {
		var x, y float64
		fmt.Fscan(in, &x, &y)
		farthest = math.Max(farthest, math.Hypot(x, y))
	}
	fmt.Printf("0 0 %.10f\n", farthest)
}
