package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufSize = 1 << 16

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufSize)
	out := bufio.NewWriterSize(os.Stdout, bufSize)
	defer out.Flush()
	readInt := func() int {
		n, c := 0, byte(' ')
		for c == ' ' || c == '\n' || c == '\r' {
			c, _ = in.ReadByte()
		}
		for c >= '0' && c <= '9' {
			n = n*10 + int(c-'0')
			c, _ = in.ReadByte()
		}
		return n
	}
	n, m := readInt(), readInt()
	from, to := make([]int, m), make([]int, m)
	for i := 0; i < m; i++ {
		from[i], to[i] = readInt(), readInt()
	}
	q := readInt()
	cuts := make([]int, q)
	cut := make([]bool, m)
	for k := range cuts {
		cuts[k] = readInt() - 1
		cut[cuts[k]] = true
	}
	parent := make([]int, n+1)
	for v := range parent {
		parent[v] = v
	}
	find := func(v int) int {
		root := v
		for parent[root] != root {
			root = parent[root]
		}
		for parent[v] != root {
			parent[v], v = root, parent[v]
		}
		return root
	}
	pieces := n
	join := func(i int) {
		if a, b := find(from[i]), find(to[i]); a != b {
			parent[a] = b
			pieces--
		}
	}
	// run backwards: start from the web after all cuts and put the threads
	// back one by one, last cut first
	for i := 0; i < m; i++ {
		if !cut[i] {
			join(i)
		}
	}
	answers := make([]int, q)
	for k := q - 1; k >= 0; k-- {
		answers[k] = pieces
		join(cuts[k])
	}
	for k, a := range answers {
		if k > 0 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.Itoa(a))
	}
	out.WriteByte('\n')
}
