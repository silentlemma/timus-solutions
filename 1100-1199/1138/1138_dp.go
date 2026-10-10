package main

import "fmt"

// percent is the base: a raise must be a whole number of percent of it
const percent = 100

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var n, s int
	fmt.Scan(&n, &s)
	if s > n {
		fmt.Println(0)
		return
	}
	// jobs[a] is the longest run of jobs from salary s ending at salary a; a
	// raise from a is a whole percent exactly when it is a multiple of
	// a / gcd(a, 100)
	jobs := make([]int, n+1)
	jobs[s] = 1
	best := 1
	for a := s; a <= n; a++ {
		if jobs[a] == 0 {
			continue
		}
		if jobs[a] > best {
			best = jobs[a]
		}
		step := a / gcd(a, percent)
		for b := a + step; b <= n; b += step {
			if jobs[b] <= jobs[a] {
				jobs[b] = jobs[a] + 1
			}
		}
	}
	fmt.Println(best)
}
