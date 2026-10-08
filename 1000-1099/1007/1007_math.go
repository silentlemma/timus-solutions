package main

import (
	"bufio"
	"fmt"
	"os"
)

// restore undoes at most one change: the sum of the positions (from 1) of the
// ones of a sent word is divisible by n+1.
func restore(s []byte, n int) []byte {
	mod := n + 1
	w := 0
	for i, c := range s {
		if c == '1' {
			w += i + 1
		}
	}
	if len(s) == n {
		// a raised zero at position p adds exactly p to the weight
		if w%mod != 0 {
			s[w%mod-1] = '0'
		}
		return s
	}
	// onesAfter: ones to the right of the changed place; they shift by one
	onesAfter := 0
	if len(s) == n-1 {
		for i := len(s); i >= 0; i-- {
			for d := 0; d <= 1; d++ {
				if (w+onesAfter+d*(i+1))%mod == 0 {
					return append(append(append([]byte{}, s[:i]...), byte('0'+d)), s[i:]...)
				}
			}
			if i > 0 && s[i-1] == '1' {
				onesAfter++
			}
		}
	} else {
		for i := len(s) - 1; i >= 0; i-- {
			if (w-onesAfter-int(s[i]-'0')*(i+1))%mod == 0 {
				return append(s[:i:i], s[i+1:]...)
			}
			if s[i] == '1' {
				onesAfter++
			}
		}
	}
	return s
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n int
	fmt.Fscan(in, &n)
	sc := bufio.NewScanner(in)
	sc.Buffer(make([]byte, 0, bufio.MaxScanTokenSize), bufio.MaxScanTokenSize)
	sc.Split(bufio.ScanWords)
	for sc.Scan() {
		out.Write(restore(append([]byte{}, sc.Bytes()...), n))
		out.WriteByte('\n')
	}
}
