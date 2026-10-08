package main

import (
	"container/heap"
	"fmt"
	"strings"
)

const (
	size       = 8
	faces      = 6
	directions = 4
	bottom     = 4
	inf        = int64(1) << 60
)

// faces in the input order near, far, top, right, bottom, left; a roll in
// direction d puts the face from position source[d][i] to position i
var (
	dx     = [directions]int{0, 0, 1, -1}
	dy     = [directions]int{1, -1, 0, 0}
	source = [directions][faces]int{
		{4, 2, 0, 3, 1, 5}, {2, 4, 1, 3, 0, 5}, {0, 1, 5, 2, 3, 4}, {0, 1, 3, 4, 5, 2}}
)

type item struct {
	dist  int64
	state int
}

type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].dist < q[j].dist }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	it := old[len(old)-1]
	*q = old[:len(old)-1]
	return it
}

func main() {
	var from, to string
	var value [faces]int64
	fmt.Scan(&from, &to)
	for i := range value {
		fmt.Scan(&value[i])
	}

	// the 24 orientations: which original face is at each position
	var identity [faces]int
	for i := range identity {
		identity[i] = i
	}
	orient := [][faces]int{identity}
	id := map[[faces]int]int{identity: 0}
	var next [][directions]int
	for o := 0; o < len(orient); o++ {
		next = append(next, [directions]int{})
		for d := 0; d < directions; d++ {
			var r [faces]int
			for i := range r {
				r[i] = orient[o][source[d][i]]
			}
			if _, ok := id[r]; !ok {
				id[r] = len(orient)
				orient = append(orient, r)
			}
			next[o][d] = id[r]
		}
	}

	// Dijkstra over (cell, orientation); a state costs its bottom face
	m := len(orient)
	state := func(x, y, o int) int { return (x*size+y)*m + o }
	dist := make([]int64, size*size*m)
	prev := make([]int, size*size*m)
	for i := range dist {
		dist[i], prev[i] = inf, -1
	}
	sx, sy := int(from[0]-'a'), int(from[1]-'1')
	tx, ty := int(to[0]-'a'), int(to[1]-'1')
	dist[state(sx, sy, 0)] = value[bottom]
	q := &queue{{value[bottom], state(sx, sy, 0)}}
	for q.Len() > 0 {
		it := heap.Pop(q).(item)
		if it.dist > dist[it.state] {
			continue
		}
		o, x, y := it.state%m, it.state/m/size, it.state/m%size
		for k := 0; k < directions; k++ {
			nx, ny := x+dx[k], y+dy[k]
			if nx < 0 || ny < 0 || nx >= size || ny >= size {
				continue
			}
			no := next[o][k]
			ns, nd := state(nx, ny, no), it.dist+value[orient[no][bottom]]
			if nd < dist[ns] {
				dist[ns], prev[ns] = nd, it.state
				heap.Push(q, item{nd, ns})
			}
		}
	}

	best := state(tx, ty, 0)
	for o := 0; o < m; o++ {
		if dist[state(tx, ty, o)] < dist[best] {
			best = state(tx, ty, o)
		}
	}
	var route []string
	for s := best; s >= 0; s = prev[s] {
		c := s / m
		route = append([]string{string(rune('a'+c/size)) + string(rune('1'+c%size))}, route...)
	}
	fmt.Println(dist[best], strings.Join(route, " "))
}
