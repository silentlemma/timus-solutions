package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
)

const indexBits = 10
const indexMask = (1 << indexBits) - 1
const outputDigits = 10
const floatBits = 64

func solve(x, y []int64) []int64 {
	n := len(x)
	order := make([]int, n)
	position := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(i, j int) bool {
		a, b := order[i], order[j]
		if y[a] != y[b] {
			return y[a] > y[b]
		}
		if x[a] != x[b] {
			return x[a] < x[b]
		}
		return a < b
	})
	px, py := make([]int64, n+1), make([]int64, n+1)
	best := make([]int64, n+1)
	for i, id := range order {
		position[id] = i
		px[i+1], py[i+1] = px[i]+x[id], py[i]+y[id]
	}
	tx, ty := px[n], py[n]
	record := func(k int, a, b int64) {
		value := a*a + b*b
		if value > best[k] {
			best[k] = value
		}
		a, b = tx-a, ty-b
		value = a*a + b*b
		if value > best[n-k] {
			best[n-k] = value
		}
	}
	for k := 0; k <= n; k++ {
		record(k, px[k], py[k])
	}
	events := make([]int, 0, n*(n-1)/2)
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if y[i] == y[j] {
				continue
			}
			high, low := i, j
			if y[high] < y[low] {
				high, low = low, high
			}
			events = append(events, (high<<indexBits)|low)
		}
	}
	less := func(a, b int) bool {
		ah, al, bh, bl := a>>indexBits, a&indexMask, b>>indexBits, b&indexMask
		return (x[al]-x[ah])*(y[bh]-y[bl]) < (x[bl]-x[bh])*(y[ah]-y[al])
	}
	sort.Slice(events, func(i, j int) bool { return less(events[i], events[j]) })
	ends := make([]int, n)
	for i := range ends {
		ends[i] = -1
	}
	starts := make([]int, 0, n)
	intervals := make([][2]int, 0, n)
	for at := 0; at < len(events); {
		after := at + 1
		for after < len(events) && !less(events[at], events[after]) {
			after++
		}
		if after == at+1 {
			a, b := position[events[at]>>indexBits], position[events[at]&indexMask]
			left := a
			if b < left {
				left = b
			}
			first, second := order[left], order[left+1]
			order[left], order[left+1] = second, first
			position[first], position[second] = left+1, left
			k := left + 1
			px[k] += x[second] - x[first]
			py[k] += y[second] - y[first]
			record(k, px[k], py[k])
		} else {
			starts, intervals = starts[:0], intervals[:0]
			for i := at; i < after; i++ {
				a, b := position[events[i]>>indexBits], position[events[i]&indexMask]
				if a > b {
					a, b = b, a
				}
				if ends[a] < 0 {
					starts = append(starts, a)
				}
				if b > ends[a] {
					ends[a] = b
				}
			}
			sort.Ints(starts)
			for _, left := range starts {
				right := ends[left]
				ends[left] = -1
				last := len(intervals) - 1
				if last >= 0 && left <= intervals[last][1] {
					if right > intervals[last][1] {
						intervals[last][1] = right
					}
				} else {
					intervals = append(intervals, [2]int{left, right})
				}
			}
			for _, interval := range intervals {
				left, right := interval[0], interval[1]
				for a, b := left, right; a < b; a, b = a+1, b-1 {
					order[a], order[b] = order[b], order[a]
				}
				a, b := px[left], py[left]
				for i := left; i <= right; i++ {
					id := order[i]
					position[id] = i
					a, b = a+x[id], b+y[id]
					px[i+1], py[i+1] = a, b
					if i < right {
						record(i+1, a, b)
					}
				}
			}
		}
		at = after
	}
	return best[1:]
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	if _, err := fmt.Fscan(in, &n); err != nil {
		return
	}
	x, y := make([]int64, n), make([]int64, n)
	for i := range x {
		fmt.Fscan(in, &x[i], &y[i])
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, value := range solve(x, y) {
		fmt.Fprintln(out, strconv.FormatFloat(math.Sqrt(float64(value)), 'f', outputDigits, floatBits))
	}
}
