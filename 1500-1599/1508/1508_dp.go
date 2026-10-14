package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(in, &n, &k)
	groups := make([]int, k)
	for j := range groups {
		fmt.Fscan(in, &groups[j])
	}
	var line string
	fmt.Fscan(in, &line)
	dots := make([]int, n+1) // dots[i]: known empty cells among the first i
	for i := 0; i < n; i++ {
		dots[i+1] = dots[i]
		if line[i] == '.' {
			dots[i+1]++
		}
	}
	// fits tells whether a group can cover the cells s ... s + length - 1
	fits := func(s, length int) bool {
		return s >= 0 && s+length <= n && dots[s+length] == dots[s]
	}
	grid := func(rows int) [][]bool {
		g := make([][]bool, rows)
		for i := range g {
			g[i] = make([]bool, k+1)
		}
		return g
	}
	// pre[i][j]: the first i cells can hold the first j groups
	pre := grid(n + 1)
	pre[0][0] = true
	for i := 1; i <= n; i++ {
		for j := 0; j <= k; j++ {
			ok := line[i-1] != 'X' && pre[i-1][j]
			if !ok && j > 0 && fits(i-groups[j-1], groups[j-1]) {
				s := i - groups[j-1]
				if s == 0 {
					ok = j == 1
				} else {
					ok = line[s-1] != 'X' && pre[s-1][j-1]
				}
			}
			pre[i][j] = ok
		}
	}
	if !pre[n][k] {
		fmt.Println("Impossible")
		return
	}
	// suf[i][j]: the cells from i on can hold the groups from j on
	suf := grid(n + 2)
	suf[n][k] = true
	for i := n - 1; i >= 0; i-- {
		for j := k; j >= 0; j-- {
			ok := line[i] != 'X' && suf[i+1][j]
			if !ok && j < k && fits(i, groups[j]) {
				end := i + groups[j]
				if end == n {
					ok = j+1 == k
				} else {
					ok = line[end] != 'X' && suf[end+1][j+1]
				}
			}
			suf[i][j] = ok
		}
	}
	cover := make([]int, n+1) // difference array of the cells some group can cover
	for j, length := range groups {
		for s := 0; s+length <= n; s++ {
			if !fits(s, length) {
				continue
			}
			end := s + length
			left := s == 0 && j == 0 || s > 0 && line[s-1] != 'X' && pre[s-1][j]
			right := end == n && j+1 == k || end < n && line[end] != 'X' && suf[end+1][j+1]
			if left && right {
				cover[s]++
				cover[end]--
			}
		}
	}
	out := make([]byte, n)
	run := 0
	for c := 0; c < n; c++ {
		run += cover[c]
		white := false
		for j := 0; j <= k && line[c] != 'X'; j++ {
			white = white || pre[c][j] && suf[c+1][j]
		}
		switch {
		case white && run > 0:
			out[c] = '?'
		case white:
			out[c] = '.'
		default:
			out[c] = 'X'
		}
	}
	fmt.Println(string(out))
}
