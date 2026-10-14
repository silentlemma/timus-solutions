package main

import "fmt"

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}

func max(a, b int64) int64 {
	if a > b {
		return a
	}
	return b
}

func main() {
	var k, l, n int64
	fmt.Scan(&k, &l, &n)
	d := k - l
	// with W wins and R losses the team has n + 2W - R points; the goals
	// split into a common part, scored and conceded alike, plus at least
	// one goal of margin per win and per loss
	var best, worst int64
	if d >= 0 {
		// no losses: the margin d covers up to d wins, the rest are draws
		best, worst = n+2*min(d, n), n+2
		if d == 0 {
			worst = n
		}
	} else {
		// no wins: up to -d losses, at least one
		best, worst = n-1, n-min(-d, n)
	}
	if k >= 1 && l >= 1 && n >= 2 {
		// wins and losses together: one goal each is enough, so one loss
		// and up to k wins, or one win and up to l losses
		best = max(best, n-1+2*min(k, n-1))
		worst = min(worst, n+2-min(l, n-1))
	}
	fmt.Println(best, worst)
}
