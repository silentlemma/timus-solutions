package main

import (
	"bufio"
	"os"
	"strconv"
)

const shaves = 2
const maxTime = 2000
const inputSize = 4096
const decimalBase = 10
const outputReserve = 1200

type edge struct{ to, next, cap uint16 }
type flow struct {
	edges                  []edge
	head, at, level, queue []uint16
}

func (f *flow) add(a, b, cap int) {
	f.edges = append(f.edges, edge{uint16(b), f.head[a], uint16(cap)})
	f.head[a] = uint16(len(f.edges) - 1)
	f.edges = append(f.edges, edge{uint16(a), f.head[b], 0})
	f.head[b] = uint16(len(f.edges) - 1)
}

func (f *flow) push(v, sink uint16, limit uint16) uint16 {
	if v == sink {
		return limit
	}
	for f.at[v] != 0 {
		e := f.at[v]
		w := f.edges[e].to
		if f.edges[e].cap != 0 && f.level[w] == f.level[v]+1 {
			cap := limit
			if f.edges[e].cap < cap {
				cap = f.edges[e].cap
			}
			got := f.push(w, sink, cap)
			if got != 0 {
				f.edges[e].cap -= got
				f.edges[e^1].cap += got
				return got
			}
		}
		f.at[v] = f.edges[e].next
	}
	return 0
}

func (f *flow) solve(sink, need int) int {
	total := 0
	for total < need {
		for i := range f.level {
			f.level[i] = 0
			f.at[i] = f.head[i]
		}
		f.queue[0] = 0
		f.level[0] = 1
		length := 1
		for i := 0; i < length; i++ {
			v := f.queue[i]
			for e := f.head[v]; e != 0; e = f.edges[e].next {
				w := f.edges[e].to
				if f.edges[e].cap != 0 && f.level[w] == 0 {
					f.level[w] = f.level[v] + 1
					f.queue[length] = w
					length++
				}
			}
		}
		if f.level[sink] == 0 {
			break
		}
		for total < need {
			got := f.push(0, uint16(sink), uint16(need-total))
			if got == 0 {
				break
			}
			total += int(got)
		}
	}
	return total
}

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, inputSize)
	n, k := number(in), number(in)
	start, end := make([]int, n), make([]int, n)
	var index [maxTime + 1]uint16
	for i := range start {
		start[i] = number(in)
		end[i] = start[i] + number(in)
		index[start[i]] = 1
		index[end[i]] = 1
	}
	cuts := make([]int, 0, shaves*n)
	for t := range index {
		if index[t] != 0 {
			index[t] = uint16(len(cuts))
			cuts = append(cuts, t)
		}
	}
	blocks := len(cuts) - 1
	sink := n + blocks + 1
	edgeCount := n + blocks
	for i := range start {
		start[i] = int(index[start[i]])
		end[i] = int(index[end[i]])
		edgeCount += end[i] - start[i]
	}
	f := flow{edges: make([]edge, shaves, shaves*(edgeCount+1)), head: make([]uint16, sink+1),
		at: make([]uint16, sink+1), level: make([]uint16, sink+1), queue: make([]uint16, sink+1)}
	for i := range start {
		f.add(0, i+1, shaves)
		for j := start[i]; j < end[i]; j++ {
			cap := cuts[j+1] - cuts[j]
			if cap > shaves {
				cap = shaves
			}
			f.add(i+1, n+j+1, cap)
		}
	}
	for j := 0; j < blocks; j++ {
		cap := k * (cuts[j+1] - cuts[j])
		if cap > shaves*n {
			cap = shaves * n
		}
		f.add(n+j+1, sink, cap)
	}
	if f.solve(sink, shaves*n) < shaves*n {
		os.Stdout.WriteString("No\n")
		return
	}
	output := make([]byte, 0, outputReserve)
	output = append(output, "Yes\n"...)
	dealt := make([]int, blocks)
	for i := 1; i <= n; i++ {
		var times [shaves]int
		used := 0
		for e := f.head[i]; e != 0; e = f.edges[e].next {
			w := int(f.edges[e].to)
			if w <= n || w >= sink {
				continue
			}
			block := w - n - 1
			for count := f.edges[e^1].cap; count > 0; count-- {
				times[used] = cuts[block] + dealt[block]%(cuts[block+1]-cuts[block])
				used++
				dealt[block]++
			}
		}
		if times[0] > times[1] {
			times[0], times[1] = times[1], times[0]
		}
		output = strconv.AppendInt(output, int64(times[0]), decimalBase)
		output = append(output, ' ')
		output = strconv.AppendInt(output, int64(times[1]), decimalBase)
		output = append(output, '\n')
	}
	os.Stdout.Write(output)
}
