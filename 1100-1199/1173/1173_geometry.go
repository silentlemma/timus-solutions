package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
)

// scale: coordinates have at most three decimals, so in thousandths they
// are exact integers and every turn below is decided without rounding
const scale = 1000

type friend struct {
	x, y int64
	id   int
}

func half(p friend) int {
	if p.y > 0 || (p.y == 0 && p.x > 0) {
		return 0
	}
	return 1
}

func cross(p, q friend) int64 {
	return p.x*q.y - p.y*q.x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	exact := func() int64 {
		var v float64
		fmt.Fscan(in, &v)
		return int64(math.Round(v * scale))
	}
	hx, hy := exact(), exact()
	var n int
	fmt.Fscan(in, &n)
	friends := make([]friend, n)
	for i := range friends {
		friends[i].x = exact() - hx
		friends[i].y = exact() - hy
		fmt.Fscan(in, &friends[i].id)
	}
	sort.Slice(friends, func(i, j int) bool {
		p, q := friends[i], friends[j]
		if half(p) != half(q) {
			return half(p) < half(q)
		}
		return cross(p, q) > 0
	})
	// consecutive friends by angle, joined in turn, never cross; the house
	// closes the loop across one angular gap, which must be the one wider
	// than half a turn if there is one
	start := 0
	for i := 0; i < n; i++ {
		if cross(friends[(i+n-1)%n], friends[i]) < 0 {
			start = i
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, 0)
	for k := 0; k < n; k++ {
		fmt.Fprintln(out, friends[(start+k)%n].id)
	}
	fmt.Fprintln(out, 0)
}
