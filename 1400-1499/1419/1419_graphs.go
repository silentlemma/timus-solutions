package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const degree = 3

type link struct{ to, id int }

type frame struct{ v, via, k int }

func realMap(w, h int, lines [][]byte) bool {
	adj := make([][]link, w*h)
	edges := 0
	for r, line := range lines {
		for c, ch := range line {
			if (r%2 == 0 && c%2 == 0) || ch == ' ' {
				continue
			}
			// the symbol must fit its gap: - between columns, | between rows, \ or / across
			var dr, dc int
			switch {
			case r%2 == 0 && ch == '-':
				dr, dc = 0, 1
			case c%2 == 0 && ch == '|':
				dr, dc = 1, 0
			case r%2 == 1 && c%2 == 1 && ch == '\\':
				dr, dc = 1, 1
			case r%2 == 1 && c%2 == 1 && ch == '/':
				dr, dc = 1, -1
			default:
				return false
			}
			a := (r-dr)/2*w + (c-dc)/2
			b := a + dr*w + dc
			adj[a] = append(adj[a], link{b, edges})
			adj[b] = append(adj[b], link{a, edges})
			edges++
		}
	}
	for _, v := range adj {
		if len(v) != degree {
			return false
		}
	}
	// iterative low-link search: a tree edge to v is a bridge if low[v] > tin[parent]
	tin, low := make([]int, w*h), make([]int, w*h)
	for i := range tin {
		tin[i] = -1
	}
	tin[0] = 0
	timer := 0
	stack := []frame{{0, -1, 0}}
	for len(stack) > 0 {
		f := &stack[len(stack)-1]
		v := f.v
		if f.k < len(adj[v]) {
			l := adj[v][f.k]
			f.k++
			if l.id == f.via {
				continue
			}
			if tin[l.to] < 0 {
				timer++
				tin[l.to], low[l.to] = timer, timer
				stack = append(stack, frame{l.to, l.id, 0})
			} else if tin[l.to] < low[v] {
				low[v] = tin[l.to]
			}
			continue
		}
		stack = stack[:len(stack)-1]
		if len(stack) > 0 {
			p := stack[len(stack)-1].v
			if low[v] < low[p] {
				low[p] = low[v]
			}
			if low[v] > tin[p] {
				return false
			}
		}
	}
	for _, t := range tin {
		if t < 0 {
			return false
		}
	}
	return true
}

func main() {
	in := bufio.NewReader(os.Stdin)
	first, _ := in.ReadString('\n')
	var m, n int
	fmt.Sscan(first, &m, &n)
	picture := make([][]byte, n)
	for r := range picture {
		line, _ := in.ReadString('\n')
		line = strings.TrimRight(line, "\r\n")
		row := []byte(strings.Repeat(" ", m))
		copy(row, line)
		picture[r] = row
	}
	if realMap((m+1)/2, (n+1)/2, picture) {
		fmt.Println("Island world")
	} else {
		fmt.Println("Just a picture")
	}
}
