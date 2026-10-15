package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func zFunction(s string) []int {
	n := len(s)
	z := make([]int, n)
	left, right := 0, 0
	for i := 1; i < n; i++ {
		k := 0
		if i < right {
			k = z[i-left]
			if right-i < k {
				k = right - i
			}
		}
		for i+k < n && s[k] == s[i+k] {
			k++
		}
		z[i] = k
		if i+k > right {
			left, right = i, i+k
		}
	}
	return z
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var word, last string
	fmt.Fscan(in, &word, &last)
	m, n := len(word), len(last)
	z := zFunction(word + "#" + last)
	// from a cut at position p the next piece can end anywhere in
	// p + 1 .. p + z[p]; so the reachable cuts are always 0 .. reach
	parent := make([]int, n+1)
	reach := 0
	for p := 0; p <= reach && p < n; p++ {
		far := p + z[m+1+p]
		for q := reach + 1; q <= far; q++ {
			parent[q] = p
		}
		if far > reach {
			reach = far
		}
	}
	if reach < n {
		fmt.Println("Yes")
		return
	}
	var pieces []string
	for q := n; q > 0; q = parent[q] {
		pieces = append(pieces, last[parent[q]:q])
	}
	for i, j := 0, len(pieces)-1; i < j; i, j = i+1, j-1 {
		pieces[i], pieces[j] = pieces[j], pieces[i]
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, "No")
	fmt.Fprintln(out, strings.Join(pieces, " "))
}
