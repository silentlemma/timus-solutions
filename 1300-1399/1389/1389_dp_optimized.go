package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 8192
const pairReserve = 24
const chosen uint32 = 1 << 31

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	n, m := number(in), number(in)
	head, to, next := make([]uint32, n), make([]uint32, 2*m), make([]uint32, 2*m)
	parentEdge, order := make([]uint32, n), make([]uint32, n)
	for i := 0; i < m; i++ {
		a, b := number(in)-1, number(in)-1
		to[2*i] = uint32(b)
		next[2*i] = head[a]
		head[a] = uint32(2*i + 1)
		to[2*i+1] = uint32(a)
		next[2*i+1] = head[b]
		head[b] = uint32(2*i + 2)
	}
	tail := 1
	for position := 0; position < tail; position++ {
		v := order[position]
		for link := head[v]; link != 0; link = next[link-1] {
			edge := link - 1
			if parentEdge[v] != 0 && edge == (parentEdge[v]-1)^1 {
				continue
			}
			u := to[edge]
			parentEdge[u] = edge + 1
			order[tail] = u
			tail++
		}
	}
	used := make([]bool, n)
	count := 0
	for position := n - 1; position > 0; position-- {
		v := order[position]
		edge := parentEdge[v] - 1
		parent := to[edge^1]
		if used[v] || used[parent] {
			continue
		}
		used[v], used[parent] = true, true
		count++
		// The links are no longer traversed, so their high bits can mark chosen roads.
		next[edge&^1] |= chosen
	}
	output := make([]byte, 0, bufferSize)
	output = strconv.AppendInt(output, int64(count), 10)
	output = append(output, '\n')
	for i := 0; i < m; i++ {
		if next[2*i]&chosen != 0 {
			if len(output)+pairReserve > cap(output) {
				os.Stdout.Write(output)
				output = output[:0]
			}
			output = strconv.AppendUint(output, uint64(to[2*i+1]+1), 10)
			output = append(output, ' ')
			output = strconv.AppendUint(output, uint64(to[2*i]+1), 10)
			output = append(output, '\n')
		}
	}
	os.Stdout.Write(output)
}
