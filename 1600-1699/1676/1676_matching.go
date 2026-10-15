package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const bufSize = 1 << 20

var (
	n, m         int
	beats        [][]byte // beats[i][j] == '1' when fighter j beats monster i
	owner, match []int
	seen         []bool
)

// augment is Kuhn's augmenting search from monster u.
func augment(u int) bool {
	for j := 0; j < m; j++ {
		if beats[u][j] == '1' && !seen[j] {
			seen[j] = true
			if owner[j] < 0 || augment(owner[j]) {
				owner[j], match[u] = u, j
				return true
			}
		}
	}
	return false
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufSize)
	out := bufio.NewWriterSize(os.Stdout, bufSize)
	defer out.Flush()
	fmt.Fscan(in, &n, &m)
	var cells strings.Builder
	for cells.Len() < n*m {
		var word string
		if _, err := fmt.Fscan(in, &word); err != nil {
			break
		}
		cells.WriteString(word)
	}
	all := cells.String()
	beats = make([][]byte, n)
	for i := range beats {
		beats[i] = []byte(all[i*m : (i+1)*m])
	}
	owner, match = make([]int, m), make([]int, n)
	for j := range owner {
		owner[j] = -1
	}
	for i := 0; i < n; i++ {
		seen = make([]bool, m)
		if !augment(i) {
			// some monster cannot be beaten in any assignment
			row := strings.Repeat("1", m) + "\n"
			out.WriteString(strings.Repeat(row, n))
			return
		}
	}
	// i may take fighter j if j is free or its own, or if j's monster k moves on:
	// with k -> k2 when k can take k2's fighter, k reaches i (closing a cycle)
	// or reaches a monster (k included) that some free fighter beats
	next := make([][]int, n)
	loose := make([]bool, n)
	for k := 0; k < n; k++ {
		for j := 0; j < m; j++ {
			if beats[k][j] == '1' {
				if owner[j] < 0 {
					loose[k] = true
				} else if owner[j] != k {
					next[k] = append(next[k], owner[j])
				}
			}
		}
	}
	reach := make([][]bool, n)
	helped := make([]bool, n)
	for k := 0; k < n; k++ {
		reach[k] = make([]bool, n)
		queue := []int{k}
		for h := 0; h < len(queue); h++ {
			for _, k2 := range next[queue[h]] {
				if !reach[k][k2] {
					reach[k][k2] = true
					queue = append(queue, k2)
				}
			}
		}
		helped[k] = loose[k]
		for x := 0; x < n; x++ {
			helped[k] = helped[k] || reach[k][x] && loose[x]
		}
	}
	row := make([]byte, m+1)
	row[m] = '\n'
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			ok := beats[i][j] == '1' &&
				(owner[j] < 0 || match[i] == j || helped[owner[j]] || reach[owner[j]][i])
			row[j] = '1'
			if ok {
				row[j] = '0'
			}
		}
		out.Write(row)
	}
}
