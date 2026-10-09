package main

import "fmt"

func digits(v, base int) []int {
	var out []int
	for ; v > 0; v /= base {
		out = append(out, v%base)
	}
	for i, j := 0, len(out)-1; i < j; i, j = i+1, j-1 {
		out[i], out[j] = out[j], out[i]
	}
	return out
}

func fits(x, y, base int) bool {
	dx, dy := digits(x, base), digits(y, base)
	j := 0
	for i := 0; i < len(dx) && j < len(dy); i++ {
		if dx[i] == dy[j] {
			j++
		}
	}
	return j == len(dy)
}

func answer(x, y int) int {
	base := 2
	for ; base*base <= x; base++ {
		if fits(x, y, base) {
			return base
		}
	}
	// from here on x has two digits x / b and x % b, and y must be one of them
	best := 0
	low := x/(y+1) + 1
	if low < base {
		low = base
	}
	if low <= x/y {
		best = low
	}
	// x % b == y means that b divides x - y and is larger than y
	least := base
	if y+1 > least {
		least = y + 1
	}
	n := x - y
	for d := 1; d*d <= n; d++ {
		if n%d == 0 {
			for _, b := range []int{d, n / d} {
				if b >= least && (best == 0 || b < best) {
					best = b
				}
			}
		}
	}
	return best
}

func main() {
	var x, y int
	fmt.Scan(&x, &y)
	if best := answer(x, y); best == 0 {
		fmt.Println("No solution")
	} else {
		fmt.Println(best)
	}
}
