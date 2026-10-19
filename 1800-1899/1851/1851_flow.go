package main

import (
	"bufio"
	"fmt"
	"os"
)

// network keeps arcs in pairs e, e ^ 1: an undirected edge is two arcs of
// full capacity, each the reverse of the other
type network struct {
	head               [][]int
	target, cap        []int
	level, arc         []int
}

func (g *network) link(a, b, forward, backward int) {
	g.head[a] = append(g.head[a], len(g.target))
	g.target = append(g.target, b)
	g.cap = append(g.cap, forward)
	g.head[b] = append(g.head[b], len(g.target))
	g.target = append(g.target, a)
	g.cap = append(g.cap, backward)
}

func (g *network) levels(source, sink int) bool {
	for i := range g.level {
		g.level[i] = -1
	}
	g.level[source] = 0
	queue := []int{source}
	for i := 0; i < len(queue); i++ {
		v := queue[i]
		for _, e := range g.head[v] {
			if g.cap[e] > 0 && g.level[g.target[e]] < 0 {
				g.level[g.target[e]] = g.level[v] + 1
				queue = append(queue, g.target[e])
			}
		}
	}
	return g.level[sink] >= 0
}

func (g *network) push(v, sink, amount int) int {
	if v == sink {
		return amount
	}
	for ; g.arc[v] < len(g.head[v]); g.arc[v]++ {
		e := g.head[v][g.arc[v]]
		if g.cap[e] > 0 && g.level[g.target[e]] == g.level[v]+1 {
			limit := amount
			if g.cap[e] < limit {
				limit = g.cap[e]
			}
			if got := g.push(g.target[e], sink, limit); got > 0 {
				g.cap[e] -= got
				g.cap[e^1] += got
				return got
			}
		}
	}
	return 0
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var s, p string
	fmt.Fscan(in, &s, &p)
	n, m := len(s), len(p)
	// every erased character is a node; a node on the source side becomes
	// 1, on the sink side 0. Characters s[j] and p[i] meet once in every
	// window where j - i is between 0 and n - m, and differing costs 1.
	nodeS, nodeP := make([]int, n), make([]int, m)
	count := 0
	for j := range nodeS {
		nodeS[j] = -1
		if s[j] == '?' {
			nodeS[j] = count
			count++
		}
	}
	for i := range nodeP {
		nodeP[i] = -1
		if p[i] == '?' {
			nodeP[i] = count
			count++
		}
	}
	source, sink := count, count+1
	// pairs with a fixed 1 cost when the node is 0, and with a fixed 0 when 1
	ones, zeros := make([]int, count), make([]int, count)
	base := 0
	g := &network{head: make([][]int, count+2), level: make([]int, count+2), arc: make([]int, count+2)}
	for i := 0; i < m; i++ {
		for j := i; j <= i+n-m; j++ {
			u, v := nodeP[i], nodeS[j]
			switch {
			case u < 0 && v < 0:
				if p[i] != s[j] {
					base++
				}
			case u < 0:
				if p[i] == '1' {
					ones[v]++
				} else {
					zeros[v]++
				}
			case v < 0:
				if s[j] == '1' {
					ones[u]++
				} else {
					zeros[u]++
				}
			default:
				g.link(u, v, 1, 1)
			}
		}
	}
	for w := 0; w < count; w++ {
		// a node with both kinds of fixed partners pays the smaller anyway
		both := ones[w]
		if zeros[w] < both {
			both = zeros[w]
		}
		base += both
		if ones[w] > both {
			g.link(source, w, ones[w]-both, 0)
		}
		if zeros[w] > both {
			g.link(w, sink, zeros[w]-both, 0)
		}
	}
	flow := 0
	for g.levels(source, sink) {
		for i := range g.arc {
			g.arc[i] = 0
		}
		for got := g.push(source, sink, n*m); got > 0; got = g.push(source, sink, n*m) {
			flow += got
		}
	}
	// the source side of the last search is a minimum cut
	g.levels(source, sink)
	sb, pb := []byte(s), []byte(p)
	for j := range sb {
		if nodeS[j] >= 0 {
			sb[j] = '0'
			if g.level[nodeS[j]] >= 0 {
				sb[j] = '1'
			}
		}
	}
	for i := range pb {
		if nodeP[i] >= 0 {
			pb[i] = '0'
			if g.level[nodeP[i]] >= 0 {
				pb[i] = '1'
			}
		}
	}
	fmt.Printf("%d\n%s\n%s\n", base+flow, sb, pb)
}
