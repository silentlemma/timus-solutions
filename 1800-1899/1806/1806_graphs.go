package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const digits = 10

type item struct {
	time int64
	node int
}

type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].time < q[j].time }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	last := old[len(old)-1]
	*q = old[:len(old)-1]
	return last
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(reader, &n); err != nil {
		return
	}
	cost := make([]int64, digits)
	for p := range cost {
		fmt.Fscan(reader, &cost[p])
	}
	place := make([]int64, digits)
	place[digits-1] = 1
	for p := digits - 2; p >= 0; p-- {
		place[p] = place[p+1] * digits
	}
	number := make([]int64, n)
	index := make(map[int64]int, n)
	for i := range number {
		var s string
		fmt.Fscan(reader, &s)
		for _, ch := range s {
			number[i] = number[i]*digits + int64(ch-'0')
		}
		index[number[i]] = i
	}
	best := make([]int64, n)
	before := make([]int, n)
	for i := range best {
		best[i] = -1
		before[i] = -1
	}
	best[0] = 0
	q := &queue{{0, 0}}
	relax := func(value, time int64, from int) {
		v, ok := index[value]
		if ok && (best[v] == -1 || time < best[v]) {
			best[v] = time
			before[v] = from
			heap.Push(q, item{time, v})
		}
	}
	var digit [digits]int64
	for q.Len() > 0 {
		cur := heap.Pop(q).(item)
		u, d := cur.node, cur.time
		if d > best[u] {
			continue
		}
		if u == n-1 {
			break
		}
		value := number[u]
		for p := 0; p < digits; p++ {
			digit[p] = value / place[p] % digits
		}
		// neighbours with the first change at digit p share a prefix of p
		for p := 0; p < digits; p++ {
			low := value - digit[p]*place[p]
			for other := int64(0); other < digits; other++ {
				if other != digit[p] {
					relax(low+other*place[p], d+cost[p], u)
				}
			}
			for r := p + 1; r < digits; r++ {
				if digit[r] != digit[p] {
					relax(value+(digit[r]-digit[p])*(place[p]-place[r]), d+cost[p], u)
				}
			}
		}
	}
	if best[n-1] == -1 {
		fmt.Println(-1)
		return
	}
	path := []int{n - 1}
	for path[len(path)-1] != 0 {
		path = append(path, before[path[len(path)-1]])
	}
	parts := make([]string, len(path))
	for i, v := range path {
		parts[len(path)-1-i] = strconv.Itoa(v + 1)
	}
	fmt.Println(best[n-1])
	fmt.Println(len(path))
	fmt.Println(strings.Join(parts, " "))
}
