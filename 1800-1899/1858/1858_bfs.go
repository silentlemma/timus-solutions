package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const faces = 6

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	side, n := next(), next()
	count := n * n * n
	// crystals with the same rune touch: the crystals and their contacts
	// form the n x n x n grid, whatever the turns of the crystals
	near := make([][]int, count)
	first := make(map[int]int, faces*count)
	for c := 0; c < count; c++ {
		for f := 0; f < faces; f++ {
			mark := next()
			if mark == 0 {
				continue
			}
			if other, ok := first[mark]; ok {
				near[c] = append(near[c], other)
				near[other] = append(near[other], c)
			} else {
				first[mark] = c
			}
		}
	}
	// spread gives the grid steps from start to every crystal
	spread := func(start int) []int {
		steps := make([]int, count)
		for i := range steps {
			steps[i] = -1
		}
		steps[start] = 0
		queue := []int{start}
		for i := 0; i < len(queue); i++ {
			for _, w := range near[queue[i]] {
				if steps[w] < 0 {
					steps[w] = steps[queue[i]] + 1
					queue = append(queue, w)
				}
			}
		}
		return steps
	}
	// a corner touches the fewest crystals; the three corners n - 1 steps
	// away lie along the edges from it, and the steps to a corner and to
	// one of them give the coordinate along that edge
	corner := 0
	for c := 1; c < count; c++ {
		if len(near[c]) < len(near[corner]) {
			corner = c
		}
	}
	origin := spread(corner)
	var axes [][]int
	for c := 0; c < count; c++ {
		if origin[c] == n-1 && len(near[c]) == len(near[corner]) {
			axes = append(axes, spread(c))
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	m := next()
	for k := 0; k < m; k++ {
		a, b := next()-1, next()-1
		square := 0.0
		for _, far := range axes {
			x, y := (origin[a]-far[a]+n-1)/2, (origin[b]-far[b]+n-1)/2
			square += float64((x - y) * (x - y))
		}
		fmt.Fprintf(out, "%.7f\n", float64(side)*math.Sqrt(square))
	}
}
