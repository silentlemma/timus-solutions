package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type link struct{ to, joy int }

// a route value through a child, and that child
type option struct{ value, child int }

func (a option) better(b option) bool {
	return a.value > b.value || (a.value == b.value && a.child > b.child)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var n, k int
	fmt.Fscan(reader, &n, &k)
	joy := make([]int, n+1)
	for i := 1; i <= n; i++ {
		fmt.Fscan(reader, &joy[i])
	}
	adj := make([][]link, n+1)
	for i := 0; i < k; i++ {
		var a, b, c int
		fmt.Fscan(reader, &a, &b, &c)
		adj[a] = append(adj[a], link{b, c})
		adj[b] = append(adj[b], link{a, c})
	}
	// down[v]: the best route that starts at v and goes away from its parent,
	// nxt[v] the next city on it; the routes are in a forest, so each tree once
	down := append([]int{}, joy...)
	nxt := make([]int, n+1)
	parent := make([]int, n+1)
	for i := range parent {
		parent[i] = -1
	}
	best, center, endA, endB := -1, 0, 0, 0
	for root := 1; root <= n; root++ {
		if parent[root] != -1 {
			continue
		}
		parent[root] = 0
		var order []int
		stack := []int{root}
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			order = append(order, v)
			for _, l := range adj[v] {
				if parent[l.to] == -1 {
					parent[l.to] = v
					stack = append(stack, l.to)
				}
			}
		}
		for i := len(order) - 1; i >= 0; i-- {
			v := order[i]
			var first, second option
			for _, l := range adj[v] {
				if l.to != parent[v] {
					o := option{l.joy + down[l.to], l.to}
					if o.better(first) {
						first, second = o, first
					} else if o.better(second) {
						second = o
					}
				}
			}
			down[v], nxt[v] = joy[v]+first.value, first.child
			if joy[v]+first.value+second.value > best {
				best = joy[v] + first.value + second.value
				center, endA, endB = v, first.child, second.child
			}
		}
	}
	var left, right []int
	for a := endA; a != 0; a = nxt[a] {
		left = append(left, a)
	}
	for b := endB; b != 0; b = nxt[b] {
		right = append(right, b)
	}
	route := make([]string, 0, len(left)+len(right)+1)
	for i := len(left) - 1; i >= 0; i-- {
		route = append(route, strconv.Itoa(left[i]))
	}
	route = append(route, strconv.Itoa(center))
	for _, b := range right {
		route = append(route, strconv.Itoa(b))
	}
	fmt.Println(best)
	fmt.Println(len(route))
	fmt.Println(strings.Join(route, " "))
}
