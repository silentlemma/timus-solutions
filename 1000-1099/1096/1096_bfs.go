package main

import (
	"bufio"
	"fmt"
	"os"
)

type state struct{ x, y, bus int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var k int
	fmt.Fscan(in, &k)
	route := make([]int, k)
	back := make([]int, k)
	byRoute := map[int][]int{}
	for j := 0; j < k; j++ {
		fmt.Fscan(in, &route[j], &back[j])
		byRoute[route[j]] = append(byRoute[route[j]], j)
	}
	var t, s1, s2 int
	fmt.Fscan(in, &t, &s1, &s2)
	// a state is the plate in hand: the first one, or the plate of bus j; a
	// driver swaps when the plate in hand shows the route of his bus
	came := make([]int, k)
	queue := []state{{s1, s2, -1}}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		for _, r := range []int{cur.x, cur.y} {
			buses := byRoute[r]
			delete(byRoute, r)
			for _, i := range buses {
				came[i] = cur.bus
				if route[i] == t || back[i] == t {
					var path []int
					for ; i >= 0; i = came[i] {
						path = append(path, i+1)
					}
					w := bufio.NewWriter(os.Stdout)
					defer w.Flush()
					fmt.Fprintln(w, len(path))
					for p := len(path) - 1; p >= 0; p-- {
						fmt.Fprintln(w, path[p])
					}
					return
				}
				queue = append(queue, state{route[i], back[i], i})
			}
		}
	}
	fmt.Println("IMPOSSIBLE")
}
