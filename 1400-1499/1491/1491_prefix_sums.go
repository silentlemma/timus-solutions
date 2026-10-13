package main

import (
	"bufio"
	"os"
	"strconv"
)

const buffer = 1 << 20

func main() {
	reader := bufio.NewReaderSize(os.Stdin, buffer)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readInt := func() int {
		x := 0
		c, _ := reader.ReadByte()
		for c < '0' || c > '9' {
			c, _ = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			x = x*10 + int(c-'0')
			var err error
			if c, err = reader.ReadByte(); err != nil {
				break
			}
		}
		return x
	}
	n := readInt()
	// every gift adds c to the knights a..b: mark it at both ends of the
	// range, then a running sum gives each knight's total
	diff := make([]int64, n+2)
	for k := 0; k <= n; k++ {
		a, b, c := readInt(), readInt(), int64(readInt())
		diff[a] += c
		diff[b+1] -= c
	}
	var total int64
	for i := 1; i <= n; i++ {
		total += diff[i]
		if i > 1 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.FormatInt(total, 10))
	}
	writer.WriteByte('\n')
}
