package main

import (
	"io/ioutil"
	"math/big"
	"os"
	"strconv"
)

const scale int64 = 20000000

func gcd(a, b int64) int64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func exactFloor(load, stage, lower int64) int64 {
	num, den := big.NewInt(0), big.NewInt(1)
	factor := load * (2*stage - 1)
	rest, part := new(big.Int), new(big.Int)
	for i := int64(1); i < stage; i++ {
		d := 2*i - 1
		r := factor % d
		if r == 0 {
			continue
		}
		g := gcd(d, rest.Mod(den, big.NewInt(d)).Int64())
		multiplier := big.NewInt(d / g)
		part.Div(den, big.NewInt(g))
		part.Mul(part, big.NewInt(r))
		num.Mul(num, multiplier)
		num.Add(num, part)
		den.Mul(den, multiplier)
	}
	// At most the next integer can lie in the fixed-point enclosing interval.
	if num.Cmp(part.Mul(den, big.NewInt(lower+1))) >= 0 {
		lower++
	}
	return lower
}

func lineCeiling(distance, load, stage int64) int64 {
	factor := load * (2*stage - 1)
	whole := (stage-1)*load + (2*stage-1)*distance
	lower := int64(0)
	for i := int64(1); i < stage; i++ {
		d := 2*i - 1
		whole -= factor / d
		lower += (factor % d) * scale / d
	}
	floor := lower / scale
	if stage > 1 && (lower+stage-2)/scale != floor {
		floor = exactFloor(load, stage, floor)
	}
	return whole - floor
}

func main() {
	raw, _ := ioutil.ReadAll(os.Stdin)
	position := 0
	next := func() int64 {
		for position < len(raw) && raw[position] <= ' ' {
			position++
		}
		value := int64(0)
		for position < len(raw) && raw[position] >= '0' && raw[position] <= '9' {
			value = value*10 + int64(raw[position]-'0')
			position++
		}
		return value
	}
	distance, load := next(), next()
	lower, stage := int64(0), int64(1)
	for lower+load*scale/(2*stage-1) < distance*scale {
		lower += load * scale / (2*stage - 1)
		stage++
	}
	// The active affine line must be this stage or the immediately preceding one.
	answer := lineCeiling(distance, load, stage)
	if stage > 1 {
		previous := lineCeiling(distance, load, stage-1)
		if previous > answer {
			answer = previous
		}
	}
	os.Stdout.WriteString(strconv.FormatInt(answer, 10) + "\n")
}
