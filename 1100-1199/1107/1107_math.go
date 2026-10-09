package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufSize = 1 << 16

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufSize)
	// readInt skips separators and reads one non-negative number
	readInt := func() int {
		c, _ := in.ReadByte()
		for c < '0' || c > '9' {
			c, _ = in.ReadByte()
		}
		v := 0
		for c >= '0' && c <= '9' {
			v = v*10 + int(c-'0')
			c, _ = in.ReadByte()
		}
		return v
	}
	n, k := readInt(), readInt()
	readInt()
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	out.WriteString("YES\n")
	// removing an item changes the sum by 1..N and replacing one by -N+1..N-1,
	// never by a multiple of N + 1, so similar sets differ modulo N + 1
	for i := 0; i < k; i++ {
		count, sum := readInt(), 0
		for j := 0; j < count; j++ {
			sum += readInt()
		}
		out.WriteString(strconv.Itoa(sum%(n+1)+1) + "\n")
	}
}
