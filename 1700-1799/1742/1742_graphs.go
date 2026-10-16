package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	fresh = iota
	walking
	done
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	to := make([]int, n+1)
	incoming := make([]int, n+1)
	for v := 1; v <= n; v++ {
		fmt.Fscan(in, &to[v])
		incoming[to[v]]++
	}
	// follow the arrows from every new programmer to find the cycles
	state := make([]int, n+1)
	var path []int
	cycles, onCycles, bare := 0, 0, 0
	for start := 1; start <= n; start++ {
		path = path[:0]
		v := start
		for state[v] == fresh {
			state[v] = walking
			path = append(path, v)
			v = to[v]
		}
		if state[v] == walking {
			cycles++
			// a cycle nobody else points into needs a group of its own
			alone := true
			for u := v; ; {
				onCycles++
				if incoming[u] != 1 {
					alone = false
				}
				if u = to[u]; u == v {
					break
				}
			}
			if alone {
				bare++
			}
		}
		for _, u := range path {
			state[u] = done
		}
	}
	// fewest: every programmer nobody names starts a group, and so does
	// every bare cycle; most: a cycle goes into one group as soon as a
	// group enters it, and everyone else can stand alone
	starts := 0
	for v := 1; v <= n; v++ {
		if incoming[v] == 0 {
			starts++
		}
	}
	fmt.Println(starts+bare, n-onCycles+cycles)
}
