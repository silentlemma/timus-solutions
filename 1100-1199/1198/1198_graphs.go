package main

import (
	"bufio"
	"os"
	"strconv"
)

const buffer = 1 << 16

var reader = bufio.NewReaderSize(os.Stdin, buffer)

func readInt() int {
	c, err := reader.ReadByte()
	for err == nil && (c < '0' || c > '9') {
		c, err = reader.ReadByte()
	}
	v := 0
	for err == nil && c >= '0' && c <= '9' {
		v = v*10 + int(c-'0')
		c, err = reader.ReadByte()
	}
	return v
}

// search marks everything reachable from root that is not marked yet and
// returns how many vertices it marked.
func search(root int, start []int, edges []int32, seen []bool) int {
	queue := []int{root}
	seen[root] = true
	for head := 0; head < len(queue); head++ {
		u := queue[head]
		for _, v := range edges[start[u]:start[u+1]] {
			if !seen[v] {
				seen[v] = true
				queue = append(queue, int(v))
			}
		}
	}
	return len(queue)
}

func main() {
	n := readInt()
	start := make([]int, n+1)
	edges := []int32{}
	for i := 0; i < n; i++ {
		for v := readInt(); v != 0; v = readInt() {
			edges = append(edges, int32(v-1))
		}
		start[i+1] = len(edges)
	}
	// the reverse graph in the same compact form, built by counting
	rstart := make([]int, n+1)
	redges := make([]int32, len(edges))
	for _, v := range edges {
		rstart[v+1]++
	}
	for i := 0; i < n; i++ {
		rstart[i+1] += rstart[i]
	}
	fill := append([]int{}, rstart[:n]...)
	for u := 0; u < n; u++ {
		for _, v := range edges[start[u]:start[u+1]] {
			redges[fill[v]] = int32(u)
			fill[v]++
		}
	}

	// nobody outside the marked set can reach the root of the last search,
	// so that root lies in a strongly connected component with no way in
	seen := make([]bool, n)
	root := 0
	for u := 0; u < n; u++ {
		if !seen[u] {
			root = u
			search(u, start, edges, seen)
		}
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	if search(root, start, edges, make([]bool, n)) == n {
		backward := make([]bool, n)
		search(root, rstart, redges, backward)
		for u := 0; u < n; u++ {
			if backward[u] {
				out.WriteString(strconv.Itoa(u+1) + " ")
			}
		}
	}
	out.WriteString("0\n")
}
