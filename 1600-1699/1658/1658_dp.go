package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	longest = 100 // digits allowed in the answer
	top     = 9   // the largest digit
	maxS1   = longest * top
	maxS2   = longest * top * top
	none    = 255
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	// fewest[s1][s2]: the fewest nonzero digits with these sums, none if
	// more than 100 are needed or none will do
	fewest := make([]uint8, (maxS1+1)*(maxS2+1))
	for k := range fewest {
		fewest[k] = none
	}
	at := func(s1, s2 int) int { return s1*(maxS2+1) + s2 }
	fewest[0] = 0
	for s1 := 1; s1 <= maxS1; s1++ {
		for s2 := 1; s2 <= maxS2; s2++ {
			best := none
			for d := 1; d <= top && d <= s1 && d*d <= s2; d++ {
				if v := int(fewest[at(s1-d, s2-d*d)]) + 1; v < best {
					best = v
				}
			}
			if best <= longest {
				fewest[at(s1, s2)] = uint8(best)
			}
		}
	}
	var t int
	fmt.Fscan(in, &t)
	for ; t > 0; t-- {
		var s1, s2 int
		fmt.Fscan(in, &s1, &s2)
		if s1 > maxS1 || s2 > maxS2 || fewest[at(s1, s2)] == none {
			fmt.Fprintln(out, "No solution")
			continue
		}
		// the smallest digit first that still leaves a way to finish; the
		// digits come out sorted, so each search starts at the last one
		d := 1
		var digits []byte
		for left := int(fewest[at(s1, s2)]) - 1; left >= 0; left-- {
			for d*d > s2 || d > s1 || int(fewest[at(s1-d, s2-d*d)]) != left {
				d++
			}
			digits = append(digits, byte('0'+d))
			s1, s2 = s1-d, s2-d*d
		}
		fmt.Fprintln(out, string(digits))
	}
}
