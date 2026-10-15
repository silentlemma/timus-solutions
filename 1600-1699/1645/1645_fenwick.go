package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	place := make([]int, n+1) // place[s]: finishing position of skier s
	for p := 1; p <= n; p++ {
		var s int
		fmt.Fscan(in, &s)
		place[s] = p
	}
	tree := make([]int, n+1) // finishing positions of the skiers who started before
	for skier := 1; skier <= n; skier++ {
		p := place[skier]
		earlier := 0 // started and finished before: undecided
		for i := p - 1; i > 0; i &= i - 1 {
			earlier += tree[i]
		}
		// started later yet finished before: surely faster
		faster := p - 1 - earlier
		// started before yet finished later: surely slower, the rest undecided
		fmt.Fprintln(out, faster+1, (n-skier)+earlier+1)
		for i := p; i <= n; i += i & -i {
			tree[i]++
		}
	}
}
