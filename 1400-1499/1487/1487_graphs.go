package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	wordBits = 64
	buffer   = 1 << 20
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	var n int
	fmt.Fscan(reader, &n)
	winners := make([][]int, n)
	indegree := make([]int, n)
	for i := 0; i < n; i++ {
		var row string
		fmt.Fscan(reader, &row)
		for j := 0; j < n; j++ {
			if row[j] == '1' {
				winners[i] = append(winners[i], j)
				indegree[j]++
			}
		}
	}
	// stronger[v]: every team that is stronger than v, as a bit set; the
	// results are transitive, so the wins form an acyclic graph
	words := (n + wordBits - 1) / wordBits
	stronger := make([][]uint64, n)
	for v := range stronger {
		stronger[v] = make([]uint64, words)
	}
	var queue []int
	for v := 0; v < n; v++ {
		if indegree[v] == 0 {
			queue = append(queue, v)
		}
	}
	for h := 0; h < len(queue); h++ {
		v := queue[h]
		for _, u := range winners[v] {
			for w := 0; w < words; w++ {
				stronger[u][w] |= stronger[v][w]
			}
			stronger[u][v/wordBits] |= 1 << uint(v%wordBits)
			indegree[u]--
			if indegree[u] == 0 {
				queue = append(queue, u)
			}
		}
	}
	// A plays better than B when no team stronger than B is stronger than A
	var q int
	fmt.Fscan(reader, &q)
	for ; q > 0; q-- {
		var a, b int
		fmt.Fscan(reader, &a, &b)
		common := false
		for w := 0; w < words && !common; w++ {
			common = stronger[a-1][w]&stronger[b-1][w] != 0
		}
		if common {
			fmt.Fprintln(writer, "No")
		} else {
			fmt.Fprintln(writer, "YES")
		}
	}
}
