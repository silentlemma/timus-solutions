package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type edge struct {
	u, v int
	a    int64
}

type arc struct {
	to int
	a  int64
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscan(in, &n, &m)
	edges := make([]edge, m)
	adj := make([][]arc, n)
	for i := range edges {
		e := &edges[i]
		fmt.Fscan(in, &e.u, &e.v, &e.a)
		e.u--
		e.v--
		adj[e.u] = append(adj[e.u], arc{e.v, e.a})
		adj[e.v] = append(adj[e.v], arc{e.u, e.a})
	}
	// in halves of a rouble, each debt in a component is sign * t + base for
	// the debt t of its first student; an edge closing an odd cycle fixes t
	sign, base, twice := make([]int64, n), make([]int64, n), make([]int64, n)
	for start := 0; start < n; start++ {
		if sign[start] != 0 {
			continue
		}
		sign[start] = 1
		comp := []int{start}
		fixed, t := false, int64(0)
		for head := 0; head < len(comp); head++ {
			v := comp[head]
			for _, e := range adj[v] {
				u := e.to
				if sign[u] == 0 {
					sign[u], base[u] = -sign[v], 2*e.a-base[v]
					comp = append(comp, u)
				} else if sign[u] == sign[v] && !fixed {
					fixed, t = true, (2*e.a-base[u]-base[v])/(2*sign[v])
				}
			}
		}
		if !fixed {
			// no odd cycle: one debt can move freely against its neighbours
			fmt.Fprintln(out, "IMPOSSIBLE")
			return
		}
		for _, v := range comp {
			twice[v] = sign[v]*t + base[v]
		}
	}
	// the claims may also contradict each other
	for _, e := range edges {
		if twice[e.u]+twice[e.v] != 2*e.a {
			fmt.Fprintln(out, "IMPOSSIBLE")
			return
		}
	}
	for _, t := range twice {
		minus, half := "", "00"
		if t < 0 {
			minus, t = "-", -t
		}
		if t%2 != 0 {
			half = "50"
		}
		out.WriteString(minus + strconv.FormatInt(t/2, 10) + "." + half + "\n")
	}
}
