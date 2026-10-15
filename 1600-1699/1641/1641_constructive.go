package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var n, k, m int
	if _, err := fmt.Scan(&n, &k, &m); err != nil {
		return
	}
	// rooms in turn: every room gets someone, and the split is as even as
	// possible, which leaves the most pairs from different rooms
	room := make([]int, n)
	for i := range room {
		room[i] = i % k
	}
	// neighbours in this order always have different rooms
	var days [][2]int
	for i := 0; i+1 < n; i += 2 {
		days = append(days, [2]int{i, i + 1})
	}
	if n%2 == 1 {
		other := 0
		if room[n-1] == room[0] {
			other = 1
		}
		days = append(days, [2]int{other, n - 1})
	}
	used := map[[2]int]bool{}
	for _, d := range days {
		used[d] = true
	}
	for i := 0; i < n && len(days) < m; i++ {
		for j := i + 1; j < n && len(days) < m; j++ {
			if room[i] != room[j] && !used[[2]int{i, j}] {
				days = append(days, [2]int{i, j})
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, r := range room {
		fmt.Fprintln(out, r+1)
	}
	for _, d := range days[:m] {
		fmt.Fprintln(out, d[0]+1, d[1]+1)
	}
}
