package main

import (
	"os"
	"strconv"
)

const (
	maxAlphabet = 50
	maxStates   = 101
	byteValues  = 256
	inputSize   = 512
	outputSize  = 128
	limbCount   = 10
	limbBase    = 1000000000
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

func (in *input) start() byte {
	c := in.next()
	for c != 0 && c <= ' ' {
		c = in.next()
	}
	return c
}

func (in *input) number() int {
	c, value := in.start(), 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c = in.next()
	}
	return value
}

type node struct {
	next         [maxAlphabet]uint8
	fail, degree uint8
	bad          bool
}

type big [limbCount]uint32

func nonzero(value *big) bool {
	for _, digit := range value {
		if digit != 0 {
			return true
		}
	}
	return false
}

func add(destination, source *big, weight uint8) {
	var carry uint64
	for i := range destination {
		value := uint64(destination[i]) + uint64(source[i])*uint64(weight) + carry
		destination[i] = uint32(value % limbBase)
		carry = value / limbBase
	}
	// 50^50 has85 digits, below the90-digit capacity of these ten limbs.
	if carry != 0 {
		panic("count overflow")
	}
}

func main() {
	var in input
	n, m, p := in.number(), in.number(), in.number()
	var index [byteValues]uint8
	c := in.start()
	for letter := 0; letter < n; letter++ {
		index[c] = uint8(letter)
		c = in.next()
	}
	var nodes [maxStates]node
	states := 1
	for word := 0; word < p; word++ {
		state := uint8(0)
		for c = in.start(); c > ' '; c = in.next() {
			letter := index[c]
			if nodes[state].next[letter] == 0 {
				nodes[state].next[letter] = uint8(states)
				states++
			}
			state = nodes[state].next[letter]
		}
		nodes[state].bad = true
	}
	var queue [maxStates]uint8
	tail := 0
	for letter := 0; letter < n; letter++ {
		if child := nodes[0].next[letter]; child != 0 {
			queue[tail] = child
			tail++
		}
	}
	for head := 0; head < tail; head++ {
		state := queue[head]
		failure := nodes[state].fail
		nodes[state].bad = nodes[state].bad || nodes[failure].bad
		for letter := 0; letter < n; letter++ {
			if child := nodes[state].next[letter]; child != 0 {
				nodes[child].fail = nodes[failure].next[letter]
				queue[tail] = child
				tail++
			} else {
				nodes[state].next[letter] = nodes[failure].next[letter]
			}
		}
	}
	var weights [maxStates][maxAlphabet]uint8
	for state := 0; state < states; state++ {
		if nodes[state].bad {
			continue
		}
		var counts [maxStates]uint8
		for letter := 0; letter < n; letter++ {
			target := nodes[state].next[letter]
			if !nodes[target].bad {
				counts[target]++
			}
		}
		// All failure links are complete; each row can now become weighted safe edges.
		for target, weight := range counts[:states] {
			if weight != 0 {
				edge := nodes[state].degree
				nodes[state].next[edge] = uint8(target)
				weights[state][edge] = weight
				nodes[state].degree++
			}
		}
	}
	var layers [2][maxStates]big
	current, next := &layers[0], &layers[1]
	current[0][0] = 1
	for step := 0; step < m; step++ {
		for state := 0; state < states; state++ {
			next[state] = big{}
		}
		for state := 0; state < states; state++ {
			if !nonzero(&current[state]) {
				continue
			}
			for edge := uint8(0); edge < nodes[state].degree; edge++ {
				target := nodes[state].next[edge]
				add(&next[target], &current[state], weights[state][edge])
			}
		}
		current, next = next, current
	}
	var total big
	for state := 0; state < states; state++ {
		add(&total, &current[state], 1)
	}
	last := limbCount - 1
	for last > 0 && total[last] == 0 {
		last--
	}
	var buffer [outputSize]byte
	output := strconv.AppendUint(buffer[:0], uint64(total[last]), 10)
	for digit := last - 1; digit >= 0; digit-- {
		for divisor := uint32(limbBase / 10); divisor > 0; divisor /= 10 {
			output = append(output, byte('0'+total[digit]/divisor%10))
		}
	}
	os.Stdout.Write(append(output, '\n'))
}
