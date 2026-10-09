package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	children := make([][]int, n+1)
	parents := make([]int, n+1)
	for v := 1; v <= n; v++ {
		for {
			var c int
			fmt.Fscan(in, &c)
			if c == 0 {
				break
			}
			children[v] = append(children[v], c)
			parents[c]++
		}
	}
	// Kahn's algorithm: a member may speak once all its parents have spoken
	var order []int
	for v := 1; v <= n; v++ {
		if parents[v] == 0 {
			order = append(order, v)
		}
	}
	for i := 0; i < len(order); i++ {
		for _, c := range children[order[i]] {
			parents[c]--
			if parents[c] == 0 {
				order = append(order, c)
			}
		}
	}
	words := make([]string, len(order))
	for i, v := range order {
		words[i] = fmt.Sprint(v)
	}
	fmt.Println(strings.Join(words, " "))
}
