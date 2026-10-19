package main

import (
	"bufio"
	"fmt"
	"os"
)

func complete(n, k int, next []int) bool {
	indegree := make([]int, n+1)
	for vertex := 1; vertex <= n; vertex++ {
		if next[vertex] != 0 {
			indegree[next[vertex]]++
			if indegree[next[vertex]] > 1 {
				return false
			}
		}
	}

	visited := make([]bool, n+1)
	buckets := make([][][]int, n+1)
	for start := 1; start <= n; start++ {
		if indegree[start] != 0 {
			continue
		}
		path := make([]int, 0)
		for vertex := start; vertex != 0; vertex = next[vertex] {
			visited[vertex] = true
			path = append(path, vertex)
		}
		buckets[len(path)] = append(buckets[len(path)], path)
	}
	for start := 1; start <= n; start++ {
		if visited[start] {
			continue
		}
		length := 0
		for vertex := start; !visited[vertex]; vertex = next[vertex] {
			visited[vertex] = true
			length++
		}
		if k%length != 0 {
			return false
		}
	}

	lengths := make([]int, 0)
	radices := make([]int, 0)
	states := 1
	for length := 1; length <= n; length++ {
		if len(buckets[length]) != 0 {
			lengths = append(lengths, length)
			radices = append(radices, len(buckets[length])+1)
			states *= len(buckets[length]) + 1
		}
	}

	// A mixed-radix state records how many paths of every length are used.
	digits := make([][]int, states)
	groups := make([]int, 0)
	for state := 0; state < states; state++ {
		digits[state] = make([]int, len(lengths))
		value, weight := state, 0
		for kind, length := range lengths {
			digits[state][kind] = value % radices[kind]
			value /= radices[kind]
			weight += digits[state][kind] * length
		}
		if weight != 0 && k%weight == 0 {
			groups = append(groups, state)
		}
	}

	possible := make([]bool, states)
	choice := make([]int, states)
	possible[0] = true
	for state := 1; state < states; state++ {
		anchor := len(lengths) - 1
		for digits[state][anchor] == 0 {
			anchor--
		}
		for _, group := range groups {
			if group > state {
				break
			}
			if digits[group][anchor] == 0 || !possible[state-group] {
				continue
			}
			fits := true
			for kind := range lengths {
				if digits[group][kind] > digits[state][kind] {
					fits = false
					break
				}
			}
			if fits {
				possible[state] = true
				choice[state] = group
				break
			}
		}
	}
	if !possible[states-1] {
		return false
	}

	for state := states - 1; state != 0; {
		group := choice[state]
		paths := make([][]int, 0)
		for kind, length := range lengths {
			for count := 0; count < digits[group][kind]; count++ {
				last := len(buckets[length]) - 1
				paths = append(paths, buckets[length][last])
				buckets[length] = buckets[length][:last]
			}
		}
		for index, path := range paths {
			next[path[len(path)-1]] = paths[(index+1)%len(paths)][0]
		}
		state -= group
	}
	return true
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var n, k int
	if _, err := fmt.Fscan(input, &n, &k); err != nil {
		return
	}
	next := make([]int, n+1)
	for vertex := 1; vertex <= n; vertex++ {
		fmt.Fscan(input, &next[vertex])
	}
	if !complete(n, k, next) {
		fmt.Fprintln(output, "No")
		return
	}
	fmt.Fprintln(output, "Yes")
	for vertex := 1; vertex <= n; vertex++ {
		if vertex != 1 {
			fmt.Fprint(output, " ")
		}
		fmt.Fprint(output, next[vertex])
	}
	fmt.Fprintln(output)
}
