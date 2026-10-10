package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	fresh = iota
	onPath
	good
)

func consistent(names []int) bool {
	zeros := 0
	for _, k := range names {
		if k == 0 {
			zeros++
		}
	}
	if zeros != 1 {
		return false
	}
	state := make([]int, len(names)+1)
	var path []int
	for start := 1; start <= len(names); start++ {
		// follow the accusations until a confessor or a child already known
		// to lead to one; meeting the current path again means a ring
		path = path[:0]
		v := start
		for v != 0 && state[v] == fresh {
			state[v] = onPath
			path = append(path, v)
			v = names[v-1]
		}
		if v != 0 && state[v] == onPath {
			return false
		}
		for _, u := range path {
			state[u] = good
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var n int
		fmt.Fscan(in, &n)
		names := make([]int, n)
		for i := range names {
			fmt.Fscan(in, &names[i])
		}
		if consistent(names) {
			fmt.Fprintln(out, "YES")
		} else {
			fmt.Fprintln(out, "NO")
		}
	}
}
