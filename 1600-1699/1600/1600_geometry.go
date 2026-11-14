package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
)

const (
	dimensions = 3
	components = 2 * dimensions
)

type object [components]big.Int

func ratio(numerator, denominator *big.Int) float64 {
	var fraction big.Rat
	value, _ := fraction.SetFrac(numerator, denominator).Float64()
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var count int
	if _, err := fmt.Fscan(input, &count); err != nil {
		return
	}

	values := make([]big.Rat, 1+count*components)
	var scale, divisor, tokenDenominator big.Int
	scale.SetInt64(1)
	for i := range values {
		var token string
		if _, err := fmt.Fscan(input, &token); err != nil {
			return
		}
		if _, ok := values[i].SetString(token); !ok {
			return
		}
		tokenDenominator.Set(values[i].Denom())
		divisor.GCD(nil, nil, &scale, &tokenDenominator)
		scale.Quo(&scale, &divisor).Mul(&scale, &tokenDenominator)
	}
	scaled := func(dst *big.Int, value *big.Rat) {
		dst.Quo(&scale, value.Denom()).Mul(dst, value.Num())
	}
	var limit big.Int
	scaled(&limit, &values[0])
	limit.Mul(&limit, &limit)
	objects := make([]object, count)
	for i := range objects {
		for j := range objects[i] {
			scaled(&objects[i][j], &values[1+i*components+j])
		}
	}

	best := math.Inf(1)
	first, second := 0, 0
	var position, velocity, term, projection, speed, gap, projectionSquared, discriminant big.Int
	for i := range objects {
		for j := i + 1; j < count; j++ {
			projection.SetInt64(0)
			speed.SetInt64(0)
			gap.Neg(&limit)
			for axis := 0; axis < dimensions; axis++ {
				position.Sub(&objects[j][axis], &objects[i][axis])
				velocity.Sub(&objects[j][axis+dimensions], &objects[i][axis+dimensions])
				projection.Add(&projection, term.Mul(&position, &velocity))
				speed.Add(&speed, term.Mul(&velocity, &velocity))
				gap.Add(&gap, term.Mul(&position, &position))
			}
			if projection.Sign() >= 0 {
				continue
			}
			projectionSquared.Mul(&projection, &projection)
			discriminant.Sub(&projectionSquared, term.Mul(&speed, &gap))
			if discriminant.Sign() < 0 {
				continue
			}
			// Normalize after the exact sign test and use the stable smaller root.
			root := math.Sqrt(ratio(&discriminant, &projectionSquared))
			time := ratio(&gap, projection.Neg(&projection)) / (1 + root)
			if time < best {
				best, first, second = time, i+1, j+1
			}
		}
	}
	if first == 0 {
		fmt.Println("OK")
	} else {
		fmt.Printf("ALARM!\n%.3f %d %d\n", best, first, second)
	}
}
