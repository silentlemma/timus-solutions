package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

// the four small triangles of a unit square, cut by both its diagonals
const (
	south = iota
	east
	north
	west
	parts
)

const triangle = 3

// outward directions of a triangle's edges, counterclockwise from +x
const (
	right = iota
	upRight
	up
	upLeft
	left
	downLeft
	down
	downRight
)

var parent []int

func find(a int) int {
	for parent[a] != a {
		parent[a] = parent[parent[a]]
		a = parent[a]
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var m, n, k int
	fmt.Fscan(in, &m, &n, &k)
	// a cut runs from border to border, so it is a whole line of one of the
	// four kinds: x = c, y = c, x - y = c or x + y = c
	vert, hor := make([]bool, m+1), make([]bool, n+1)
	diff, sum := make([]bool, m+n+1), make([]bool, m+n+1)
	for ; k > 0; k-- {
		var x1, y1, x2, y2 int
		fmt.Fscan(in, &x1, &y1, &x2, &y2)
		switch {
		case x1 == x2:
			vert[x1] = true
		case y1 == y2:
			hor[y1] = true
		case x2-x1 == y2-y1:
			diff[x1-y1+n] = true
		default:
			sum[x1+y1] = true
		}
	}
	cell := func(i, j, t int) int { return (i*n+j)*parts + t }
	parent = make([]int, m*n*parts)
	for a := range parent {
		parent[a] = a
	}
	out := make([]uint, m*n*parts)
	// side joins two small triangles, or records their outward directions
	// when a cut separates them
	side := func(a, da, b, db int, cut bool) {
		if cut {
			out[a] |= 1 << da
			out[b] |= 1 << db
		} else {
			parent[find(a)] = find(b)
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			s, e, no, w := cell(i, j, south), cell(i, j, east), cell(i, j, north), cell(i, j, west)
			side(s, upRight, e, downLeft, sum[i+j+1])
			side(s, upLeft, w, downRight, diff[i-j+n])
			side(e, upLeft, no, downRight, diff[i-j+n])
			side(no, downLeft, w, upRight, sum[i+j+1])
			if j == 0 {
				out[s] |= 1 << down
			} else {
				side(s, down, cell(i, j-1, north), up, hor[j])
			}
			if i == 0 {
				out[w] |= 1 << left
			} else {
				side(w, left, cell(i-1, j, east), right, vert[i])
			}
			if j == n-1 {
				out[no] |= 1 << up
			}
			if i == m-1 {
				out[e] |= 1 << right
			}
		}
	}
	// every piece is convex with sides in these 8 directions, one side per
	// direction, so a piece is a triangle when its edges face 3 directions
	faces := make([]uint, len(out))
	for a, d := range out {
		faces[find(a)] |= d
	}
	count := 0
	for a, d := range faces {
		if find(a) == a && bits.OnesCount(d) == triangle {
			count++
		}
	}
	fmt.Println(count)
}
