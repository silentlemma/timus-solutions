package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type end struct{ room, pos int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	rows := make([][]int, n)
	for u := range rows {
		var k int
		fmt.Fscan(in, &k)
		rows[u] = make([]int, k)
		for i := range rows[u] {
			fmt.Fscan(in, &rows[u][i])
			rows[u][i]--
		}
	}
	// pair the k-th mention of v in room u with the k-th mention of u in room
	// v; a door to the room itself is mentioned twice in its own row
	var ends [][2]end
	waiting := map[[2]int][]int{}
	for u := 0; u < n; u++ {
		for i, v := range rows[u] {
			key := [2]int{u, v}
			if v < u {
				key = [2]int{v, u}
			}
			if q := waiting[key]; len(q) > 0 {
				ends[q[0]][1] = end{u, i}
				waiting[key] = q[1:]
			} else {
				waiting[key] = append(q, len(ends))
				ends = append(ends, [2]end{{u, i}, {-1, -1}})
			}
		}
	}
	// a dummy room joined to every room of odd degree makes all degrees even
	dummy, edges := n, len(ends)
	adj := make([][][2]int, n+1)
	for e, pair := range ends {
		u, v := pair[0].room, pair[1].room
		adj[u] = append(adj[u], [2]int{v, e})
		adj[v] = append(adj[v], [2]int{u, e})
	}
	for u := 0; u < n; u++ {
		if len(adj[u])%2 == 1 {
			adj[u] = append(adj[u], [2]int{dummy, edges})
			adj[dummy] = append(adj[dummy], [2]int{u, edges})
			edges++
		}
	}
	// walk Euler circuits and orient each door along the walk
	used := make([]bool, edges)
	tail := make([]int, edges)
	ptr := make([]int, n+1)
	for start := 0; start <= n; start++ {
		stack := []int{start}
		for len(stack) > 0 {
			u := stack[len(stack)-1]
			for ptr[u] < len(adj[u]) && used[adj[u][ptr[u]][1]] {
				ptr[u]++
			}
			if ptr[u] == len(adj[u]) {
				stack = stack[:len(stack)-1]
				continue
			}
			v, e := adj[u][ptr[u]][0], adj[u][ptr[u]][1]
			used[e] = true
			tail[e] = u
			stack = append(stack, v)
		}
	}
	colours := make([][]string, n)
	for u := range colours {
		colours[u] = make([]string, len(rows[u]))
	}
	for e, pair := range ends {
		a, b := pair[0], pair[1]
		// green on the side the walk leaves from, orange where it enters
		if tail[e] == a.room {
			colours[a.room][a.pos], colours[b.room][b.pos] = "G", "Y"
		} else {
			colours[a.room][a.pos], colours[b.room][b.pos] = "Y", "G"
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for u := 0; u < n; u++ {
		out.WriteString(strings.Join(colours[u], " ") + "\n")
	}
}
