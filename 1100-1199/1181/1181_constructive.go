package main

import (
	"bufio"
	"fmt"
	"os"
)

const triangle = 3

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	var color string
	fmt.Fscan(in, &n, &color)
	poly := make([]int, n)
	for v := range poly {
		poly[v] = v
	}
	var cuts [][2]int
	for len(poly) > triangle {
		m := len(poly)
		counts := map[byte]int{}
		for _, v := range poly {
			counts[color[v]]++
		}
		lonely := -1
		for k := 0; k < m && lonely < 0; k++ {
			if counts[color[poly[k]]] == 1 {
				lonely = k
			}
		}
		if lonely >= 0 {
			// a color met once: every triangle of the fan from that vertex
			// has it plus two neighbouring vertices, which differ
			for j := 2; j < m-1; j++ {
				cuts = append(cuts, [2]int{poly[lonely], poly[(lonely+j)%m]})
			}
			break
		}
		// every color is met twice or more; a vertex whose neighbours differ
		// exists, as otherwise two colors would alternate around the whole
		// polygon, and cutting it off leaves all three colors
		k := 0
		for color[poly[(k+m-1)%m]] == color[poly[(k+1)%m]] {
			k++
		}
		cuts = append(cuts, [2]int{poly[(k+m-1)%m], poly[(k+1)%m]})
		poly = append(poly[:k], poly[k+1:]...)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(cuts))
	for _, c := range cuts {
		fmt.Fprintln(out, c[0]+1, c[1]+1)
	}
}
