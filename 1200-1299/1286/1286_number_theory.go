package main

import "fmt"

func gcd(a, b int64) int64 {
	if a < 0 {
		a = -a
	}
	if b < 0 {
		b = -b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var p, q, x, y, x1, y1 int64
	fmt.Scan(&p, &q, &x, &y, &x1, &y1)
	dx, dy, g := x1-x, y1-y, gcd(p, q)
	var ok bool
	switch {
	case g == 0:
		ok = dx == 0 && dy == 0
	case dx%g != 0 || dy%g != 0:
		ok = false
	default:
		// with p/g and q/g coprime, the moves reach every point of the
		// lattice g Z^2, except that when both are odd every move keeps the
		// parity of (dx + dy) / g
		bothOdd := (p/g)%2 != 0 && (q/g)%2 != 0
		ok = !bothOdd || (dx/g+dy/g)%2 == 0
	}
	if ok {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
