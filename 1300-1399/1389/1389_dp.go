package main

import (
	"bufio"
	"os"
	"strconv"
)

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, m := next(), next()
	a, b := make([]int, m), make([]int, m)
	adj := make([][]int, n+1)
	for i := 0; i < m; i++ {
		a[i], b[i] = next(), next()
		adj[a[i]] = append(adj[a[i]], i)
		adj[b[i]] = append(adj[b[i]], i)
	}
	// breadth-first order from city 1 with the road to each parent
	parent, up := make([]int, n+1), make([]int, n+1)
	for i := range up {
		up[i] = -1
	}
	parent[1] = -1
	order := []int{1}
	for k := 0; k < len(order); k++ {
		v := order[k]
		for _, e := range adj[v] {
			u := a[e] + b[e] - v
			if u != parent[v] {
				parent[u], up[u] = v, e
				order = append(order, u)
			}
		}
	}
	// leaves first: close the road to the parent while both ends are free
	used, chosen := make([]bool, n+1), make([]bool, m)
	count := 0
	for k := len(order) - 1; k >= 0; k-- {
		v := order[k]
		if up[v] >= 0 && !used[v] && !used[parent[v]] {
			used[v], used[parent[v]] = true, true
			chosen[up[v]] = true
			count++
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString(strconv.Itoa(count) + "\n")
	for i := 0; i < m; i++ {
		if chosen[i] {
			out.WriteString(strconv.Itoa(a[i]) + " " + strconv.Itoa(b[i]) + "\n")
		}
	}
}
