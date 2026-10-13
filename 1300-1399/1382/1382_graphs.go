package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type key struct{ kind, value int }

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	// variable i is true when friend i's first statement is the true one,
	// and literal 2 v means v while 2 v + 1 means not v
	groups := map[key][]int{} // claims about one person or one card: at most one holds
	var order []key
	add := func(k key, lit int) {
		if _, ok := groups[k]; !ok {
			order = append(order, k)
		}
		groups[k] = append(groups[k], lit)
	}
	for i := 0; i < n; i++ {
		var a, b, c int
		fmt.Fscan(in, &a, &b, &c)
		add(key{0, i + 1}, 2*i)
		add(key{1, a}, 2*i)
		add(key{0, b}, 2*i+1)
		add(key{1, c}, 2*i+1)
	}
	count := n
	var clauses [][2]int // one of the two literals must hold
	for _, k := range order {
		// at most one: helper s_j means some of the first j members holds
		prev := -1
		for _, lit := range groups[k] {
			s := count
			count++
			clauses = append(clauses, [2]int{lit ^ 1, 2 * s})
			if prev >= 0 {
				clauses = append(clauses, [2]int{2*prev + 1, 2 * s}, [2]int{2*prev + 1, lit ^ 1})
			}
			prev = s
		}
	}
	m := 2 * count
	graph := make([][]int, m)
	for _, cl := range clauses {
		graph[cl[0]^1] = append(graph[cl[0]^1], cl[1])
		graph[cl[1]^1] = append(graph[cl[1]^1], cl[0])
	}
	// Tarjan's components, numbered from the sinks up
	index, low, comp := make([]int, m), make([]int, m), make([]int, m)
	for i := range index {
		index[i] = -1
	}
	onStack := make([]bool, m)
	var stack []int
	counter, comps := 0, 0
	for root := 0; root < m; root++ {
		if index[root] >= 0 {
			continue
		}
		work := [][2]int{{root, 0}}
		for len(work) > 0 {
			v, k := work[len(work)-1][0], work[len(work)-1][1]
			work = work[:len(work)-1]
			if k == 0 {
				index[v], low[v] = counter, counter
				counter++
				stack = append(stack, v)
				onStack[v] = true
			} else if low[graph[v][k-1]] < low[v] {
				low[v] = low[graph[v][k-1]]
			}
			descended := false
			for k < len(graph[v]) {
				u := graph[v][k]
				k++
				if index[u] < 0 {
					work = append(work, [2]int{v, k}, [2]int{u, 0})
					descended = true
					break
				}
				if onStack[u] && index[u] < low[v] {
					low[v] = index[u]
				}
			}
			if !descended && low[v] == index[v] {
				for {
					u := stack[len(stack)-1]
					stack = stack[:len(stack)-1]
					onStack[u] = false
					comp[u] = comps
					if u == v {
						break
					}
				}
				comps++
			}
		}
	}
	// a literal holds when its component comes before its negation's
	out := make([]string, n)
	for i := range out {
		out[i] = "2"
		if comp[2*i] < comp[2*i+1] {
			out[i] = "1"
		}
	}
	fmt.Println(strings.Join(out, " "))
}
