package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

type doll struct{ inner, outer, id int }
type predecessor struct {
	parent, best []int
	rank         []byte
}

func newPredecessor(n int) predecessor {
	d := predecessor{make([]int, n+1), make([]int, n+1), make([]byte, n+1)}
	for i := range d.parent {
		d.parent[i] = i
		d.best[i] = i
	}
	return d
}
func (d *predecessor) find(x int) int {
	for d.parent[x] != x {
		d.parent[x] = d.parent[d.parent[x]]
		x = d.parent[x]
	}
	return x
}
func (d *predecessor) erase(x int) {
	a, b := d.find(x), d.find(x-1)
	if d.rank[a] < d.rank[b] {
		a, b = b, a
	}
	d.parent[b] = a
	if d.best[b] < d.best[a] {
		d.best[a] = d.best[b]
	}
	if d.rank[a] == d.rank[b] {
		d.rank[a]++
	}
}
func solve(items []doll) []int {
	limit := 0
	for _, item := range items {
		if item.outer > limit {
			limit = item.outer
		}
	}
	limit++
	sort.Slice(items, func(i, j int) bool {
		if items[i].inner != items[j].inner {
			return items[i].inner < items[j].inner
		}
		if items[i].outer != items[j].outer {
			return items[i].outer < items[j].outer
		}
		return items[i].id < items[j].id
	})
	available := newPredecessor(len(items))
	answer := make([]int, 0, len(items))
	for range items {
		cut := sort.Search(len(items), func(i int) bool { return items[i].inner >= limit })
		position := available.best[available.find(cut)]
		if position == 0 {
			return nil
		}
		item := items[position-1]
		answer = append(answer, item.id)
		limit = item.outer
		available.erase(position)
	}
	return answer
}
func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	items := make([]doll, n)
	for i := range items {
		fmt.Fscan(in, &items[i].inner, &items[i].outer)
		items[i].id = i + 1
	}
	answer := solve(items)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if answer == nil {
		fmt.Fprintln(out, "No")
		return
	}
	fmt.Fprintln(out, "Yes")
	for i, v := range answer {
		if i > 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, v)
	}
	fmt.Fprintln(out)
}
