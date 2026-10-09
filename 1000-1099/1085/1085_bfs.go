package main

import (
	"bufio"
	"fmt"
	"os"
)

const ticket = 4

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	routes := make([][]int, m)
	routesAt := make([][]int, n+1)
	for r := range routes {
		var size int
		fmt.Fscan(in, &size)
		routes[r] = make([]int, size)
		for i := range routes[r] {
			fmt.Fscan(in, &routes[r][i])
			routesAt[routes[r][i]] = append(routesAt[routes[r][i]], r)
		}
	}
	var k int
	fmt.Fscan(in, &k)
	total := make([]int, n+1)
	ok := make([]bool, n+1)
	for t := range ok {
		ok[t] = true
	}
	for f := 0; f < k; f++ {
		var money, start, card int
		fmt.Fscan(in, &money, &start, &card)
		// fewest rides from the start to every stop; a ride covers a whole route
		rides := make([]int, n+1)
		for i := range rides {
			rides[i] = -1
		}
		used := make([]bool, m)
		rides[start] = 0
		queue := []int{start}
		for len(queue) > 0 {
			u := queue[0]
			queue = queue[1:]
			for _, r := range routesAt[u] {
				if used[r] {
					continue
				}
				used[r] = true
				for _, v := range routes[r] {
					if rides[v] < 0 {
						rides[v] = rides[u] + 1
						queue = append(queue, v)
					}
				}
			}
		}
		for t := 1; t <= n; t++ {
			cost := ticket * rides[t]
			if card == 1 {
				cost = 0
			}
			if rides[t] < 0 || cost > money {
				ok[t] = false
			} else {
				total[t] += cost
			}
		}
	}
	stop := 0
	for t := 1; t <= n; t++ {
		if ok[t] && (stop == 0 || total[t] < total[stop]) {
			stop = t
		}
	}
	if stop == 0 {
		fmt.Println(0)
	} else {
		fmt.Println(stop, total[stop])
	}
}
