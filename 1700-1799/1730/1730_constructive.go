package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var name string
	fmt.Fscan(in, &name)
	animals := strings.Split(name, "-")
	num := make([]int, len(animals))
	den := make([]int, len(animals))
	leaves := 1
	for i := range animals {
		var fraction string
		fmt.Fscan(in, &fraction)
		fmt.Sscanf(fraction, "%d/%d", &num[i], &den[i])
		g := gcd(num[i], den[i])
		num[i] /= g
		den[i] /= g
		// a crossing halves every share, so only shares with a power of
		// two below can come out
		if den[i]&(den[i]-1) != 0 {
			fmt.Fprintln(out, "No solution")
			return
		}
		if den[i] > leaves {
			leaves = den[i]
		}
	}
	// give each animal its share of the equal leaves, in order, and cross
	// halves of the leaves; a half that is one animal is just that animal
	var owner []int
	for i := range animals {
		for k := 0; k < num[i]*(leaves/den[i]); k++ {
			owner = append(owner, i)
		}
	}
	var rows []string
	var build func(lo, hi int) int
	build = func(lo, hi int) int {
		if owner[lo] == owner[hi-1] {
			rows = append(rows, animals[owner[lo]])
		} else {
			mid := (lo + hi) / 2
			left := build(lo, mid)
			right := build(mid, hi)
			rows = append(rows, fmt.Sprintf("%d %d", left, right))
		}
		return len(rows)
	}
	build(0, leaves)
	fmt.Fprintln(out, len(rows))
	for _, row := range rows {
		fmt.Fprintln(out, row)
	}
}
