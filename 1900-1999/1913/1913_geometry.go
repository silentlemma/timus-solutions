package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
)

const terminals = 3
const discriminantScale int64 = 4

type point struct{ x, y int64 }
type position struct{ x, y float64 }

func squaredDistance(first, second point) int64 {
	dx, dy := first.x-second.x, first.y-second.y
	return dx*dx + dy*dy
}

func radicalAtMost(target, coefficient, radicand int64) bool {
	if coefficient == 0 || radicand == 0 {
		return target >= 0
	}
	left := new(big.Int).Mul(big.NewInt(target), big.NewInt(target))
	right := new(big.Int).Mul(big.NewInt(coefficient), big.NewInt(coefficient))
	right.Mul(right, big.NewInt(radicand))
	comparison := left.Cmp(right)
	if coefficient > 0 {
		return target >= 0 && comparison >= 0
	}
	return target >= 0 || comparison <= 0
}

func commonPoint(points [terminals]point, radii [terminals]int64) (position, bool) {
	for _, p := range points {
		inside := true
		for index, center := range points {
			inside = inside && squaredDistance(p, center) <= radii[index]*radii[index]
		}
		if inside {
			return position{float64(p.x), float64(p.y)}, true
		}
	}
	for first := 0; first < terminals; first++ {
		for second := first + 1; second < terminals; second++ {
			third := terminals - first - second
			origin := points[first]
			dx, dy := points[second].x-origin.x, points[second].y-origin.y
			distance := dx*dx + dy*dy
			radiusSquared := radii[first] * radii[first]
			along := distance + radiusSquared - radii[second]*radii[second]
			discriminant := discriminantScale*radiusSquared*distance - along*along
			if discriminant < 0 {
				continue
			}
			wx, wy := origin.x-points[third].x, origin.y-points[third].y
			target := distance * (radii[third]*radii[third] - radiusSquared - wx*wx - wy*wy)
			target -= along * (wx*dx + wy*dy)
			cross := wy*dx - wx*dy
			for _, sign := range []int64{-1, 1} {
				if radicalAtMost(target, sign*cross, discriminant) {
					height := float64(sign) * math.Sqrt(float64(discriminant))
					return position{
						float64(origin.x) + (float64(along)*float64(dx)-height*float64(dy))/
							float64(2*distance),
						float64(origin.y) + (float64(along)*float64(dy)+height*float64(dx))/
							float64(2*distance)}, true
				}
			}
		}
	}
	return position{}, false
}

func solve(radius int64, points [terminals]point) ([2]position, bool) {
	var answer [2]position
	reachSquared := (2 * radius) * (2 * radius)
	if squaredDistance(points[0], points[1]) <= reachSquared &&
		squaredDistance(points[0], points[2]) <= reachSquared {
		for index := 0; index < 2; index++ {
			answer[index] = position{float64(points[0].x+points[index+1].x) / 2,
				float64(points[0].y+points[index+1].y) / 2}
		}
		return answer, true
	}
	for doubled := 0; doubled < terminals; doubled++ {
		radii := [terminals]int64{radius, radius, radius}
		radii[doubled] *= 2
		if hub, ok := commonPoint(points, radii); ok {
			midpoint := position{(hub.x + float64(points[doubled].x)) / 2,
				(hub.y + float64(points[doubled].y)) / 2}
			return [2]position{hub, midpoint}, true
		}
	}
	return answer, false
}

func main() {
	in, out := bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var radius int64
	var points [terminals]point
	fmt.Fscan(in, &radius)
	for index := range points {
		fmt.Fscan(in, &points[index].x, &points[index].y)
	}
	answer, ok := solve(radius, points)
	if !ok {
		fmt.Fprintln(out, "Death")
		return
	}
	fmt.Fprintln(out, "Now we have enough power")
	for _, p := range answer {
		fmt.Fprintf(out, "%.12f %.12f\n", p.x, p.y)
	}
}
