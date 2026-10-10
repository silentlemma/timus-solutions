package main

import "fmt"

var n int
var monsters, volleys, memo []int

func alive(mask int) int {
	sum := 0
	for i := 0; i < n; i++ {
		if mask>>i&1 == 1 {
			sum += monsters[i]
		}
	}
	return sum
}

// damage is the least damage still to come with these balconies occupied,
// where the monsters left after each volley fire once
func damage(mask int) int {
	if mask == 0 {
		return 0
	}
	if memo[mask] >= 0 {
		return memo[mask]
	}
	best := -1
	for _, v := range volleys {
		if mask&v != 0 {
			rest := mask &^ v
			if cost := alive(rest) + damage(rest); best < 0 || cost < best {
				best = cost
			}
		}
	}
	memo[mask] = best
	return best
}

func main() {
	fmt.Scan(&n)
	monsters = make([]int, n)
	for i := range monsters {
		fmt.Scan(&monsters[i])
	}
	// a volley at i clears balconies i - 1, i and i + 1 around the circle
	for i := 0; i < n; i++ {
		volleys = append(volleys, 1<<((i+n-1)%n)|1<<i|1<<((i+1)%n))
	}
	memo = make([]int, 1<<n)
	for k := range memo {
		memo[k] = -1
	}
	fmt.Println(damage(1<<n - 1))
}
