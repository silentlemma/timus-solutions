package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type rider struct{ finish, id int }

// riders by the farthest stop first
type farthest []rider

func (h farthest) Len() int            { return len(h) }
func (h farthest) Less(a, b int) bool  { return h[a].finish > h[b].finish }
func (h farthest) Swap(a, b int)       { h[a], h[b] = h[b], h[a] }
func (h *farthest) Push(x interface{}) { *h = append(*h, x.(rider)) }
func (h *farthest) Pop() interface{} {
	old := *h
	x := old[len(old)-1]
	*h = old[:len(old)-1]
	return x
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k, price int
	fmt.Fscan(in, &n, &m, &k, &price)
	starts := make([][]int, n+1)
	finish := make([]int, k+1)
	ends := make([]int, n+1)
	for i := 1; i <= k; i++ {
		var s int
		fmt.Fscan(in, &s, &finish[i])
		starts[s] = append(starts[s], i)
	}
	taken := make([]bool, k+1)
	onBoard := &farthest{}
	riding := 0
	for stop := 1; stop <= n; stop++ {
		riding -= ends[stop]
		for _, i := range starts[stop] {
			taken[i] = true
			heap.Push(onBoard, rider{finish[i], i})
			ends[finish[i]]++
			riding++
		}
		// too many: drop whoever would ride the longest
		for riding > m {
			r := heap.Pop(onBoard).(rider)
			taken[r.id] = false
			ends[r.finish]--
			riding--
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	count := 0
	var list []byte
	for i := 1; i <= k; i++ {
		if taken[i] {
			if count > 0 {
				list = append(list, ' ')
			}
			list = strconv.AppendInt(list, int64(i), 10)
			count++
		}
	}
	fmt.Fprintln(out, count*price)
	out.Write(list)
	out.WriteByte('\n')
}
