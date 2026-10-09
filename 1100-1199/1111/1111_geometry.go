package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"sort"
	"strconv"
	"strings"
)

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const (
	pointDen  = 4
	squareDen = 8
)

type fraction struct {
	num *big.Int
	den int64
}

func add(a, b *big.Int) *big.Int { return new(big.Int).Add(a, b) }
func sub(a, b *big.Int) *big.Int { return new(big.Int).Sub(a, b) }
func mul(a, b *big.Int) *big.Int { return new(big.Int).Mul(a, b) }

func max0(v *big.Int) *big.Int {
	if v.Sign() < 0 {
		return new(big.Int)
	}
	return v
}

// distance is the squared distance from P to the square with diagonal
// (x1, y1)-(x2, y2)
func distance(x1, y1, x2, y2 int64, px, py *big.Int) fraction {
	// doubled coordinates of P relative to the centre, and the diagonal
	qx := sub(mul(px, big.NewInt(2)), big.NewInt(x1+x2))
	qy := sub(mul(py, big.NewInt(2)), big.NewInt(y1+y2))
	dx, dy := x2-x1, y2-y1
	h := dx*dx + dy*dy
	if h == 0 {
		return fraction{add(mul(qx, qx), mul(qy, qy)), pointDen}
	}
	// projections on the two side directions, the diagonal turned by +-45
	// degrees; inside the square both stay within h
	s1 := new(big.Int).Abs(add(mul(qx, big.NewInt(dx-dy)), mul(qy, big.NewInt(dy+dx))))
	s2 := new(big.Int).Abs(add(mul(qx, big.NewInt(dx+dy)), mul(qy, big.NewInt(dy-dx))))
	a, b := max0(sub(s1, big.NewInt(h))), max0(sub(s2, big.NewInt(h)))
	return fraction{add(mul(a, a), mul(b, b)), squareDen * h}
}

// compare uses exact cross products
func compare(p, q fraction) int {
	return mul(p.num, big.NewInt(q.den)).Cmp(mul(q.num, big.NewInt(p.den)))
}

func main() {
	in := bufio.NewReader(os.Stdin)
	next := func() int64 {
		var token string
		fmt.Fscan(in, &token)
		v, _ := strconv.ParseInt(token, 10, 64)
		return v
	}
	n := int(next())
	type square struct{ x1, y1, x2, y2 int64 }
	sq := make([]square, n)
	for i := range sq {
		sq[i] = square{next(), next(), next(), next()}
	}
	var sx, sy string
	fmt.Fscan(in, &sx, &sy)
	px, _ := new(big.Int).SetString(sx, 10)
	py, _ := new(big.Int).SetString(sy, 10)
	dist := make([]fraction, n)
	order := make([]int, n)
	for i, s := range sq {
		dist[i] = distance(s.x1, s.y1, s.x2, s.y2, px, py)
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		i, j := order[a], order[b]
		c := compare(dist[i], dist[j])
		return c < 0 || (c == 0 && i < j)
	})
	out := make([]string, n)
	for i, v := range order {
		out[i] = strconv.Itoa(v + 1)
	}
	fmt.Println(strings.Join(out, " "))
}
