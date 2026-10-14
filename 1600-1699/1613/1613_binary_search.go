package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const bufSize = 1 << 20 // the longest line: 69999 counts

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, bufSize), bufSize)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n := next()
	// (passengers, city) pairs in order: the cities with one count are
	// consecutive and sorted by number
	count, city := make([]int, n), make([]int, n)
	order := make([]int, n)
	for i := range order {
		count[i], order[i] = next(), i
	}
	sort.Slice(order, func(a, b int) bool {
		if count[order[a]] != count[order[b]] {
			return count[order[a]] < count[order[b]]
		}
		return order[a] < order[b]
	})
	sorted := make([]int, n)
	for k, i := range order {
		sorted[k], city[k] = count[i], i+1
	}
	q := next()
	out := make([]byte, q)
	for i := range out {
		lo, hi, x := next(), next(), next()
		// the first city with count x and number at least lo
		k := sort.Search(n, func(k int) bool {
			return sorted[k] > x || (sorted[k] == x && city[k] >= lo)
		})
		out[i] = '0'
		if k < n && sorted[k] == x && city[k] <= hi {
			out[i] = '1'
		}
	}
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	w.Write(out)
	w.WriteByte('\n')
}
