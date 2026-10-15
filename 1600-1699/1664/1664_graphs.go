package main

import (
	"bufio"
	"container/heap"
	"os"
	"sort"
	"strconv"
)

const (
	far     = int64(1) << 62
	bufSize = 1 << 16
)

type item struct {
	d    int64
	face int
}

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

type link struct {
	to  int
	cap int64
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufSize)
	out := bufio.NewWriterSize(os.Stdout, bufSize)
	defer out.Flush()
	readInt := func() int64 {
		n, c, neg := int64(0), byte(' '), false
		for c == ' ' || c == '\n' || c == '\r' {
			c, _ = in.ReadByte()
		}
		if c == '-' {
			neg = true
			c, _ = in.ReadByte()
		}
		for c >= '0' && c <= '9' {
			n = n*10 + int64(c-'0')
			c, _ = in.ReadByte()
		}
		if neg {
			return -n
		}
		return n
	}
	n := int(readInt())
	xs, ys := make([]int64, n), make([]int64, n)
	for i := 0; i < n; i++ {
		xs[i], ys[i] = readInt(), readInt()
	}
	m := int(readInt())
	// half-edge 2i runs from ends[i] to tips[i], 2i + 1 back; pipe m is an
	// extra edge from the source, leaving to the left, round the outside to
	// the sink, arriving from the right
	ends, tips, caps := make([]int, m+1), make([]int, m+1), make([]int64, m)
	for i := 0; i < m; i++ {
		ends[i], tips[i], caps[i] = int(readInt())-1, int(readInt())-1, readInt()
	}
	ends[m], tips[m] = 0, n-1
	halves := 2*m + 2
	origin := make([]int, halves)
	dx, dy := make([]int64, halves), make([]int64, halves)
	for i := 0; i <= m; i++ {
		a, b := ends[i], tips[i]
		origin[2*i], origin[2*i+1] = a, b
		dx[2*i], dy[2*i] = xs[b]-xs[a], ys[b]-ys[a]
		dx[2*i+1], dy[2*i+1] = -dx[2*i], -dy[2*i]
	}
	dx[2*m], dy[2*m], dx[2*m+1], dy[2*m+1] = -1, 0, 1, 0
	around := make([][]int, n)
	for h := 0; h < halves; h++ {
		around[origin[h]] = append(around[origin[h]], h)
	}
	// counterclockwise from the +x axis, compared exactly
	before := func(g, h int) bool {
		lowG := dy[g] < 0 || (dy[g] == 0 && dx[g] < 0)
		lowH := dy[h] < 0 || (dy[h] == 0 && dx[h] < 0)
		if lowG != lowH {
			return lowH
		}
		return dx[g]*dy[h]-dy[g]*dx[h] > 0
	}
	pos := make([]int, halves)
	for _, list := range around {
		sort.Slice(list, func(i, j int) bool { return before(list[i], list[j]) })
		for k, h := range list {
			pos[h] = k
		}
	}
	// faces: after arriving at a vertex, leave by the next edge clockwise
	face := make([]int, halves)
	for h := range face {
		face[h] = -1
	}
	faces := 0
	for h := 0; h < halves; h++ {
		if face[h] >= 0 {
			continue
		}
		for g := h; face[g] < 0; {
			face[g] = faces
			list := around[origin[g^1]]
			k := pos[g^1] - 1
			if k < 0 {
				k = len(list) - 1
			}
			g = list[k]
		}
		faces++
	}
	// the minimum cut is the shortest path between the two faces next to
	// the extra edge, with pipe capacities as lengths
	links := make([][]link, faces)
	for i := 0; i < m; i++ {
		a, b := face[2*i], face[2*i+1]
		links[a] = append(links[a], link{b, caps[i]})
		links[b] = append(links[b], link{a, caps[i]})
	}
	dist := make([]int64, faces)
	for f := range dist {
		dist[f] = far
	}
	dist[face[2*m]] = 0
	q := &queue{{0, face[2*m]}}
	for q.Len() > 0 {
		top := heap.Pop(q).(item)
		if top.d > dist[top.face] {
			continue
		}
		for _, l := range links[top.face] {
			if d := top.d + l.cap; d < dist[l.to] {
				dist[l.to] = d
				heap.Push(q, item{d, l.to})
			}
		}
	}
	// the flow from ends[i] to tips[i] is the difference of the distances
	// of the faces on its two sides
	flow := make([]int64, m)
	total := int64(0)
	for i := 0; i < m; i++ {
		left, right := dist[face[2*i]], dist[face[2*i+1]]
		if left != far && right != far {
			flow[i] = right - left
		}
		if ends[i] == 0 {
			total += flow[i]
		} else if tips[i] == 0 {
			total -= flow[i]
		}
	}
	sign := int64(1)
	if total < 0 {
		sign = -1
	}
	out.WriteString(strconv.FormatInt(total*sign, 10) + "\n")
	for i := 0; i < m; i++ {
		a, b, f := ends[i], tips[i], flow[i]*sign
		if f < 0 {
			a, b, f = b, a, -f
		}
		out.WriteString(strconv.Itoa(a+1) + " " + strconv.Itoa(b+1) + " ")
		out.WriteString(strconv.FormatInt(f, 10) + "\n")
	}
}
