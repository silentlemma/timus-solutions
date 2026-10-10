package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// edges of the cube: A B C D around the bottom face, E F G H above them
var edges = []string{"AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"}

const (
	// the cube is bipartite; every operation changes one chamber of each side
	evenSide = "ACFH"
	cells    = "ABCDEFGH"
)

func even(c byte) bool { return strings.IndexByte(evenSide, c) >= 0 }

func main() {
	count := map[byte]int{}
	balance := 0
	for i := range cells {
		var v int
		fmt.Scan(&v)
		count[cells[i]] = v
		if even(cells[i]) {
			balance += v
		} else {
			balance -= v
		}
	}
	if balance != 0 {
		fmt.Println("IMPOSSIBLE")
		return
	}
	near := map[byte][]byte{}
	for _, e := range edges {
		near[e[0]] = append(near[e[0]], e[1])
		near[e[1]] = append(near[e[1]], e[0])
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	emit := func(a, b, sign byte) { out.Write([]byte{a, b, sign, '\n'}) }
	// annihilate along every edge as long as both ends hold duons; afterwards
	// every edge has an empty end
	for _, e := range edges {
		k := count[e[0]]
		if count[e[1]] < k {
			k = count[e[1]]
		}
		for j := 0; j < k; j++ {
			emit(e[0], e[1], '-')
		}
		count[e[0]] -= k
		count[e[1]] -= k
	}
	// what is left can only sit at two opposite corners u and w, in equal
	// numbers; a pair made on the middle edge of a path u x y w removes both
	for i := range evenSide {
		u := evenSide[i]
		if count[u] == 0 {
			continue
		}
		var w, y byte
		for j := range cells {
			if c := cells[j]; w == 0 && count[c] > 0 && !even(c) {
				w = c
			}
		}
		x := near[u][0]
		for _, c := range near[x] {
			for _, d := range near[w] {
				if y == 0 && c == d {
					y = c
				}
			}
		}
		for k := 0; k < count[u]; k++ {
			emit(x, y, '+')
			emit(u, x, '-')
			emit(y, w, '-')
		}
		count[w] -= count[u]
		count[u] = 0
	}
}
