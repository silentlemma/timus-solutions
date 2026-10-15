package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const (
	dim  = 3
	tiny = 1e-14
	same = 1e-7 // equal edge lengths up to rounding
)

type vec [dim]float64

type mat [dim]vec // rows

var phi = (1 + math.Sqrt(5)) / 2

func dot(a, b vec) float64 { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }

func unit(v vec) vec {
	n := math.Sqrt(dot(v, v))
	return vec{v[0] / n, v[1] / n, v[2] / n}
}

func cross(a, b vec) vec {
	return vec{a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]}
}

func dist(a, b vec) float64 {
	d := vec{a[0] - b[0], a[1] - b[1], a[2] - b[2]}
	return math.Sqrt(dot(d, d))
}

func apply(m mat, v vec) vec { return vec{dot(m[0], v), dot(m[1], v), dot(m[2], v)} }

func compose(a, b mat) mat {
	var r mat
	for i := 0; i < dim; i++ {
		for j := 0; j < dim; j++ {
			for k := 0; k < dim; k++ {
				r[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return r
}

// rotation by angle around axis, right-handed
func rotation(axis vec, angle float64) mat {
	u := unit(axis)
	x, y, z := u[0], u[1], u[2]
	c, s := math.Cos(angle), math.Sin(angle)
	t := 1 - c
	return mat{
		{t*x*x + c, t*x*y - s*z, t*x*z + s*y},
		{t*x*y + s*z, t*y*y + c, t*y*z - s*x},
		{t*x*z - s*y, t*y*z + s*x, t*z*z + c},
	}
}

func solid(name string) []vec {
	signs := []float64{-1, 1}
	var pts []vec
	switch name {
	case "tetrahedron":
		pts = []vec{{1, 1, 1}, {1, -1, -1}, {-1, 1, -1}, {-1, -1, 1}}
	case "octahedron":
		pts = []vec{{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {0, 0, 1}, {0, 0, -1}}
	case "icosahedron":
		for _, a := range signs {
			for _, b := range signs {
				pts = append(pts, vec{0, a, b * phi}, vec{a, b * phi, 0}, vec{b * phi, 0, a})
			}
		}
	default:
		for _, x := range signs {
			for _, y := range signs {
				for _, z := range signs {
					pts = append(pts, vec{x, y, z})
				}
			}
		}
		if name == "dodecahedron" {
			for _, a := range signs {
				for _, b := range signs {
					pts = append(pts, vec{0, a / phi, b * phi}, vec{a / phi, b * phi, 0}, vec{b * phi, 0, a / phi})
				}
			}
		}
	}
	for i := range pts {
		pts[i] = unit(pts[i])
	}
	return pts
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var name string
	var n int
	if _, err := fmt.Fscan(in, &name, &n); err != nil {
		return
	}
	guns := solid(name)
	edge := math.Inf(1)
	for _, a := range guns {
		for _, b := range guns {
			if d := dist(a, b); d > same && d < edge {
				edge = d
			}
		}
	}
	// turn the solid so that one gun points along z and a neighbour lies in
	// the half-plane x >= 0 of Oxz; any choice is the same up to symmetry
	z, near := guns[0], guns[0]
	for _, g := range guns {
		if math.Abs(dist(g, z)-edge) < same {
			near = g
			break
		}
	}
	along := dot(near, z)
	x := unit(vec{near[0] - along*z[0], near[1] - along*z[1], near[2] - along*z[2]})
	y := cross(z, x)
	for i, g := range guns {
		guns[i] = unit(vec{dot(g, x), dot(g, y), dot(g, z)})
	}
	turn := mat{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}
	total := 0.0
	for i := 0; i < n; i++ {
		var v vec
		fmt.Fscan(in, &v[0], &v[1], &v[2])
		target := unit(vec{-v[0], -v[1], -v[2]}) // the ship comes from there
		gun := apply(turn, guns[0])
		for _, g := range guns {
			if turned := apply(turn, g); dot(turned, target) > dot(gun, target) {
				gun = turned
			}
		}
		angle := math.Acos(math.Max(-1, math.Min(1, dot(gun, target))))
		total += angle
		axis := cross(gun, target)
		if angle > tiny && math.Sqrt(dot(axis, axis)) > tiny {
			// the shortest turn: around the axis normal to both directions
			turn = compose(rotation(axis, angle), turn)
		}
	}
	fmt.Printf("%.5f\n", total)
}
