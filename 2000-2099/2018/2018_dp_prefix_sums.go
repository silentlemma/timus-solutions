package main

import "fmt"

const mod = 1000000007

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	// one[i], two[i]: sequences of length i that end with a run of ones or twos,
	// the empty sequence counts once on both sides, so one[0] = two[0] = 1
	one := make([]int, n+1)
	two := make([]int, n+1)
	sumOne := make([]int, n+1)
	sumTwo := make([]int, n+1)
	one[0], two[0], sumOne[0], sumTwo[0] = 1, 1, 1, 1
	for i := 1; i <= n; i++ {
		// the last run of ones has length 1..a and follows a sequence ending in twos
		one[i] = sumTwo[i-1]
		if i-a-1 >= 0 {
			one[i] -= sumTwo[i-a-1]
		}
		two[i] = sumOne[i-1]
		if i-b-1 >= 0 {
			two[i] -= sumOne[i-b-1]
		}
		one[i] = (one[i]%mod + mod) % mod
		two[i] = (two[i]%mod + mod) % mod
		sumOne[i] = (sumOne[i-1] + one[i]) % mod
		sumTwo[i] = (sumTwo[i-1] + two[i]) % mod
	}
	fmt.Println((one[n] + two[n]) % mod)
}
