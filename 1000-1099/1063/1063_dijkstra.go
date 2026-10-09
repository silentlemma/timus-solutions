package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math/bits"
	"os"
)

const (
	faces = 6
	masks = 1 << faces
)

// state: the faces split into connected groups, the faces that have
// dominoes and the faces of odd degree
type state struct {
	group       [faces]int
	active, odd int
}

// normalize relabels the groups in order of first appearance and packs the state
func normalize(s *state) int {
	var name [faces]int
	for v := range name {
		name[v] = -1
	}
	next, code := 0, 0
	for v := 0; v < faces; v++ {
		if name[s.group[v]] < 0 {
			name[s.group[v]] = next
			next++
		}
		code = code*faces + name[s.group[v]]
	}
	for v := 0; v < faces; v++ {
		s.group[v] = name[s.group[v]]
	}
	return (code*masks+s.active)*masks + s.odd
}

func join(s *state, a, b int) {
	ga, gb := s.group[a], s.group[b]
	for v := range s.group {
		if s.group[v] == gb {
			s.group[v] = ga
		}
	}
	s.active |= 1<<uint(a) | 1<<uint(b)
	s.odd ^= 1<<uint(a) ^ 1<<uint(b)
}

func done(s state) bool {
	group := -1
	for v := 0; v < faces; v++ {
		if s.active>>uint(v)&1 == 1 {
			if group >= 0 && s.group[v] != group {
				return false
			}
			group = s.group[v]
		}
	}
	return bits.OnesCount(uint(s.odd)) <= 2
}

type item struct{ dist, key int }
type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].dist < q[j].dist }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	x := old[len(old)-1]
	*q = old[:len(old)-1]
	return x
}

type link struct{ prev, a, b int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	var start state
	for v := 0; v < faces; v++ {
		start.group[v] = v
	}
	for k := 0; k < n; k++ {
		var a, b int
		fmt.Fscan(in, &a, &b)
		join(&start, a-1, b-1)
	}
	// Dijkstra over the states: adding the domino (a, b) costs a + b, joins
	// the groups of a and b and flips the parity of both faces
	dist := map[int]int{}
	states := map[int]state{}
	parent := map[int]link{}
	key := normalize(&start)
	dist[key] = 0
	states[key] = start
	q := &queue{{0, key}}
	for q.Len() > 0 {
		top := heap.Pop(q).(item)
		if top.dist > dist[top.key] {
			continue
		}
		if done(states[top.key]) {
			key = top.key
			break
		}
		for a := 0; a < faces; a++ {
			for b := a + 1; b < faces; b++ {
				next := states[top.key]
				join(&next, a, b)
				nk := normalize(&next)
				cost := top.dist + (a + 1) + (b + 1)
				if old, seen := dist[nk]; !seen || cost < old {
					dist[nk] = cost
					states[nk] = next
					parent[nk] = link{top.key, a + 1, b + 1}
					heap.Push(q, item{cost, nk})
				}
			}
		}
	}
	var added [][2]int
	for k := key; ; {
		l, ok := parent[k]
		if !ok {
			break
		}
		added = append(added, [2]int{l.a, l.b})
		k = l.prev
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	fmt.Fprintf(w, "%d\n%d\n", dist[key], len(added))
	for _, e := range added {
		fmt.Fprintf(w, "%d %d\n", e[0], e[1])
	}
}
