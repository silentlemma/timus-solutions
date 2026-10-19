package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

const bufferSize = 1 << 20

type cable struct {
	owner   int
	x, time int64
}

type event struct {
	at          int64 // walking cost from the foot to the point
	kind        int   // 0 a landing, 1 a start: landings first at one point
	start, time int64
}

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufferSize)
	readInt := func() int64 {
		n, c, neg := int64(0), byte(0), false
		for c, _ = reader.ReadByte(); c == ' ' || c == '\n' || c == '\r'; c, _ = reader.ReadByte() {
		}
		if c == '-' {
			neg = true
			c, _ = reader.ReadByte()
		}
		for ; c >= '0' && c <= '9'; c, _ = reader.ReadByte() {
			n = n*10 + int64(c-'0')
		}
		if neg {
			return -n
		}
		return n
	}
	n := int(readInt())
	xs := make([]int64, n+1)
	for i := range xs {
		xs[i] = readInt()
	}
	speed := make([]int64, n)
	var cables []cable
	for i := 0; i < n; i++ {
		speed[i] = readInt()
		m := int(readInt())
		for j := 0; j < m; j++ {
			x, t := readInt(), readInt()
			// a start at the first vertex of a segment is the last point of
			// the segment before it
			owner := i
			if i > 0 && x == xs[i] {
				owner = i - 1
			}
			cables = append(cables, cable{owner, x, t})
		}
	}
	walk := make([]int64, n+1)
	for i := 0; i < n; i++ {
		walk[i+1] = walk[i] + speed[i]*abs(xs[i+1]-xs[i])
	}
	cost := func(seg int, x int64) int64 { return walk[seg] + speed[seg]*abs(x-xs[seg]) }
	// every point but the foot belongs to one segment, which owns its x
	// range without its first vertex; a cable lands on the first later
	// segment owning its x, found by painting the segments from the top down
	keys := make([]int64, 0, len(cables))
	for _, c := range cables {
		keys = append(keys, c.x)
	}
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
	unique := keys[:0]
	for i, k := range keys {
		if i == 0 || k != keys[i-1] {
			unique = append(unique, k)
		}
	}
	keys = unique
	size := 1
	for size < len(keys) {
		size *= 2
	}
	paint := make([]int, 2*size)
	for i := range paint {
		paint[i] = n
	}
	cover := func(lo, hi, seg int) {
		for lo, hi = lo+size, hi+size; lo < hi; lo, hi = lo/2, hi/2 {
			if lo&1 == 1 {
				paint[lo] = seg
				lo++
			}
			if hi&1 == 1 {
				hi--
				paint[hi] = seg
			}
		}
	}
	look := func(i int) int {
		// paints only go down, so the lowest segment is the latest one
		best := n
		for i += size; i > 0; i /= 2 {
			if paint[i] < best {
				best = paint[i]
			}
		}
		return best
	}
	byOwner := make([][]int, n)
	for k, c := range cables {
		byOwner[c.owner] = append(byOwner[c.owner], k)
	}
	events := make([]event, 0, 2*len(cables))
	for seg := n - 1; seg >= 0; seg-- {
		for _, k := range byOwner[seg] {
			c := cables[k]
			at := sort.Search(len(keys), func(i int) bool { return keys[i] >= c.x })
			from := cost(c.owner, c.x)
			events = append(events, event{from, 1, 0, 0})
			events = append(events, event{cost(look(at), c.x), 0, from, c.time})
		}
		a, b := xs[seg], xs[seg+1]
		lo, hi := b, a-1
		if a < b {
			lo, hi = a+1, b
		}
		from := sort.Search(len(keys), func(i int) bool { return keys[i] >= lo })
		to := sort.Search(len(keys), func(i int) bool { return keys[i] > hi })
		cover(from, to, seg)
	}
	sort.Slice(events, func(i, j int) bool {
		if events[i].at != events[j].at {
			return events[i].at < events[j].at
		}
		return events[i].kind < events[j].kind
	})
	// going up, the best time at a point is its walking cost plus the least
	// (time - walking cost) over the landings so far
	best := make(map[int64]int64, len(cables))
	gain := int64(0)
	for _, e := range events {
		if e.kind == 0 {
			if v := best[e.start] + e.time - e.at; v < gain {
				gain = v
			}
		} else {
			best[e.at] = e.at + gain
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, strconv.FormatInt(walk[n]+gain, 10))
}
