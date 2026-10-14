package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const base = 10

// scaled returns the decimal text times 10^d, as an integer
func scaled(text string, d int) int64 {
	whole, frac := text, ""
	if dot := strings.IndexByte(text, '.'); dot >= 0 {
		whole, frac = text[:dot], text[dot+1:]
	}
	var v int64
	for _, c := range whole {
		v = v*base + int64(c-'0')
	}
	for i := 0; i < d; i++ {
		v *= base
		if i < len(frac) {
			v += int64(frac[i] - '0')
		}
	}
	return v
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var d, n int
	fmt.Fscan(in, &d, &n)
	one := int64(1)
	for i := 0; i < d; i++ {
		one *= base
	}
	// only the fractional parts matter, and a whole number fits any group
	var values []int64
	seen := map[int64]bool{0: true}
	for i := 0; i < n; i++ {
		var text string
		fmt.Fscan(in, &text)
		if v := scaled(text, d) % one; !seen[v] {
			seen[v] = true
			values = append(values, v)
		}
	}
	den := 2 * one
	// an average v (times 10^d) over q goblins comes from a total p when
	// (2v - 1) q <= den p < (2v + 1) q; q = 10^d always works, as the
	// interval is then at least 1 long
	for q := int64(1); q <= one; q++ {
		fits := true
		for i, v := range values {
			low := ((2*v-1)*q + den - 1) / den // the smallest total allowed
			if low*den >= (2*v+1)*q {
				// the average that failed is likely to fail again: try it first
				copy(values[1:i+1], values[:i])
				values[0] = v
				fits = false
				break
			}
		}
		if fits {
			fmt.Println(q)
			return
		}
	}
}
