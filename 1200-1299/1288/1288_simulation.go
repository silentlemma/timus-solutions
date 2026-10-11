package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const (
	signalDigits = 6 // signal values are read in millionths
	factorDigits = 3 // A has at most three decimals
	signal       = 1000000
	factor       = 1000
	wall, low    = 95, 35
)

// scaled reads a non-negative decimal as an exact multiple of 1 / 10^digits
func scaled(token string, digits int) int64 {
	whole, frac := token, ""
	if dot := strings.IndexByte(token, '.'); dot >= 0 {
		whole, frac = token[:dot], token[dot+1:]
	}
	frac = (frac + strings.Repeat("0", digits))[:digits]
	w, _ := strconv.Atoi("0" + whole)
	f, _ := strconv.Atoi(frac)
	scale := 1
	for i := 0; i < digits; i++ {
		scale *= 10
	}
	return int64(w*scale + f)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	word := func() string {
		var s string
		fmt.Fscan(in, &s)
		return s
	}
	var n, d int
	var start, stop, level [2]int
	fmt.Fscan(in, &n, &d, &start[0], &stop[0], &level[0], &start[1], &stop[1], &level[1])
	a := scaled(word(), factorDigits)
	raw := make([]int64, n)
	for i := range raw {
		raw[i] = scaled(word(), signalDigits)
	}
	unit := int64(signal * factor)
	// the front wall: the first value of 95 or more after a value of 35 or less
	surface, seen := -1, false
	for i := 0; i < n && surface < 0; i++ {
		if seen && raw[i] >= wall*signal {
			surface = i
		}
		seen = seen || raw[i] <= low*signal
	}
	if surface < 0 {
		fmt.Println("No surface.")
		return
	}
	fmt.Printf("Surface found at %d.\n", surface+1)
	// after the wall every value is multiplied by 1 + (m - f) A, here in
	// units of 1 / (signal * factor)
	value := make([]int64, n)
	for i := range raw {
		if i <= surface {
			value[i] = raw[i] * factor
		} else {
			value[i] = raw[i] * (factor + int64(i-surface)*a)
		}
	}
	bottom := -1
	seen = false
	for i := surface + 1; i < n && bottom < 0; i++ {
		if seen && i-surface >= d && value[i] >= wall*unit {
			bottom = i
		}
		seen = seen || value[i] <= low*unit
	}
	if bottom < 0 {
		fmt.Println("No bottom.")
	} else {
		fmt.Printf("Bottom found at %d.\n", bottom-surface)
	}
	end := n - 1
	if bottom >= 0 {
		end = bottom - 1
	}
	for c := range start {
		lo, hi := surface+start[c], surface+stop[c]
		if hi > end {
			hi = end
		}
		if lo > hi {
			fmt.Printf("Channel %d: No search.\n", c+1)
			continue
		}
		best := lo
		for i := lo + 1; i <= hi; i++ {
			if value[i] > value[best] {
				best = i
			}
		}
		if value[best] >= int64(level[c])*unit {
			fmt.Printf("Channel %d: Object at %d.\n", c+1, best-surface)
		} else {
			fmt.Printf("Channel %d: No object.\n", c+1)
		}
	}
}
