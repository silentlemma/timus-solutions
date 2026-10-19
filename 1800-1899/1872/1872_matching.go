package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
)

// waiting teams by their largest area
type waitList struct {
	ids  []int
	high []int
}

func (w *waitList) Len() int           { return len(w.ids) }
func (w *waitList) Less(i, j int) bool { return w.high[w.ids[i]] < w.high[w.ids[j]] }
func (w *waitList) Swap(i, j int)      { w.ids[i], w.ids[j] = w.ids[j], w.ids[i] }
func (w *waitList) Push(x interface{}) { w.ids = append(w.ids, x.(int)) }
func (w *waitList) Pop() interface{} {
	last := w.ids[len(w.ids)-1]
	w.ids = w.ids[:len(w.ids)-1]
	return last
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	area := make([]int, n)
	for i := range area {
		fmt.Fscan(reader, &area[i])
	}
	low, high := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(reader, &low[i], &high[i])
	}
	order, byLow := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		order[i], byLow[i] = i, i
	}
	sort.Slice(order, func(a, b int) bool { return area[order[a]] < area[order[b]] })
	sort.Slice(byLow, func(a, b int) bool { return low[byLow[a]] < low[byLow[b]] })
	sizes := make([]int, n)
	for i, k := range order {
		sizes[i] = area[k]
	}
	// rooms from the smallest up, each to the waiting team whose largest
	// area is the smallest
	waiting := &waitList{high: high}
	team := make([]int, n)
	at := 0
	for place := 0; place < n; place++ {
		for at < n && low[byLow[at]] <= sizes[place] {
			heap.Push(waiting, byLow[at])
			at++
		}
		if waiting.Len() == 0 || high[waiting.ids[0]] < sizes[place] {
			fmt.Fprintln(writer, "Let's search for another office.")
			return
		}
		team[place] = heap.Pop(waiting).(int)
	}
	// the team in room place takes rooms first[place] .. last[place] in
	// sorted order; another seating exists exactly when two teams could swap
	first, last := make([]int, n), make([]int, n)
	for p, t := range team {
		first[p] = sort.SearchInts(sizes, low[t])
		last[p] = sort.SearchInts(sizes, high[t]+1) - 1
	}
	for q := 1; q < n; q++ {
		for p := first[q]; p < q; p++ {
			if last[p] >= q {
				fmt.Fprintln(writer, "Ask Shiftman for help.")
				return
			}
		}
	}
	room := make([]int, n)
	for p, t := range team {
		room[t] = order[p] + 1
	}
	fmt.Fprintln(writer, "Perfect!")
	for i, r := range room {
		if i > 0 {
			fmt.Fprint(writer, " ")
		}
		fmt.Fprint(writer, r)
	}
	fmt.Fprintln(writer)
}
