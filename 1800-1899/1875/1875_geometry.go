package main

import "fmt"

const monkeys = 5

var xs, ys [monkeys]int64

// oneShot: y / x = b - c x along a shot, so the slopes y / x of points on
// one shot lie on a line in x; compared with all fractions cleared
func oneShot(i, j, k int) bool {
	left := (ys[k]*xs[i] - ys[i]*xs[k]) * xs[j] * (xs[j] - xs[i])
	right := (ys[j]*xs[i] - ys[i]*xs[j]) * xs[k] * (xs[k] - xs[i])
	return left == right
}

func main() {
	for i := 0; i < monkeys; i++ {
		fmt.Scan(&xs[i], &ys[i])
	}
	full := 1<<monkeys - 1
	shots := []int{}
	for i := 0; i < monkeys; i++ {
		shots = append(shots, 1<<i)
	}
	for i := 0; i < monkeys; i++ {
		for j := 0; j < monkeys; j++ {
			// gravity bends the path down: the slope y / x must fall as x grows
			if xs[i] < xs[j] && ys[i]*xs[j] > ys[j]*xs[i] {
				mask := 0
				for k := 0; k < monkeys; k++ {
					if oneShot(i, j, k) {
						mask |= 1 << k
					}
				}
				shots = append(shots, mask)
			}
		}
	}
	need := make([]int, full+1)
	for mask := 1; mask <= full; mask++ {
		need[mask] = monkeys
	}
	for mask := 0; mask <= full; mask++ {
		for _, shot := range shots {
			if need[mask]+1 < need[mask|shot] {
				need[mask|shot] = need[mask] + 1
			}
		}
	}
	fmt.Println(need[full])
}
