package main

import (
	"bufio"
	"fmt"
	"os"
)

// read bytes through a refillable buffer without allocating numeric tokens.
var input = bufio.NewReader(os.Stdin)

func nextInt() int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c, err = input.ReadByte()
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = input.ReadByte()
	}
	return value * sign
}

func main() {
	n, m := nextInt(), nextInt()
	width := n + 1
	// costs are 1..10000; zero marks an absent edge in the compact matrix.
	cost := make([]uint16, width*width)
	indegree, best := make([]int, width), make([]int, width)
	for i := 0; i < m; i++ {
		a, b, c := nextInt(), nextInt(), nextInt()
		cost[a*width+b] = uint16(c)
		indegree[b]++
	}
	start, finish := nextInt(), nextInt()
	for i := range best {
		best[i] = -1
	}
	// at most 499 edges of cost 10000 keep every path sum within signed 32 bits.
	best[start] = 0
	order := make([]int, 0, n)
	for v := 1; v <= n; v++ {
		if indegree[v] == 0 {
			order = append(order, v)
		}
	}
	for at := 0; at < len(order); at++ {
		v := order[at]
		for w := 1; w <= n; w++ {
			c := int(cost[v*width+w])
			if c == 0 {
				continue
			}
			if best[v] >= 0 && best[v]+c > best[w] {
				best[w] = best[v] + c
			}
			indegree[w]--
			if indegree[w] == 0 {
				order = append(order, w)
			}
		}
	}
	if best[finish] < 0 {
		fmt.Println("No solution")
	} else {
		fmt.Println(best[finish])
	}
}
