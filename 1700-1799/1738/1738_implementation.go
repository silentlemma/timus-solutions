package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	hexPins = 1 << 16
	digits  = 4
	nibble  = 15
	bits    = 4
	base    = 10
)

func main() {
	in := bufio.NewReader(os.Stdin)
	var n int
	fmt.Fscan(in, &n)
	pins := make([]int, n+1)
	for i := 1; i <= n; i++ {
		var text string
		fmt.Fscan(in, &text)
		fmt.Sscanf(text, "%x", &pins[i])
	}
	// differing hex digits of two pins: nonzero nibbles of their xor
	differ := make([]int, hexPins)
	for x := 1; x < hexPins; x++ {
		differ[x] = differ[x>>bits]
		if x&nibble != 0 {
			differ[x]++
		}
	}
	var count [digits + 1]int64
	longest := len(strconv.Itoa(n))
	for i := 1; i <= n; i++ {
		pin := pins[i]
		// each pair is counted from its smaller number: a digit raised in
		// place, which never repeats a number, or a digit inserted
		for place, rest := 1, i; rest > 0; place, rest = place*base, rest/base {
			for d := rest%base + 1; d < base; d++ {
				j := i + (d-rest%base)*place
				if j > n {
					break
				}
				count[differ[pin^pins[j]]]++
			}
		}
		s := strconv.Itoa(i)
		if len(s) >= longest {
			continue
		}
		near := map[int]bool{}
		for p := 0; p <= len(s); p++ {
			for d := byte('0'); d <= '9'; d++ {
				t := s[:p] + string(d) + s[p:]
				if t[0] != '0' {
					j, _ := strconv.Atoi(t)
					near[j] = true
				}
			}
		}
		for j := range near {
			if j <= n {
				count[differ[pin^pins[j]]]++
			}
		}
	}
	for k := 1; k <= digits; k++ {
		sep := " "
		if k == digits {
			sep = "\n"
		}
		fmt.Print(count[k], sep)
	}
}
