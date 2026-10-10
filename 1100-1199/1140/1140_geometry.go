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
	total := map[string]int{}
	for k := 0; k < n; k++ {
		var d string
		var length int
		fmt.Fscan(in, &d, &length)
		total[d] += length
	}
	// a step along Y is a step along X and one along Z, so the walk ends at
	// a X + b Z; going back with m steps along Y costs |a - m| + |m| + |b - m|,
	// which is smallest at the median of a, 0 and b
	a := total["X"] + total["Y"]
	b := total["Z"] + total["Y"]
	three := []int{a, 0, b}
	sort.Ints(three)
	m := three[1]
	dirs := []string{"X", "Y", "Z"}
	lens := []int{m - a, -m, m - b}
	var lines []string
	for k, d := range dirs {
		if lens[k] != 0 {
			lines = append(lines, fmt.Sprintf("%s %d", d, lens[k]))
		}
	}
	fmt.Println(len(lines))
	for _, line := range lines {
		fmt.Println(line)
	}
}
