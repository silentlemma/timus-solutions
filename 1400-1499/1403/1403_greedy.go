package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// byReward: a min-heap of order numbers by reward.
type byReward struct {
	items  []int
	reward []int
}

func (h byReward) Len() int            { return len(h.items) }
func (h byReward) Less(a, b int) bool  { return h.reward[h.items[a]] < h.reward[h.items[b]] }
func (h byReward) Swap(a, b int)       { h.items[a], h.items[b] = h.items[b], h.items[a] }
func (h *byReward) Push(x interface{}) { h.items = append(h.items, x.(int)) }
func (h *byReward) Pop() interface{} {
	last := h.items[len(h.items)-1]
	h.items = h.items[:len(h.items)-1]
	return last
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	deadline, reward, orders := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &deadline[i], &reward[i])
		orders[i] = i
	}
	sort.Slice(orders, func(a, b int) bool { return deadline[orders[a]] < deadline[orders[b]] })
	// by deadline: keep the best orders that fit, dropping the cheapest when
	// there are more orders than days so far
	kept := &byReward{reward: reward}
	for _, i := range orders {
		heap.Push(kept, i)
		if kept.Len() > deadline[i] {
			heap.Pop(kept)
		}
	}
	chosen := kept.items
	sort.Slice(chosen, func(a, b int) bool { return deadline[chosen[a]] < deadline[chosen[b]] })
	parts := make([]string, len(chosen))
	for k, i := range chosen {
		parts[k] = strconv.Itoa(i + 1)
	}
	fmt.Printf("%d\n%s\n", len(chosen), strings.Join(parts, " "))
}
