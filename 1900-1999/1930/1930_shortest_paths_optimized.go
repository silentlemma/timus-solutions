package main

import (
	"fmt"
	"os"
)

func minimumChanges(adjacency [][]int, start, target int) int {
	stateCount := 2 * len(adjacency)
	distance := make([]int, stateCount)
	settled := make([]bool, stateCount)
	for i := range distance {
		distance[i] = stateCount
	}
	first := 2 * start
	distance[first], distance[first+1] = 0, 0
	front, back := []int{first, first + 1}, []int{}
	for len(front)+len(back) > 0 {
		if len(front) == 0 {
			// transfer deferred back entries only when the front stack is exhausted.
			for left, right := 0, len(back)-1; left < right; left, right = left+1, right-1 {
				back[left], back[right] = back[right], back[left]
			}
			front, back = back, front[:0]
		}
		state := front[len(front)-1]
		front = front[:len(front)-1]
		if settled[state] {
			continue
		}
		settled[state] = true
		city, gear := state/2, state&1
		if city == target {
			return distance[state]
		}
		for _, nextState := range adjacency[city] {
			cost := 0
			if nextState&1 != gear {
				cost = 1
			}
			candidate := distance[state] + cost
			if candidate < distance[nextState] {
				distance[nextState] = candidate
				if cost == 0 {
					front = append(front, nextState)
				} else {
					back = append(back, nextState)
				}
			}
		}
	}
	return -1
}

const inputBuffer = 4096

// refills bound storage even when whitespace or tokens cross a buffer boundary.
type reader struct {
	buffer   [inputBuffer]byte
	at, size int
}

func (r *reader) read() byte {
	if r.at == r.size {
		r.size, _ = os.Stdin.Read(r.buffer[:])
		r.at = 0
		if r.size == 0 {
			return 0
		}
	}
	c := r.buffer[r.at]
	r.at++
	return c
}
func (r *reader) next() int {
	c := r.read()
	for c != 0 && c != '-' && (c < '0' || c > '9') {
		c = r.read()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = r.read()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = r.read()
	}
	return sign * value
}

func main() {
	input := reader{}
	var count, roads int
	count, roads = input.next(), input.next()
	adjacency := make([][]int, count)
	for i := 0; i < roads; i++ {
		var lower, upper int
		lower, upper = input.next(), input.next()
		lower--
		upper--
		adjacency[lower] = append(adjacency[lower], 2*upper)
		adjacency[upper] = append(adjacency[upper], 2*lower+1)
	}
	var start, target int
	start, target = input.next(), input.next()
	fmt.Println(minimumChanges(adjacency, start-1, target-1))
}
