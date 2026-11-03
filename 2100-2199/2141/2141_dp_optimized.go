package main

import (
	"bufio"
	"os"
	"strconv"
)

const bufferSize = 4096
const outputSize = 32

var reader = bufio.NewReaderSize(os.Stdin, bufferSize)

func nextInt() int64 {
	ch, _ := reader.ReadByte()
	for ch <= ' ' {
		ch, _ = reader.ReadByte()
	}
	sign, value := int64(1), int64(0)
	if ch == '-' {
		sign = -1
		ch, _ = reader.ReadByte()
	}
	for ch >= '0' && ch <= '9' {
		value = value*10 + int64(ch-'0')
		ch, _ = reader.ReadByte()
	}
	return sign * value
}

func main() {
	n := nextInt()
	plus, minus := nextInt(), int64(0)
	best := plus
	if best < 0 {
		best = 0
	}
	for i := int64(1); i < n; i++ {
		value := nextInt()
		nextPlus := value
		if minus > 0 {
			nextPlus += minus
		}
		minus = plus - value
		plus = nextPlus
		if plus > best {
			best = plus
		}
		if minus > best {
			best = minus
		}
	}
	var storage [outputSize]byte
	out := strconv.AppendInt(storage[:0], best, 10)
	out = append(out, '\n')
	os.Stdout.Write(out)
}
