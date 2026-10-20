package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

const triangleSize = 3

type reader struct {
	data []byte
	pos  int
}

func (r *reader) nextInt() int {
	for r.pos < len(r.data) && r.data[r.pos] <= ' ' {
		r.pos++
	}
	value := 0
	for r.pos < len(r.data) && r.data[r.pos] >= '0' && r.data[r.pos] <= '9' {
		value = value*10 + int(r.data[r.pos]-'0')
		r.pos++
	}
	return value
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := reader{data: data}
	n := input.nextInt()
	adj := make([][]bool, n)
	for u := range adj {
		adj[u] = make([]bool, n)
		for v := range adj[u] {
			adj[u][v] = input.nextInt() == 1
		}
	}

	used := make([]bool, n)
	pairs := make([][2]int, 0, n/2)
	for u := 0; u < n; u++ {
		if used[u] {
			continue
		}
		for v := 0; v < n; v++ {
			if !used[v] && adj[u][v] {
				used[u], used[v] = true, true
				pairs = append(pairs, [2]int{u, v})
				break
			}
		}
	}

	unmatched := make([]int, 0)
	for u := 0; u < n; u++ {
		if !used[u] {
			unmatched = append(unmatched, u)
		}
	}
	for i := 0; i+1 < len(unmatched); i += 2 {
		u, v := unmatched[i], unmatched[i+1]
		// Two unmatched vertices always admit an augmentation through one pair.
		for j, pair := range pairs {
			a, b := pair[0], pair[1]
			if adj[u][a] && adj[v][b] {
				pairs[j] = [2]int{u, a}
				pairs = append(pairs, [2]int{v, b})
				break
			}
			if adj[u][b] && adj[v][a] {
				pairs[j] = [2]int{u, b}
				pairs = append(pairs, [2]int{v, a})
				break
			}
		}
	}

	triangle := -1
	extra := -1
	if len(unmatched)%2 == 1 {
		extra = unmatched[len(unmatched)-1]
		for i, pair := range pairs {
			if adj[extra][pair[0]] && adj[extra][pair[1]] {
				triangle = i
				break
			}
		}
	}

	output := bufio.NewWriter(os.Stdout)
	fmt.Fprintln(output, "YES")
	fmt.Fprintln(output, len(pairs))
	for i, pair := range pairs {
		if i == triangle {
			fmt.Fprintln(output, triangleSize, pair[0]+1, pair[1]+1, extra+1)
		} else {
			fmt.Fprintln(output, 2, pair[0]+1, pair[1]+1)
		}
	}
	output.Flush()
}
