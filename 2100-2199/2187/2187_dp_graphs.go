package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const negativeInfinity int64 = -1 << 60

type fastInput struct {
	data []byte
	pos  int
}

func (input *fastInput) nextInt() int {
	for input.data[input.pos] <= ' ' {
		input.pos++
	}
	value := 0
	for input.pos < len(input.data) && input.data[input.pos] > ' ' {
		value = value*10 + int(input.data[input.pos]-'0')
		input.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := fastInput{data: data}
	n, m := input.nextInt(), input.nextInt()
	treasure, cost := make([]int64, n), make([]int64, n)
	for vertex := range treasure {
		treasure[vertex] = int64(input.nextInt())
	}
	for length := 1; length < n; length++ {
		cost[length] = int64(input.nextInt())
	}

	first, second, degree := make([]int, m), make([]int, m), make([]int, n)
	for edge := 0; edge < m; edge++ {
		first[edge], second[edge] = input.nextInt()-1, input.nextInt()-1
		degree[first[edge]]++
		degree[second[edge]]++
	}
	offset := make([]int, n+1)
	for edge := range first {
		u, v := first[edge], second[edge]
		if degree[u] < degree[v] {
			offset[u+1]++
		} else if degree[v] < degree[u] {
			offset[v+1]++
		}
	}
	for vertex := 0; vertex < n; vertex++ {
		offset[vertex+1] += offset[vertex]
	}
	next := append([]int(nil), offset...)
	adjacent := make([]int, offset[n])
	for edge := range first {
		u, v := first[edge], second[edge]
		if degree[u] < degree[v] {
			adjacent[next[u]] = v
			next[u]++
		} else if degree[v] < degree[u] {
			adjacent[next[v]] = u
			next[v]++
		}
	}

	count := make([]int, n+1)
	for _, value := range degree {
		count[value+1]++
	}
	for value := 0; value < n; value++ {
		count[value+1] += count[value]
	}
	order := make([]int, n)
	for vertex, value := range degree {
		order[count[value]] = vertex
		count[value]++
	}

	// A state stores the profit before paying for the unfinished journey.
	states := make([][]int64, n)
	states[0] = []int64{treasure[0]}
	answer := treasure[0]
	for _, u := range order {
		current := states[u]
		states[u] = nil
		if len(current) == 0 {
			continue
		}
		best := current[0]
		for length := 1; length < len(current); length++ {
			if current[length] != negativeInfinity {
				candidate := current[length] - cost[length] + treasure[u]
				if candidate > best {
					best = candidate
				}
			}
		}
		current[0] = best
		if best > answer {
			answer = best
		}
		for edge := offset[u]; edge < offset[u+1]; edge++ {
			v := adjacent[edge]
			target := states[v]
			if len(target) <= len(current) {
				target = append(target, make([]int64, len(current)+1-len(target))...)
				for length := len(states[v]); length < len(target); length++ {
					target[length] = negativeInfinity
				}
			}
			for length, value := range current {
				if value > target[length+1] {
					target[length+1] = value
				}
			}
			states[v] = target
		}
	}
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, answer)
	output.Flush()
}
