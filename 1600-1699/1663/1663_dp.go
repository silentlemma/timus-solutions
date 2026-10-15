package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const toll = 1000

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	people := make([]int, n)
	for i := range people {
		fmt.Fscan(in, &people[i])
	}
	if n == 2 {
		fmt.Println("1 2")
		return
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.SliceStable(order, func(a, b int) bool { return people[order[a]] < people[order[b]] })
	p, q := make([]int64, n), make([]int64, n)
	for i, t := range order {
		p[i] = int64(people[t])
		q[i] = toll / p[i]
	}
	// towns sorted by size: the best tour climbs to the last town on one path
	// and comes back on the other; up[j] costs a climb ending at the newest
	// town and a return ending at town j, down[j] the other way round
	up, down := []int64{q[0] * p[1]}, []int64{q[1] * p[0]}
	var shiftUp, shiftDown int64
	fromDown, fromUp := []int{0, 0}, []int{0, 0}
	for m := 1; m < n-2; m++ {
		nxt, bestUp, bestDown := m+1, 0, 0
		for j := 1; j < m; j++ {
			if down[j]+q[j]*p[nxt] < down[bestUp]+q[bestUp]*p[nxt] {
				bestUp = j
			}
			if up[j]+q[nxt]*p[j] < up[bestDown]+q[nxt]*p[bestDown] {
				bestDown = j
			}
		}
		newUp := down[bestUp] + shiftDown + q[bestUp]*p[nxt]
		newDown := up[bestDown] + shiftUp + q[nxt]*p[bestDown]
		shiftUp += q[m] * p[nxt]
		shiftDown += q[nxt] * p[m]
		up = append(up, newUp-shiftUp)
		down = append(down, newDown-shiftDown)
		fromDown = append(fromDown, bestUp)
		fromUp = append(fromUp, bestDown)
	}
	last, m := n-1, n-2
	climbing, j, best := true, 0, int64(-1)
	for k := 0; k < m; k++ {
		closeUp := up[k] + shiftUp + q[m]*p[last] + q[last]*p[k]
		closeDown := down[k] + shiftDown + q[k]*p[last] + q[last]*p[m]
		if best < 0 || closeUp < best {
			best, climbing, j = closeUp, true, k
		}
		if closeDown < best {
			best, climbing, j = closeDown, false, k
		}
	}
	// walk back: town m is on the climbing path or not, the other path ends at j
	onUp := make([]bool, n)
	for ; m >= 1; m-- {
		onUp[m] = climbing
		if j == m-1 {
			if climbing {
				j = fromDown[m]
			} else {
				j = fromUp[m]
			}
			climbing = !climbing
		}
	}
	tour := []int{0}
	for k := 1; k < n-1; k++ {
		if onUp[k] {
			tour = append(tour, k)
		}
	}
	tour = append(tour, n-1)
	for k := n - 2; k >= 1; k-- {
		if !onUp[k] {
			tour = append(tour, k)
		}
	}
	start := 0
	for i := range tour {
		tour[i] = order[tour[i]]
		if tour[i] == 0 {
			start = i
		}
	}
	words := make([]string, n)
	for i := range words {
		words[i] = strconv.Itoa(tour[(start+i)%n] + 1)
	}
	fmt.Println(strings.Join(words, " "))
}
