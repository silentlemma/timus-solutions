package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strings"
)

type item struct {
	cost int
	tail string
}

type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].cost < q[j].cost }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	x := old[len(old)-1]
	*q = old[:len(old)-1]
	return x
}

// the previous tail, the new piece of text, and whether the tail starts a search
type link struct {
	from, piece string
	first       bool
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(reader, &n)
	words := make([]string, n)
	for i := range words {
		fmt.Fscan(reader, &words[i])
	}
	// a state is the tail by which one parse runs ahead of the other; the
	// cost is the length of the text so far, and Dijkstra finds the shortest text
	dist := map[string]int{}
	back := map[string]link{}
	q := &queue{}
	relax := func(tail string, cost int, l link) {
		if d, ok := dist[tail]; ok && d <= cost {
			return
		}
		dist[tail], back[tail] = cost, l
		heap.Push(q, item{cost, tail})
	}
	for _, u := range words {
		for _, v := range words {
			if u != v && strings.HasPrefix(v, u) {
				relax(v[len(u):], len(v), link{"", v, true})
			}
		}
	}
	for q.Len() > 0 {
		top := heap.Pop(q).(item)
		if top.cost > dist[top.tail] {
			continue
		}
		tail := top.tail
		for _, w := range words {
			if w == tail { // both parses end together: rebuild the text from its pieces
				var pieces []string
				for t := tail; ; t = back[t].from {
					pieces = append(pieces, back[t].piece)
					if back[t].first {
						break
					}
				}
				var sb strings.Builder
				for i := len(pieces) - 1; i >= 0; i-- {
					sb.WriteString(pieces[i])
				}
				fmt.Println("YES")
				fmt.Println(sb.String())
				return
			}
			if strings.HasPrefix(w, tail) {
				rest := w[len(tail):]
				relax(rest, top.cost+len(rest), link{tail, rest, false})
			} else if strings.HasPrefix(tail, w) {
				relax(tail[len(w):], top.cost, link{tail, "", false})
			}
		}
	}
	fmt.Println("NO")
}
