package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 1 << 16

var (
	n, q                              int
	head, nxt, to                     []int
	askHead, askNext, askDist, answer []int
	depth, path, stack                []int
)

// walk the tree from root in preorder: when a vertex is reached, path holds
// its ancestors by depth, so a query at it with d <= depth is answered at
// once; returns the deepest vertex
func walk(root int) int {
	for v := range depth {
		depth[v] = -1
	}
	depth[root] = 0
	deepest := root
	stack = append(stack[:0], root)
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		path[depth[v]] = v
		if depth[v] > depth[deepest] {
			deepest = v
		}
		for i := askHead[v]; i >= 0; i = askNext[i] {
			if answer[i] == 0 && askDist[i] <= depth[v] {
				answer[i] = path[depth[v]-askDist[i]]
			}
		}
		for e := head[v]; e >= 0; e = nxt[e] {
			if depth[to[e]] < 0 {
				depth[to[e]] = depth[v] + 1
				stack = append(stack, to[e])
			}
		}
	}
	return deepest
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufferSize)
	readInt := func() int {
		x := 0
		c, err := reader.ReadByte()
		for err == nil && c <= ' ' {
			c, err = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			x = x*10 + int(c-'0')
			c, _ = reader.ReadByte()
		}
		return x
	}
	n, q = readInt(), readInt()
	head = make([]int, n+1)
	for v := range head {
		head[v] = -1
	}
	for i := 0; i < n-1; i++ {
		a, b := readInt(), readInt()
		to = append(to, b)
		nxt = append(nxt, head[a])
		head[a] = len(to) - 1
		to = append(to, a)
		nxt = append(nxt, head[b])
		head[b] = len(to) - 1
	}
	askHead = make([]int, n+1)
	for v := range askHead {
		askHead[v] = -1
	}
	askNext = make([]int, q)
	askDist = make([]int, q)
	answer = make([]int, q)
	for i := 0; i < q; i++ {
		v := readInt()
		askDist[i] = readInt()
		askNext[i] = askHead[v]
		askHead[v] = i
	}
	depth = make([]int, n+1)
	path = make([]int, n+1)
	// at least one diameter end is farthest from any vertex; the walk from
	// vertex 1 finds one end, and the walk from there finds the other
	a := walk(1)
	b := walk(a)
	walk(b)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	for i := 0; i < q; i++ {
		writer.WriteString(strconv.Itoa(answer[i]))
		writer.WriteByte('\n')
	}
}
