package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var w, h, x, y int
	fmt.Fscan(in, &w, &h, &x, &y)
	// the map padded by a ring of outside cells
	pw, ph := w+2, h+2
	land := make([]bool, pw*ph)
	for i := 1; i <= h; i++ {
		for j := 1; j <= w; {
			c, err := in.ReadByte()
			if err != nil {
				break
			}
			if c == '#' || c == '.' {
				land[i*pw+j] = c == '#'
				j++
			}
		}
	}
	step4 := []int{1, -1, pw, -pw}
	step8 := []int{1, -1, pw, -pw, pw + 1, pw - 1, -pw + 1, -pw - 1}
	inside := func(c int) bool {
		r, k := c/pw, c%pw
		return r >= 1 && r <= h && k >= 1 && k <= w
	}
	// flood visits every cell reachable from start through cells for which
	// ok holds, moving along the given steps
	flood := func(start int, ok func(int) bool, steps []int, mark []bool) {
		stack := []int{start}
		mark[start] = true
		for len(stack) > 0 {
			c := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, d := range steps {
				if n := c + d; n >= 0 && n < len(mark) && !mark[n] && ok(n) {
					mark[n] = true
					stack = append(stack, n)
				}
			}
		}
	}
	// the sacred sea: sea cells joined to the drowning point by 8 directions
	sacred := make([]bool, pw*ph)
	start := y*pw + x
	if !land[start] {
		flood(start, func(c int) bool { return inside(c) && !land[c] }, step8, sacred)
	}
	// an eight-connected sea stops every four-connected path, so what the
	// outside cannot reach without crossing the sacred sea lies inside it
	outside := make([]bool, pw*ph)
	flood(0, func(c int) bool { return !sacred[c] }, step4, outside)
	seen := make([]bool, pw*ph)
	count := 0
	for c := range land {
		if land[c] && !outside[c] && !seen[c] {
			count++
			flood(c, func(n int) bool { return land[n] }, step4, seen)
		}
	}
	fmt.Println(count)
}
