package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	timeLimit = 30000
	buffer    = 1 << 16
)

var reader = bufio.NewReaderSize(os.Stdin, buffer)

func readInt() int {
	c, _ := reader.ReadByte()
	for c < '0' || c > '9' {
		c, _ = reader.ReadByte()
	}
	v := 0
	for c >= '0' && c <= '9' {
		v = v*10 + int(c-'0')
		c, _ = reader.ReadByte()
	}
	return v
}

func main() {
	n := readInt()
	// the latest start among the talks that end at each minute
	latest := make([]int, timeLimit+1)
	for i := 0; i < n; i++ {
		s, e := readInt(), readInt()
		if s > latest[e] {
			latest[e] = s
		}
	}
	// take the talk that ends first among those starting after the last one
	count, last := 0, 0
	for e := 1; e <= timeLimit; e++ {
		if latest[e] > last {
			count++
			last = e
		}
	}
	fmt.Println(count)
}
