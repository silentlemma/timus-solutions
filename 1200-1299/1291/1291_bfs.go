package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		x, _ := strconv.Atoi(in.Text())
		return x
	}
	n := next()
	teeth := make([]int, n+1)
	adj := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		teeth[i] = next()
		for j := next(); j != 0; j = next() {
			// a link may be listed at one end only, so store it both ways
			adj[i] = append(adj[i], j)
			adj[j] = append(adj[j], i)
		}
	}
	root, speed := next(), next()
	// meshed gears share the speed of their rims, speed * teeth, and turn
	// opposite ways; so gear j turns at +-speed * teeth[root] / teeth[j]
	rim := speed * teeth[root]
	sign := make([]int, n+1)
	sign[root] = 1
	queue := []int{root}
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		for _, v := range adj[u] {
			if sign[v] == 0 {
				sign[v] = -sign[u]
				queue = append(queue, v)
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 1; i <= n; i++ {
		if sign[i] == 0 {
			fmt.Fprintln(out, "0/1")
		} else {
			g := gcd(rim, teeth[i])
			fmt.Fprintf(out, "%d/%d\n", sign[i]*rim/g, teeth[i]/g)
		}
	}
}
