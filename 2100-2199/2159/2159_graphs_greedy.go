package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

type tokenReader struct {
	data string
	pos  int
}

func (r *tokenReader) next() string {
	for r.pos < len(r.data) && r.data[r.pos] <= ' ' {
		r.pos++
	}
	start := r.pos
	for r.pos < len(r.data) && r.data[r.pos] > ' ' {
		r.pos++
	}
	return r.data[start:r.pos]
}

func (r *tokenReader) number() int {
	value := 0
	for _, digit := range r.next() {
		value = value*10 + int(digit-'0')
	}
	return value
}

type wordHeap struct {
	words []string
	nodes []int
}

func (h *wordHeap) push(id int) {
	h.nodes = append(h.nodes, id)
	index := len(h.nodes) - 1
	for index > 0 {
		parent := (index - 1) / 2
		if h.words[h.nodes[parent]] <= h.words[id] {
			break
		}
		h.nodes[index] = h.nodes[parent]
		index = parent
	}
	h.nodes[index] = id
}

func (h *wordHeap) pop() int {
	result := h.nodes[0]
	last := h.nodes[len(h.nodes)-1]
	h.nodes = h.nodes[:len(h.nodes)-1]
	if len(h.nodes) == 0 {
		return result
	}
	index := 0
	for {
		child := index*2 + 1
		if child >= len(h.nodes) {
			break
		}
		if child+1 < len(h.nodes) && h.words[h.nodes[child+1]] < h.words[h.nodes[child]] {
			child++
		}
		if h.words[last] <= h.words[h.nodes[child]] {
			break
		}
		h.nodes[index] = h.nodes[child]
		index = child
	}
	h.nodes[index] = last
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	reader := tokenReader{data: string(data)}
	keywordCount := reader.number()
	ruleCount := reader.number()
	capacity := keywordCount + 2*ruleCount
	ids := make(map[string]int, capacity)
	words := make([]string, 0, capacity)
	edges := make([][]int, 0, capacity)
	intern := func(word string) int {
		if id, found := ids[word]; found {
			return id
		}
		id := len(words)
		ids[word] = id
		words = append(words, word)
		edges = append(edges, nil)
		return id
	}
	required := make([]int, 0, capacity)
	for i := 0; i < keywordCount; i++ {
		required = append(required, intern(reader.next()))
	}
	for i := 0; i < ruleCount; i++ {
		from := intern(reader.next())
		to := intern(reader.next())
		edges[from] = append(edges[from], to)
	}

	needed := make([]bool, len(words))
	for _, id := range required {
		needed[id] = true
	}
	// Only rules reachable from required words matter.
	for index := 0; index < len(required); index++ {
		for _, to := range edges[required[index]] {
			if !needed[to] {
				needed[to] = true
				required = append(required, to)
			}
		}
	}
	indegree := make([]int, len(words))
	for _, from := range required {
		for _, to := range edges[from] {
			indegree[to]++
		}
	}
	ready := wordHeap{words: words, nodes: make([]int, 0, len(required))}
	for _, id := range required {
		if indegree[id] == 0 {
			ready.push(id)
		}
	}
	answer := make([]int, 0, len(required))
	for len(ready.nodes) > 0 {
		from := ready.pop()
		answer = append(answer, from)
		for _, to := range edges[from] {
			indegree[to]--
			if indegree[to] == 0 {
				ready.push(to)
			}
		}
	}

	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if len(answer) != len(required) {
		fmt.Fprintln(writer, "-1")
		return
	}
	for index, id := range answer {
		if index != 0 {
			writer.WriteByte(' ')
		}
		writer.WriteString(words[id])
	}
	writer.WriteByte('\n')
}
