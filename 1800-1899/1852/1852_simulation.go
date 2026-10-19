package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const dimensions = 3

type vec [dimensions]int

const names = "UDLRFB"

// the outward normal of every face, in the order of names
var faces = []vec{{0, 1, 0}, {0, -1, 0}, {-1, 0, 0}, {1, 0, 0}, {0, 0, 1}, {0, 0, -1}}

func dot(a, b vec) int { return a[0]*b[0] + a[1]*b[1] + a[2]*b[2] }

// turn gives a quarter turn of v about the axis a: counter-clockwise seen
// from the tip of a for sign 1, clockwise for sign -1
func turn(v, a vec, sign int) vec {
	cross := vec{a[1]*v[2] - a[2]*v[1], a[2]*v[0] - a[0]*v[2], a[0]*v[1] - a[1]*v[0]}
	along := dot(a, v)
	var r vec
	for k := range r {
		r[k] = sign*cross[k] + a[k]*along
	}
	return r
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var moves string
	fmt.Fscan(bufio.NewReader(os.Stdin), &moves)
	// a sticker is a cubie position with every coordinate in -1..1 and the
	// outward normal of a face that cubie touches
	type sticker struct{ p, n vec }
	var stickers []sticker
	index := map[sticker]int{}
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			for z := -1; z <= 1; z++ {
				for _, n := range faces {
					if dot(vec{x, y, z}, n) == 1 {
						index[sticker{vec{x, y, z}, n}] = len(stickers)
						stickers = append(stickers, sticker{vec{x, y, z}, n})
					}
				}
			}
		}
	}
	count := len(stickers)
	// the place every sticker moves to under each letter
	table := map[byte][]int{}
	for f, a := range faces {
		for _, sign := range []int{1, -1} {
			letter := names[f]
			if sign == -1 {
				letter = strings.ToLower(names[f : f+1])[0]
			}
			to := make([]int, count)
			for i, s := range stickers {
				to[i] = i
				if dot(s.p, a) == 1 {
					to[i] = index[sticker{turn(s.p, a, sign), turn(s.n, a, sign)}]
				}
			}
			table[letter] = to
		}
	}
	// where each sticker ends up after the whole sequence
	place := make([]int, count)
	for i := range place {
		place[i] = i
	}
	for i := 0; i < len(moves); i++ {
		to := table[moves[i]]
		for j, p := range place {
			place[j] = to[p]
		}
	}
	// the sequence returns the cube after the lcm of the cycle lengths
	order := 1
	seen := make([]bool, count)
	for start := range place {
		length := 0
		for i := start; !seen[i]; i = place[i] {
			seen[i] = true
			length++
		}
		if length > 0 {
			order = order / gcd(order, length) * length
		}
	}
	fmt.Println(order - 1)
}
