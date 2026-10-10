package main

import (
	"bufio"
	"fmt"
	"os"
)

// face positions in the input: front, right, left, back, top, bottom; a
// quarter turn about the vertical axis (front goes right) and one about the
// left-right axis (top goes front), as new position from old position
const (
	faces = 6
	front = 0
	right = 1
	left  = 2
	back  = 3
)

var (
	spin = [faces]int{2, 0, 3, 1, 4, 5}
	tip  = [faces]int{4, 1, 2, 5, 3, 0}
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// all 24 rotations as position -> original face
	var start [faces]int
	for p := range start {
		start[p] = p
	}
	seen := map[[faces]int]bool{start: true}
	stack := [][faces]int{start}
	var rotations [][faces]int
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		rotations = append(rotations, cur)
		for _, turn := range [][faces]int{spin, tip} {
			var next [faces]int
			for p := 0; p < faces; p++ {
				next[p] = cur[turn[p]]
			}
			if !seen[next] {
				seen[next] = true
				stack = append(stack, next)
			}
		}
	}
	// each cube can show a given ring of side colours at most once, since its
	// faces all differ; the tallest tower is the most common ring
	rings := map[string]int{}
	best := 0
	for i := 0; i < n; i++ {
		var cube string
		fmt.Fscan(in, &cube)
		for _, rot := range rotations {
			ring := string([]byte{cube[rot[front]], cube[rot[right]], cube[rot[back]], cube[rot[left]]})
			rings[ring]++
			if rings[ring] > best {
				best = rings[ring]
			}
		}
	}
	fmt.Println(best)
}
