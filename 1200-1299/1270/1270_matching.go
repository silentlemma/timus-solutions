package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	faces  = 6
	coords = 3 // the cell's place does not matter
)

// faces in the input order: front, up, right, down, left, back; a turn p
// gives face f the colour of face p[f]; spin turns the cube about the
// vertical axis, tip about the left-right one
var spin = [faces]int{2, 1, 5, 3, 0, 4}
var tip = [faces]int{1, 5, 2, 0, 4, 3}

// rotations lists all 24 rotations of a cube, from two quarter turns
func rotations() [][faces]int {
	var start [faces]int
	for f := range start {
		start[f] = f
	}
	found := map[[faces]int]bool{start: true}
	queue := [][faces]int{start}
	for k := 0; k < len(queue); k++ {
		for _, g := range [][faces]int{spin, tip} {
			var q [faces]int
			for f := range q {
				q[f] = queue[k][g[f]]
			}
			if !found[q] {
				found[q] = true
				queue = append(queue, q)
			}
		}
	}
	return queue
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n)
	cubes := make([][faces]int, n)
	for i := range cubes {
		for f := range cubes[i] {
			fmt.Fscan(in, &cubes[i][f])
		}
	}
	fmt.Fscan(in, &m)
	turns := rotations()
	// fits[j]: the cubes that can stand in cell j, turned somehow
	fits := make([][]int, m)
	for j := range fits {
		var skip int
		for k := 0; k < coords; k++ {
			fmt.Fscan(in, &skip)
		}
		var need [faces]int
		for f := range need {
			fmt.Fscan(in, &need[f])
		}
		for i, cube := range cubes {
			for _, p := range turns {
				ok := true
				for f, c := range need {
					if c != 0 && c != cube[p[f]] {
						ok = false
						break
					}
				}
				if ok {
					fits[j] = append(fits[j], i)
					break
				}
			}
		}
	}
	// Kuhn's augmenting paths from every cell
	owner := make([]int, n)
	for i := range owner {
		owner[i] = -1
	}
	var seen []bool
	var augment func(j int) bool
	augment = func(j int) bool {
		for _, i := range fits[j] {
			if !seen[i] {
				seen[i] = true
				if owner[i] < 0 || augment(owner[i]) {
					owner[i] = j
					return true
				}
			}
		}
		return false
	}
	for j := 0; j < m; j++ {
		seen = make([]bool, n)
		if !augment(j) {
			fmt.Println(0)
			return
		}
	}
	cubeOf := make([]int, m)
	for i, j := range owner {
		if j >= 0 {
			cubeOf[j] = i + 1
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, c := range cubeOf {
		fmt.Fprintln(out, c)
	}
}
