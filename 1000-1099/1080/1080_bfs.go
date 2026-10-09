package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	adj := make([][]int, n+1)
	for i := 1; i <= n; i++ {
		for {
			var v int
			fmt.Fscan(in, &v)
			if v == 0 {
				break
			}
			adj[i] = append(adj[i], v)
			adj[v] = append(adj[v], i)
		}
	}
	// the map is connected, so the colour of the first country decides all
	color := make([]int, n+1)
	for i := range color {
		color[i] = -1
	}
	color[1] = 0
	queue := []int{1}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		for _, v := range adj[u] {
			if color[v] < 0 {
				color[v] = 1 - color[u]
				queue = append(queue, v)
			} else if color[v] == color[u] {
				fmt.Println(-1)
				return
			}
		}
	}
	var out strings.Builder
	for i := 1; i <= n; i++ {
		out.WriteString(fmt.Sprint(color[i]))
	}
	fmt.Println(out.String())
}
