package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
)

const (
	lowestSymbol = 33
	symbolCount  = 90
	alphabetSize = symbolCount * symbolCount * symbolCount
)

func encode(token []byte) int {
	code := (int(token[0])-lowestSymbol)*symbolCount + int(token[1]) - lowestSymbol
	return code*symbolCount + int(token[2]) - lowestSymbol
}

type windowCounter struct {
	deficit  []int32
	ring     []int
	missing  int
	position int
	used     int
}

func newWindowCounter(pattern []int) *windowCounter {
	c := &windowCounter{
		deficit: make([]int32, alphabetSize),
		ring:    make([]int, len(pattern)), missing: len(pattern),
	}
	for _, code := range pattern {
		c.deficit[code]++
	}
	return c
}

func (c *windowCounter) push(code int) bool {
	if c.used == len(c.ring) {
		old := c.ring[c.position]
		if c.deficit[old] >= 0 {
			c.missing++
		}
		c.deficit[old]++
	} else {
		c.used++
	}
	if c.deficit[code] > 0 {
		c.missing--
	}
	c.deficit[code]--
	c.ring[c.position] = code
	c.position++
	if c.position == len(c.ring) {
		c.position = 0
	}
	return c.missing == 0
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	boundary := bytes.IndexByte(data, '\n')
	patternTokens := bytes.Fields(data[:boundary])
	pattern := make([]int, len(patternTokens))
	for index, token := range patternTokens {
		pattern[index] = encode(token)
	}
	c := newWindowCounter(pattern)
	answer := 0
	for _, token := range bytes.Fields(data[boundary+1:]) {
		if c.push(encode(token)) {
			answer++
		}
	}
	fmt.Println(answer)
}
