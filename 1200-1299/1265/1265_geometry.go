package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
	"strings"
)

const (
	digits = 6 // the input has at most six digits after the point
	scale  = 1000000
)

// scaled is the number times 10^6 as an exact integer
func scaled(token string) int64 {
	sign := int64(1)
	if strings.HasPrefix(token, "-") {
		sign = -1
	}
	token = strings.TrimLeft(token, "+-")
	whole, frac := token, ""
	if dot := strings.IndexByte(token, '.'); dot >= 0 {
		whole, frac = token[:dot], token[dot+1:]
	}
	frac = (frac + strings.Repeat("0", digits))[:digits]
	w, _ := strconv.Atoi("0" + whole)
	f, _ := strconv.Atoi(frac)
	return sign * (int64(w)*scale + int64(f))
}

func mul(a, b int64) *big.Int {
	return new(big.Int).Mul(big.NewInt(a), big.NewInt(b))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	next := func() int64 {
		var s string
		fmt.Fscan(in, &s)
		return scaled(s)
	}
	ex, ey, tx, ty := next(), next(), next(), next()
	ax, ay, bx, by := next(), next(), next(), next()
	// mirror from A along s; the eye and the target relative to A
	sx, sy := bx-ax, by-ay
	ex, ey, tx, ty = ex-ax, ey-ay, tx-ax, ty-ay
	// heights above the mirror line (times |s|), both on one side
	he, ht := sx*ey-sy*ex, sx*ty-sy*tx
	if (he > 0) != (ht > 0) {
		fmt.Println("INVISIBLE")
		return
	}
	// the ray to the target's image meets the line at the projections
	// weighted by the heights: u = (pe * ht + pt * he) / ((he + ht) |s|^2)
	pe, pt := sx*ex+sy*ey, sx*tx+sy*ty
	num := new(big.Int).Add(mul(pe, ht), mul(pt, he))
	sum := new(big.Int).Add(big.NewInt(he), big.NewInt(ht))
	den := new(big.Int).Mul(sum, new(big.Int).Add(mul(sx, sx), mul(sy, sy)))
	if den.Sign() < 0 {
		num.Neg(num)
		den.Neg(den)
	}
	if num.Sign() >= 0 && num.Cmp(den) <= 0 {
		fmt.Println("VISIBLE")
	} else {
		fmt.Println("INVISIBLE")
	}
}
