package main

import "fmt"

func main() {
	var k, p int64
	fmt.Scan(&k, &p)
	// an ent with w words teaches an old ent who ends with w + 1 words and a
	// young one who ends with 2w, so with g(m) ents knowing 2m (or 2m + 1)
	// words: g(1) = 1 and g(m) = g(m - 1) + g(m / 2)
	if k < 2 {
		fmt.Println(0)
		return
	}
	top, half := k/2, k/2/2 // only g up to half is looked up again
	g := make([]int32, half+1)
	cur := 1 % p
	if half >= 1 {
		g[1] = int32(cur)
	}
	for m := int64(2); m <= top; m++ {
		cur = (cur + int64(g[m/2])) % p
		if m <= half {
			g[m] = int32(cur)
		}
	}
	fmt.Println(cur)
}
