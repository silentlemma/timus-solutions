package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type vec struct{ x, y int }

func half(v vec) int {
	if v.y > 0 || (v.y == 0 && v.x > 0) {
		return 0
	}
	return 1
}

func cross(a, b vec) int { return a.x*b.y - a.y*b.x }

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	p := make([]vec, n)
	for i := range p {
		fmt.Fscan(reader, &p[i].x, &p[i].y)
	}
	for i := n - 1; i >= 0; i-- {
		p[i] = vec{p[i].x - p[0].x, p[i].y - p[0].y}
	}
	order := make([]int, 0, n-1)
	for i := 1; i < n; i++ {
		order = append(order, i)
	}
	// by angle around the first pumpkin, nearer first on the same ray
	sort.Slice(order, func(i, j int) bool {
		a, b := p[order[i]], p[order[j]]
		if half(a) != half(b) {
			return half(a) < half(b)
		}
		if c := cross(a, b); c != 0 {
			return c > 0
		}
		return abs(a.x)+abs(a.y) < abs(b.x)+abs(b.y)
	})
	// cut the circle after a turn of at least half a circle, if there is one:
	// then every step turns by less than that and the walk never meets itself
	m, start := len(order), 0
	for k := 0; k < m; k++ {
		a, b := p[order[(k+m-1)%m]], p[order[k]]
		c := cross(a, b)
		if c < 0 || (c == 0 && a.x*b.x+a.y*b.y < 0) {
			start = k
		}
	}
	fmt.Fprintf(writer, "%d\n1\n", n)
	for k := 0; k < m; k++ {
		fmt.Fprintln(writer, order[(start+k)%m]+1)
	}
}
