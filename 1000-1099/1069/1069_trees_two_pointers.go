package main

import (
	"os"
	"strconv"
)

const (
	maxVertices   = 7500
	inputSize     = 4096
	outputSize    = 8192
	numberReserve = 16
)

type input struct {
	bytes            [inputSize]byte
	position, length int
}

func (in *input) next() byte {
	if in.position == in.length {
		in.length, _ = os.Stdin.Read(in.bytes[:])
		in.position = 0
		if in.length == 0 {
			return 0
		}
	}
	c := in.bytes[in.position]
	in.position++
	return c
}

func (in *input) number() (uint16, bool) {
	c := in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	if c == 0 {
		return 0, false
	}
	value := uint16(0)
	for c >= '0' && c <= '9' {
		value = value*10 + uint16(c-'0')
		c = in.next()
	}
	return value, true
}

var output = make([]byte, 0, outputSize)

func flush() {
	pending := output
	for len(pending) > 0 {
		count, err := os.Stdout.Write(pending)
		pending = pending[count:]
		if err != nil || count == 0 {
			break
		}
	}
	output = output[:0]
}

func number(value uint16) {
	if len(output)+numberReserve >= cap(output) {
		flush()
	}
	output = strconv.AppendUint(output, uint64(value), 10)
}

func main() {
	var in input
	var code [maxVertices]uint16
	var remaining, parent, first, next [maxVertices + 1]uint16
	length := 0
	for {
		value, ok := in.number()
		if !ok {
			break
		}
		code[length] = value
		length++
		remaining[value]++
	}
	n := length + 1
	pointer := 1
	for remaining[pointer] != 0 {
		pointer++
	}
	leaf := uint16(pointer)
	for step, c := range code[:length] {
		parent[leaf] = c
		remaining[c]--
		if step+1 == length {
			break
		}
		// A newly freed smaller label wins immediately; otherwise the scan only advances.
		if remaining[c] == 0 && int(c) < pointer {
			leaf = c
		} else {
			pointer++
			for remaining[pointer] != 0 {
				pointer++
			}
			leaf = uint16(pointer)
		}
	}
	// Descending prepends produce increasing child lists rooted at the final vertex N.
	for vertex := n - 1; vertex >= 1; vertex-- {
		p := parent[vertex]
		next[vertex] = first[p]
		first[p] = uint16(vertex)
	}
	for vertex := 1; vertex <= n; vertex++ {
		number(uint16(vertex))
		output = append(output, ':')
		pending := parent[vertex]
		for child := first[vertex]; child != 0; child = next[child] {
			if pending != 0 && pending < child {
				output = append(output, ' ')
				number(pending)
				pending = 0
			}
			output = append(output, ' ')
			number(child)
		}
		if pending != 0 {
			output = append(output, ' ')
			number(pending)
		}
		output = append(output, '\n')
	}
	flush()
}
