package main

import (
	"fmt"
	"strings"
)

const (
	hundredthsPerPercent = 100
	whole                = 100 * hundredthsPerPercent
)

// hundredths: a percentage with at most two decimals, in hundredths of a percent.
func hundredths(s string) int64 {
	var integer, fraction int64
	parts := strings.SplitN(s, ".", 2)
	for _, c := range parts[0] {
		integer = integer*10 + int64(c-'0')
	}
	if len(parts) == 2 {
		scale := int64(hundredthsPerPercent)
		for _, c := range parts[1] {
			if scale == 1 {
				break
			}
			scale /= 10
			fraction += int64(c-'0') * scale
		}
	}
	return integer*hundredthsPerPercent + fraction
}

func main() {
	var a, b string
	fmt.Scan(&a, &b)
	p, q := hundredths(a), hundredths(b)
	// the fewest conductors above p are p*n/whole + 1, and n is the answer
	// as soon as their share is below q
	for n := int64(1); ; n++ {
		if c := p*n/whole + 1; c*whole < q*n {
			fmt.Println(n)
			return
		}
	}
}
