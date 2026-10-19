package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufSize = 1 << 16

var reader *bufio.Reader

func readToken() byte {
	c, _ := reader.ReadByte()
	for c == ' ' || c == '\n' || c == '\r' {
		c, _ = reader.ReadByte()
	}
	return c
}

func readInt() int64 {
	c := readToken()
	var x int64
	for c >= '0' && c <= '9' {
		x = x*10 + int64(c-'0')
		var err error
		c, err = reader.ReadByte()
		if err != nil {
			break
		}
	}
	return x
}

func main() {
	reader = bufio.NewReaderSize(os.Stdin, bufSize)
	writer := bufio.NewWriterSize(os.Stdout, bufSize)
	defer writer.Flush()

	n := int(readInt())
	head := make([]int, n+1)
	for i := range head {
		head[i] = -1
	}
	nxt := make([]int, 2*n)
	to := make([]int, 2*n)
	wt := make([]int64, 2*n)
	for e := 0; e < 2*(n-1); e += 2 {
		u, v, w := int(readInt()), int(readInt()), readInt()
		to[e], wt[e], nxt[e], head[u] = v, w, head[u], e
		to[e+1], wt[e+1], nxt[e+1], head[v] = u, w, head[v], e+1
	}

	tin := make([]int, n+1)
	parent := make([]int, n+1)
	depth := make([]int64, n+1)
	order := make([]int, 0, n)
	parent[1] = 1
	stack := []int{1}
	for len(stack) > 0 {
		v := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		tin[v] = len(order)
		order = append(order, v)
		for e := head[v]; e >= 0; e = nxt[e] {
			u := to[e]
			if u != parent[v] {
				parent[u] = v
				depth[u] = depth[v] + wt[e]
				stack = append(stack, u)
			}
		}
	}

	// The LCA of u != v is the parent with the smallest preorder number among
	// the vertices in the preorder range (tin[u], tin[v]].
	lg := make([]int, n+1)
	for i := 2; i <= n; i++ {
		lg[i] = lg[i/2] + 1
	}
	table := make([][]int32, lg[n]+1)
	table[0] = make([]int32, n)
	for i, v := range order {
		table[0][i] = int32(tin[parent[v]])
	}
	for k := 1; k <= lg[n]; k++ {
		prev, half := table[k-1], 1<<(k-1)
		row := make([]int32, n-(1<<k)+1)
		for i := range row {
			row[i] = prev[i]
			if prev[i+half] < row[i] {
				row[i] = prev[i+half]
			}
		}
		table[k] = row
	}
	dist := func(u, v int) int64 {
		if u == v {
			return 0
		}
		lo, hi := tin[u], tin[v]
		if lo > hi {
			lo, hi = hi, lo
		}
		lo++
		k := lg[hi-lo+1]
		x, y := table[k][lo], table[k][hi-(1<<k)+1]
		if y < x {
			x = y
		}
		return depth[u] + depth[v] - 2*depth[order[x]]
	}

	fen := make([]int, n+1)
	top := 1 << lg[n]
	kth := func(k int) int {
		p := 0
		for step := top; step > 0; step >>= 1 {
			if p+step <= n && fen[p+step] < k {
				p += step
				k -= fen[p]
			}
		}
		return order[p]
	}
	add := func(p, d int) {
		for i := p + 1; i <= n; i += i & -i {
			fen[i] += d
		}
	}

	q := int(readInt())
	total := 0
	var doubled int64 // the sum of distances around the marked vertices in preorder
	buf := make([]byte, 0, bufSize)
	for ; q > 0; q-- {
		adding := readToken() == '+'
		v := int(readInt())
		p := tin[v]
		if !adding {
			add(p, -1)
			total--
		}
		if total > 0 {
			before := 0
			for i := p; i > 0; i -= i & -i {
				before += fen[i]
			}
			ka, kb := before, before+1
			if before == 0 {
				ka = total
			}
			if before == total {
				kb = 1
			}
			a, b := kth(ka), kth(kb)
			change := dist(a, v) + dist(v, b) - dist(a, b)
			if adding {
				doubled += change
			} else {
				doubled -= change
			}
		}
		if adding {
			add(p, 1)
			total++
		}
		buf = strconv.AppendInt(buf, doubled/2, 10)
		buf = append(buf, '\n')
		if len(buf) > bufSize/2 {
			writer.Write(buf)
			buf = buf[:0]
		}
	}
	writer.Write(buf)
}
