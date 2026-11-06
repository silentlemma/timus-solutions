package main

import "os"

const maxNodes = 1000
const root = 1
const bufferSize = 256

type input struct {
	buffer     [bufferSize]byte
	start, end int
}

func (in *input) byte() byte {
	if in.start == in.end {
		in.start = 0
		in.end, _ = os.Stdin.Read(in.buffer[:])
		if in.end == 0 {
			return 0
		}
	}
	result := in.buffer[in.start]
	in.start++
	return result
}

func (in *input) token() byte {
	c := in.byte()
	for c != 0 && c <= ' ' {
		c = in.byte()
	}
	return c
}

func (in *input) integer() int {
	c := in.token()
	sign := 1
	if c == '-' {
		sign = -1
		c = in.byte()
	} else if c == '+' {
		c = in.byte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = in.byte()
	}
	return sign * value
}

type position struct {
	parent, remaining uint16
	first, second     int8
}

func main() {
	var in input
	n := in.integer()
	var tree [maxNodes + 1]position
	tree[root].first, tree[root].second = -1, 1
	for i := 2; i <= n; i++ {
		kind := in.token()
		parent := in.integer()
		tree[parent].remaining++
		p := &tree[i]
		p.parent = uint16(parent)
		if kind == 'L' {
			value := int8(in.integer())
			p.first, p.second = value, value
		} else {
			p.first, p.second = -1, 1
		}
	}
	// Once a node is ready, its child count becomes the link in a stack.
	var ready uint16
	for i := 2; i <= n; i++ {
		if tree[i].remaining == 0 {
			tree[i].remaining = ready
			ready = uint16(i)
		}
	}
	for ready != 0 && ready != root {
		child := tree[ready]
		ready = child.remaining
		parent := &tree[child.parent]
		// Keep the result for each possible player to move. A child is
		// evaluated for the other player because the move consumes a turn.
		if child.second > parent.first {
			parent.first = child.second
		}
		if child.first < parent.second {
			parent.second = child.first
		}
		parent.remaining--
		if parent.remaining == 0 {
			parent.remaining = ready
			ready = child.parent
		}
	}
	switch tree[root].first {
	case -1:
		os.Stdout.WriteString("-1\n")
	case 1:
		os.Stdout.WriteString("+1\n")
	default:
		os.Stdout.WriteString("0\n")
	}
}
