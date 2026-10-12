package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

const eps = 1e-7

type point struct{ x, y float64 }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	cities := make([]point, n)
	for i := range cities {
		var x, y int
		fmt.Fscan(in, &x, &y)
		cities[i] = point{float64(x), float64(y)}
	}
	var big, small int
	fmt.Fscan(in, &big, &small)
	reach := float64(big - small) // how far a center may be
	if reach < 0 {
		fmt.Println(0)
		return
	}
	// a best circle can be moved until it passes through two centers or
	// stands on one, so only such places need to be tried
	places := append([]point{}, cities...)
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			a := cities[i]
			dx, dy := cities[j].x-a.x, cities[j].y-a.y
			half := math.Hypot(dx, dy) / 2
			if half > 0 && half <= reach {
				rise := math.Sqrt(math.Max(0, reach*reach-half*half)) / (2 * half)
				mx, my := a.x+dx/2, a.y+dy/2
				places = append(places, point{mx - dy*rise, my + dx*rise}, point{mx + dy*rise, my - dx*rise})
			}
		}
	}
	limit := (reach + eps) * (reach + eps)
	best := 0
	for _, p := range places {
		inside := 0
		for _, c := range cities {
			dx, dy := c.x-p.x, c.y-p.y
			if dx*dx+dy*dy <= limit {
				inside++
			}
		}
		if inside > best {
			best = inside
		}
	}
	fmt.Println(best)
}
