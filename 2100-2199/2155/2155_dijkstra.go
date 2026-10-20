package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const infinity int64 = 1 << 60

type reader struct {
	data []byte
	pos  int
}

func (r *reader) integer() int {
	for r.data[r.pos] <= ' ' {
		r.pos++
	}
	value := 0
	for r.data[r.pos] >= '0' && r.data[r.pos] <= '9' {
		value = value*10 + int(r.data[r.pos]-'0')
		r.pos++
	}
	return value
}

func (r *reader) word() []byte {
	for r.data[r.pos] <= ' ' {
		r.pos++
	}
	start := r.pos
	for r.data[r.pos] > ' ' {
		r.pos++
	}
	return r.data[start:r.pos]
}

type entry struct {
	vertex int
	time   int64
}

type minHeap []entry

func (h *minHeap) push(value entry) {
	*h = append(*h, value)
	index := len(*h) - 1
	for index > 0 {
		parent := (index - 1) / 2
		if (*h)[parent].time <= value.time {
			break
		}
		(*h)[index] = (*h)[parent]
		index = parent
	}
	(*h)[index] = value
}

func (h *minHeap) pop() entry {
	result := (*h)[0]
	last := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	if len(*h) == 0 {
		return result
	}
	index := 0
	for index*2+1 < len(*h) {
		child := index*2 + 1
		if child+1 < len(*h) && (*h)[child+1].time < (*h)[child].time {
			child++
		}
		if last.time <= (*h)[child].time {
			break
		}
		(*h)[index] = (*h)[child]
		index = child
	}
	(*h)[index] = last
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	r := reader{data: append(data, ' ')}
	height, width := r.integer(), r.integer()
	stride := width + 2
	size := (height + 2) * stride
	person := r.integer()*stride + r.integer()
	drone := r.integer()*stride + r.integer()
	cost := make([]int, size)
	for row := 1; row <= height; row++ {
		for column := 1; column <= width; column++ {
			cost[row*stride+column] = r.integer()
		}
	}
	wind := make([]byte, size)
	for row := 1; row <= height; row++ {
		copy(wind[row*stride+1:row*stride+width+1], r.word())
	}
	distance := make([]int64, size)
	for vertex := range distance {
		distance[vertex] = infinity
	}
	distance[person] = 0
	queue := make(minHeap, 0, height*width)
	queue.push(entry{person, 0})
	steps := [...]int{-stride, stride, -1, 1}
	for len(queue) > 0 {
		current := queue.pop()
		if current.time != distance[current.vertex] {
			continue
		}
		for _, step := range steps {
			next := current.vertex + step
			if cost[next] == 0 {
				continue
			}
			arrival := current.time + int64(cost[next])
			if arrival < distance[next] {
				distance[next] = arrival
				queue.push(entry{next, arrival})
			}
		}
	}
	firstVisit := make([]int, size)
	for vertex := range firstVisit {
		firstVisit[vertex] = -1
	}
	path := make([]int, 0, height*width)
	for cost[drone] != 0 && firstVisit[drone] == -1 {
		firstVisit[drone] = len(path)
		path = append(path, drone)
		switch wind[drone] {
		case 'U':
			drone -= stride
		case 'D':
			drone += stride
		case 'L':
			drone--
		case 'R':
			drone++
		}
	}
	cycleStart := firstVisit[drone]
	cycleLength := int64(len(path) - cycleStart)
	answer := infinity
	for time, vertex := range path {
		candidate := int64(time)
		if distance[vertex] > candidate {
			if cycleStart == -1 || time < cycleStart {
				continue
			}
			difference := distance[vertex] - candidate
			candidate += (difference + cycleLength - 1) / cycleLength * cycleLength
		}
		if candidate < answer {
			answer = candidate
		}
	}
	if answer == infinity {
		answer = -1
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, answer)
	out.Flush()
}
