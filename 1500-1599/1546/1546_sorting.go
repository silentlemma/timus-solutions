package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

// the whole input is at most 100 KB, so even a single name fits
const maxInput = 1 << 17

type name struct {
	text, main string
	zeros      []int
}

// keyOf writes a name so that plain string order compares it: a number becomes
// "0", its length without leading zeros in seven digits and those digits, a
// letter becomes "1" and itself, so numbers come first and compare by value
func keyOf(s string) name {
	var main strings.Builder
	var zeros []int
	for i := 0; i < len(s); {
		if s[i] < '0' || s[i] > '9' {
			main.WriteByte('1')
			main.WriteByte(s[i])
			i++
			continue
		}
		start := i
		for i < len(s) && s[i] == '0' {
			i++
		}
		digits := i
		for i < len(s) && s[i] >= '0' && s[i] <= '9' {
			i++
		}
		fmt.Fprintf(&main, "0%07d%s", i-digits, s[digits:i])
		zeros = append(zeros, start-digits)
	}
	return name{s, main.String(), zeros}
}

func main() {
	in := bufio.NewScanner(os.Stdin)
	in.Buffer(make([]byte, 0, maxInput), maxInput)
	in.Split(bufio.ScanWords)
	var names []name
	for in.Scan() {
		names = append(names, keyOf(in.Text()))
	}
	// letters and numbers by value first; then, run by run, more leading zeros first
	sort.SliceStable(names, func(a, b int) bool {
		x, y := names[a], names[b]
		if x.main != y.main {
			return x.main < y.main
		}
		for i := range x.zeros {
			if x.zeros[i] != y.zeros[i] {
				return x.zeros[i] < y.zeros[i]
			}
		}
		return false
	})
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, n := range names {
		out.WriteString(n.text)
		out.WriteByte('\n')
	}
}
