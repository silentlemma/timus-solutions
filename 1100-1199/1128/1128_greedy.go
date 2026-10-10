package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	enemies := make([][]int, n)
	for v := range enemies {
		var k int
		fmt.Fscan(in, &k)
		enemies[v] = make([]int, k)
		for i := range enemies[v] {
			fmt.Fscan(in, &enemies[v][i])
			enemies[v][i]--
		}
	}
	side := make([]int, n)
	work := make([]int, n)
	for v := range work {
		work[v] = v
	}
	// a child with two or more enemies on its side has at most one on the
	// other, so moving it removes at least one pair of enemies sharing a
	// group; the moves stop after at most as many steps as there are pairs
	for len(work) > 0 {
		v := work[len(work)-1]
		work = work[:len(work)-1]
		same := 0
		for _, u := range enemies[v] {
			if side[u] == side[v] {
				same++
			}
		}
		if same >= 2 {
			side[v] ^= 1
			work = append(work, enemies[v]...)
			work = append(work, v)
		}
	}
	var group, other []string
	for v := 0; v < n; v++ {
		if side[v] == side[0] {
			group = append(group, strconv.Itoa(v+1))
		} else {
			other = append(other, strconv.Itoa(v+1))
		}
	}
	small := group
	if len(other) < len(group) {
		small = other
	}
	fmt.Println(len(small))
	fmt.Println(strings.Join(small, " "))
}
