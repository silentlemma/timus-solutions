package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"math"
	"os"
)

const maxDistance = 3.0e9
const closeDistance = 1.0e-5
const splitter = 134217729.0
const piHigh = 3.141592653589793
const piLow = 1.2246467991473532e-16

type doubleDouble struct {
	high, low float64
}

func exactInteger(value int64) doubleDouble {
	high := float64(value)
	return doubleDouble{high, float64(value - int64(high))}
}

func (a doubleDouble) add(b doubleDouble) doubleDouble {
	sum := a.high + b.high
	part := sum - a.high
	error := (a.high - (sum - part)) + (b.high - part) + a.low + b.low
	high := sum + error
	return doubleDouble{high, error - (high - sum)}
}

func (a doubleDouble) sub(b doubleDouble) doubleDouble {
	return a.add(doubleDouble{-b.high, -b.low})
}

func (a doubleDouble) mul(b doubleDouble) doubleDouble {
	product := a.high * b.high
	splitA := splitter * a.high
	highA := splitA - (splitA - a.high)
	lowA := a.high - highA
	splitB := splitter * b.high
	highB := splitB - (splitB - b.high)
	lowB := b.high - highB
	error := ((highA*highB - product) + highA*lowB) + lowA*highB
	error += lowA*lowB + a.high*b.low + a.low*b.high
	high := product + error
	return doubleDouble{high, error - (high - product)}
}

func (a doubleDouble) nonnegative() bool {
	return a.high > 0 || (a.high == 0 && a.low >= 0)
}

type distance struct {
	value             float64
	base, denominator int64
	square            bool
}

type point struct {
	x, y int64
}

type polygon struct {
	vertices                      []point
	dx, dy, lengthSquared, rx, ry []int64
	radii                         []float64
	extras                        []doubleDouble
	perimeter                     float64
	size                          int
}

type scanner struct {
	data  []byte
	index int
}

func (s *scanner) next() int64 {
	for s.index < len(s.data) && s.data[s.index] <= ' ' {
		s.index++
	}
	sign := int64(1)
	if s.data[s.index] == '-' {
		sign = -1
		s.index++
	}
	value := int64(0)
	for s.index < len(s.data) && s.data[s.index] >= '0' && s.data[s.index] <= '9' {
		value = value*10 + int64(s.data[s.index]-'0')
		s.index++
	}
	return value * sign
}

func cross(ax, ay, bx, by int64) int64 {
	return ax*by - ay*bx
}

func (p *polygon) visible(edge int, query point) bool {
	return cross(p.dx[edge], p.dy[edge], query.x-p.vertices[edge].x,
		query.y-p.vertices[edge].y) < 0
}

func (p *polygon) endDot(edge int, query point) int64 {
	next := (edge + 1) % p.size
	return (p.vertices[next].x-query.x)*p.dx[edge] +
		(p.vertices[next].y-query.y)*p.dy[edge]
}

func (p *polygon) distance(query point) distance {
	first := p.visible(0, query)
	last := p.visible(p.size-1, query)
	var shown, hidden int
	if first != last {
		if first {
			shown, hidden = 0, p.size-1
		} else {
			shown, hidden = p.size-1, 0
		}
	} else {
		qx := query.x - p.vertices[0].x
		qy := query.y - p.vertices[0].y
		low, high := 1, p.size-1
		for high-low > 1 {
			middle := (low + high) / 2
			turn := cross(p.rx[middle], p.ry[middle], qx, qy)
			if (first && turn <= 0) || (!first && turn >= 0) {
				low = middle
			} else {
				high = middle
			}
		}
		if first {
			shown, hidden = 0, low
		} else {
			shown, hidden = low, 0
			if !p.visible(shown, query) {
				return distance{0, 0, 1, false}
			}
		}
	}

	projection := (query.x-p.vertices[shown].x)*p.dx[shown] +
		(query.y-p.vertices[shown].y)*p.dy[shown]
	closest := shown
	// Restrict the derivative test to the visible chain to keep each search monotone.
	if projection > p.lengthSquared[shown] {
		low, high := 0, (hidden-shown+p.size)%p.size
		for high-low > 1 {
			middle := (low + high) / 2
			edge := (shown + middle) % p.size
			if !p.visible(edge, query) || p.endDot(edge, query) >= 0 {
				high = middle
			} else {
				low = middle
			}
		}
		closest = (shown + high) % p.size
	} else if projection < 0 {
		low, high := 0, (shown-hidden+p.size)%p.size
		for high-low > 1 {
			middle := (low + high) / 2
			edge := (hidden + middle) % p.size
			if p.visible(edge, query) && p.endDot(edge, query) >= 0 {
				high = middle
			} else {
				low = middle
			}
		}
		closest = (hidden + high) % p.size
	}

	qx := query.x - p.vertices[closest].x
	qy := query.y - p.vertices[closest].y
	projection = qx*p.dx[closest] + qy*p.dy[closest]
	if projection <= 0 {
		return distance{math.Hypot(float64(qx), float64(qy)), qx*qx + qy*qy, 1, false}
	}
	if projection >= p.lengthSquared[closest] {
		next := (closest + 1) % p.size
		qx = query.x - p.vertices[next].x
		qy = query.y - p.vertices[next].y
		return distance{math.Hypot(float64(qx), float64(qy)), qx*qx + qy*qy, 1, false}
	}
	base := cross(p.dx[closest], p.dy[closest], qx, qy)
	return distance{math.Abs(float64(base)) / math.Sqrt(float64(p.lengthSquared[closest])),
		base, p.lengthSquared[closest], true}
}

