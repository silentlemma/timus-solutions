package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const bufferSize = 1 << 16

var reader = bufio.NewReaderSize(os.Stdin, bufferSize)

func readInt() int {
	c, _ := reader.ReadByte()
	for c < '0' {
		c, _ = reader.ReadByte()
	}
	v := 0
	for c >= '0' {
		v = v*10 + int(c-'0')
		var err error
		c, err = reader.ReadByte()
		if err != nil {
			break
		}
	}
	return v
}

func main() {
	n := readInt()
	tall := make([]int, n)
	for i := range tall {
		tall[i] = readInt()
	}
	q := readInt()
	x := make([]int, q)
	most := 0
	for i := range x {
		x[i] = readInt()
		if x[i] > most {
			most = x[i]
		}
	}
	// tent of height t at every odd multiple of t; the envelope of all
	// tents is the answer, and centres beyond 2 * most never matter
	limit := 2 * most
	height := make([]int32, limit+1)
	sort.Ints(tall)
	for i, t := range tall {
		if i > 0 && t == tall[i-1] {
			continue
		}
		if t >= most {
			height[most] = int32(most)
			break
		}
		for c := t; c <= limit; c += 2 * t {
			height[c] = int32(t)
		}
	}
	// best[x] = max over c of height[c] - |x - c|, by two sweeps
	for i := 1; i <= limit; i++ {
		if height[i-1]-1 > height[i] {
			height[i] = height[i-1] - 1
		}
	}
	for i := limit - 1; i >= 0; i-- {
		if height[i+1]-1 > height[i] {
			height[i] = height[i+1] - 1
		}
	}
	out := bufio.NewWriterSize(os.Stdout, bufferSize)
	defer out.Flush()
	for _, v := range x {
		out.WriteString(strconv.Itoa(int(height[v])))
		out.WriteByte('\n')
	}
}
