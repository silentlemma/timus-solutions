package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
)

const (
	vertexCount   = 3
	decimalPlaces = 10
	scale         = int64(10000000000)
)

type point struct {
	x, y int64
}

func subtract(a, b point) point {
	return point{a.x - b.x, a.y - b.y}
}

func dot(a, b point) int64 {
	return a.x*b.x + a.y*b.y
}

func cross(a, b point) int64 {
	return a.x*b.y - a.y*b.x
}

func absolute(value int64) int64 {
	if value < 0 {
		return -value
	}
	return value
}

func product(factors ...int64) *big.Int {
	result := big.NewInt(1)
	for _, factor := range factors {
		result.Mul(result, big.NewInt(factor))
	}
	return result
}

func roundedArea(numerator, denominator *big.Int) int64 {
	value := new(big.Int).Mul(numerator, big.NewInt(scale))
	half := new(big.Int).Quo(denominator, big.NewInt(2))
	value.Add(value, half)
	return value.Quo(value, denominator).Int64()
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var points [vertexCount + 1]point
	for i := range points {
		fmt.Fscan(reader, &points[i].x, &points[i].y)
	}
	var best int64
	count := 0
	for i := 0; i < vertexCount; i++ {
		a := points[i]
		d := subtract(points[(i+1)%vertexCount], a)
		v := subtract(points[(i+2)%vertexCount], a)
		w := subtract(points[vertexCount], a)
		s := dot(d, d)
		p := dot(d, v)
		x := dot(d, w)
		height := absolute(cross(d, v))
		q := absolute(cross(d, w))
		// A right triangle's two legs describe the same rectangles.
		if p < 0 || p >= s {
			continue
		}
		area := roundedArea(product(q, height-q), big.NewInt(height))
		if area > best {
			best = area
		}
		count++
		if x < p {
			area = roundedArea(product(height, x, p-x), product(p, p))
		} else if x > p {
			area = roundedArea(product(height, s-x, x-p), product(s-p, s-p))
		} else {
			continue
		}
		if area > best {
			best = area
		}
		count++
	}
	writer := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(writer, "%d.%0*d\n%d\n", best/scale, decimalPlaces, best%scale, count)
	writer.Flush()
}
