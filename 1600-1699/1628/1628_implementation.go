package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var m, n, k int
	if _, err := fmt.Fscan(in, &m, &n, &k); err != nil {
		return
	}
	black := map[[2]int]bool{}
	rows, cols := make([][]int, m+2), make([][]int, n+2)
	for i := 0; i < k; i++ {
		var x, y int
		fmt.Fscan(in, &x, &y)
		black[[2]int{x, y}] = true
		rows[x] = append(rows[x], y)
		cols[y] = append(cols[y], x)
	}
	closed := func(x, y int) bool {
		return x < 1 || x > m || y < 1 || y > n || black[[2]int{x, y}]
	}
	count := 0
	// A white run of length 2 or more is a strip by itself; a single white
	// cell is one only if it is closed in the other direction too.
	for x := 1; x <= m; x++ {
		r := append(rows[x], n+1)
		sort.Ints(r)
		prev := 0
		for _, b := range r {
			length := b - prev - 1
			if length >= 2 || (length == 1 && closed(x-1, prev+1) && closed(x+1, prev+1)) {
				count++
			}
			prev = b
		}
	}
	for y := 1; y <= n; y++ {
		c := append(cols[y], m+1)
		sort.Ints(c)
		prev := 0
		for _, b := range c {
			if b-prev-1 >= 2 {
				count++
			}
			prev = b
		}
	}
	fmt.Println(count)
}
