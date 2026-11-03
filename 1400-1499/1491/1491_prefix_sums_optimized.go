package main

import (
	"bufio"
	"os"
	"strconv"
)

const buffer = 4096

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
	diff := make([]int32, n+2)
	for k := 0; k <= n; k++ {
		a, b, c := readInt(), readInt(), int32(readInt())
		diff[a] += c
		diff[b+1] -= c
	}
	// At most(n+1)*10000<=1000010000 coins, so int32 cells cannot overflow.
	var total int32
	for i := 1; i <= n; i++ {
		total += diff[i]
		if i > 1 {
			writer.WriteByte(' ')
		}
		writer.WriteString(strconv.FormatInt(int64(total), 10))
	}
	writer.WriteByte('\n')
}
