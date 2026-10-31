package main

import "fmt"

var monsters, volleys []int
var memo = map[int]int{0: 0}

// store only reachable masks, with the living sum included in each cost.
func damage(mask int) int {
	if value, ok := memo[mask]; ok {
		return value
	}
	best, sum := -1, 0
	for i, v := range volleys {
		if mask>>uint(i)&1 != 0 {
			sum += monsters[i]
		}
		rest := mask &^ v
		if rest != mask {
			cost := damage(rest)
			if best < 0 || cost < best {
				best = cost
			}
		}
	}
	memo[mask] = best + sum
	return best + sum
}

func main() {
	var n int
	fmt.Scan(&n)
	monsters, volleys = make([]int, n), make([]int, n)
	total := 0
	for i := range monsters {
		fmt.Scan(&monsters[i])
		total += monsters[i]
		volleys[i] = 1<<uint((i+n-1)%n) | 1<<uint(i) | 1<<uint((i+1)%n)
	}
	fmt.Println(damage(1<<uint(n)-1) - total)
}
