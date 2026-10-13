package main

import (
	"bufio"
	"os"
	"strconv"
)

const buffer = 1 << 20 // long lines of stops

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, buffer), buffer)
	in.Split(bufio.ScanWords)
	next := func() int {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return v
	}
	n, m := next(), next()
	routes := make([][]int, n)
	onStop := make([][]int, m+1)
	for r := 0; r < n; r++ {
		k := next()
		routes[r] = make([]int, k)
		for i := range routes[r] {
			routes[r][i] = next()
			onStop[routes[r][i]] = append(onStop[routes[r][i]], r)
		}
	}
	a, b := next(), next()
	// one ride along a route reaches any of its stops, both ways; layers of rides
	rides, cameBy, boarded := make([]int, m+1), make([]int, m+1), make([]int, n)
	for i := range rides {
		rides[i], cameBy[i] = -1, -1
	}
	for i := range boarded {
		boarded[i] = -1
	}
	rides[a] = 0
	queue := []int{a}
	for head := 0; head < len(queue) && rides[b] < 0; head++ {
		st := queue[head]
		for _, r := range onStop[st] {
			if boarded[r] >= 0 {
				continue
			}
			boarded[r] = st // the stop where the route was first taken
			for _, nxt := range routes[r] {
				if rides[nxt] < 0 {
					rides[nxt] = rides[st] + 1
					cameBy[nxt] = r
					queue = append(queue, nxt)
				}
			}
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if rides[b] < 0 {
		out.WriteString("-1\n")
		return
	}
	path := []int{b}
	for path[len(path)-1] != a {
		path = append(path, boarded[cameBy[path[len(path)-1]]])
	}
	out.WriteString(strconv.Itoa(rides[b]) + "\n")
	for i := len(path) - 1; i >= 0; i-- {
		out.WriteString(strconv.Itoa(path[i]))
		if i > 0 {
			out.WriteByte(' ')
		}
	}
	out.WriteByte('\n')
}
