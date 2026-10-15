package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	dim      = 3
	vertices = 4
	opposite = 3
)

// each face and the vertex opposite it
var faces = [vertices][vertices]int{{0, 1, 2, 3}, {0, 1, 3, 2}, {0, 2, 3, 1}, {1, 2, 3, 0}}

func main() {
	in := bufio.NewReader(os.Stdin)
	var v [vertices][dim]int64
	for i := range v {
		fmt.Fscan(in, &v[i][0], &v[i][1], &v[i][2])
	}
	var n int
	fmt.Fscan(in, &n)
	var normals [vertices][dim]int64
	for f, face := range faces {
		var u, w, d [dim]int64
		for t := 0; t < dim; t++ {
			u[t] = v[face[1]][t] - v[face[0]][t]
			w[t] = v[face[2]][t] - v[face[0]][t]
			d[t] = v[face[opposite]][t] - v[face[0]][t]
		}
		c := [dim]int64{u[1]*w[2] - u[2]*w[1], u[2]*w[0] - u[0]*w[2], u[0]*w[1] - u[1]*w[0]}
		// point the cross product, twice the face area long, away from the body
		if c[0]*d[0]+c[1]*d[1]+c[2]*d[2] > 0 {
			c = [dim]int64{-c[0], -c[1], -c[2]}
		}
		normals[f] = c
	}
	// a lit face gives area * intensity * cosine = (cross . star) / 2, and the
	// doubled total is a plain integer sum; the body is convex, so no shadows
	total := int64(0)
	for i := 0; i < n; i++ {
		var s [dim]int64
		fmt.Fscan(in, &s[0], &s[1], &s[2])
		for _, c := range normals {
			if dot := c[0]*s[0] + c[1]*s[1] + c[2]*s[2]; dot > 0 {
				total += dot
			}
		}
	}
	fmt.Printf("%d.00000\n", total)
}
