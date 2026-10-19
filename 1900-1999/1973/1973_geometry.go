package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const diagonalWeight = 2
const pairWeight = 3
const normalizer = 27

type point struct{ x, y int64 }

func expectation(vertices []point) float64 {
	origin := vertices[0]
	previousX := vertices[1].x - origin.x
	previousY := vertices[1].y - origin.y
	var numerator, weightedX, weightedY big.Int
	var total int64
	for _, vertex := range vertices[2:] {
		x, y := vertex.x-origin.x, vertex.y-origin.y
		area := previousX*y - previousY*x
		sumX, sumY := previousX+x, previousY+y
		left := new(big.Int).Mul(&weightedX, big.NewInt(sumY))
		right := new(big.Int).Mul(&weightedY, big.NewInt(sumX))
		between := new(big.Int).Sub(left, right)
		d := big.NewInt(area)
		cube := new(big.Int).Mul(d, d)
		cube.Mul(cube, d)
		cube.Mul(cube, big.NewInt(diagonalWeight))
		paired := new(big.Int).Mul(d, between)
		paired.Mul(paired, big.NewInt(pairWeight))
		numerator.Add(&numerator, cube)
		numerator.Add(&numerator, paired)
		weightedX.Add(&weightedX, new(big.Int).Mul(d, big.NewInt(sumX)))
		weightedY.Add(&weightedY, new(big.Int).Mul(d, big.NewInt(sumY)))
		total += area
		previousX, previousY = x, y
	}
	denominator := new(big.Int).Mul(big.NewInt(total), big.NewInt(total))
	denominator.Mul(denominator, big.NewInt(normalizer))
	ratio := new(big.Rat).SetFrac(&numerator, denominator)
	answer, _ := ratio.Float64()
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var count int
	fmt.Fscan(in, &count)
	vertices := make([]point, count)
	for i := range vertices {
		fmt.Fscan(in, &vertices[i].x, &vertices[i].y)
	}
	fmt.Fprintf(out, "%.12f\n", expectation(vertices))
}
