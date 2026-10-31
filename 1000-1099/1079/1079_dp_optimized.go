package main

import (
	"bufio"
	"os"
	"strconv"
)

const top = 99999
const lastParent = (top + 1) / 2

// parsing digits directly avoids formatted input and per-token allocations.
func readInt(in *bufio.Reader) int {
	value := 0
	c, err := in.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.ReadByte()
	}
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, err = in.ReadByte()
	}
	return value
}

func main() {
	// n < 2^17 bounds every stern value by fibonacci(19) = 4181, fitting 16 bits.
	a := make([]uint16, lastParent+1)
	best := make([]uint16, top+1)
	a[1], best[1] = 1, 1
	for i := 2; i <= top; i++ {
		value := a[i/2]
		if i%2 != 0 {
			value += a[i/2+1]
		}
		// later terms only refer to indices in the first half.
		if i <= lastParent {
			a[i] = value
		}
		best[i] = best[i-1]
		if value > best[i] {
			best[i] = value
		}
	}
	in := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()
	for {
		n := readInt(in)
		if n == 0 {
			break
		}
		w.WriteString(strconv.Itoa(int(best[n])))
		w.WriteByte('\n')
	}
}
