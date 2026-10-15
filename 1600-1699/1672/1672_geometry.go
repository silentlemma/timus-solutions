package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	dim    = 3
	steps  = 60   // halvings in each bisection
	sphere = 1500 // directions tried for the narrowest width

	tiny   = 1e-13 // where the local search stops
	near   = 1e-10 // equal widths, relative to the diameter
	rounds = 400   // passes of a local search, which may creep on forever

	helper = 0.9               // a helper axis closer than this to n gives a poor cross product
	golden = 2.399963229728653 // the golden angle, spreading directions over the sphere
)

type vec [dim]float64
type frame [dim]vec
type int3 [dim]int64

func dot(a, b vec) float64 { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }

func cross(a, b vec) vec {
	return vec{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}

// comb gives s * a + t * b.
func comb(a vec, s float64, b vec, t float64) vec {
	return vec{s*a[0] + t*b[0], s*a[1] + t*b[1], s*a[2] + t*b[2]}
}

func unit(a vec) vec {
	n := math.Sqrt(dot(a, a))
	return vec{a[0] / n, a[1] / n, a[2] / n}
}

// turn rotates v by angle around the unit vector axis (Rodrigues).
func turn(v, axis vec, angle float64) vec {
	c, s := math.Cos(angle), math.Sin(angle)
	k := dot(axis, v) * (1 - c)
	w := cross(axis, v)
	return vec{v[0]*c + w[0]*s + axis[0]*k, v[1]*c + w[1]*s + axis[1]*k, v[2]*c + w[2]*s + axis[2]*k}
}

// across gives two unit vectors completing n to a right-handed frame.
func across(n vec) (vec, vec) {
	aid := vec{1, 0, 0}
	if math.Abs(n[0]) > helper {
		aid = vec{0, 1, 0}
	}
	a := unit(cross(n, aid))
	return a, cross(n, a)
}

var pts []vec

func width(u vec) float64 {
	lo, hi := math.Inf(1), math.Inf(-1)
	for _, p := range pts {
		s := dot(p, u)
		lo, hi = math.Min(lo, s), math.Max(hi, s)
	}
	return hi - lo
}

func spread(f frame) float64 {
	w0, w1, w2 := width(f[0]), width(f[1]), width(f[2])
	return math.Max(w0, math.Max(w1, w2)) - math.Min(w0, math.Min(w1, w2))
}

func show(f frame) {
	for _, u := range f {
		fmt.Printf("%.15f %.15f %.15f\n", u[0], u[1], u[2])
	}
}

// enclosure retains a nonzero winding, which survives subdivision.
func enclosure(scale float64) frame {
	type vertex struct {
		q [4]float64
		r [2]float64
	}
	var answer frame
	found := false
	at := func(q [4]float64) vertex {
		w, x, y, z := q[0], q[1], q[2], q[3]
		f := frame{{1 - 2*(y*y+z*z), 2 * (x*y + w*z), 2 * (x*z - w*y)},
			{2 * (x*y - w*z), 1 - 2*(x*x+z*z), 2 * (y*z + w*x)},
			{2 * (x*z + w*y), 2 * (y*z - w*x), 1 - 2*(x*x+y*y)}}
		ws := vec{width(f[0]), width(f[1]), width(f[2])}
		if math.Max(ws[0], math.Max(ws[1], ws[2]))-math.Min(ws[0], math.Min(ws[1], ws[2])) <= near*scale {
			answer, found = f, true
		}
		return vertex{q, [2]float64{ws[0] - ws[2], ws[1] - ws[2]}}
	}
	middle := func(a, b vertex) vertex {
		var q [4]float64
		norm := 0.0
		for i := range q {
			q[i] = a.q[i] + b.q[i]
			norm += q[i] * q[i]
		}
		norm = math.Sqrt(norm)
		for i := range q {
			q[i] /= norm
		}
		return at(q)
	}
	var edge func(vertex, vertex) float64
	edge = func(a, b vertex) float64 {
		if found {
			return 0
		}
		distance := 0.0
		for i := range a.q {
			distance += (a.q[i] - b.q[i]) * (a.q[i] - b.q[i])
		}
		distance = math.Sqrt(distance)
		u, v := a.r, b.r
		// Each residual changes by at most 4 * diameter * chord length.
		if math.Max(math.Abs(u[0]), math.Abs(u[1])) > 4*scale*distance {
			return math.Atan2(u[0]*v[1]-u[1]*v[0], u[0]*v[0]+u[1]*v[1])
		}
		m := middle(a, b)
		return edge(a, m) + edge(m, b)
	}
	winding := func(a, b, c vertex) float64 { return edge(a, b) + edge(b, c) + edge(c, a) }
	// The boundary cycles the axes, so its winding cannot be zero.
	rim := [dim]vertex{
		at([4]float64{1, 0, 0, 0}),
		at([4]float64{-0.5, 0.5, 0.5, 0.5}),
		at([4]float64{-0.5, -0.5, -0.5, -0.5}),
	}
	r2 := 1 / math.Sqrt(2)
	center := at([4]float64{0, r2, -r2, 0})
	var triangle [dim]vertex
	for i := 0; i < dim; i++ {
		if math.Abs(winding(center, rim[i], rim[(i+1)%dim])) > math.Pi {
			triangle = [dim]vertex{center, rim[i], rim[(i+1)%dim]}
			break
		}
	}
	for !found {
		a, b, c := triangle[0], triangle[1], triangle[2]
		ab, bc, ca := middle(a, b), middle(b, c), middle(c, a)
		for _, tri := range [][dim]vertex{{a, ab, ca}, {ab, b, bc}, {ca, bc, c}, {ab, bc, ca}} {
			if math.Abs(winding(tri[0], tri[1], tri[2])) > math.Pi {
				triangle = tri
				break
			}
		}
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var count int
	fmt.Fscan(in, &count)
	ints := make([]int3, count)
	for i := range ints {
		fmt.Fscan(in, &ints[i][0], &ints[i][1], &ints[i][2])
		pts = append(pts, vec{float64(ints[i][0]), float64(ints[i][1]), float64(ints[i][2])})
	}
	// Accept the initial coordinate frame when its box is already a cube.
	aligned := frame{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
	ws := vec{width(aligned[0]), width(aligned[1]), width(aligned[2])}
	if ws[0] == ws[1] && ws[1] == ws[2] {
		show(aligned)
		return
	}
	// the shape of the swarm, decided exactly on the integers
	diff := func(i int) int3 {
		return int3{ints[i][0] - ints[0][0], ints[i][1] - ints[0][1], ints[i][2] - ints[0][2]}
	}
	icross := func(a, b int3) int3 {
		return int3{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
	}
	var first, normal int3
	for i := 1; i < count && first == (int3{}); i++ {
		first = diff(i)
	}
	for i := 1; i < count && normal == (int3{}); i++ {
		normal = icross(first, diff(i))
	}
	if normal == (int3{}) {
		// all on a line of direction d: an axis at angle acos(1/sqrt 3) to the
		// line each, so the three widths are the length over sqrt 3
		d := unit(vec{float64(first[0]), float64(first[1]), float64(first[2])})
		u, v := across(d)
		r3, r2, r6 := 1/math.Sqrt(dim), 1/math.Sqrt(2), 1/math.Sqrt(2*dim)
		show(frame{comb(comb(d, r3, u, r2), 1, v, r6), comb(comb(d, r3, u, -r2), 1, v, r6),
			comb(d, r3, v, -2*r6)})
		return
	}
	flat := true
	for i := 1; i < count; i++ {
		d := diff(i)
		flat = flat && normal[0]*d[0]+normal[1]*d[1]+normal[2]*d[2] == 0
	}
	// widest direction: the diameter, where no other width can be larger
	bestLength := int64(-1)
	var nMax vec
	for _, p := range ints {
		for _, q := range ints {
			dx, dy, dz := p[0]-q[0], p[1]-q[1], p[2]-q[2]
			if l := dx*dx + dy*dy + dz*dz; l > bestLength {
				bestLength = l
				nMax = vec{float64(dx), float64(dy), float64(dz)}
			}
		}
	}
	nMax = unit(nMax)
	// narrowest direction: the normal of a flat swarm, else a search
	var nMin vec
	if flat {
		nMin = unit(vec{float64(normal[0]), float64(normal[1]), float64(normal[2])})
	} else {
		wMin := math.Inf(1)
		for i := 0; i < sphere; i++ {
			z := 1 - float64(2*i+1)/(2*sphere)
			r := math.Sqrt(1 - z*z)
			u := vec{r * math.Cos(golden*float64(i)), r * math.Sin(golden*float64(i)), z}
			if w := width(u); w < wMin {
				wMin, nMin = w, u
			}
		}
		step := 2 * math.Pi / math.Sqrt(sphere)
		for round := 0; round < rounds && step > tiny; round++ {
			a, b := across(nMin)
			moved := false
			for _, axis := range []vec{a, b, unit(comb(a, 1, b, 1)), unit(comb(a, 1, b, -1))} {
				for _, sign := range []float64{1, -1} {
					cand := unit(turn(nMin, axis, sign*step))
					if w := width(cand); w < wMin {
						wMin, nMin, moved = w, cand, true
					}
				}
			}
			if !moved {
				step /= 2
			}
		}
	}
	// frames along the great circle from nMin to nMax: the third axis is the
	// turned n, the first two the turned a0, b0 rotated by phi
	hinge := cross(nMin, nMax)
	if dot(hinge, hinge) < tiny {
		hinge, _ = across(nMin)
	}
	hinge = unit(hinge)
	angle := math.Acos(math.Max(-1, math.Min(1, dot(nMin, nMax))))
	a0, b0 := across(nMin)
	at := func(t, phi float64) frame {
		n := turn(nMin, hinge, angle*t)
		a, b := turn(a0, hinge, angle*t), turn(b0, hinge, angle*t)
		c, s := math.Cos(phi), math.Sin(phi)
		return frame{comb(a, c, b, s), comb(a, -s, b, c), n}
	}
	// phi in [0, pi/2] with equal first two widths: the difference changes
	// sign over a quarter turn, as the axes swap places
	balance := func(t float64) float64 {
		gapAt := func(phi float64) float64 {
			f := at(t, phi)
			return width(f[0]) - width(f[1])
		}
		lo, hi := 0.0, math.Pi/2
		if gapAt(lo) > 0 {
			lo, hi = hi, lo
		}
		for i := 0; i < steps; i++ {
			mid := (lo + hi) / 2
			if gapAt(mid) > 0 {
				hi = mid
			} else {
				lo = mid
			}
		}
		return (lo + hi) / 2
	}
	// Try equalizing the third width; the candidate is checked afterwards.
	lo, hi := 0.0, 1.0
	for i := 0; i < steps; i++ {
		mid := (lo + hi) / 2
		f := at(mid, balance(mid))
		if width(f[2])-width(f[0]) < 0 {
			lo = mid
		} else {
			hi = mid
		}
	}
	t := (lo + hi) / 2
	result := at(t, balance(t))
	scale := math.Max(1, width(nMax))
	if spread(result) > near*scale {
		result = enclosure(scale)
	}
	show(result)
}
