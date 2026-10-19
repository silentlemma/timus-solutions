package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
)

const (
	dimension           = 3
	quaternionSize      = 4
	fitIterations       = 12
	weightedIterations  = 6
	jacobiIterations    = 24
	balanceIterations   = 128
	eigenRoundoffFactor = 256
	eps                 = 1e-6
	cellWidth           = 10 * eps
	gate                = 5 * eps
	roundoffGuard       = 2e-15
	numericEps          = eps + roundoffGuard
	eps2                = numericEps * numericEps
	angleRoundoff       = 1e-12
	searchRoundoff      = 1e-16
	certificateRoundoff = roundoffGuard * eps / 2
	singularLimit       = 1e-30
	stepLimit           = 1e-15
	minWeight           = 1e-10
	machineEps          = 2.220446049250313e-16
)

var weightPowers = [...]int{0, 1, 2, 4, 8, 16}

type vec [dimension]float64
type matrix [dimension]vec
type pose [quaternionSize]float64
type key [dimension]int

func dot(a, b vec) float64 { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }
func cross(a, b vec) vec {
	return vec{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}
func norm(a vec) float64 { return math.Sqrt(dot(a, a)) }
func unit(a vec) vec {
	length := norm(a)
	for i := range a {
		a[i] /= length
	}
	return a
}
func subtract(a, b vec) vec      { return vec{a[0] - b[0], a[1] - b[1], a[2] - b[2]} }
func distance2(a, b vec) float64 { d := subtract(a, b); return dot(d, d) }
func frame(a, b vec) matrix {
	z := unit(a)
	y := unit(cross(z, unit(b)))
	return matrix{cross(y, z), y, z}
}
func project(a vec, basis matrix) vec {
	return vec{dot(a, basis[0]), dot(a, basis[1]), dot(a, basis[2])}
}
func unproject(a vec, basis matrix) vec {
	var result vec
	for i := range result {
		for j := range a {
			result[i] += a[j] * basis[j][i]
		}
	}
	return result
}
func cell(p vec) key {
	return key{int(math.Floor(p[0] / cellWidth)), int(math.Floor(p[1] / cellWidth)),
		int(math.Floor(p[2] / cellWidth))}
}
func solve3(a matrix, rhs vec) (vec, bool) {
	for column := 0; column < dimension; column++ {
		pivot := column
		for i := column + 1; i < dimension; i++ {
			if math.Abs(a[i][column]) > math.Abs(a[pivot][column]) {
				pivot = i
			}
		}
		if math.Abs(a[pivot][column]) < singularLimit {
			return vec{}, false
		}
		a[pivot], a[column] = a[column], a[pivot]
		rhs[pivot], rhs[column] = rhs[column], rhs[pivot]
		divisor := a[column][column]
		for j := range a[column] {
			a[column][j] /= divisor
		}
		rhs[column] /= divisor
		for i := 0; i < dimension; i++ {
			if i == column {
				continue
			}
			factor := a[i][column]
			for j := 0; j < dimension; j++ {
				a[i][j] -= factor * a[column][j]
			}
			rhs[i] -= factor * rhs[column]
		}
	}
	return rhs, true
}
func normalMatrix(points []vec, weights []float64, scale float64) matrix {
	var xx, yy, zz, xy, xz, yz float64
	for i, p := range points {
		w := weights[i]
		xx += w * p[0] * p[0]
		yy += w * p[1] * p[1]
		zz += w * p[2] * p[2]
		xy += w * p[0] * p[1]
		xz += w * p[0] * p[2]
		yz += w * p[1] * p[2]
	}
	return matrix{{yy + zz, -xy, -xz / scale}, {-xy, xx + zz, -yz / scale},
		{-xz / scale, -yz / scale, (xx + yy) / (scale * scale)}}
}
func gradient(points, targets []vec, weights []float64) vec {
	var result vec
	for i, p := range points {
		g := cross(p, subtract(targets[i], p))
		for j := range result {
			result[j] += weights[i] * g[j]
		}
	}
	return result
}
func quaternionStep(omega vec, current pose) pose {
	angle := norm(omega)
	if angle == 0 {
		return current
	}
	factor := math.Sin(angle/2) / angle
	a := math.Cos(angle / 2)
	b, c, d := omega[0]*factor, omega[1]*factor, omega[2]*factor
	w, x, y, z := current[0], current[1], current[2], current[dimension]
	result := pose{
		a*w - b*x - c*y - d*z, a*x + b*w + c*z - d*y,
		a*y - b*z + c*w + d*x, a*z + b*y - c*x + d*w,
	}
	var squared sum
	for _, value := range result {
		squared.add(value * value)
	}
	length := math.Sqrt(squared.value())
	for i := range result {
		result[i] /= length
	}
	return result
}
func quaternionApply(points []vec, current pose) []vec {
	w, x, y, z := current[0], current[1], current[2], current[dimension]
	rows := matrix{{1 - 2*(y*y+z*z), 2 * (x*y - w*z), 2 * (x*z + w*y)},
		{2 * (x*y + w*z), 1 - 2*(x*x+z*z), 2 * (y*z - w*x)},
		{2 * (x*z - w*y), 2 * (y*z + w*x), 1 - 2*(x*x+y*y)}}
	result := make([]vec, len(points))
	for i, p := range points {
		result[i] = project(p, rows)
	}
	return result
}
func residuals(points, targets []vec) []float64 {
	result := make([]float64, len(points))
	for i, p := range points {
		result[i] = distance2(p, targets[i])
	}
	return result
}
func maximum(values []float64) float64 {
	result := 0.0
	for _, value := range values {
		result = math.Max(result, value)
	}
	return result
}

type sum struct{ total, correction float64 }

func (s *sum) add(x float64) {
	next := s.total + x
	if math.Abs(s.total) >= math.Abs(x) {
		s.correction += (s.total - next) + x
	} else {
		s.correction += (x - next) + s.total
	}
	s.total = next
}
func (s sum) value() float64 { return s.total + s.correction }
func eigenLower(a matrix) float64 {
	for iteration := 0; iteration < jacobiIterations; iteration++ {
		p, q := 0, 1
		for i := 0; i < dimension; i++ {
			for j := i + 1; j < dimension; j++ {
				if math.Abs(a[i][j]) > math.Abs(a[p][q]) {
					p, q = i, j
				}
			}
		}
		value := a[p][q]
		if math.Abs(value) < singularLimit {
			break
		}
		tau := (a[q][q] - a[p][p]) / (2 * value)
		t := math.Copysign(1, tau) / (math.Abs(tau) + math.Hypot(1, tau))
		c := 1 / math.Sqrt(1+t*t)
		s := t * c
		a[p][p] -= t * value
		a[q][q] += t * value
		a[p][q], a[q][p] = 0, 0
		for k := 0; k < dimension; k++ {
			if k == p || k == q {
				continue
			}
			oldp, oldq := a[k][p], a[k][q]
			a[k][p] = c*oldp - s*oldq
			a[p][k] = a[k][p]
			a[k][q] = s*oldp + c*oldq
			a[q][k] = a[k][q]
		}
	}
	lower := math.Inf(1)
	for i := 0; i < dimension; i++ {
		bound := a[i][i]
		for j := 0; j < dimension; j++ {
			if i != j {
				bound -= math.Abs(a[i][j])
			}
		}
		lower = math.Min(lower, bound)
	}
	return lower
}
func lowerCertificate(points, targets []vec, weights []float64) float64 {
	var error sum
	var gradients [dimension]sum
	var entries [dimension][dimension]sum
	for k, p := range points {
		q, w := targets[k], weights[k]
		e := subtract(q, p)
		g := cross(p, e)
		error.add(w * dot(e, e))
		for i := 0; i < dimension; i++ {
			gradients[i].add(w * g[i])
			diagonal := 0.0
			for j := 0; j < dimension; j++ {
				if i != j {
					diagonal += p[j] * q[j]
				}
			}
			entries[i][i].add(w * diagonal)
			for j := 0; j < i; j++ {
				entries[i][j].add(-w / 2 * (p[i]*q[j] + p[j]*q[i]))
			}
		}
	}
	var h matrix
	var g vec
	for i := 0; i < dimension; i++ {
		g[i] = gradients[i].value()
		for j := 0; j <= i; j++ {
			h[i][j] = entries[i][j].value()
			h[j][i] = h[i][j]
		}
	}
	rowNorm := 0.0
	for _, row := range h {
		rowNorm = math.Max(rowNorm, math.Abs(row[0])+math.Abs(row[1])+math.Abs(row[2]))
	}
	eigen := eigenLower(h) - eigenRoundoffFactor*machineEps*rowNorm
	if eigen <= 0 {
		return math.Inf(-1)
	}
	return error.value() - dot(g, g)/eigen
}
func parameterRotation(p, center vec) vec {
	u, v, theta := center[0], center[1], center[2]
	sine, cosine := math.Sin(theta), math.Cos(theta)
	x, y, z := cosine*p[0]-sine*p[1], sine*p[0]+cosine*p[1], p[2]
	c := 1 / math.Sqrt(1+u*u+v*v)
	value := u*x + v*y
	h := c*z - c*c*value/(1+c)
	return vec{x + u*h, y + v*h, c * (z - value)}
}

type box struct {
	lower         float64
	serial        int
	center, radii vec
}
type boxes []box

func (h boxes) Len() int { return len(h) }
func (h boxes) Less(i, j int) bool {
	if h[i].lower != h[j].lower {
		return h[i].lower < h[j].lower
	}
	return h[i].serial < h[j].serial
}
func (h boxes) Swap(i, j int)           { h[i], h[j] = h[j], h[i] }
func (h *boxes) Push(value interface{}) { *h = append(*h, value.(box)) }
func (h *boxes) Pop() interface{} {
	old := *h
	last := old[len(old)-1]
	*h = old[:len(old)-1]
	return last
}

type solver struct {
	points, normalized, source, targets []vec
	angles                              [][]float64
	mapping                             []int
	normal                              matrix
	scale, angular, chord               float64
}

func (s *solver) angleRow(index int) []float64 {
	if s.angles[index] == nil {
		row := make([]float64, len(s.points))
		p := s.normalized[index]
		for i, q := range s.normalized {
			row[i] = math.Atan2(norm(cross(p, q)), dot(p, q))
		}
		s.angles[index] = row
	}
	return s.angles[index]
}
func (s *solver) angleExcluded(index int) bool {
	a, b := s.angleRow(index), s.angleRow(s.mapping[index])
	for i, j := range s.mapping {
		if math.Abs(a[i]-b[j]) > 2*s.angular+angleRoundoff {
			return true
		}
	}
	return false
}
func (s *solver) fit(weights []float64, iterations int, currentPose pose) ([]vec, pose) {
	current := quaternionApply(s.source, currentPose)
	for iteration := 0; iteration < iterations; iteration++ {
		g := gradient(current, s.targets, weights)
		g[2] /= s.scale
		omega, ok := solve3(normalMatrix(current, weights, s.scale), g)
		if !ok {
			break
		}
		omega[2] /= s.scale
		currentPose = quaternionStep(omega, currentPose)
		current = quaternionApply(s.source, currentPose)
		if maximum(residuals(current, s.targets)) <= eps2 || norm(omega) < stepLimit {
			break
		}
	}
	return current, currentPose
}
func (s *solver) bounded(twist float64) bool {
	norms := make([]float64, len(s.source))
	rho := make([]float64, len(s.source))
	for i, p := range s.source {
		norms[i] = norm(p)
		rho[i] = math.Hypot(p[0], p[1])
	}
	h := &boxes{}
	serial := 0
	add := func(center, radii vec) bool {
		planar := 2 * math.Hypot(radii[0], radii[1])
		lower, worst := 0.0, 0.0
		for i, p := range s.source {
			d := math.Sqrt(distance2(parameterRotation(p, center), s.targets[i]))
			bound := norms[i]*planar + rho[i]*radii[2]
			if d > eps+bound+searchRoundoff {
				return false
			}
			worst = math.Max(worst, d)
			lower = math.Max(lower, d-bound)
		}
		if worst <= numericEps {
			return true
		}
		serial++
		heap.Push(h, box{lower, serial, center, radii})
		return false
	}
	if add(vec{}, vec{math.Tan(s.angular), math.Tan(s.angular), twist}) {
		return true
	}
	for h.Len() > 0 {
		b := heap.Pop(h).(box)
		axis := 0
		largest := b.radii[0]
		for i := 1; i < dimension; i++ {
			value := b.radii[i]
			if i == 2 {
				value *= s.scale
			}
			if value > largest {
				largest, axis = value, i
			}
		}
		b.radii[axis] /= 2
		for _, sign := range [...]float64{-1, 1} {
			child := b.center
			child[axis] += sign * b.radii[axis]
			if add(child, b.radii) {
				return true
			}
		}
	}
	return false
}
func (s *solver) feasible(twist float64) bool {
	weights := make([]float64, len(s.source))
	for i := range weights {
		weights[i] = 1
	}
	g := gradient(s.source, s.targets, weights)
	g[2] /= s.scale
	omega, ok := solve3(s.normal, g)
	quick := s.source
	if ok {
		omega[2] /= s.scale
		quick = quaternionApply(s.source, quaternionStep(omega, pose{1, 0, 0, 0}))
		if maximum(residuals(quick, s.targets)) <= eps2 {
			return true
		}
	}
	distances := residuals(quick, s.targets)
	critical := 0
	for i, d := range distances {
		if d > distances[critical] {
			critical = i
		}
	}
	if s.angleExcluded(critical) {
		return false
	}
	current, currentPose := s.fit(weights, fitIterations, pose{1, 0, 0, 0})
	for _, power := range weightPowers {
		distances = residuals(current, s.targets)
		largest := maximum(distances)
		if largest <= eps2 {
			return true
		}
		var total sum
		for i := range weights {
			weights[i] = 1
			if power != 0 {
				weights[i] = math.Max(minWeight, math.Pow(distances[i]/largest, float64(power)))
			}
			total.add(weights[i])
		}
		if lowerCertificate(current, s.targets, weights) > (eps*eps+certificateRoundoff)*total.value() {
			return false
		}
		current, currentPose = s.fit(weights, weightedIterations, currentPose)
	}
	for i := range weights {
		weights[i] = 1
	}
	for iteration := 0; iteration < balanceIterations; iteration++ {
		distances = residuals(current, s.targets)
		largest := maximum(distances)
		if largest <= eps2 {
			return true
		}
		var total sum
		for i := range weights {
			weights[i] = math.Max(minWeight, weights[i]*math.Exp((distances[i]/largest-1)/2))
			total.add(weights[i])
		}
		for i := range weights {
			weights[i] /= total.value()
		}
		if lowerCertificate(current, s.targets, weights) > eps*eps+certificateRoundoff {
			return false
		}
		current, currentPose = s.fit(weights, weightedIterations, currentPose)
	}
	return s.bounded(twist)
}
func (s *solver) count() int {
	n := len(s.points)
	s.angles = make([][]float64, n)
	anchor := 1
	minimumNorm := math.Inf(1)
	for _, p := range s.points {
		s.normalized = append(s.normalized, unit(p))
		minimumNorm = math.Min(minimumNorm, norm(p))
	}
	for i := 1; i < n; i++ {
		candidate := norm(cross(s.normalized[0], s.normalized[i]))
		if candidate > s.scale {
			s.scale, anchor = candidate, i
		}
	}
	cosine := dot(s.normalized[0], s.normalized[anchor])
	alpha := math.Atan2(s.scale, cosine)
	basis := frame(s.points[0], s.points[anchor])
	for _, p := range s.points {
		s.source = append(s.source, project(p, basis))
	}
	weights := make([]float64, n)
	for i := range weights {
		weights[i] = 1
	}
	s.normal = normalMatrix(s.source, weights, s.scale)
	s.chord = eps / minimumNorm
	s.angular = 2 * math.Asin(s.chord/2)
	lookup := make(map[key][]int)
	for i, p := range s.points {
		k := cell(p)
		for dx := -1; dx <= 1; dx++ {
			for dy := -1; dy <= 1; dy++ {
				for dz := -1; dz <= 1; dz++ {
					neighbor := key{k[0] + dx, k[1] + dy, k[2] + dz}
					lookup[neighbor] = append(lookup[neighbor], i)
				}
			}
		}
	}
	accepted := make(map[string]bool)
	for p := 0; p < n; p++ {
		for q := 0; q < n; q++ {
			if p == q {
				continue
			}
			sine := norm(cross(s.normalized[p], s.normalized[q]))
			targetCosine := dot(s.normalized[p], s.normalized[q])
			tolerance := 2*s.angular + angleRoundoff
			if math.Abs(sine-s.scale) > tolerance || math.Abs(targetCosine-cosine) > tolerance {
				continue
			}
			beta := math.Atan2(sine, targetCosine)
			if sine == 0 || math.Abs(alpha-beta) > tolerance {
				continue
			}
			targetBasis := frame(s.points[p], s.points[q])
			s.mapping = nil
			used := make([]bool, n)
			worst := 0.0
			for _, coordinate := range s.source {
				rotated := unproject(coordinate, targetBasis)
				best := gate * gate
				closest := -1
				for _, j := range lookup[cell(rotated)] {
					error := distance2(rotated, s.points[j])
					if error < best {
						best, closest = error, j
					}
				}
				if closest < 0 || used[closest] {
					break
				}
				used[closest] = true
				s.mapping = append(s.mapping, closest)
				worst = math.Max(worst, best)
			}
			if len(s.mapping) != n {
				continue
			}
			// Every index fits one byte because the input has at most 200 points.
			encoded := make([]byte, n)
			for i, j := range s.mapping {
				encoded[i] = byte(j)
			}
			if worst <= eps2 {
				accepted[string(encoded)] = true
				continue
			}
			s.targets = nil
			for _, j := range s.mapping {
				s.targets = append(s.targets, project(s.points[j], targetBasis))
			}
			twist := 2 * math.Asin(math.Min(1, s.chord/math.Sqrt(s.scale*sine)))
			if s.feasible(twist) {
				accepted[string(encoded)] = true
			}
		}
	}
	return len(accepted)
}
func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	points := make([]vec, n)
	for i := range points {
		fmt.Fscan(in, &points[i][0], &points[i][1], &points[i][2])
	}
	s := solver{points: points}
	fmt.Println(s.count())
}
