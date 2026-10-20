package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const scale int64 = 1000

type point struct {
	x, y int64
}

type input struct {
	data []byte
	pos  int
}

func (in *input) next() int64 {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	var value int64
	for in.pos < len(in.data) && in.data[in.pos] > ' ' {
		digit := in.data[in.pos]
		in.pos++
		if digit != '.' {
			value = value*10 + int64(digit-'0')
		}
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	n := int(in.next())
	points := make([]point, n)
	var minimum, maximum int64
	for i := range points {
		points[i] = point{in.next(), in.next()}
		if i == 0 || points[i].x < minimum {
			minimum = points[i].x
		}
		if points[i].x > maximum {
			maximum = points[i].x
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	left := int((minimum + scale - 1) / scale)
	right := int(maximum / scale)
	if left > right {
		fmt.Fprintln(out, 0)
		return
	}
	lower, upper := make([]int, right+1), make([]int, right+1)
	for i, a := range points {
		b := points[(i+1)%n]
		if a.x == b.x {
			continue
		}
		bottom := a.x < b.x
		if !bottom {
			a, b = b, a
		}
		begin := int((a.x + scale - 1) / scale)
		end := int(b.x / scale)
		dx, dy := b.x-a.x, b.y-a.y
		denominator := dx * scale
		numerator := a.y*dx + (int64(begin)*scale-a.x)*dy
		target := upper
		if bottom {
			numerator--
			target = lower
		}
		for column := begin; column <= end; column++ {
			target[column] = int(numerator / denominator)
			numerator += dy * scale
		}
	}
	limit := 0
	for _, value := range upper {
		if value > limit {
			limit = value
		}
	}
	if right < limit {
		limit = right
	}
	mu, composite := make([]int, limit+1), make([]bool, limit+1)
	for i := range mu {
		mu[i] = 1
	}
	for prime := 2; prime <= limit; prime++ {
		if composite[prime] {
			continue
		}
		for multiple := prime; multiple <= limit; multiple += prime {
			composite[multiple] = true
			mu[multiple] = -mu[multiple]
		}
		square := prime * prime
		for multiple := square; multiple <= limit; multiple += square {
			mu[multiple] = 0
		}
	}
	var answer int64
	for divisor := 1; divisor <= limit; divisor++ {
		if mu[divisor] == 0 {
			continue
		}
		var subtotal int64
		begin := ((left + divisor - 1) / divisor) * divisor
		for column := begin; column <= right; column += divisor {
			subtotal += int64(upper[column]/divisor - lower[column]/divisor)
		}
		answer += int64(mu[divisor]) * subtotal
	}
	fmt.Fprintln(out, answer)
}
