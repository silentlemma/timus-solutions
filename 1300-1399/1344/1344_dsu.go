package main

import (
	"fmt"
	"math"
)

const (
	ceiling, turnip, free = 0, -1, -2
	one, mass             = 0, 1 // the turnip's weight of 1 and the unknown mass
)

type port struct {
	node, target int
	down         bool
}

var (
	kind, x1, x2, up, parent, shift []int
	zero                            []bool // the whole group must have no tension
)

func rope(i int) int { return 2*i + 2 }     // tension in the rope over block i
func axle(i int) int { return rope(i) + 1 } // tension in the rope at the axle of block i

// every tension is a power of two times the tension at the root of its
// group: value(x) = 2^shift[x] * value(root)
func find(x int) int {
	if parent[x] == x {
		return x
	}
	root := find(parent[x])
	shift[x] += shift[parent[x]]
	parent[x] = root
	return root
}

// value(x) = 2^k * value(y)
func tie(x, y, k int) {
	rx, ry := find(x), find(y)
	if rx == ry {
		if shift[x] != k+shift[y] {
			zero[rx] = true
		}
		return
	}
	parent[rx] = ry
	shift[rx] = k + shift[y] - shift[x]
	zero[ry] = zero[ry] || zero[rx]
}

// the two rope ends and the axle, with the way they leave the block; a
// first-type block hangs its rope ends down
func ports(i int) []port {
	down := kind[i] == 1
	return []port{{rope(i), x1[i], down}, {rope(i), x2[i], down}, {axle(i), up[i], !down}}
}

func main() {
	var n int
	fmt.Scan(&n)
	kind, x1, x2, up = make([]int, n), make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&kind[i], &x1[i], &x2[i], &up[i])
	}
	parent, shift, zero = make([]int, 2*n+2), make([]int, 2*n+2), make([]bool, 2*n+2)
	for v := range parent {
		parent[v] = v
	}
	for i := 0; i < n; i++ {
		tie(axle(i), rope(i), 1) // the axle holds both ends of the rope
		for _, p := range ports(i) {
			switch {
			case p.target == turnip:
				tie(p.node, one, 0)
			case p.target == free:
				tie(p.node, mass, 0)
			case p.target != ceiling:
				// the other end leaves block target the opposite way
				for _, q := range ports(p.target - 1) {
					if q.target == i+1 && q.down != p.down {
						tie(p.node, q.node, 0)
						break
					}
				}
			}
		}
	}
	r1, rm := find(one), find(mass)
	switch {
	case zero[r1]:
		fmt.Println("No solution")
	case r1 == rm:
		fmt.Printf("%.4f\n", math.Ldexp(1, shift[mass]-shift[one]))
	case zero[rm]:
		fmt.Printf("%.4f\n", 0.0)
	default:
		fmt.Println("Any")
	}
}
