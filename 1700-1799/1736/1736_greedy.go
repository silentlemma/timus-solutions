package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const win = 3

var signs = []string{"<", "<=", ">=", ">"}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	left := make([]int, n)
	for i := range left {
		fmt.Fscan(in, &left[i])
	}
	got := make([][]int, n)
	active := make([]int, n)
	for i := range got {
		got[i] = make([]int, n)
		active[i] = i
	}
	ok := true
	// the weakest team plays all its games now: it keeps its own points
	// and hands the rest out, three a game, to the strongest teams first
	for ok && len(active) > 1 {
		sort.Slice(active, func(a, b int) bool {
			x, y := active[a], active[b]
			if left[x] != left[y] {
				return left[x] < left[y]
			}
			return x < y
		})
		weak := active[0]
		give := win*(len(active)-1) - left[weak]
		if give < 0 {
			break
		}
		for k := len(active) - 1; k >= 1; k-- {
			t := active[k]
			share := give
			if share > win {
				share = win
			}
			give -= share
			left[t] -= share
			got[t][weak], got[weak][t] = share, win-share
			if left[t] < 0 {
				ok = false
			}
		}
		left[weak] = 0
		if give != 0 {
			ok = false
		}
		active = active[1:]
	}
	for _, x := range left {
		if x != 0 {
			ok = false
		}
	}
	if !ok {
		fmt.Fprintln(out, "INCORRECT")
		return
	}
	fmt.Fprintln(out, "CORRECT")
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			fmt.Fprintf(out, "%d %s %d\n", i+1, signs[got[i][j]], j+1)
		}
	}
}
