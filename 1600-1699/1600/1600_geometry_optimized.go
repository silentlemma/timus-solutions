package main

import (
	"bufio"
	"fmt"
	"math"
	"math/big"
	"os"
	"strconv"
)

const maxObjects = 500
const floatBits = 64
const dimensions = 3
const fieldsPerObject = 2 * dimensions

type object struct {
	x, y, z float64
	u, v, w float64
}

// Recompute the quadratic from the input decimals when rounding could change its roots.
func exactQuadratic(first, second [fieldsPerObject]string, distance string) (float64, bool) {
	var speed, projection, gap big.Rat
	var delta [fieldsPerObject]big.Rat
	for i := range delta {
		var x, y big.Rat
		x.SetString(first[i])
		y.SetString(second[i])
		delta[i].Sub(&y, &x)
	}
	var term big.Rat
	for i := 0; i < dimensions; i++ {
		x, v := &delta[i], &delta[i+dimensions]
		gap.Add(&gap, term.Mul(x, x))
		speed.Add(&speed, term.Mul(v, v))
		projection.Add(&projection, term.Mul(x, v))
	}
	if projection.Sign() >= 0 {
		return 0, false
	}
	var threshold, discriminant big.Rat
	threshold.SetString(distance)
	gap.Sub(&gap, term.Mul(&threshold, &threshold))
	discriminant.Mul(&projection, &projection)
	discriminant.Sub(&discriminant, term.Mul(&speed, &gap))
	if discriminant.Sign() < 0 {
		return 0, false
	}
	b, _ := projection.Float64()
	c, _ := gap.Float64()
	disc, _ := discriminant.Float64()
	return c / (-b + math.Sqrt(disc)), true
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	n, err := strconv.Atoi(input.Text())
	if err != nil || n < 0 || n > maxObjects {
		return
	}
	input.Scan()
	distanceText := input.Text()
	distance, _ := strconv.ParseFloat(distanceText, floatBits)
	threshold := distance * distance
	var objects [maxObjects]object
	var decimals [maxObjects][fieldsPerObject]string
	for i := 0; i < n; i++ {
		var values [fieldsPerObject]float64
		for field := range values {
			input.Scan()
			decimals[i][field] = input.Text()
			values[field], _ = strconv.ParseFloat(decimals[i][field], floatBits)
		}
		position, velocity := values[:dimensions], values[dimensions:]
		objects[i] = object{position[0], position[1], position[2], velocity[0], velocity[1], velocity[2]}
	}
	best := math.Inf(1)
	first, second := -1, -1
	for i := 0; i < n; i++ {
		p := &objects[i]
		for j := i + 1; j < n; j++ {
			q := &objects[j]
			x, y, z := q.x-p.x, q.y-p.y, q.z-p.z
			u, v, w := q.u-p.u, q.v-p.v, q.w-p.w
			projection := x*u + y*v + z*w
			if projection >= 0 {
				continue
			}
			length := x*x + y*y + z*z
			offset := length - threshold
			speed := u*u + v*v + w*w
			discriminant := projection*projection - speed*offset
			const roundoff = 1e-12
			var t float64
			if math.Abs(discriminant) <= roundoff*(projection*projection+speed*(length+threshold)) ||
				offset <= roundoff*(length+threshold) {
				var hits bool
				t, hits = exactQuadratic(decimals[i], decimals[j], distanceText)
				if !hits {
					continue
				}
			} else if discriminant < 0 {
				continue
			} else {
				t = offset / (-projection + math.Sqrt(discriminant))
			}
			if t >= 0 && t < best {
				best, first, second = t, i+1, j+1
			}
		}
	}
	if first < 0 {
		fmt.Println("OK")
	} else {
		fmt.Printf("ALARM!\n%.3f %d %d\n", best, first, second)
	}
}
