package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	span  = 10000 // coordinates lie in [-span, span]
	reach = 10    // direction parts lie in [-reach, reach]
	width = 2*span + 1
	turn  = 2*reach + 1
)

func gcd(a, b int) int {
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

type rabbit struct{ line, place int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	rx, ry := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &rx[i], &ry[i])
	}
	var q, x, y, vx, vy, ax, bx, ay, by, avx, bvx, avy, bvy int
	fmt.Fscan(in, &q, &x, &y, &vx, &vy, &ax, &bx, &ay, &by, &avx, &bvx, &avy, &bvy)
	// every direction is filed under its primitive vector
	var primitive [][2]int
	index := map[[2]int]int{}
	code := make([]int, turn*turn)
	for dx := -reach; dx <= reach; dx++ {
		for dy := -reach; dy <= reach; dy++ {
			g := gcd(dx, dy)
			if g == 0 {
				continue
			}
			key := [2]int{dx / g, dy / g}
			k, ok := index[key]
			if !ok {
				k = len(primitive)
				index[key] = k
				primitive = append(primitive, key)
			}
			code[(dx+reach)*turn+dy+reach] = k
		}
	}
	kinds := len(primitive)
	xs, ys, kind := make([]int32, q), make([]int32, q), make([]int32, q)
	start := make([]int, kinds+1)
	for i := 0; i < q; i++ {
		xs[i], ys[i] = int32(x), int32(y)
		kind[i] = int32(code[(vx+reach)*turn+vy+reach])
		start[kind[i]+1]++
		x = (ax*(x+span)+bx)%width - span
		y = (ay*(y+span)+by)%width - span
		vx = (avx*(vx+reach)+bvx)%turn - reach
		vy = (avy*(vy+reach)+bvy)%turn - reach
	}
	// the shots in order of their direction, by counting
	for k := 0; k < kinds; k++ {
		start[k+1] += start[k]
	}
	shots := make([]int32, q)
	fill := append([]int(nil), start[:kinds]...)
	for i := 0; i < q; i++ {
		shots[fill[kind[i]]] = int32(i)
		fill[kind[i]]++
	}
	best, bestCount := 0, -1
	rabbits := make([]rabbit, n)
	for k := 0; k < kinds; k++ {
		if start[k] == start[k+1] {
			continue
		}
		dx, dy := primitive[k][0], primitive[k][1]
		// rabbits by the line along (dx, dy) and then by the place on it
		for i := 0; i < n; i++ {
			rabbits[i] = rabbit{rx[i]*dy - ry[i]*dx, rx[i]*dx + ry[i]*dy}
		}
		sort.Slice(rabbits, func(i, j int) bool {
			if rabbits[i].line != rabbits[j].line {
				return rabbits[i].line < rabbits[j].line
			}
			return rabbits[i].place < rabbits[j].place
		})
		for j := start[k]; j < start[k+1]; j++ {
			i := int(shots[j])
			line := int(xs[i])*dy - int(ys[i])*dx
			place := int(xs[i])*dx + int(ys[i])*dy
			from := sort.Search(n, func(t int) bool {
				r := rabbits[t]
				return r.line > line || (r.line == line && r.place >= place)
			})
			to := sort.Search(n, func(t int) bool { return rabbits[t].line > line })
			got := to - from
			// a later shot wins a tie
			if got > bestCount || (got == bestCount && i > best) {
				best, bestCount = i, got
			}
		}
	}
	fmt.Println(best+1, bestCount)
}
