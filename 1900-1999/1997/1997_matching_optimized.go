package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 8192
const pairReserve = 24

type matcher struct {
	low, shortEnd, longStart, cursor, queue []uint16
	left, right, distance                   []int16
	shortest                                int16
}

func (h *matcher) layer() bool {
	count := len(h.left)
	h.shortest = int16(count + 1)
	tail := 0
	for u := 0; u < count; u++ {
		h.distance[u] = -1
		h.cursor[u] = h.low[u]
		if h.left[u] < 0 {
			h.distance[u] = 0
			h.queue[tail] = uint16(u)
			tail++
		}
	}
	for head := 0; head < tail; head++ {
		u := h.queue[head]
		if h.distance[u] >= h.shortest {
			continue
		}
		// Each row consists of two disjoint sorted exit-index intervals.
		for v := int(h.low[u]); v < count; v++ {
			if v == int(h.shortEnd[u]) {
				v = int(h.longStart[u])
				if v >= count {
					break
				}
			}
			mate := h.right[v]
			if mate < 0 {
				h.shortest = h.distance[u] + 1
			} else if h.distance[mate] < 0 {
				h.distance[mate] = h.distance[u] + 1
				h.queue[tail] = uint16(mate)
				tail++
			}
		}
	}
	return int(h.shortest) <= count
}

func (h *matcher) augment(u int) bool {
	for {
		if h.cursor[u] == h.shortEnd[u] {
			h.cursor[u] = h.longStart[u]
		}
		v := h.cursor[u]
		if int(v) >= len(h.right) {
			break
		}
		h.cursor[u]++
		mate := h.right[v]
		if mate < 0 {
			if h.distance[u]+1 != h.shortest {
				continue
			}
		} else if h.distance[mate] != h.distance[u]+1 || !h.augment(int(mate)) {
			continue
		}
		h.left[u] = int16(v)
		h.right[v] = int16(u)
		return true
	}
	h.distance[u] = -1
	return false
}

func number(in *bufio.Reader) int32 {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := int32(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int32(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	a, b := number(in), number(in)
	n := int(number(in))
	entries, exits := make([]int32, 0, n/2), make([]int32, 0, n/2)
	for i := 0; i < n; i++ {
		time, direction := number(in), number(in)
		if direction == 0 {
			entries = append(entries, time)
		} else {
			exits = append(exits, time)
		}
	}
	if len(entries) != len(exits) {
		os.Stdout.WriteString("Liar\n")
		return
	}
	count := len(entries)
	h := matcher{
		low:       make([]uint16, count),
		shortEnd:  make([]uint16, count),
		longStart: make([]uint16, count),
		cursor:    make([]uint16, count),
		queue:     make([]uint16, count),
		left:      make([]int16, count),
		right:     make([]int16, count),
		distance:  make([]int16, count),
	}
	lo, short, long := 0, 0, 0
	for u, entry := range entries {
		for lo < count && exits[lo] <= entry {
			lo++
		}
		for short < count && exits[short] <= entry+b {
			short++
		}
		for long < count && exits[long] < entry+a {
			long++
		}
		h.low[u], h.shortEnd[u], h.longStart[u] = uint16(lo), uint16(short), uint16(long)
		h.left[u], h.right[u] = -1, -1
	}
	matched := 0
	for h.layer() {
		for u := 0; u < count; u++ {
			if h.left[u] < 0 && h.augment(u) {
				matched++
			}
		}
	}
	if matched != count {
		os.Stdout.WriteString("Liar\n")
		return
	}
	output := make([]byte, 0, bufferSize)
	output = append(output, "No reason\n"...)
	for u, entry := range entries {
		if len(output)+pairReserve > cap(output) {
			os.Stdout.Write(output)
			output = output[:0]
		}
		output = strconv.AppendInt(output, int64(entry), 10)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(exits[h.left[u]]), 10)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
