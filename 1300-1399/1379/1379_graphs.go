package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const (
	// weights in grams, times in minutes
	truck = 3000000
	cup   = 100
	order = 10000000
	day   = 24 * 60
)

type road struct {
	to, time int
	limit    int64
}

type item struct{ d, v int }
type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].d < q[j].d }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	x := old[len(old)-1]
	*q = old[:len(old)-1]
	return x
}

var n int
var adj [][]road

// inTime: can a truck of this weight reach n within a day?
func inTime(weight int64) bool {
	dist := make([]int, n+1)
	for i := range dist {
		dist[i] = day + 1
	}
	dist[1] = 0
	q := &queue{{0, 1}}
	for q.Len() > 0 {
		it := heap.Pop(q).(item)
		if it.v == n {
			return true
		}
		if it.d > dist[it.v] {
			continue
		}
		for _, r := range adj[it.v] {
			if r.limit >= weight && it.d+r.time < dist[r.to] {
				dist[r.to] = it.d + r.time
				heap.Push(q, item{dist[r.to], r.to})
			}
		}
	}
	return false
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n = next()
	m := next()
	if n == 1 {
		fmt.Println(order) // the cups are already there
		return
	}
	adj = make([][]road, n+1)
	var limits []int64
	for i := 0; i < m; i++ {
		a, b, t, limit := next(), next(), next(), int64(next())
		adj[a] = append(adj[a], road{b, t, limit})
		adj[b] = append(adj[b], road{a, t, limit})
		if limit >= truck {
			limits = append(limits, limit)
		}
	}
	// the heaviest possible truck weighs as much as some road allows, and
	// fewer roads are open to a heavier one, so search the road limits
	sort.Slice(limits, func(i, j int) bool { return limits[i] < limits[j] })
	best := int64(-1)
	lo, hi := 0, len(limits)-1
	for lo <= hi {
		mid := (lo + hi) / 2
		if inTime(limits[mid]) {
			best, lo = limits[mid], mid+1
		} else {
			hi = mid - 1
		}
	}
	if best < 0 {
		fmt.Println(0)
	} else if c := (best - truck) / cup; c < order {
		fmt.Println(c)
	} else {
		fmt.Println(order)
	}
}
