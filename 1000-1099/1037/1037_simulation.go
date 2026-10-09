package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	blocks   = 30000
	lifetime = 600
)

// a min-heap of block numbers
type minHeap []int

func (h *minHeap) push(v int) {
	*h = append(*h, v)
	a := *h
	for i := len(a) - 1; i > 0; {
		p := (i - 1) / 2
		if a[p] <= a[i] {
			break
		}
		a[p], a[i] = a[i], a[p]
		i = p
	}
}

func (h *minHeap) pop() int {
	a := *h
	top := a[0]
	last := len(a) - 1
	a[0] = a[last]
	a = a[:last]
	for i := 0; ; {
		c := 2*i + 1
		if c >= len(a) {
			break
		}
		if c+1 < len(a) && a[c+1] < a[c] {
			c++
		}
		if a[i] <= a[c] {
			break
		}
		a[i], a[c] = a[c], a[i]
		i = c
	}
	*h = a
	return top
}

func main() {
	sc := bufio.NewScanner(bufio.NewReader(os.Stdin))
	sc.Split(bufio.ScanWords)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	// expiry[b]: when block b becomes free, unless it is accessed again
	expiry := make([]int, blocks+1)
	busy := make([]bool, blocks+1)
	// times never decrease, so the expiries are queued in order; an entry is
	// stale when the block was accessed again later
	var queue [][2]int
	head := 0
	freed := &minHeap{}
	fresh := 1
	for sc.Scan() {
		t, _ := strconv.Atoi(sc.Text())
		sc.Scan()
		op := sc.Text()
		for head < len(queue) && queue[head][0] <= t {
			e, b := queue[head][0], queue[head][1]
			head++
			if busy[b] && expiry[b] == e {
				busy[b] = false
				freed.push(b)
			}
		}
		var b int
		if op == "+" {
			// freed blocks are all smaller than the never used ones
			if len(*freed) > 0 {
				b = freed.pop()
			} else {
				b = fresh
				fresh++
			}
			w.WriteString(strconv.Itoa(b))
		} else {
			sc.Scan()
			b, _ = strconv.Atoi(sc.Text())
			if !busy[b] {
				w.WriteString("-\n")
				continue
			}
			w.WriteString("+")
		}
		w.WriteString("\n")
		busy[b] = true
		expiry[b] = t + lifetime
		queue = append(queue, [2]int{expiry[b], b})
	}
}
