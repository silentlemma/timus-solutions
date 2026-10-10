package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	segs := make([][2]int, n)
	for i := range segs {
		fmt.Fscan(in, &segs[i][0], &segs[i][1])
	}
	// the segment that ends first leaves the most room for the rest; touching
	// ends share no inner point
	sort.Slice(segs, func(i, j int) bool { return segs[i][1] < segs[j][1] })
	var chosen [][2]int
	for _, s := range segs {
		if len(chosen) == 0 || s[0] >= chosen[len(chosen)-1][1] {
			chosen = append(chosen, s)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(chosen))
	for _, s := range chosen {
		fmt.Fprintln(out, s[0], s[1])
	}
}
