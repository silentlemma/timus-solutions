package main

import (
	"bufio"
	"container/heap"
	"io/ioutil"
	"os"
	"strconv"
)

const (
	inf = int64(1) << 62
)

type item struct {
	dist int64
	v    int
}

type minHeap []item

func (h minHeap) Len() int            { return len(h) }
func (h minHeap) Less(i, j int) bool  { return h[i].dist < h[j].dist }
func (h minHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap) Push(x interface{}) { *h = append(*h, x.(item)) }
func (h *minHeap) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func isDigit(c byte) bool { return c >= '0' && c <= '9' }

func main() {
	data, _ := ioutil.ReadAll(bufio.NewReader(os.Stdin))
	pos := 0
	number := func() int64 {
		for !isDigit(data[pos]) {
			pos++
		}
		v := int64(0)
		for pos < len(data) && isDigit(data[pos]) {
			v = v*10 + int64(data[pos]-'0')
			pos++
		}
		return v
	}
	n := int(number())
	var origin, target []int
	var capacity, flow, cost []int64
	out := make([][]int, n+1)
	into := make([][]int, n+1)
	balance := make([]int64, n+1) // outflow minus inflow
	// each pipe ends with a comma or a dot, each station with a dot
	for i := 1; i <= n; {
		c := data[pos]
		if isDigit(c) {
			e, a := len(target), int(number())
			b, f, d := number(), number(), number()
			out[i] = append(out[i], e)
			into[a] = append(into[a], e)
			origin = append(origin, i)
			target = append(target, a)
			capacity = append(capacity, b)
			flow = append(flow, f)
			cost = append(cost, d)
			balance[i] += f
			balance[a] -= f
			continue
		}
		if c == '.' {
			i++
		}
		pos++
	}

	// one more unit from any station with a well to station n through the
	// residual network: a pipe with spare room is free, a full one costs d,
	// and pushing back existing flow is free
	dist := make([]int64, n+1)
	cameBy := make([]int, n+1)
	step := make([]int64, n+1)
	h := &minHeap{}
	for i := 1; i <= n; i++ {
		dist[i], cameBy[i] = inf, -1
		if i < n && balance[i] > 0 {
			dist[i] = 0
			heap.Push(h, item{0, i})
		}
	}
	for h.Len() > 0 {
		cur := heap.Pop(h).(item)
		du, u := cur.dist, cur.v
		if du > dist[u] {
			continue
		}
		for _, e := range out[u] {
			nd := du
			if flow[e] == capacity[e] {
				nd += cost[e]
			}
			if v := target[e]; nd < dist[v] {
				dist[v], cameBy[v], step[v] = nd, e, 1
				heap.Push(h, item{nd, v})
			}
		}
		for _, e := range into[u] {
			if v := origin[e]; flow[e] > 0 && du < dist[v] {
				dist[v], cameBy[v], step[v] = du, e, -1
				heap.Push(h, item{du, v})
			}
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	if dist[n] == inf {
		w.WriteString("Impossible\n")
		return
	}
	for v := n; cameBy[v] >= 0; {
		e := cameBy[v]
		flow[e] += step[v]
		if step[v] == 1 {
			v = origin[e]
		} else {
			v = target[e]
		}
	}
	w.WriteString(strconv.FormatInt(dist[n], 10) + "\n")
	for i := 1; i <= n; i++ {
		for k, e := range out[i] {
			if k > 0 {
				w.WriteString(", ")
			}
			w.WriteString(strconv.Itoa(target[e]) + " " + strconv.FormatInt(flow[e], 10))
		}
		w.WriteString(".\n")
	}
}
