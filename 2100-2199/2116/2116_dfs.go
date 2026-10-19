package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int64
	var a, b int
	fmt.Fscan(in, &n, &a, &b)
	if b == 0 {
		fmt.Println(n * n)
		return
	}

	// For these moves, components stabilize at a side of twice b.
	side := 2 * b
	if n < int64(side) {
		side = int(n)
	}
	seen := make([]bool, side*side)
	stack := make([]int, 0, side*side)
	answer := 0
	for start := range seen {
		if seen[start] {
			continue
		}
		answer++
		seen[start] = true
		stack = append(stack, start)
		for len(stack) > 0 {
			cell := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			x, y := cell/side, cell%side
			for orientation := 0; orientation < 2; orientation++ {
				dx, dy := a, b
				if orientation == 1 {
					dx, dy = b, a
				}
				for sx := -1; sx <= 1; sx += 2 {
					for sy := -1; sy <= 1; sy += 2 {
						nx, ny := x+sx*dx, y+sy*dy
						if nx < 0 || nx >= side || ny < 0 || ny >= side {
							continue
						}
						next := nx*side + ny
						if !seen[next] {
							seen[next] = true
							stack = append(stack, next)
						}
					}
				}
			}
		}
	}
	fmt.Println(answer)
}
