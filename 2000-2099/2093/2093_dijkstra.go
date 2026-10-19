package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	inputBufferSize = 65536
	percentScale    = int64(100)
	maxSlowdown     = int64(100500)
	snowLimit       = (maxSlowdown - 1) * percentScale
	infinity        = int64(1 << 62)
)

type input struct {
	buffer [inputBufferSize]byte
	pos    int
	size   int
}

func (in *input) nextInt() int64 {
	value := int64(0)
	started := false
	for {
		if in.pos == in.size {
			in.size, _ = os.Stdin.Read(in.buffer[:])
			in.pos = 0
			if in.size == 0 {
				return value
			}
		}
		ch := in.buffer[in.pos]
		in.pos++
		if ch >= '0' && ch <= '9' {
			value = value*10 + int64(ch-'0')
			started = true
		} else if started {
			return value
		}
	}
}

type arc struct {
	to   int32
	road int32
	next int32
}

type cleaning struct {
	start  int64
	finish int64
	road   int32
}

type schedule []cleaning

func (s schedule) Len() int {
	return len(s)
}

func (s schedule) Less(i, j int) bool {
	if s[i].road != s[j].road {
		return s[i].road < s[j].road
	}
	return s[i].start < s[j].start
}

func (s schedule) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

type state struct {
	time   int64
	vertex int32
}

type minHeap []state

func (h *minHeap) push(item state) {
	*h = append(*h, item)
	pos := len(*h) - 1
	for pos > 0 {
		parent := (pos - 1) / 2
		if (*h)[parent].time <= item.time {
			break
		}
		(*h)[pos] = (*h)[parent]
		pos = parent
	}
	(*h)[pos] = item
}

func (h *minHeap) pop() state {
	answer := (*h)[0]
	last := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	pos := 0
	for 2*pos+1 < len(*h) {
		child := 2*pos + 1
		if child+1 < len(*h) && (*h)[child+1].time < (*h)[child].time {
			child++
		}
		if last.time <= (*h)[child].time {
			break
		}
		(*h)[pos] = (*h)[child]
		pos = child
	}
	if len(*h) > 0 {
		(*h)[pos] = last
	}
	return answer
}

func arrival(at, cleared, base int64) int64 {
	departure := at
	if departure < cleared {
		departure = cleared
	}
	elapsed := departure - cleared
	if elapsed > snowLimit {
		elapsed = snowLimit
	}
	duration := base + (elapsed*base+percentScale-1)/percentScale
	return departure + duration
}

func earliest(at, base int64, events schedule) int64 {
	cleared := int64(0)
	// Later gaps start after any feasible arrival in the current gap.
	for _, event := range events {
		candidate := arrival(at, cleared, base)
		if candidate <= event.start {
			return candidate
		}
		cleared = event.finish
	}
	return arrival(at, cleared, base)
}

func main() {
	in := input{}
	n := int(in.nextInt())
	m := int(in.nextInt())
	heads := make([]int32, n)
	for i := range heads {
		heads[i] = -1
	}
	arcs := make([]arc, 0, 2*m)
	bases := make([]int64, m)
	for road := range bases {
		a := int32(in.nextInt() - 1)
		b := int32(in.nextInt() - 1)
		bases[road] = in.nextInt()
		arcs = append(arcs, arc{b, int32(road), heads[a]})
		heads[a] = int32(len(arcs) - 1)
		arcs = append(arcs, arc{a, int32(road), heads[b]})
		heads[b] = int32(len(arcs) - 1)
	}
	k := int(in.nextInt())
	events := make(schedule, k)
	offsets := make([]int, m+1)
	for i := range events {
		road := int32(in.nextInt() - 1)
		events[i] = cleaning{in.nextInt(), in.nextInt(), road}
		offsets[road+1]++
	}
	sort.Sort(events)
	for road := range bases {
		offsets[road+1] += offsets[road]
	}
	distances := make([]int64, n)
	for i := range distances {
		distances[i] = infinity
	}
	distances[0] = 0
	queue := minHeap{{0, 0}}
	for len(queue) > 0 {
		current := queue.pop()
		if current.time != distances[current.vertex] {
			continue
		}
		if current.vertex == int32(n-1) {
			break
		}
		for index := heads[current.vertex]; index >= 0; index = arcs[index].next {
			edge := arcs[index]
			road := edge.road
			next := earliest(current.time, bases[road], events[offsets[road]:offsets[road+1]])
			if next < distances[edge.to] {
				distances[edge.to] = next
				queue.push(state{next, edge.to})
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, distances[n-1])
	out.Flush()
}
