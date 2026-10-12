package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	chunk   = 1 << 16
	longest = 1 << 24 // the longest line the scanner accepts
)

func main() {
	sc := bufio.NewScanner(bufio.NewReaderSize(os.Stdin, chunk))
	sc.Buffer(make([]byte, chunk), longest)
	sc.Split(bufio.ScanWords)
	next := func() int {
		sc.Scan()
		v, _ := strconv.Atoi(sc.Text())
		return v
	}
	k := next()
	// children 0..k-1 are boys and k..2k-1 girls; likes[v] is the child v
	// likes, or -1; nobody is liked by two, so the likes form paths and cycles
	likes, partner := make([]int, 2*k), make([]int, 2*k)
	liked, seen := make([]bool, 2*k), make([]bool, 2*k)
	for i := 0; i < 2*k; i++ {
		likes[i], partner[i] = -1, -1
		if x := next(); x != 0 {
			if i < k {
				likes[i] = k + x - 1
			} else {
				likes[i] = x - 1
			}
			liked[likes[i]] = true
		}
	}
	var chain []int
	// pair the children along the likes from start, two by two; on an odd
	// path the last one, who likes nobody, stays free
	pairAlong := func(start int) {
		chain = chain[:0]
		for v := start; v >= 0 && !seen[v]; v = likes[v] {
			seen[v] = true
			chain = append(chain, v)
		}
		for i := 0; i+1 < len(chain); i += 2 {
			partner[chain[i]], partner[chain[i+1]] = chain[i+1], chain[i]
		}
	}
	for v := 0; v < 2*k; v++ {
		if !liked[v] {
			pairAlong(v)
		}
	}
	for v := 0; v < 2*k; v++ {
		if !seen[v] {
			pairAlong(v) // what is left are cycles, always of even length
		}
	}
	// the free children like nobody and can be paired in any way
	g := k
	for b := 0; b < k; b++ {
		if partner[b] >= 0 {
			continue
		}
		for partner[g] >= 0 {
			g++
		}
		partner[b], partner[g] = g, b
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for i := 0; i < k; i++ {
		if i > 0 {
			out.WriteByte(' ')
		}
		out.WriteString(strconv.Itoa(partner[i] - k + 1))
	}
	out.WriteByte('\n')
}
