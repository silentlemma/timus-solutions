package main

import (
	"fmt"
	"math"
	"math/big"
)

const (
	digits   = 10
	fullTurn = 360
	halfTurn = 180
	vertices = 3
)

type point struct{ x, y int64 }

func cross(o, a, b point) int64 { return (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x) }

func length2(a, b point) int64 { return (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) }

// decimal prints num / den with exactly ten digits after the point
func decimal(num, den int64) string {
	return new(big.Rat).SetFrac64(num, den).FloatString(digits)
}

func main() {
	var target, token [vertices]point
	for i := range target {
		fmt.Scan(&target[i].x, &target[i].y)
	}
	for i := range token {
		fmt.Scan(&token[i].x, &token[i].y)
	}

	// a correspondence works when the sides match and the turn is the same
	// (the token cannot be flipped over)
	orders := [][vertices]int{{0, 1, 2}, {0, 2, 1}, {1, 0, 2}, {1, 2, 0}, {2, 0, 1}, {2, 1, 0}}
	var fits [][vertices]point
	for _, idx := range orders {
		order := [vertices]point{target[idx[0]], target[idx[1]], target[idx[2]]}
		if length2(token[0], token[1]) == length2(order[0], order[1]) &&
			length2(token[0], token[2]) == length2(order[0], order[2]) &&
			length2(token[1], token[2]) == length2(order[1], order[2]) &&
			(cross(token[0], token[1], token[2]) > 0) == (cross(order[0], order[1], order[2]) > 0) {
			fits = append(fits, order)
		}
	}
	if len(fits) == 0 {
		fmt.Println(0)
		return
	}
	for _, order := range fits {
		dx, dy := order[0].x-token[0].x, order[0].y-token[0].y
		shift := true
		for i := 1; i < vertices; i++ {
			shift = shift && order[i].x-token[i].x == dx && order[i].y-token[i].y == dy
		}
		if shift {
			fmt.Println(1, decimal(dx, 1), decimal(dy, 1))
			return
		}
	}

	order := fits[0]
	ux, uy := token[1].x-token[0].x, token[1].y-token[0].y
	wx, wy := order[1].x-order[0].x, order[1].y-order[0].y
	angle := math.Atan2(float64(ux*wy-uy*wx), float64(ux*wx+uy*wy)) * halfTurn / math.Pi
	if angle < 0 {
		angle += fullTurn
	}

	// the centre is a vertex that stays, or it lies on the perpendicular
	// bisector of every vertex and its image: 2 d . c = |t|^2 - |s|^2
	cx, cy := "", ""
	for i := 0; i < vertices; i++ {
		if token[i] == order[i] {
			cx, cy = decimal(token[i].x, 1), decimal(token[i].y, 1)
		}
	}
	if cx == "" {
		var a, b, e [vertices]int64
		for i := 0; i < vertices; i++ {
			a[i] = 2 * (order[i].x - token[i].x)
			b[i] = 2 * (order[i].y - token[i].y)
			e[i] = order[i].x*order[i].x + order[i].y*order[i].y -
				token[i].x*token[i].x - token[i].y*token[i].y
		}
		for i := 0; i < vertices && cx == ""; i++ {
			for j := i + 1; j < vertices && cx == ""; j++ {
				if det := a[i]*b[j] - a[j]*b[i]; det != 0 {
					cx = decimal(e[i]*b[j]-e[j]*b[i], det)
					cy = decimal(a[i]*e[j]-a[j]*e[i], det)
				}
			}
		}
	}
	fmt.Printf("2 %s %s %.10f\n", cx, cy, angle)
}
