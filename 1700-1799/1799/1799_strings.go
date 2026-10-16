package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	alphabet = 26
	maxWord  = 1 << 20
)

// automaton is a suffix automaton; first[v] is the end of the first
// occurrence of v, and prefix[i] the state of the prefix ending at i
type automaton struct {
	next              [][alphabet]int32
	link, size, first []int
	prefix            []int
	last              int
}

func (a *automaton) add(parent, length, end int) int {
	var none [alphabet]int32
	for c := range none {
		none[c] = -1
	}
	a.next = append(a.next, none)
	a.link = append(a.link, parent)
	a.size = append(a.size, length)
	a.first = append(a.first, end)
	return len(a.size) - 1
}

func (a *automaton) extend(c, end int) {
	cur := a.add(0, a.size[a.last]+1, end)
	p := a.last
	for p != -1 && a.next[p][c] == -1 {
		a.next[p][c] = int32(cur)
		p = a.link[p]
	}
	if p != -1 {
		q := int(a.next[p][c])
		if a.size[p]+1 == a.size[q] {
			a.link[cur] = q
		} else {
			clone := a.add(a.link[q], a.size[p]+1, a.first[q])
			a.next[clone] = a.next[q]
			for p != -1 && int(a.next[p][c]) == q {
				a.next[p][c] = int32(clone)
				p = a.link[p]
			}
			a.link[q] = clone
			a.link[cur] = clone
		}
	}
	a.last = cur
}

func build(s string) *automaton {
	a := &automaton{}
	a.add(-1, 0, 0)
	for i := 0; i < len(s); i++ {
		a.extend(int(s[i]-'a'), i)
		a.prefix = append(a.prefix, a.last)
	}
	return a
}

// fenwick supports adding to a range of positions and summing a prefix
type fenwick struct{ plain, scaled []int64 }

func (f *fenwick) point(tree []int64, at int, value int64) {
	for at++; at < len(tree); at += at & -at {
		tree[at] += value
	}
}

func (f *fenwick) sum(count int) int64 {
	var a, b int64
	for at := count; at > 0; at -= at & -at {
		a += f.plain[at]
		b += f.scaled[at]
	}
	return a*int64(count) - b
}

func (f *fenwick) add(from, to int, value int64) {
	if from >= to {
		return
	}
	f.point(f.plain, from, value)
	f.point(f.plain, to, -value)
	f.point(f.scaled, from, value*int64(from))
	f.point(f.scaled, to, -value*int64(to))
}

type edge struct {
	source, dest, from, to int
	distinct               int64
}

func swagness(s string) int64 {
	n := len(s)
	sam := build(s)
	states := len(sam.size)
	order := make([]int, states)
	for v := range order {
		order[v] = v
	}
	sort.Slice(order, func(i, j int) bool { return sam.size[order[i]] < sam.size[order[j]] })

	// a state with exactly one way out is squeezed into the edge through it
	only := make([]int, states)
	target := make([]int, states)
	extra := make([]int, states)
	keep := make([]bool, states)
	for v := 0; v < states; v++ {
		ways := 0
		for c := 0; c < alphabet; c++ {
			if sam.next[v][c] != -1 {
				ways++
				only[v] = int(sam.next[v][c])
			}
		}
		keep[v] = v == 0 || ways != 1
	}
	for k := states - 1; k >= 0; k-- {
		v := order[k]
		if keep[v] {
			target[v] = v
		} else {
			target[v] = target[only[v]]
			extra[v] = 1 + extra[only[v]]
		}
	}
	// the compressed edges and, for each, its label s[from .. to]
	var edges []edge
	for u := 0; u < states; u++ {
		if !keep[u] {
			continue
		}
		for c := 0; c < alphabet; c++ {
			t := int(sam.next[u][c])
			if t == -1 {
				continue
			}
			dest := target[t]
			to := sam.first[dest]
			edges = append(edges, edge{u, dest, to - extra[t], to, 0})
		}
	}

	// the suffix link tree in Euler order
	children := make([][]int, states)
	for v := 1; v < states; v++ {
		children[sam.link[v]] = append(children[sam.link[v]], v)
	}
	tin := make([]int, states)
	tout := make([]int, states)
	timer := 1
	stackV, stackAt := []int{0}, []int{0}
	for len(stackV) > 0 {
		top := len(stackV) - 1
		v := stackV[top]
		if stackAt[top] == len(children[v]) {
			tout[v] = timer
			stackV, stackAt = stackV[:top], stackAt[:top]
			continue
		}
		child := children[v][stackAt[top]]
		stackAt[top]++
		tin[child] = timer
		timer++
		stackV, stackAt = append(stackV, child), append(stackAt, 0)
	}
	// the latest end seen in a subtree, as a segment tree of maxima
	size := 1
	for size < states {
		size *= 2
	}
	latest := make([]int, 2*size)
	query := func(lo, hi int) int {
		best := 0
		for lo, hi = lo+size, hi+size; lo < hi; lo, hi = lo/2, hi/2 {
			if lo&1 == 1 {
				if latest[lo] > best {
					best = latest[lo]
				}
				lo++
			}
			if hi&1 == 1 {
				hi--
				if latest[hi] > best {
					best = latest[hi]
				}
			}
		}
		return best
	}
	update := func(at, value int) {
		at += size
		latest[at] = value
		for ; at > 1; at /= 2 {
			m := latest[at]
			if latest[at^1] > m {
				m = latest[at^1]
			}
			latest[at/2] = m
		}
	}

	byEnd := make([][]int, n+1)
	for e := range edges {
		byEnd[edges[e].to+1] = append(byEnd[edges[e].to+1], e)
	}
	// count[p]: distinct substrings of s[0 .. end) whose last occurrence
	// starts at p; the states on one suffix link path that share their
	// last end form chains, and top[end] is the state just above a chain
	count := &fenwick{make([]int64, n+1), make([]int64, n+1)}
	seen := make([]bool, states)
	seen[0] = true
	top := make([]int, n+1)
	for end := 1; end <= n; end++ {
		v := sam.prefix[end-1]
		count.add(end-sam.size[v], end, 1)
		u := v
		for !seen[u] {
			seen[u] = true
			u = sam.link[u]
		}
		for u != 0 {
			was := query(tin[u], tout[u])
			above := top[was]
			count.add(was-sam.size[u], was-sam.size[above], -1)
			top[was] = u
			u = above
		}
		update(tin[v], end)
		top[end] = 0
		for _, e := range byEnd[end] {
			edges[e].distinct = count.sum(end) - count.sum(edges[e].from)
		}
	}

	// each compressed edge stands for as many tree edges as there are
	// paths from the root to its source
	paths := make([]int64, states)
	paths[0] = 1
	out := make([][]int, states)
	for e := range edges {
		out[edges[e].source] = append(out[edges[e].source], e)
	}
	var total int64
	for _, v := range order {
		if !keep[v] || paths[v] == 0 {
			continue
		}
		for _, e := range out[v] {
			total += paths[v] * edges[e].distinct
			paths[edges[e].dest] += paths[v]
		}
	}
	return total
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, maxWord), maxWord)
	scanner.Split(bufio.ScanWords)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if !scanner.Scan() {
		return
	}
	n, _ := strconv.Atoi(scanner.Text())
	for i := 0; i < n; i++ {
		scanner.Scan()
		fmt.Fprintln(writer, swagness(scanner.Text()))
	}
}
