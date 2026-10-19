package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const focalScale = 3
const axisScale = 6

func main() {
	input := bufio.NewReader(os.Stdin)
	var a, b, c int64
	fmt.Fscan(input, &a, &b, &c)
	x, y, z := a*a, b*b, c*c
	discriminant := 2 * ((x-y)*(x-y) + (y-z)*(y-z) + (z-x)*(z-x))
	gap := math.Sqrt(float64(discriminant))
	focalDistance := math.Sqrt(2*gap) / focalScale
	radius := math.Sqrt(float64(x+y+z)+gap) / axisScale
	fmt.Printf("%.12f %.12f\n", focalDistance, radius)
}
