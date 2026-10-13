package main

import "fmt"

const faces = 4

func main() {
	var a, b string
	fmt.Scan(&a, &b)
	same := false
	var try func(p []int, used int)
	try = func(p []int, used int) {
		if len(p) == faces {
			inversions := 0
			for i := 0; i < faces; i++ {
				for j := i + 1; j < faces; j++ {
					if p[i] > p[j] {
						inversions++
					}
				}
			}
			// the rotations of a tetrahedron move its faces by exactly the even permutations
			if inversions%2 != 0 {
				return
			}
			for i := 0; i < faces; i++ {
				if b[i] != a[p[i]] {
					return
				}
			}
			same = true
			return
		}
		for k := 0; k < faces; k++ {
			if used>>k&1 == 0 {
				try(append(p, k), used|1<<k)
			}
		}
	}
	try(nil, 0)
	if same {
		fmt.Println("equal")
	} else {
		fmt.Println("different")
	}
}
