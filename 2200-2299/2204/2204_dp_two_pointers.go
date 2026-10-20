package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const options = 2

type interval struct {
	left  int
	right int
}

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

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	in := scanner{data: data}
	n, m := in.nextInt(), in.nextInt()
	exams := make([][options]interval, n)
	for i := range exams {
		for j := range exams[i] {
			exams[i][j] = interval{in.nextInt(), in.nextInt()}
		}
	}
	trips := make([]interval, m)
	for i := range trips {
		trips[i] = interval{in.nextInt(), in.nextInt()}
	}

	cost := [options]int{}
	last := [options]int{-1, -1}
	first, end := 0, 0
	for _, exam := range exams {
		var nextCost, nextLast [options]int
		for option, current := range exam {
			for first < m && trips[first].right < current.left {
				first++
			}
			for end < m && trips[end].left <= current.right {
				end++
			}
			count := end - first
			best := cost[0]
			// An already canceled trip can continue through the next exam.
			if count > 0 && last[0] == first {
				best--
			}
			other := cost[1]
			if count > 0 && last[1] == first {
				other--
			}
			if other < best {
				best = other
			}
			nextCost[option] = best + count
			nextLast[option] = -1
			if count > 0 {
				nextLast[option] = end - 1
			}
		}
		cost, last = nextCost, nextLast
	}
	best := cost[0]
	if cost[1] < best {
		best = cost[1]
	}
	out := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(out, m-best)
	out.Flush()
}
