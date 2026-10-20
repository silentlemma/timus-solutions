package main

import (
	"bufio"
	"os"
	"strconv"
)

type edge struct {
	to   int
	s, w int64
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	next := func() int {
		scanner.Scan()
		v, _ := strconv.Atoi(scanner.Text())
		return v
	}
	n, m, q := next(), next(), next()
	from := make([]int, m)
	edges := make([]edge, m)
	size := n
	for i := 0; i < m; i++ {
		from[i] = next()
		edges[i] = edge{next(), int64(next()), int64(next())}
		if from[i] > size {
			size = from[i]
		}
		if edges[i].to > size {
			size = edges[i].to
		}
	}
	adj := make([][]edge, size+1)
	indegree := make([]int, size+1)
	for i, e := range edges {
		adj[from[i]] = append(adj[from[i]], e)
		indegree[e.to]++
	}

	// The best route maximizes its smallest ratio s / w, stored as a
	// numerator and denominator; 1 / 0 stands for the empty route at 1.
	num := make([]int64, size+1)
	den := make([]int64, size+1)
	reached := make([]bool, size+1)
	reached[1] = true
	num[1] = 1
	order := make([]int, 0, size)
	for v := 1; v <= size; v++ {
		if indegree[v] == 0 {
			order = append(order, v)
		}
	}
	for head := 0; head < len(order); head++ {
		u := order[head]
		for _, e := range adj[u] {
			indegree[e.to]--
			if indegree[e.to] == 0 {
				order = append(order, e.to)
			}
			if !reached[u] {
				continue
			}
			a, b := num[u], den[u]
			if e.s*b < a*e.w {
				a, b = e.s, e.w
			}
			if !reached[e.to] || num[e.to]*b < a*den[e.to] {
				reached[e.to] = true
				num[e.to], den[e.to] = a, b
			}
		}
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 0; i < q; i++ {
		priceS, priceW := int64(next()), int64(next())
		if reached[n] && priceS*num[n] > priceW*den[n] {
			writer.WriteString("YES\n")
		} else {
			writer.WriteString("NO\n")
		}
	}
}
