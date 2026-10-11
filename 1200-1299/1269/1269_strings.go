package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	// a line without its line break
	readLine := func() []byte {
		line, _ := in.ReadBytes('\n')
		return bytes.TrimRight(line, "\r\n")
	}
	n, _ := strconv.Atoi(string(bytes.TrimSpace(readLine())))
	words := make([][]byte, n)
	total := 1
	for i := range words {
		words[i] = readLine()
		total += len(words[i])
	}
	// build the trie as first-child / next-sibling lists
	child := make([]int32, total)
	sibling := make([]int32, total)
	ends := make([]int32, total)
	char := make([]byte, total)
	for i := range child {
		child[i], sibling[i] = -1, -1
	}
	nodes := int32(1)
	for _, w := range words {
		v := int32(0)
		for _, c := range w {
			u := child[v]
			for u >= 0 && char[u] != c {
				u = sibling[u]
			}
			if u < 0 {
				u = nodes
				nodes++
				char[u] = c
				sibling[u] = child[v]
				child[v] = u
			}
			v = u
		}
		if int32(len(w)) > ends[v] {
			ends[v] = int32(len(w))
		}
	}
	words = nil
	// renumber in breadth-first order: the children of v then take the
	// numbers first[v] .. first[v] + count[v] - 1, and label[u] is the
	// byte leading to u
	first := make([]int32, nodes)
	count := make([]int32, nodes)
	longest := make([]int32, nodes)
	label := make([]byte, nodes)
	old := make([]int32, 1, nodes)
	for v := int32(0); v < nodes; v++ {
		first[v] = int32(len(old))
		for u := child[old[v]]; u >= 0; u = sibling[u] {
			label[len(old)] = char[u]
			longest[len(old)] = ends[u]
			old = append(old, u)
		}
		count[v] = int32(len(old)) - first[v]
	}
	// the child of v along byte c, or -1
	walk := func(v int32, c byte) int32 {
		i := bytes.IndexByte(label[first[v]:first[v]+count[v]], c)
		if i < 0 {
			return -1
		}
		return first[v] + int32(i)
	}
	// failure links in the same order; a node also takes the longest word
	// of its failure node, which comes earlier
	fail := make([]int32, nodes)
	for v := int32(1); v < nodes; v++ {
		for u := first[v]; u < first[v]+count[v]; u++ {
			f := fail[v]
			g := walk(f, label[u])
			for g < 0 && f != 0 {
				f = fail[f]
				g = walk(f, label[u])
			}
			if g < 0 {
				g = 0
			}
			fail[u] = g
			if longest[g] > longest[u] {
				longest[u] = longest[g]
			}
		}
	}
	m, _ := strconv.Atoi(string(bytes.TrimSpace(readLine())))
	for row := 1; row <= m; row++ {
		line := readLine()
		v, best := int32(0), len(line)+1
		for i, c := range line {
			g := walk(v, c)
			for g < 0 && v != 0 {
				v = fail[v]
				g = walk(v, c)
			}
			if g < 0 {
				g = 0
			}
			v = g
			if longest[v] > 0 && i+2-int(longest[v]) < best {
				best = i + 2 - int(longest[v])
			}
		}
		if best <= len(line) {
			fmt.Println(row, best)
			return
		}
	}
	fmt.Println("Passed")
}
