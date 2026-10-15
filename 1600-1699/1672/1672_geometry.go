package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

const (
	dim    = 3
	steps  = 60   // halvings in each bisection
	sphere = 1500 // directions tried for the narrowest width

	grid   = 80 // grid side of the fallback search
	starts = 4  // best grid cells it zooms in around
	zooms  = 14 // rounds of zooming, each one zoom times finer
	zoom   = 5

	tiny   = 1e-13 // where the local search stops
	near   = 1e-10 // equal widths, relative to the diameter
	rounds = 400   // passes of a local search, which may creep on forever

	helper    = 0.9                // a helper axis closer than this to n gives a poor cross product
	golden    = 2.399963229728653  // the golden angle, spreading directions over the sphere
	firstTurn = 0.7853981633974483 // pi / 4, the first turn of the polish
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

func cost(f frame) float64 {
	w0, w1, w2 := width(f[0]), width(f[1]), width(f[2])
	return (w0-w1)*(w0-w1) + (w1-w2)*(w1-w2) + (w2-w0)*(w2-w0)
}

func show(f frame) {
	for _, u := range f {
		fmt.Printf("%.15f %.15f %.15f\n", u[0], u[1], u[2])
	}
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
	// at nMin the third width is the smallest, at nMax the largest
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
		// the chosen balance jumped. A solution still lies in the (t, phi)
		// square, as the third width is the smallest along t = 0 and the
		// largest along t = 1: scan it, then zoom in around the best cells
		quarter := math.Pi / 2
		type cell struct{ c, t, p float64 }
		var cells []cell
		for i := 0; i < grid; i++ {
			for j := 0; j < grid; j++ {
				ti, pj := float64(i)/(grid-1), quarter*float64(j)/(grid-1)
				cells = append(cells, cell{cost(at(ti, pj)), ti, pj})
			}
		}
		sort.Slice(cells, func(i, j int) bool { return cells[i].c < cells[j].c })
		for _, start := range cells[:starts] {
			dt, dp := 1.0/(grid-1), quarter/(grid-1)
			here := start
			for z := 0; z < zooms; z++ {
				tc, pc := here.t, here.p
				for a := -zoom; a <= zoom; a++ {
					ta := math.Min(1, math.Max(0, tc+float64(a)*dt/zoom))
					for b := -zoom; b <= zoom; b++ {
						pb := pc + float64(b)*dp/zoom
						if c := cost(at(ta, pb)); c < here.c {
							here = cell{c, ta, pb}
						}
					}
				}
				dt, dp = dt/zoom, dp/zoom
			}
			result = at(here.t, here.p)
			if spread(result) <= near*scale {
				break
			}
		}
	}
	// polish by small turns of the frame about its own axes
	best := cost(result)
	step := tiny * 2
	if spread(result) > near*scale {
		step = firstTurn
	}
	for round := 0; round < rounds && step > tiny; round++ {
		moved := false
		for k := 0; k < dim; k++ {
			for _, sign := range []float64{1, -1} {
				cand := result
				for i := 0; i < dim; i++ {
					if i != k {
						cand[i] = turn(result[i], result[k], sign*step)
					}
				}
				if c := cost(cand); c < best {
					best, result, moved = c, cand, true
				}
			}
		}
		if !moved {
			step /= 2
		}
	}
	show(result)
}
