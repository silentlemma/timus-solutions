package main

import "fmt"

const (
	mod    = 1000000009
	low    = 100
	high   = 1000
	pairs  = 100
	window = 3
)

func main() {
	var n int
	fmt.Scan(&n)
	var source, target [high - low]int
	// ways[t]: numbers of the length so far that end in the two digits t and
	// whose every three neighbouring digits form a three-digit prime
	var ways, nextWays [pairs]int
	count := 0
	for p := low; p < high; p++ {
		prime := true
		for d := 2; d*d <= p; d++ {
			if p%d == 0 {
				prime = false
				break
			}
		}
		if prime {
			source[count], target[count] = p/10, p%pairs
			count++
			ways[p%pairs]++
		}
	}
	// reuse both arrays; the sum of two residues fits even a signed 32-bit int.
	for step := window; step < n; step++ {
		for i := range nextWays {
			nextWays[i] = 0
		}
		// a prime abc extends a number ending in ab (source) to one ending in bc (target)
		for i := 0; i < count; i++ {
			value := nextWays[target[i]] + ways[source[i]]
			if value >= mod {
				value -= mod
			}
			nextWays[target[i]] = value
		}
		ways = nextWays
	}
	total := 0
	for _, value := range ways {
		total += value
		if total >= mod {
			total -= mod
		}
	}
	fmt.Println(total)
}
