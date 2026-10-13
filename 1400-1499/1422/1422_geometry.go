package main

import (
	"bufio"
	"fmt"
	"os"
)

const dims = 3 // x, y and z

func gcd(a, b int32) int32 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func abs(a int32) int32 {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	p := make([][dims]int32, n)
	for i := range p {
		fmt.Fscan(in, &p[i][0], &p[i][1], &p[i][2])
	}
	best := 1
	for i := 0; i < n && n-i > best; i++ {
		same := 0
		lines := make(map[[dims]int32]int, n-i)
		most := 0
		for j := i + 1; j < n; j++ {
			dx, dy, dz := p[j][0]-p[i][0], p[j][1]-p[i][1], p[j][2]-p[i][2]
			g := gcd(abs(dx), gcd(abs(dy), abs(dz)))
			if g == 0 {
				same++ // several flies may hang at one point
				continue
			}
			// one key per direction: reduced, with the first non-zero part positive
			if dx < 0 || (dx == 0 && (dy < 0 || (dy == 0 && dz < 0))) {
				g = -g
			}
			key := [dims]int32{dx / g, dy / g, dz / g}
			lines[key]++
			if lines[key] > most {
				most = lines[key]
			}
		}
		if 1+same+most > best {
			best = 1 + same + most
		}
	}
	fmt.Println(best)
}
