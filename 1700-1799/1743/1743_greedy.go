package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type piece struct{ low, high int }

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	pieces := make([]piece, n)
	for i := range pieces {
		var a, b int
		fmt.Fscan(in, &a, &b)
		if a > b {
			a, b = b, a
		}
		pieces[i] = piece{a, b}
	}
	// a domino is a range [low, high]; standing upright as (low, high) or
	// flipped as (high, low), two of a kind fit together when nested, and
	// one of each when they overlap; the two kinds are nested chains
	sort.Slice(pieces, func(i, j int) bool {
		if pieces[i].low != pieces[j].low {
			return pieces[i].low < pieces[j].low
		}
		return pieces[i].high > pieces[j].high
	})
	var upright, flipped []piece
	for _, p := range pieces {
		if len(upright) == 0 || p.high <= upright[len(upright)-1].high {
			upright = append(upright, p)
		} else if len(flipped) == 0 || p.high <= flipped[len(flipped)-1].high {
			flipped = append(flipped, p)
		} else {
			fmt.Fprintln(out, "NO")
			return
		}
	}
	// the innermost ranges of the two chains meet in the middle
	if len(upright) > 0 && len(flipped) > 0 {
		a, b := upright[len(upright)-1], flipped[len(flipped)-1]
		if a.high < b.low || b.high < a.low {
			fmt.Fprintln(out, "NO")
			return
		}
	}
	fmt.Fprintln(out, "YES")
	for _, p := range upright {
		fmt.Fprintln(out, p.low, p.high)
	}
	for i := len(flipped) - 1; i >= 0; i-- {
		fmt.Fprintln(out, flipped[i].high, flipped[i].low)
	}
}
