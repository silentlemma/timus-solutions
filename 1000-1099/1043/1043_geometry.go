package main

import (
	"fmt"
	"math"
	"math/big"
)

// all comparisons are exact: the center is (ux / d, uy / d) and the radius
// times d is the square root of rho2; the products need more than 64 bits
var d, rho2 *big.Int

func num(v int64) *big.Int                  { return big.NewInt(v) }
func add(a, b *big.Int) *big.Int            { return new(big.Int).Add(a, b) }
func sub(a, b *big.Int) *big.Int            { return new(big.Int).Sub(a, b) }
func mul(a, b *big.Int) *big.Int            { return new(big.Int).Mul(a, b) }
func toFloat(a *big.Int) float64            { f, _ := new(big.Float).SetInt(a).Float64(); return f }
func atLeastRho(t *big.Int) bool            { return t.Sign() >= 0 && mul(t, t).Cmp(rho2) >= 0 }
func squaredMinus(a, g *big.Int) int        { return sub(mul(a, a), mul(mul(g, g), rho2)).Sign() }
func scaledBy(k int64, u *big.Int) *big.Int { return sub(mul(num(k), d), u) }

// signMinus is the sign of alpha - gamma * sqrt(rho2)
func signMinus(alpha, gamma *big.Int) int {
	switch {
	case gamma.Sign() == 0:
		return alpha.Sign()
	case gamma.Sign() > 0:
		if alpha.Sign() <= 0 {
			return -1
		}
		return squaredMinus(alpha, gamma)
	default:
		if alpha.Sign() >= 0 {
			return 1
		}
		return -squaredMinus(alpha, gamma)
	}
}

// ceilPlus is the smallest integer k with k >= (u + sqrt(rho2)) / d
func ceilPlus(u *big.Int) int64 {
	k := int64(math.Floor((toFloat(u)+math.Sqrt(toFloat(rho2)))/toFloat(d))) - 2
	for !atLeastRho(scaledBy(k, u)) {
		k++
	}
	return k
}

// floorMinus is the largest integer k with k <= (u - sqrt(rho2)) / d
func floorMinus(u *big.Int) int64 {
	k := int64(math.Ceil((toFloat(u)-math.Sqrt(toFloat(rho2)))/toFloat(d))) + 2
	for !atLeastRho(new(big.Int).Neg(scaledBy(k, u))) {
		k--
	}
	return k
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	var ax, ay, bx, by, cx, cy int64
	fmt.Scan(&ax, &ay, &bx, &by, &cx, &cy)
	a2, b2, c2 := ax*ax+ay*ay, bx*bx+by*by, cx*cx+cy*cy
	dv := 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
	ux := num(a2*(by-cy) + b2*(cy-ay) + c2*(ay-by))
	uy := num(a2*(cx-bx) + b2*(ax-cx) + c2*(bx-ax))
	if dv < 0 {
		dv = -dv
		ux.Neg(ux)
		uy.Neg(uy)
	}
	d = num(dv)
	dx, dy := sub(mul(num(ax), d), ux), sub(mul(num(ay), d), uy)
	rho2 = add(mul(dx, dx), mul(dy, dy))
	// an extreme point of the circle is on the arc when it lies on the same side
	// of the chord AB as C; side(P) * d = alpha - gamma * sqrt(rho2)
	ex, ey := bx-ax, by-ay
	sideC := num(ex*(cy-ay) - ey*(cx-ax)).Sign()
	alpha := sub(mul(num(ex), sub(uy, mul(num(ay), d))), mul(num(ey), sub(ux, mul(num(ax), d))))
	loX, hiX := min(ax, bx), max(ax, bx)
	loY, hiY := min(ay, by), max(ay, by)
	if signMinus(alpha, num(ey)) == sideC {
		hiX = max(hiX, ceilPlus(ux))
	}
	if signMinus(alpha, num(-ey)) == sideC {
		loX = min(loX, floorMinus(ux))
	}
	if signMinus(alpha, num(-ex)) == sideC {
		hiY = max(hiY, ceilPlus(uy))
	}
	if signMinus(alpha, num(ex)) == sideC {
		loY = min(loY, floorMinus(uy))
	}
	fmt.Println((hiX - loX) * (hiY - loY))
}
