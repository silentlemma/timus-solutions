package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"sort"
)

type point struct {
	x, y int64
	id   int
}

type reader struct {
	data []byte
	pos  int
}

func (r *reader) integer() int64 {
	for r.pos < len(r.data) && r.data[r.pos] <= ' ' {
		r.pos++
	}
	sign := int64(1)
	if r.data[r.pos] == '-' {
		sign = -1
		r.pos++
	}
	value := int64(0)
	for r.pos < len(r.data) && r.data[r.pos] >= '0' && r.data[r.pos] <= '9' {
		value = value*10 + int64(r.data[r.pos]-'0')
		r.pos++
	}
	return value * sign
}

func chainSizes(p []point, left, right, order, size []int, turn int64) []int {
	n := len(p)
	head, tail, count := make([]int, n+1), make([]int, n+1), make([]int, n+1)
	previous, following := make([]int, n), make([]int, n)
	for i := range head {
		head[i], tail[i] = n, n
	}
	for i := range previous {
		previous[i], following[i] = n, n
	}
	for k := len(order) - 1; k >= 0; k-- {
		v := order[k]
		a, b := left[v], right[v]
		forward := size[a] >= size[b]
		base, small := a, b
		back, ahead := previous, following
		sign := turn
		if !forward {
			base, small = b, a
			back, ahead = following, previous
			sign = -turn
		}
		start, end, other := head[base], tail[base], head[small]
		if !forward {
			start, end, other = tail[base], head[base], tail[small]
		}
		length := count[base]
		// Reuse the larger subtree's chain and insert from its nearer end.
		for c := v; c != n; {
			next := other
			if c != v {
				next = ahead[c]
			}
			for length >= 2 {
				a = back[end]
				cross := (p[end].x-p[a].x)*(p[c].y-p[a].y) -
					(p[end].y-p[a].y)*(p[c].x-p[a].x)
				if cross*sign > 0 {
					break
				}
				end = a
				length--
			}
			if length != 0 {
				ahead[end] = c
			} else {
				start = c
			}
			back[c], ahead[c] = end, n
			end = c
			length++
			c = next
		}
		head[v], tail[v] = start, end
		if !forward {
			head[v], tail[v] = end, start
		}
		count[v] = length
	}
	return count
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	r := reader{data: data}
	n := int(r.integer())
	p := make([]point, n)
	for i := range p {
		p[i] = point{r.integer(), r.integer(), i}
	}
	sort.Slice(p, func(i, j int) bool { return p[i].x < p[j].x })
	left, right := make([]int, n), make([]int, n)
	stack := make([]int, 0, n)
	for v := range p {
		last := n
		for len(stack) != 0 && p[stack[len(stack)-1]].y < p[v].y {
			last = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		left[v], right[v] = last, n
		if len(stack) != 0 {
			right[stack[len(stack)-1]] = v
		}
		stack = append(stack, v)
	}
	root := stack[0]
	stack = append(stack[:0], root)
	order := make([]int, 0, n)
	for len(stack) != 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, v)
		if left[v] != n {
			stack = append(stack, left[v])
		}
		if right[v] != n {
			stack = append(stack, right[v])
		}
	}
	size := make([]int, n+1)
	for k := len(order) - 1; k >= 0; k-- {
		v := order[k]
		size[v] = size[left[v]] + size[right[v]] + 1
	}
	lower := chainSizes(p, left, right, order, size, 1)
	upper := chainSizes(p, left, right, order, size, -1)
	answer := make([]int, n)
	for v := range p {
		value := lower[v] + upper[v] - 2
		if value < 1 {
			value = 1
		}
		answer[p[v].id] = value
	}
	out := bufio.NewWriter(os.Stdout)
	for _, value := range answer {
		fmt.Fprintln(out, value)
	}
	out.Flush()
}
