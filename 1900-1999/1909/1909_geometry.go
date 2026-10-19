package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

type vector struct {
	x, y, z *big.Int
}

func add(a, b *big.Int) *big.Int { return new(big.Int).Add(a, b) }
func sub(a, b *big.Int) *big.Int { return new(big.Int).Sub(a, b) }
func mul(a, b *big.Int) *big.Int { return new(big.Int).Mul(a, b) }

func dot(a, b vector) *big.Int {
	return add(add(mul(a.x, b.x), mul(a.y, b.y)), mul(a.z, b.z))
}

func subtract(a, b vector) vector {
	return vector{sub(a.x, b.x), sub(a.y, b.y), sub(a.z, b.z)}
}

func scale(a vector, factor *big.Int) vector {
	return vector{mul(a.x, factor), mul(a.y, factor), mul(a.z, factor)}
}

func cross(a, b vector) vector {
	return vector{sub(mul(a.y, b.z), mul(a.z, b.y)),
		sub(mul(a.z, b.x), mul(a.x, b.z)), sub(mul(a.x, b.y), mul(a.y, b.x))}
}

func projectionSign(point, edge, velocity vector, a, b, planeDiscriminant,
	radiusSquared *big.Int) int {
	x, y := dot(edge, point), dot(edge, velocity)
	if y.Sign() == 0 {
		return x.Sign()
	}
	numerator := x
	if y.Sign() > 0 {
		numerator = new(big.Int).Neg(x)
	}
	denominator := new(big.Int).Abs(y)
	vertexOffset := add(mul(a, numerator), mul(b, denominator))
	comparison := -1
	if vertexOffset.Sign() >= 0 {
		if vertexOffset.Sign() == 0 && planeDiscriminant.Sign() == 0 {
			comparison = 0
		}
	} else {
		scaled := subtract(scale(point, y), scale(velocity, x))
		comparison = sub(dot(scaled, scaled), mul(radiusSquared, mul(y, y))).Sign()
	}
	return comparison * y.Sign()
}

func rayHits(point, velocity vector, radiusSquared *big.Int) bool {
	projection := dot(point, velocity)
	return projection.Sign() < 0 && mul(projection, projection).Cmp(
		mul(dot(velocity, velocity), sub(dot(point, point), radiusSquared))) >= 0
}

func classify(center vector, radius *big.Int, first, second, velocity vector) string {
	left, right := subtract(first, center), subtract(second, center)
	edge := subtract(right, left)
	normal, offset := cross(edge, velocity), cross(edge, left)
	radiusSquared := mul(radius, radius)
	a, b := dot(normal, normal), dot(offset, normal)
	c := sub(dot(offset, offset), mul(radiusSquared, dot(edge, edge)))
	if a.Sign() != 0 && c.Sign() > 0 && b.Sign() < 0 {
		height := dot(left, normal)
		planeDiscriminant := sub(mul(radiusSquared, a), mul(height, height))
		if planeDiscriminant.Sign() >= 0 {
			leftSign := projectionSign(left, edge, velocity, a, b, planeDiscriminant, radiusSquared)
			rightSign := projectionSign(right, edge, velocity, a, b, planeDiscriminant, radiusSquared)
			if leftSign < 0 && rightSign > 0 {
				return "Warning"
			}
		}
	}
	if rayHits(left, velocity, radiusSquared) || rayHits(right, velocity, radiusSquared) {
		return "Crash"
	}
	return "False alarm"
}

func readVector(in *bufio.Reader) vector {
	var x, y, z int64
	fmt.Fscan(in, &x, &y, &z)
	return vector{big.NewInt(x), big.NewInt(y), big.NewInt(z)}
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	center := readVector(in)
	var radius int64
	fmt.Fscan(in, &radius)
	first, second, velocity := readVector(in), readVector(in), readVector(in)
	fmt.Fprintln(out, classify(center, big.NewInt(radius), first, second, velocity))
}
