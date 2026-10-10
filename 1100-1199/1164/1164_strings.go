package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const letters = 26

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, p int
	fmt.Fscan(in, &n, &m, &p)
	// the words take their letters out of the grid one cell each, so what is
	// left does not depend on where they lie
	var left [letters]int
	var s string
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &s)
		for _, c := range s {
			left[c-'A']++
		}
	}
	for i := 0; i < p; i++ {
		fmt.Fscan(in, &s)
		for _, c := range s {
			left[c-'A']--
		}
	}
	var answer strings.Builder
	for c := 0; c < letters; c++ {
		answer.WriteString(strings.Repeat(string(rune('A'+c)), left[c]))
	}
	fmt.Println(answer.String())
}
