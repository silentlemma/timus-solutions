package main

import (
	"bufio"
	"fmt"
	"os"
)

type call struct{ from, to int }

var (
	people   int
	adj      []int
	callerOf []int // callee of each caller already busy, or -1
)

func place(person, informed int, seen *int) bool {
	for caller := 0; caller < people; caller++ {
		if adj[person]>>caller&1 == 1 && informed>>caller&1 == 1 && *seen>>caller&1 == 0 {
			*seen |= 1 << caller
			if callerOf[caller] < 0 || place(callerOf[caller], informed, seen) {
				callerOf[caller] = person
				return true
			}
		}
	}
	return false
}

// who calls whom so that every person in fresh is called by a different
// informed neighbour; nil if that cannot be done
func calls(informed, fresh int) []call {
	callerOf = make([]int, people)
	for i := range callerOf {
		callerOf[i] = -1
	}
	for person := 0; person < people; person++ {
		seen := 0
		if fresh>>person&1 == 1 && !place(person, informed, &seen) {
			return nil
		}
	}
	var plan []call
	for caller, callee := range callerOf {
		if callee >= 0 {
			plan = append(plan, call{caller, callee})
		}
	}
	return plan
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, m int
	fmt.Fscan(in, &n, &m)
	index := map[string]int{}
	var names []string
	id := func(name string) int {
		if _, ok := index[name]; !ok {
			index[name] = len(names)
			names = append(names, name)
		}
		return index[name]
	}
	edges := make([]call, m)
	for i := range edges {
		var a, b string
		fmt.Fscan(in, &a, &b)
		ia := id(a)
		edges[i] = call{ia, id(b)}
	}
	var leader string
	fmt.Fscan(in, &leader)
	start := 1 << id(leader)
	people = len(names)
	adj = make([]int, people)
	for _, e := range edges {
		adj[e.from] |= 1 << e.to
		adj[e.to] |= 1 << e.from
	}
	full := 1<<people - 1
	// breadth-first search over the sets of people who know the news
	from := make([]int, full+1)
	for i := range from {
		from[i] = -1
	}
	how := make([][]call, full+1)
	queue := []int{start}
	from[start] = start
	for head := 0; head < len(queue) && from[full] < 0; head++ {
		informed, reach := queue[head], 0
		for p := 0; p < people; p++ {
			if informed>>p&1 == 1 {
				reach |= adj[p]
			}
		}
		reach &^= informed
		for fresh := reach; fresh > 0; fresh = (fresh - 1) & reach {
			next := informed | fresh
			if from[next] >= 0 {
				continue
			}
			if plan := calls(informed, fresh); plan != nil {
				from[next] = informed
				how[next] = plan
				queue = append(queue, next)
			}
		}
	}
	var path []int
	for state := full; state != start; state = from[state] {
		path = append(path, state)
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	fmt.Fprintln(out, len(path))
	for i := len(path) - 1; i >= 0; i-- {
		fmt.Fprintln(out, len(how[path[i]]))
		for _, c := range how[path[i]] {
			fmt.Fprintln(out, names[c.from], names[c.to])
		}
	}
}
