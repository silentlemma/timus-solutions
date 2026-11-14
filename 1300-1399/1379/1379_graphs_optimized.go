package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const (
	inputBufferSize = 16 * 1024
	day             = 24 * 60
	truck           = 3000000
	cup             = 100
	order           = 10000000
	none            = -1
	vertexBits      = 9
	timeBits        = 11
	loadShift       = vertexBits + timeBits
	vertexMask      = (1 << vertexBits) - 1
	timeMask        = (1 << timeBits) - 1
)

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func canDeliver(graph [][]uint64, load int) bool {
	const maxVertices = 500
	var distance [maxVertices]int
	var next, previous [maxVertices]int
	var heads [day + 1]int
	threshold := uint64(load) << loadShift
	for i := range graph {
		distance[i] = day + 1
	}
	for i := range heads {
		heads[i] = none
	}
	distance[0], next[0], previous[0], heads[0] = 0, none, none, 0
	for minute := range heads {
		for heads[minute] != none {
			v := heads[minute]
			heads[minute] = next[v]
			if next[v] != none {
				previous[next[v]] = none
			}
			if v == len(graph)-1 {
				return true
			}
			for _, edge := range graph[v] {
				if edge < threshold {
					break
				}
				to := int(edge & vertexMask)
				arrival := minute + int(edge>>vertexBits&timeMask)
				old := distance[to]
				if arrival >= old {
					continue
				}
				if old <= day {
					before, after := previous[to], next[to]
					if before == none {
						heads[old] = after
					} else {
						next[before] = after
					}
					if after != none {
						previous[after] = before
					}
				}
				distance[to], previous[to], next[to] = arrival, none, heads[arrival]
				if heads[arrival] != none {
					previous[heads[arrival]] = to
				}
				heads[arrival] = to
			}
		}
	}
	return false
}

func main() {
	input := bufio.NewReaderSize(os.Stdin, inputBufferSize)
	n, m := number(input), number(input)
	if n == 1 {
		fmt.Println(order)
		return
	}
	graph := make([][]uint64, n)
	limits := make([]int, 0, m)
	for i := 0; i < m; i++ {
		a, b := number(input)-1, number(input)-1
		minutes, weight := number(input), number(input)
		if weight < truck+cup {
			continue
		}
		load := (weight - truck) / cup
		edge := uint64(load)<<loadShift | uint64(minutes)<<vertexBits
		graph[a] = append(graph[a], edge|uint64(b))
		graph[b] = append(graph[b], edge|uint64(a))
		limits = append(limits, load)
	}
	if len(graph[0]) == 0 || len(graph[n-1]) == 0 {
		fmt.Println(0)
		return
	}
	for _, edges := range graph {
		sort.Slice(edges, func(i, j int) bool { return edges[i] > edges[j] })
	}
	upper := int(graph[0][0] >> loadShift)
	if destinationUpper := int(graph[n-1][0] >> loadShift); destinationUpper < upper {
		upper = destinationUpper
	}
	sort.Ints(limits)
	count := 0
	for _, load := range limits {
		if load > upper {
			break
		}
		if count == 0 || load != limits[count-1] {
			limits[count] = load
			count++
		}
	}
	index := sort.Search(count, func(i int) bool { return !canDeliver(graph, limits[i]) })
	answer := 0
	if index > 0 {
		answer = limits[index-1]
	}
	fmt.Println(answer)
}
