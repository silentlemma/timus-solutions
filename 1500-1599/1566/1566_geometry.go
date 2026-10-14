package main

import (
	"fmt"
	"math"
	"sort"
)

const (
	eps   = 1e-9 // touching counts as fitting
	sides = 3
)

// apex is the third vertex of a triangle on the segment from (0, 0) to
// (base, 0) whose other sides are left (from the origin) and right
func apex(base, left, right float64) (float64, float64) {
	x := (base*base + left*left - right*right) / (2 * base)
	return x, math.Sqrt(math.Max(0, left*left-x*x))
}

// fitsOn tells whether the card can lie with its side card[0] on the
// envelope's side env[0], in either of its two mirror images
func fitsOn(env, card [sides]float64) bool {
	m, length := env[0], card[0]
	if length > m+eps {
		return false
	}
	wx, height := apex(m, env[1], env[2])
	for mirror := 0; mirror < 2; mirror++ {
		u, h := apex(length, card[1+mirror], card[2-mirror])
		if h > height+eps {
			continue
		}
		// the card slides along the side by t in [0, m - length]; its apex
		// (t + u, h) must stay between the envelope's two other sides
		lo := math.Max(0, h*wx/height-u)
		hi := math.Min(m-length, m-h*(m-wx)/height-u)
		if lo <= hi+eps {
			return true
		}
	}
	return false
}

func main() {
	e, c := make([]int, sides), make([]int, sides)
	for i := range e {
		fmt.Scan(&e[i])
	}
	for i := range c {
		fmt.Scan(&c[i])
	}
	sort.Ints(e)
	sort.Ints(c)
	fits := false
	if e[0]+e[1] == e[2] {
		// a flat envelope holds only a flat card that is no longer
		fits = c[0]+c[1] == c[2] && c[2] <= e[2]
	} else {
		// a triangle fits in another one exactly when it fits with one of its
		// sides lying on a side of the other
		for i := 0; i < sides; i++ {
			for j := 0; j < sides; j++ {
				var env, card [sides]float64
				for k := 0; k < sides; k++ {
					env[k] = float64(e[(i+k)%sides])
					card[k] = float64(c[(j+k)%sides])
				}
				fits = fits || fitsOn(env, card)
			}
		}
	}
	if fits {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
