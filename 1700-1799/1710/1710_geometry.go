package main

import "fmt"

func main() {
	var ax, ay, bx, by, cx, cy int64
	fmt.Scan(&ax, &ay, &bx, &by, &cx, &cy)
	// C' on the ray AC with |BC'| = |BC| is the other root t of
	// t^2 - 2 t (AB . u) + |AB|^2 - |BC|^2 = 0, u the unit vector along AC:
	// t' = 2 (AB . AC) / |AC| - |AC|, so C' = A + (C - A) (2 dot - |AC|^2) / |AC|^2
	dot := (bx-ax)*(cx-ax) + (by-ay)*(cy-ay)
	side := (cx-ax)*(cx-ax) + (cy-ay)*(cy-ay)
	if 2*dot <= side || dot == side {
		fmt.Println("YES")
		return
	}
	k := float64(2*dot-side) / float64(side)
	fmt.Println("NO")
	fmt.Printf("%.10f %.10f\n", float64(ax), float64(ay))
	fmt.Printf("%.10f %.10f\n", float64(bx), float64(by))
	fmt.Printf("%.10f %.10f\n", float64(ax)+float64(cx-ax)*k, float64(ay)+float64(cy-ay)*k)
}
