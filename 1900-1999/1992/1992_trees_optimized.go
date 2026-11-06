package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 16384
const outputSize = 8

type reader struct {
	data           [bufferSize]byte
	position, size int
}

func (r *reader) next() byte {
	if r.position == r.size {
		r.size, _ = os.Stdin.Read(r.data[:])
		r.position = 0
		if r.size == 0 {
			return 0
		}
	}
	value := r.data[r.position]
	r.position++
	return value
}

func (r *reader) start() byte {
	c := r.next()
	for c != 0 && c <= ' ' {
		c = r.next()
	}
	return c
}

func (r *reader) number() int {
	value := 0
	for c := r.start(); c >= '0' && c <= '9'; c = r.next() {
		value = value*10 + int(c-'0')
	}
	return value
}

func (r *reader) command() byte {
	kind, second := r.start(), r.next()
	for c := r.next(); c > ' '; c = r.next() {
	}
	if kind == 'r' {
		return second
	}
	if kind == 'c' && second == 'l' {
		return 'C'
	}
	return kind
}

type pair struct {
	first, second int32
}

func main() {
	var input reader
	count := input.number()
	input.number()
	nodes := make([]pair, count+1)
	heads := make([]pair, count+2)
	used, entities := int32(0), 1
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	var line [outputSize]byte
	for step := 0; step < count; step++ {
		kind := input.command()
		history := &heads[input.number()]
		switch kind {
		case 'l':
			used++
			nodes[used] = pair{int32(input.number()), history.first}
			*history = pair{used, 0}
		case 'o':
			node := nodes[history.first]
			used++
			nodes[used] = pair{node.first, history.second}
			*history = pair{node.second, used}
		case 'e':
			node := nodes[history.second]
			used++
			nodes[used] = pair{node.first, history.first}
			*history = pair{used, node.second}
		case 'C':
			entities++
			heads[entities] = *history
		case 'c':
			if history.first == 0 {
				out.WriteString("basic\n")
			} else {
				digits := strconv.AppendInt(line[:0], int64(nodes[history.first].first), 10)
				out.Write(append(digits, '\n'))
			}
		}
	}
	out.Flush()
}
