package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

// each token contains exactly n bytes, so readfull avoids growing line buffers.
func readString(in *bufio.Reader, n int) []byte {
	// characters from 33 to 255 may come, so skip only bytes up to the space
	c, _ := in.ReadByte()
	for c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := make([]byte, n)
	value[0] = c
	io.ReadFull(in, value[1:])
	return value
}

func main() {
	in := bufio.NewReader(os.Stdin)
	first, _ := in.ReadString('\n')
	n, _ := strconv.Atoi(strings.TrimSpace(first))
	s, t := readString(in, n), readString(in, n)

	// t is s turned left by k, that is right by n - k: find it in s + s with KMP
	// n is at most 250000, so prefix lengths fit in 32 bits.
	fail := make([]int32, n)
	for i, k := 1, 0; i < n; i++ {
		for k > 0 && t[i] != t[k] {
			k = int(fail[k-1])
		}
		if t[i] == t[k] {
			k++
		}
		fail[i] = int32(k)
	}
	for i, k := 0, 0; i+1 < 2*n; i++ {
		c := s[i%n]
		for k > 0 && c != t[k] {
			k = int(fail[k-1])
		}
		if c == t[k] {
			k++
		}
		if k == n {
			start := i - n + 1
			fmt.Println((n - start) % n)
			return
		}
	}
	fmt.Println(-1)
}