func (p *polygon) infected(day int, separation distance) bool {
	difference := p.radii[day] - separation.value
	if math.Abs(difference) > closeDistance {
		return difference > 0
	}
	// Squared distance is numerator/denominator; compare areas without a square root.
	numerator := exactInteger(separation.base)
	if separation.square {
		numerator = numerator.mul(numerator)
	}
	denominator := exactInteger(separation.denominator)
	remainder := p.extras[day].mul(denominator).sub(doubleDouble{piHigh, piLow}.mul(numerator))
	boundary := doubleDouble{p.perimeter, 0}
	left := boundary.mul(boundary).mul(numerator).mul(denominator)
	return remainder.nonnegative() && remainder.mul(remainder).sub(left).nonnegative()
}

func newPolygon(input []point) polygon {
	p := polygon{}
	count := len(input)
	for i, current := range input {
		previous := input[(i+count-1)%count]
		next := input[(i+1)%count]
		if cross(current.x-previous.x, current.y-previous.y,
			next.x-current.x, next.y-current.y) != 0 {
			p.vertices = append(p.vertices, current)
		}
	}
	p.size = len(p.vertices)
	p.dx = make([]int64, p.size)
	p.dy = make([]int64, p.size)
	p.lengthSquared = make([]int64, p.size)
	p.rx = make([]int64, p.size)
	p.ry = make([]int64, p.size)
	perimeter, correction := float64(0), float64(0)
	twiceArea := int64(0)
	for i, current := range p.vertices {
		next := p.vertices[(i+1)%p.size]
		p.dx[i] = next.x - current.x
		p.dy[i] = next.y - current.y
		p.lengthSquared[i] = p.dx[i]*p.dx[i] + p.dy[i]*p.dy[i]
		p.rx[i] = current.x - p.vertices[0].x
		p.ry[i] = current.y - p.vertices[0].y
		adjusted := math.Hypot(float64(p.dx[i]), float64(p.dy[i])) - correction
		total := perimeter + adjusted
		correction = (total - perimeter) - adjusted
		perimeter = total
		if i > 1 {
			twiceArea += cross(p.rx[i-1], p.ry[i-1], p.rx[i], p.ry[i])
		}
	}
	area := float64(twiceArea) / 2
	p.perimeter = perimeter
	halfPerimeter := perimeter / 2
	multiplier, radius := float64(1), float64(0)
	p.radii = append(p.radii, radius)
	exactArea := exactInteger(twiceArea).mul(doubleDouble{1.0 / 2, 0})
	threshold := exactArea
	p.extras = append(p.extras, doubleDouble{0, 0})
	// A + P*r + pi*r*r = A*2^day; use the stable positive root.
	for radius <= maxDistance {
		threshold = threshold.add(threshold)
		p.extras = append(p.extras, threshold.sub(exactArea))
		multiplier *= 2
		extra := area * (multiplier - 1)
		radius = extra / (halfPerimeter +
			math.Sqrt(halfPerimeter*halfPerimeter+math.Pi*extra))
		p.radii = append(p.radii, radius)
	}
	return p
}

func (p *polygon) day(query point) int {
	separation := p.distance(query)
	if separation.value == 0 {
		return 0
	}
	low, high := 0, len(p.radii)
	for low < high {
		middle := (low + high) / 2
		if p.radii[middle] >= separation.value {
			high = middle
		} else {
			low = middle + 1
		}
	}
	for low > 0 && p.infected(low-1, separation) {
		low--
	}
	for !p.infected(low, separation) {
		low++
	}
	return low
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	count := int(in.next())
	vertices := make([]point, count)
	for i := range vertices {
		vertices[i] = point{in.next(), in.next()}
	}
	p := newPolygon(vertices)
	queries := int(in.next())
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < queries; i++ {
		fmt.Fprintln(out, p.day(point{in.next(), in.next()}))
	}
}
