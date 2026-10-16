package main

import "fmt"

func main() {
	var n, p int64
	fmt.Scan(&n, &p)
	// the route is the capital, then the other n - 1 = m cities twice each
	// with no city twice in a row, then the capital; such words over m
	// pairs obey a(m) = m (2m - 1) a(m - 1) + m (m - 1) a(m - 2)
	before, current := 1%p, int64(0)
	for m := int64(2); m < n; m++ {
		next := (m*(2*m-1)%p*current + m*(m-1)%p*before) % p
		before, current = current, next
	}
	fmt.Println(current % p)
}
