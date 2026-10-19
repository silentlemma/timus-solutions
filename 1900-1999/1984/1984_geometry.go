package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func radius(count int) float64 {
	if count == 1 {
		return 1
	}
	return 1 + 1/math.Sin(math.Pi/float64(count))
}

func main() {
	var count int
	fmt.Fscan(bufio.NewReader(os.Stdin), &count)
	fmt.Printf("%.10f\n", radius(count))
}
