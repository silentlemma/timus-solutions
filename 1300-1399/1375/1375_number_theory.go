package main

import "fmt"

func main() {
	var k, p int64
	fmt.Scan(&k, &p)
	// root[v]: some y with y^2 = v (mod p), or -1 when v is not a square
	root := make([]int64, p)
	for i := range root {
		root[i] = -1
	}
	for y := int64(0); y < p; y++ {
		if v := y * y % p; root[v] < 0 {
			root[v] = y
		}
	}
	// half the values are squares, so some x soon leaves a square k - x^2
	for x := int64(0); x < p; x++ {
		if y := root[((k-x*x)%p+p)%p]; y >= 0 {
			fmt.Println(x, y)
			return
		}
	}
	fmt.Println("NO SOLUTION")
}
