package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	most = 100
	// edge: how many letters may be taken off each end before undoing a
	// doubling
	edge = 5
)

// plan: front < 0 means the letters one by one
type plan struct{ cost, front, back int }

var best = map[string]plan{}

// halve gives the word whose doubling is core, and false if core is none
func halve(core string) (string, bool) {
	half := make([]byte, 0, len(core)/2)
	for i := 0; i < len(core); i += 2 {
		if core[i] == core[i+1] {
			return "", false
		}
		half = append(half, core[i])
	}
	return string(half), true
}

// find gives the fewest phrases that build s: either all letters one by
// one, or a few letters at each end around the double of a shorter word; a
// word free of these repeats always has that shape with short ends
func find(s string) plan {
	if p, ok := best[s]; ok {
		return p
	}
	n := len(s)
	result := plan{n, -1, 0}
	for a := 0; a <= edge && a <= n; a++ {
		for b := 0; b <= edge && a+b <= n; b++ {
			size := n - a - b
			if size < 2 || size%2 == 1 {
				continue
			}
			half, ok := halve(s[a : n-b])
			if !ok {
				continue
			}
			if cost := a + b + 1 + find(half).cost; cost < result.cost {
				result = plan{cost, a, b}
			}
		}
	}
	best[s] = result
	return result
}

func phrases(s string, out []string) []string {
	p := find(s)
	if p.front < 0 {
		for i := 0; i < len(s); i++ {
			out = append(out, "back "+s[i:i+1])
		}
		return out
	}
	n := len(s)
	half, _ := halve(s[p.front : n-p.back])
	out = phrases(half, out)
	out = append(out, "double")
	for i := p.front - 1; i >= 0; i-- {
		out = append(out, "front "+s[i:i+1])
	}
	for i := n - p.back; i < n; i++ {
		out = append(out, "back "+s[i:i+1])
	}
	return out
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var word string
	if _, err := fmt.Fscan(reader, &word); err != nil {
		return
	}
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	if find(word).cost > most {
		fmt.Fprintln(writer, -1)
		return
	}
	out := phrases(word, nil)
	fmt.Fprintln(writer, len(out))
	for _, line := range out {
		fmt.Fprintln(writer, line)
	}
}
