package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
)

type parameters struct {
	speed, length, fireSpeed, fireWidth, gap, natural, shield, braking int64
}

type branch struct {
	left, right int64
}

func positivePart(value int64) int64 {
	if value > 0 {
		return value
	}
	return 0
}

func minimumEnergy(p parameters, branches []branch) float64 {
	difference := p.fireSpeed - p.speed
	best := math.Inf(1)
	for _, path := range branches {
		entry := path.left + p.length
		distance := path.right - entry
		held := entry*difference - p.gap*p.speed
		shieldNumerator := positivePart(held) * p.shield
		shieldDenominator := p.speed * difference
		delayNumerator := p.speed*(path.right-path.left+p.fireWidth) + positivePart(-held)
		var brakeNumerator, brakeDenominator *big.Int
		if delayNumerator >= 2*distance*p.fireSpeed {
			brakeNumerator = big.NewInt(p.speed * p.speed)
			brakeDenominator = big.NewInt(2 * distance)
		} else if delayNumerator <= distance*p.fireSpeed {
			brakeNumerator, brakeDenominator = big.NewInt(0), big.NewInt(1)
		} else {
			brakeNumerator = new(big.Int).Mul(big.NewInt(2*p.speed*p.speed*p.fireSpeed),
				big.NewInt(delayNumerator-distance*p.fireSpeed))
			brakeDenominator = new(big.Int).Mul(big.NewInt(delayNumerator), big.NewInt(delayNumerator))
		}
		extra := new(big.Int).Sub(brakeNumerator,
			new(big.Int).Mul(big.NewInt(p.natural), brakeDenominator))
		if extra.Sign() < 0 {
			extra.SetInt64(0)
		}
		numerator := new(big.Int).Mul(big.NewInt(p.braking), extra)
		additional, _ := new(big.Rat).SetFrac(numerator, brakeDenominator).Float64()
		cost := float64(shieldNumerator)/float64(shieldDenominator) + additional
		if cost < best {
			best = cost
		}
	}
	return best
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var p parameters
	fmt.Fscan(in, &p.speed, &p.length, &p.fireSpeed, &p.fireWidth,
		&p.gap, &p.natural, &p.shield, &p.braking)
	var count int
	fmt.Fscan(in, &count)
	branches := make([]branch, count)
	for index := range branches {
		fmt.Fscan(in, &branches[index].left, &branches[index].right)
	}
	fmt.Fprintf(out, "%.12f\n", minimumEnergy(p, branches))
}
