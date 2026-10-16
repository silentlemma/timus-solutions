package main

import (
	"bufio"
	"os"
	"strconv"
)

// splitmix64 with a fixed seed
const (
	seed    = 2010
	gamma   = 0x9e3779b97f4a7c15
	mix1    = 0xbf58476d1ce4e5b9
	mix2    = 0x94d049bb133111eb
	shift1  = 30
	shift2  = 27
	shift3  = 31
	bufSize = 1 << 20
)

var state uint64 = seed

func nextRandom() uint64 {
	state += gamma
	z := state
	z = (z ^ (z >> shift1)) * mix1
	z = (z ^ (z >> shift2)) * mix2
	return z ^ (z >> shift3)
}

func main() {
	sc := bufio.NewScanner(bufio.NewReaderSize(os.Stdin, bufSize))
	sc.Split(bufio.ScanWords)
	readInt := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	n, k := readInt(), readInt()
	// half-edge h runs from ends[h] to ends[h ^ 1], and the half-edges of
	// a vertex are chained through head and nxt
	ends := make([]int, 2*k)
	head := make([]int, n)
	nxt := make([]int, 2*k)
	for i := range head {
		head[i] = -1
	}
	for h := range ends {
		ends[h] = readInt() - 1
		nxt[h] = head[ends[h]]
		head[ends[h]] = h
	}
	comp := make([]int, n)
	tin := make([]int, n)
	parent := make([]int, n)
	upEdge := make([]int, n)
	for i := range comp {
		comp[i], parent[i], upEdge[i] = -1, -1, -1
	}
	order := make([]int, 0, n)
	stack := make([]int, 0, n)
	it := append([]int(nil), head...)
	for root := 0; root < n; root++ {
		if comp[root] >= 0 {
			continue
		}
		comp[root] = root
		tin[root] = len(order)
		order = append(order, root)
		stack = append(stack, root)
		for len(stack) > 0 {
			v := stack[len(stack)-1]
			h := it[v]
			if h < 0 {
				stack = stack[:len(stack)-1]
				continue
			}
			it[v] = nxt[h]
			w := ends[h^1]
			if comp[w] < 0 {
				comp[w] = root
				parent[w] = v
				upEdge[w] = h >> 1
				tin[w] = len(order)
				order = append(order, w)
				stack = append(stack, w)
			}
		}
	}
	// every non-tree edge joins a vertex and its ancestor; mark it with a
	// random value at both ends, so after summing over subtrees the edge
	// above v carries the xor of the non-tree edges passing over it
	cover := make([]uint64, n)
	count := make([]int, n)
	for e := 0; e < k; e++ {
		a, b := ends[2*e], ends[2*e+1]
		if upEdge[a] == e || upEdge[b] == e {
			continue
		}
		if tin[a] < tin[b] {
			a, b = b, a
		}
		r := nextRandom()
		cover[a] ^= r
		cover[b] ^= r
		count[a]++
		count[b]--
	}
	for i := n - 1; i >= 0; i-- {
		v := order[i]
		if p := parent[v]; p >= 0 {
			cover[p] ^= cover[v]
			count[p] += count[v]
		}
	}
	// a pair of edges is a cut exactly when it is a tree edge covered by
	// nothing but that non-tree edge, or two tree edges covered by the same
	// set; give tree edges values so that a path xors to zero iff it crosses no cut
	value := make([]uint64, n)
	first := make(map[uint64]int, n)
	for _, v := range order {
		if parent[v] < 0 {
			continue
		}
		if count[v] < 2 {
			// a bridge or an edge with one cover: crossing it separates
			value[v] = nextRandom()
			continue
		}
		// edges with one cover set lie on a chain and cut the tree into
		// pieces closed into a ring; a path inside the ring crosses all of
		// them or none of them, so the class must xor to zero
		rep, seen := first[cover[v]]
		if !seen {
			first[cover[v]] = v
			continue
		}
		value[v] = nextRandom()
		value[rep] ^= value[v]
	}
	label := make([]uint64, n)
	for _, v := range order {
		if parent[v] >= 0 {
			label[v] = label[parent[v]] ^ value[v]
		}
	}
	out := bufio.NewWriterSize(os.Stdout, bufSize)
	defer out.Flush()
	for q := readInt(); q > 0; q-- {
		a, b := readInt()-1, readInt()-1
		if comp[a] == comp[b] && label[a] == label[b] {
			out.WriteString("Yes\n")
		} else {
			out.WriteString("No\n")
		}
	}
}
