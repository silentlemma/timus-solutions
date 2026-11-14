package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
)

const idBits = 16
const idMask = (1 << idBits) - 1

type tripsHeap []uint64

func (h tripsHeap) Len() int           { return len(h) }
func (h tripsHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h tripsHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *tripsHeap) Push(value interface{}) {
	*h = append(*h, value.(uint64))
}
func (h *tripsHeap) Pop() interface{} {
	last := len(*h) - 1
	value := (*h)[last]
	*h = (*h)[:last]
	return value
}

func number(input *bufio.Reader) int {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	value := 0
	for err == nil && '0' <= ch && ch <= '9' {
		value = 10*value + int(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func main() {
	input := bufio.NewReader(os.Stdin)
	stops, capacity := number(input), number(input)
	requests, price := number(input), number(input)
	starts, ends := make([]uint16, stops+1), make([]uint16, stops+1)
	following, finish := make([]uint16, requests+1), make([]uint32, requests+1)
	for id := 1; id <= requests; id++ {
		start, end := number(input), number(input)
		following[id], starts[start] = starts[start], uint16(id)
		finish[id] = uint32(end)
	}
	chosen := make([]bool, requests+1)
	farthest := make(tripsHeap, 0, requests)
	riding, count := 0, 0
	for stop, first := range starts {
		riding -= int(ends[stop])
		for id := first; id != 0; id = following[id] {
			end := finish[id]
			chosen[id] = true
			ends[end]++
			riding++
			count++
			// Pack destination and passenger number into one heap key.
			heap.Push(&farthest, uint64(end)<<idBits|uint64(id))
			if riding > capacity {
				drop := heap.Pop(&farthest).(uint64)
				chosen[drop&idMask] = false
				ends[drop>>idBits]--
				riding--
				count--
			}
		}
	}
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	fmt.Fprintln(output, int64(count)*int64(price))
	separator := ""
	for id, accepted := range chosen {
		if accepted {
			fmt.Fprint(output, separator, id)
			separator = " "
		}
	}
	fmt.Fprintln(output)
}
