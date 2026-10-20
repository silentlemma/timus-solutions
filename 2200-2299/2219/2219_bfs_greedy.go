package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

type scanner struct {
	data []byte
	pos  int
}

func (s *scanner) nextInt() int {
	for s.pos < len(s.data) && s.data[s.pos] <= ' ' {
		s.pos++
	}
	value := 0
	for s.pos < len(s.data) && s.data[s.pos] >= '0' && s.data[s.pos] <= '9' {
		value = value*10 + int(s.data[s.pos]-'0')
		s.pos++
	}
	return value
}

func fill(required []int, next *[2]int, parity int, limit int64, count int) {
	for next[parity] < len(required) && int64(next[parity]) <= limit {
		required[next[parity]] = count
		next[parity] += 2
	}
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n, m, k := in.nextInt(), in.nextInt(), in.nextInt()
	head := make([]int, n)
	for i := range head {
		head[i] = -1
	}
	to, link := make([]int, 2*m), make([]int, 2*m)
	for edge := 0; edge < 2*m; edge += 2 {
		u, v := in.nextInt()-1, in.nextInt()-1
		to[edge], link[edge], head[u] = v, head[u], edge
		to[edge+1], link[edge+1], head[v] = u, head[v], edge+1
	}

	distance := make([]int, 2*n)
	for i := range distance {
		distance[i] = -1
	}
	distance[0] = 0
	queue := make([]int, 1, 2*n)
	queue[0] = 0
	for front := 0; front < len(queue); front++ {
		state := queue[front]
		vertex, parity := state/2, (state%2)^1
		for edge := head[vertex]; edge != -1; edge = link[edge] {
			nextState := 2*to[edge] + parity
			if distance[nextState] == -1 {
				distance[nextState] = distance[state] + 1
				queue = append(queue, nextState)
			}
		}
	}

	cups := make([]int, k)
	for i := range cups {
		cups[i] = in.nextInt()
	}
	sort.Ints(cups)
	prefix := make([][2]int64, k+1)
	prefix[0] = [2]int64{-1, -1}
	for i, cup := range cups {
		prefix[i+1] = prefix[i]
		prefix[i+1][cup%2] = int64(cup)
	}
	required := make([]int, 2*n)
	for i := range required {
		required[i] = -1
	}
	required[0] = 0
	next := [2]int{2, 1}
	smallest := [2]int64{-1, -1}
	sum := int64(0)
	for count := 1; count <= k; count++ {
		index := k - count
		cup := cups[index]
		sum += int64(cup)
		smallest[cup%2] = int64(cup)
		parity := int(sum % 2)
		fill(required, &next, parity, sum, count)
		// An optimal sum of the other parity replaces one selected cup.
		best := int64(-1)
		for removed := 0; removed < 2; removed++ {
			added := removed ^ 1
			if smallest[removed] != -1 && prefix[index][added] != -1 {
				candidate := sum - smallest[removed] + prefix[index][added]
				if candidate > best {
					best = candidate
				}
			}
		}
		fill(required, &next, parity^1, best, count)
	}

	out := bufio.NewWriter(os.Stdout)
	for vertex := 0; vertex < n; vertex++ {
		answer := -1
		for parity := 0; parity < 2; parity++ {
			d := distance[2*vertex+parity]
			if d != -1 && required[d] != -1 && (answer == -1 || required[d] < answer) {
				answer = required[d]
			}
		}
		if vertex != 0 {
			fmt.Fprint(out, " ")
		}
		fmt.Fprint(out, answer)
	}
	fmt.Fprintln(out)
	out.Flush()
}
