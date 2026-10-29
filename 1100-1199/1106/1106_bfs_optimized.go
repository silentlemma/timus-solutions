package main

import (
	"bufio"
	"os"
	"strconv"
)

const inputBufferSize = 4096

// the numbers are parsed by hand from a small buffer, faster than fmt.Fscan
type fastInput struct {
	reader *bufio.Reader
}

func (in fastInput) nextInt() int64 {
	c, err := in.reader.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.reader.ReadByte()
	}
	sign := int64(1)
	if c == '-' {
		sign = -1
		c, err = in.reader.ReadByte()
	}
	var value int64
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c, err = in.reader.ReadByte()
	}
	return value * sign
}

func main() {
	in := fastInput{bufio.NewReaderSize(os.Stdin, inputBufferSize)}
	n := int(in.nextInt())
	// at most 100 vertices, so a vertex number fits in a byte
	adj := make([][]byte, n+1)
	for v := 1; v <= n; v++ {
		for u := byte(in.nextInt()); u != 0; u = byte(in.nextInt()) {
			adj[v] = append(adj[v], u)
		}
	}
	// colour a BFS tree of every component by depth parity: each member has a
	// tree neighbour, its parent or a child, in the other team (side 0: not
	// reached yet; 1 and 2: the teams, a child takes the other one)
	side := make([]byte, n+1)
	// every vertex enters the queue once, so n cells are enough
	queue := make([]byte, n)
	for root := 1; root <= n; root++ {
		if side[root] != 0 {
			continue
		}
		side[root] = 1
		queue[0] = byte(root)
		tail := 1
		for head := 0; head < tail; head++ {
			v := queue[head]
			for _, u := range adj[v] {
				if side[u] == 0 {
					side[u] = 1 + side[v]%2
					queue[tail] = u
					tail++
				}
			}
		}
	}
	count := 0
	for _, group := range side {
		if group == 1 {
			count++
		}
	}
	out := bufio.NewWriter(os.Stdout)
	out.WriteString(strconv.Itoa(count))
	out.WriteByte('\n')
	separator := ""
	for v := 1; v <= n; v++ {
		if side[v] == 1 {
			out.WriteString(separator)
			out.WriteString(strconv.Itoa(v))
			separator = " "
		}
	}
	out.WriteByte('\n')
	out.Flush()
}
