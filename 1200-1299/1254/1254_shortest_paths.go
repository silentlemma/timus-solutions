package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
)

type item struct {
	key  float64
	cell int
}

type queue []item

func (q queue) Len() int            { return len(q) }
func (q queue) Less(i, j int) bool  { return q[i].key < q[j].key }
func (q queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *queue) Push(x interface{}) { *q = append(*q, x.(item)) }
func (q *queue) Pop() interface{} {
	old := *q
	x := old[len(old)-1]
	*q = old[:len(old)-1]
	return x
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m, k int
	var v float64
	fmt.Fscan(in, &n, &m, &k, &v)
	// cells over a grid with a border of buildings, so no move needs a
	// bounds check
	w := n + 2
	free := make([]bool, (m+2)*w)
	for r := 1; r <= m; r++ {
		var row string
		fmt.Fscan(in, &row)
		for c := 1; c <= n && c <= len(row); c++ {
			free[r*w+c] = row[c-1] == '.'
		}
	}
	var x, y int
	fmt.Fscan(in, &x, &y)
	at := y*w + x
	free[at] = true // John stands there, whatever the map shows
	// a step along a side costs 1, along a diagonal sqrt 2, and a diagonal
	// may pass a building's corner
	steps := []int{1, -1, w, -w, w + 1, w - 1, -w + 1, -w - 1}
	costs := []float64{1, 1, 1, 1, math.Sqrt2, math.Sqrt2, math.Sqrt2, math.Sqrt2}
	// parts of the town joined by moves, so an unreachable bomb costs nothing
	part := make([]int, len(free))
	for c, open := range free {
		if !open || part[c] != 0 {
			continue
		}
		part[c] = c + 1
		stack := []int{c}
		for len(stack) > 0 {
			a := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, s := range steps {
				if b := a + s; free[b] && part[b] == 0 {
					part[b] = c + 1
					stack = append(stack, b)
				}
			}
		}
	}
	dist := make([]float64, len(free))
	// shortest walk by A*, with the octile distance as an estimate that
	// never exceeds the true length
	walk := func(from, to int) float64 {
		guess := func(c int) float64 {
			dy, dx := abs(c/w-to/w), abs(c%w-to%w)
			if dx < dy {
				dx, dy = dy, dx
			}
			return float64(dx) + (math.Sqrt2-1)*float64(dy)
		}
		for i := range dist {
			dist[i] = math.Inf(1)
		}
		dist[from] = 0
		q := &queue{{guess(from), from}}
		for {
			it := heap.Pop(q).(item)
			if it.cell == to {
				return dist[to]
			}
			if it.key > dist[it.cell]+guess(it.cell) {
				continue
			}
			for i, s := range steps {
				b := it.cell + s
				if d := dist[it.cell] + costs[i]; free[b] && d < dist[b] {
					dist[b] = d
					heap.Push(q, item{d + guess(b), b})
				}
			}
		}
	}
	known := map[[2]int]float64{}
	total := 0.0
	for ; k > 0; k-- {
		fmt.Fscan(in, &x, &y)
		target := y*w + x
		// an unreachable bomb is skipped and John stays where he is
		if part[target] != part[at] {
			continue
		}
		d, ok := known[[2]int{at, target}]
		if !ok {
			d = walk(at, target)
			known[[2]int{at, target}], known[[2]int{target, at}] = d, d
		}
		total += d
		at = target
	}
	fmt.Printf("%.2f\n", total/v)
}
