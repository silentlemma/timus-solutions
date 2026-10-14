package main

import (
	"fmt"
	"math"
	"math/big"
	"strconv"
	"strings"
)

const (
	shooters    = 3
	indexSum    = 0 + 1 + 2
	ratioDigits = 16
	outputScale = 100000
	roundEps    = 1e-8 // absorb floating-point noise at output rounding midpoints
)

type chances [shooters]float64

var acc [shooters]float64
var order [shooters]int

var values [shooters]string
var exact [shooters]*big.Int
var stronger, weaker int
var attack [2]bool

func ratio(first, second int) float64 {
	a, b := values[first], values[second]
	x, y := a, b
	if len(x) > ratioDigits {
		x = x[:ratioDigits]
	}
	if len(y) > ratioDigits {
		y = y[:ratioDigits]
	}
	p, _ := strconv.ParseFloat(x, 64)
	q, _ := strconv.ParseFloat(y, 64)
	return (p / q) * math.Pow(10, float64((len(a)-len(x))-(len(b)-len(y))))
}

// duel: two left, first to shoot: first wins p / (p + q - p q)
func duel(first, second int) chances {
	p, q := acc[first], acc[second]
	var c chances
	if exact[first].Cmp(exact[second]) >= 0 {
		c[first] = 1 / (1 + ratio(second, first)*(1-p))
	} else {
		r := ratio(first, second)
		c[first] = r / (1 + r*(1-q))
	}
	c[second] = 1 - c[first]
	return c
}

// afterHit is the duel left after a hit, with the next living shooter first
func afterHit(turn, killed int) chances {
	first := order[(turn+1)%shooters]
	if first == killed {
		first = order[(turn+2)%shooters]
	}
	return duel(first, indexSum-killed-first)
}

// three gives the chances when all three live and order[turn] shoots; A never
// misses, so the shooting stops at A's turn at the latest
func three(turn int) chances {
	shooter := order[turn]
	if shooter == 0 {
		return afterHit(turn, stronger)
	}
	p := acc[shooter]
	miss := three((turn + 1) % shooters)
	// the weaker shooter attacks A iff (1-h)^k (1-l) >= h; ties attack
	nextIsStronger := 0
	if order[(turn+1)%shooters] != 0 {
		nextIsStronger = 1
	}
	if shooter == weaker && !attack[nextIsStronger] {
		return miss
	}
	hit := afterHit(turn, 0)
	var mixed chances
	for i := range mixed {
		mixed[i] = p*hit[i] + (1-p)*miss[i]
	}
	return mixed
}

func main() {
	var tokens [shooters]string
	fmt.Scan(&tokens[0], &tokens[1], &tokens[2])
	precision := 0
	for i, token := range tokens {
		acc[i], _ = strconv.ParseFloat(token, 64)
		if point := strings.IndexByte(token, '.'); point >= 0 && len(token)-point-1 > precision {
			precision = len(token) - point - 1
		}
	}
	for i, token := range tokens {
		fraction := 0
		if point := strings.IndexByte(token, '.'); point >= 0 {
			fraction = len(token) - point - 1
		}
		text := strings.ReplaceAll(token, ".", "") + strings.Repeat("0", precision-fraction)
		exact[i], _ = new(big.Int).SetString(text, 10)
		values[i] = exact[i].String()
	}
	stronger = 1
	if exact[1].Cmp(exact[2]) < 0 {
		stronger = 2
	}
	weaker = indexSum - stronger
	scale := new(big.Int).Exp(big.NewInt(10), big.NewInt(int64(precision)), nil)
	high, low := exact[stronger], exact[weaker]
	complement := new(big.Int).Sub(scale, high)
	product := new(big.Int).Mul(complement, new(big.Int).Sub(scale, low))
	bound := new(big.Int).Mul(high, scale)
	attack[0] = low.Sign() == 0 || product.Cmp(bound) >= 0
	attack[1] = low.Sign() == 0 ||
		new(big.Int).Mul(product, complement).Cmp(new(big.Int).Mul(bound, scale)) >= 0
	var total chances
	orders := 0
	for a := 0; a < shooters; a++ {
		for b := 0; b < shooters; b++ {
			if b == a {
				continue
			}
			order = [shooters]int{a, b, indexSum - a - b}
			c := three(0)
			for i := range total {
				total[i] += c[i]
			}
			orders++
		}
	}
	share := 1.0 / float64(orders)
	var rounded [shooters]int
	for i := range rounded {
		rounded[i] = int(total[i]*share*outputScale + 0.5 + roundEps)
	}
	fmt.Printf("%d.%05d %d.%05d %d.%05d\n", rounded[0]/outputScale, rounded[0]%outputScale,
		rounded[1]/outputScale, rounded[1]%outputScale, rounded[2]/outputScale, rounded[2]%outputScale)
}
