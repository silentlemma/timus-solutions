package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func secondDifferences(h []int64) []int64 {
	var d []int64
	for i := 0; i+2 < len(h); i++ {
		d = append(d, h[i+2]-2*h[i+1]+h[i])
	}
	return d
}

func abs(v int64) int64 {
	if v < 0 {
		return -v
	}
	return v
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Split(bufio.ScanWords)
	next := func() int64 {
		in.Scan()
		v, _ := strconv.Atoi(in.Text())
		return int64(v)
	}
	n, m := int(next()), int(next())
	x := make([]int64, m+1)
	for i := range x {
		x[i] = next()
	}
	// a section is similar exactly when the second differences agree, and then
	// a is the difference of the first steps of the two sections
	pattern := secondDifferences(x)
	pi := make([]int, len(pattern))
	for i := 1; i < len(pattern); i++ {
		k := pi[i-1]
		for k > 0 && pattern[i] != pattern[k] {
			k = pi[k-1]
		}
		if pattern[i] == pattern[k] {
			k++
		}
		pi[i] = k
	}
	found := false
	var bestA int64
	bestSlope, bestStart := 0, 0
	for slope := 1; slope <= n; slope++ {
		length := int(next())
		y := make([]int64, length+1)
		for i := range y {
			y[i] = next()
		}
		if length < m {
			continue
		}
		text := secondDifferences(y)
		k := 0
		for i := 0; i <= len(text); i++ {
			if k == len(pattern) {
				start := i - len(pattern)
				a := abs((x[1] - x[0]) - (y[start+1] - y[start]))
				if !found || a < bestA {
					found, bestA, bestSlope, bestStart = true, a, slope, start
				}
				if len(pattern) > 0 {
					k = pi[k-1]
				}
			}
			if i == len(text) || len(pattern) == 0 {
				continue
			}
			for k > 0 && text[i] != pattern[k] {
				k = pi[k-1]
			}
			if text[i] == pattern[k] {
				k++
			}
		}
	}
	if found {
		fmt.Println(bestSlope, bestStart)
	} else {
		fmt.Println(-1)
	}
}
