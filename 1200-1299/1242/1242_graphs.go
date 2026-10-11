package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// clear marks everyone reachable from the victims along one kind of link
func clear(start []int, links [][]int, cleared []bool) {
	stack := append([]int(nil), start...)
	seen := make([]bool, len(links))
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, u := range links[v] {
			if !seen[u] {
				seen[u] = true
				cleared[u] = true
				stack = append(stack, u)
			}
		}
	}
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	in.Scan()
	n, _ := strconv.Atoi(in.Text())
	parents, children := make([][]int, n+1), make([][]int, n+1)
	for in.Scan() && in.Text() != "BLOOD" {
		child, _ := strconv.Atoi(in.Text())
		in.Scan()
		parent, _ := strconv.Atoi(in.Text())
		parents[child] = append(parents[child], parent)
		children[parent] = append(children[parent], child)
	}
	cleared := make([]bool, n+1)
	var victims []int
	for in.Scan() {
		v, _ := strconv.Atoi(in.Text())
		victims = append(victims, v)
		cleared[v] = true
	}
	// the werewolf spares its ancestors and descendants, so no ancestor and
	// no descendant of a victim can be the werewolf
	clear(victims, parents, cleared)
	clear(victims, children, cleared)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	found := false
	for v := 1; v <= n; v++ {
		if !cleared[v] {
			if found {
				fmt.Fprint(out, " ")
			}
			fmt.Fprint(out, v)
			found = true
		}
	}
	if !found {
		fmt.Fprint(out, 0)
	}
	fmt.Fprintln(out)
}
