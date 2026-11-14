package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

const (
	maxSpeed     = 300
	decimal      = 10
	tolerance    = 1e-9
	outputGuard  = 1e-8
	outputDigits = 12
)

type road struct{ a, b, speed, length int }
type link struct{ vertex, index int }
type state struct {
	vertex int
	cost   float64
}
type queue []state

func (q *queue) push(value state) {
	items := append(*q, value)
	pos := len(items) - 1
	for pos > 0 {
		parent := (pos - 1) / 2
		if items[parent].cost <= value.cost {
			break
		}
		items[pos] = items[parent]
		pos = parent
	}
	items[pos] = value
	*q = items
}

func (q *queue) pop() state {
	items := *q
	first, last := items[0], items[len(items)-1]
	items = items[:len(items)-1]
	if len(items) > 0 {
		pos := 0
		for child := 1; child < len(items); child = 2*pos + 1 {
			if child+1 < len(items) && items[child+1].cost < items[child].cost {
				child++
			}
			if last.cost <= items[child].cost {
				break
			}
			items[pos] = items[child]
			pos = child
		}
		items[pos] = last
	}
	*q = items
	return first
}

func solve(n int, roads []road, deadline float64) (float64, []int) {
	graph := make([][]link, n)
	costs := make([]float64, len(roads))
	slowest, fastest := maxSpeed, 1
	for i, r := range roads {
		graph[r.a] = append(graph[r.a], link{r.b, i})
		graph[r.b] = append(graph[r.b], link{r.a, i})
		if r.speed < slowest {
			slowest = r.speed
		}
		if r.speed > fastest {
			fastest = r.speed
		}
	}
	var inverse [maxSpeed + 1]float64
	best := make([]float64, n)
	parent := make([]int, n)
	pending := make(queue, 0, n)
	route := func(limit float64) float64 {
		for i := range best {
			best[i] = math.Inf(1)
		}
		best[0] = 0
		pending = append(pending[:0], state{0, 0})
		for len(pending) > 0 {
			node := pending.pop()
			if node.cost != best[node.vertex] {
				continue
			}
			if node.vertex == n-1 {
				return node.cost
			}
			for _, edge := range graph[node.vertex] {
				candidate := node.cost + costs[edge.index]
				if candidate <= limit && candidate < best[edge.vertex] {
					best[edge.vertex] = candidate
					parent[edge.vertex] = edge.index
					pending.push(state{edge.vertex, candidate})
				}
			}
		}
		return math.Inf(1)
	}
	travel := func(extra float64) bool {
		for speed := slowest; speed <= fastest; speed++ {
			inverse[speed] = 1 / (float64(speed) + extra)
		}
		for i, r := range roads {
			costs[i] = float64(r.length) * inverse[r.speed]
		}
		return route(deadline) <= deadline
	}

	allowance := outputGuard
	if !travel(0) {
		for i, r := range roads {
			costs[i] = float64(r.length)
		}
		// The shortest physical route bounds the required speed at both ends.
		speed := route(math.Inf(1)) / deadline
		low := math.Max(0, speed-float64(fastest))
		high := math.Max(low, speed-float64(slowest))
		for high-low > tolerance*math.Max(1, high) {
			middle := (low + high) / 2
			if travel(middle) {
				high = middle
			} else {
				low = middle
			}
		}
		allowance = high + outputGuard*math.Max(1, high)
		travel(allowance)
	}
	path := make([]int, 0)
	for vertex := n - 1; vertex != 0; {
		index := parent[vertex]
		path = append(path, index+1)
		vertex ^= roads[index].a ^ roads[index].b
	}
	return allowance, path
}

func number(input *bufio.Scanner) int {
	input.Scan()
	value := 0
	for _, c := range input.Bytes() {
		value = value*decimal + int(c-'0')
	}
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	n, m := number(input), number(input)
	roads := make([]road, m)
	for i := range roads {
		roads[i] = road{number(input) - 1, number(input) - 1, number(input), number(input)}
	}
	extra, path := solve(n, roads, float64(number(input)))
	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintf(output, "%.*f %d\n", outputDigits, extra, len(path))
	for i := len(path) - 1; i >= 0; i-- {
		if i < len(path)-1 {
			output.WriteByte(' ')
		}
		output.WriteString(strconv.Itoa(path[i]))
	}
	output.WriteByte('\n')
	output.Flush()
}
