package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const camel = 1

// animal is a ray from the origin, reduced by the gcd, and the animal's kind
type animal struct{ a, b, kind int }

func gcd(x, y int) int {
	for y != 0 {
		x, y = y, x%y
	}
	return x
}

func cross(p, q animal) int { return p.a*q.b - p.b*q.a }

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	animals := make([]animal, n)
	origin := false
	for i := range animals {
		x := &animals[i]
		fmt.Fscan(reader, &x.a, &x.b, &x.kind)
		if g := gcd(x.a, x.b); g == 0 {
			origin = true // nobody can judge an animal at the origin
		} else {
			x.a, x.b = x.a/g, x.b/g
		}
	}
	if origin {
		fmt.Fprintln(writer, -1)
		return
	}
	// rays by angle, counterclockwise from the A axis
	sort.Slice(animals, func(i, j int) bool { return cross(animals[i], animals[j]) > 0 })
	var experts [][2]int
	for i := 0; i+1 < n; i++ {
		p, q := animals[i], animals[i+1]
		if cross(p, q) == 0 {
			if p.kind != q.kind {
				fmt.Fprintln(writer, -1) // every expert judges a whole ray alike
				return
			}
			continue
		}
		if p.kind == q.kind {
			continue
		}
		// a line along p + q passes strictly between the two rays
		x, y := p.a+q.a, p.b+q.b
		g := gcd(x, y)
		x, y = x/g, y/g
		if p.kind == camel {
			experts = append(experts, [2]int{y, -x})
		} else {
			experts = append(experts, [2]int{-y, x})
		}
	}
	if len(experts)%2 == 0 {
		// an odd count avoids ties; one more expert votes for the first kind
		s := -1
		if animals[0].kind == camel {
			s = 1
		}
		experts = append(experts, [2]int{s, s})
	}
	fmt.Fprintln(writer, len(experts))
	for _, e := range experts {
		fmt.Fprintln(writer, e[0], e[1])
	}
}
