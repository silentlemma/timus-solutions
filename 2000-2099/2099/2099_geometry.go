package main

import (
	"fmt"
	"math/big"
)

const dim = 3

type vec [dim]int64

func sub(u, v vec) vec { return vec{u[0] - v[0], u[1] - v[1], u[2] - v[2]} }

func dot(u, v vec) int64 { return u[0]*v[0] + u[1]*v[1] + u[2]*v[2] }

func cross(u, v vec) vec {
	return vec{u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]}
}

// bigDot is the dot product in big integers: the mixed product reaches 5 * 10^19
func bigDot(u, v vec) *big.Int {
	sum := new(big.Int)
	for i := range u {
		sum.Add(sum, new(big.Int).Mul(big.NewInt(u[i]), big.NewInt(v[i])))
	}
	return sum
}

func main() {
	var p [dim + 1]vec
	for i := range p {
		fmt.Scan(&p[i][0], &p[i][1], &p[i][2])
	}
	ab, cd, ac := sub(p[1], p[0]), sub(p[dim], p[2]), sub(p[2], p[0])
	// the turn is a right angle, the two lines meet, the turning point
	// P = A + t AB with t = (AC . AB) / |AB|^2 is not before B, and C is not
	// before P on the second line, (C - P) . CD = AC . CD >= 0
	ok := dot(ab, cd) == 0 && bigDot(ac, cross(ab, cd)).Sign() == 0 &&
		dot(ac, ab) >= dot(ab, ab) && dot(ac, cd) >= 0
	if ok {
		fmt.Println("Valid")
	} else {
		fmt.Println("Invalid")
	}
}
