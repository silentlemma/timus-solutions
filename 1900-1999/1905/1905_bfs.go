package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

const timeBase int64 = 1000001

type input struct {
	data []byte
	pos  int
}

func (in *input) next() int {
	for in.pos < len(in.data) && in.data[in.pos] <= ' ' {
		in.pos++
	}
	value := 0
	for in.pos < len(in.data) && in.data[in.pos] >= '0' && in.data[in.pos] <= '9' {
		value = value*10 + int(in.data[in.pos]-'0')
		in.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := input{data: data}
	in.next()
	count := in.next()
	origins, destinations := make([]int64, count), make([]int64, count)
	keys := make([]int64, 0, 2*count+2)
	for i := 0; i < count; i++ {
		from, to, leave, enter := in.next(), in.next(), in.next(), in.next()
		origins[i] = int64(from)*timeBase + int64(leave)
		destinations[i] = int64(to)*timeBase + int64(enter)
		keys = append(keys, origins[i], destinations[i])
	}
	from, to, start, deadline := in.next(), in.next(), in.next(), in.next()
	sourceKey, goalKey := int64(from)*timeBase+int64(start), int64(to)*timeBase+int64(deadline)
	keys = append(keys, sourceKey, goalKey)
	sort.Slice(keys, func(i, j int) bool { return keys[i] < keys[j] })
	unique := 0
	for _, key := range keys {
		if unique == 0 || key != keys[unique-1] {
			keys[unique] = key
			unique++
		}
	}
	keys = keys[:unique]
	index := func(key int64) int {
		return sort.Search(len(keys), func(i int) bool { return keys[i] >= key })
	}
	head, arrival, following := make([]int, unique), make([]int, count), make([]int, count)
	for i := range head {
		head[i] = -1
	}
	for i := 0; i < count; i++ {
		departure := index(origins[i])
		arrival[i], following[i] = index(destinations[i]), head[departure]
		head[departure] = i
	}
	source, goal := index(sourceKey), index(goalKey)
	previous, usedFlight := make([]int, unique), make([]int, unique)
	for i := range previous {
		previous[i] = -1
	}
	previous[source] = source
	queue := make([]int, 1, unique)
	queue[0] = source
	for cursor := 0; cursor < len(queue) && previous[goal] == -1; cursor++ {
		node := queue[cursor]
		next := node + 1
		if next < unique && keys[node]/timeBase == keys[next]/timeBase && previous[next] == -1 {
			previous[next] = node
			queue = append(queue, next)
		}
		for flight := head[node]; flight != -1; flight = following[flight] {
			destination := arrival[flight]
			if previous[destination] == -1 {
				previous[destination], usedFlight[destination] = node, flight+1
				queue = append(queue, destination)
			}
		}
	}
	if previous[goal] == -1 {
		fmt.Println("Impossible")
		return
	}
	route := make([]int, 0)
	for node := goal; node != source; node = previous[node] {
		if usedFlight[node] != 0 {
			route = append(route, usedFlight[node])
		}
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, len(route))
	for i := len(route) - 1; i >= 0; i-- {
		if i != len(route)-1 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, route[i])
	}
	fmt.Fprintln(out)
	out.Flush()
}
