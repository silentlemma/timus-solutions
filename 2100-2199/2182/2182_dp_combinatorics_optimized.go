package main

import (
	"bufio"
	"math/bits"
	"os"
	"strconv"
)

const (
	maxBits     = 60
	decimalBase = 10
	inputSize   = 4096
)

type input struct {
	buffer [inputSize]byte
	at     int
	size   int
}

func (in *input) readByte() byte {
	if in.at == in.size {
		in.size, _ = os.Stdin.Read(in.buffer[:])
		in.at = 0
		if in.size == 0 {
			return 0
		}
	}
	c := in.buffer[in.at]
	in.at++
	return c
}

func (in *input) number() uint64 {
	c := in.readByte()
	for c != 0 && c <= ' ' {
		c = in.readByte()
	}
	var value uint64
	for '0' <= c && c <= '9' {
		value = value*decimalBase + uint64(c-'0')
		c = in.readByte()
	}
	return value
}

func counts(n int) [maxBits + 1]uint64 {
	var count [maxBits + 1]uint64
	combinations := uint64(1)
	for k := 1; k <= n; k++ {
		combinations = combinations * uint64(n-k+1) / uint64(k)
		count[k] = 1 + combinations
	}
	count[1]--
	// Only the extra bottles remain to be passed to a smaller box.
	for k := n; k > 1; k-- {
		count[bits.OnesCount(uint(k))] += count[k] - 1
	}
	return count
}

func main() {
	var reader input
	n, q := int(reader.number()), int(reader.number())
	count := counts(n)
	var text [maxBits + 1]string
	for k := 1; k <= n; k++ {
		text[k] = strconv.FormatUint(count[k], decimalBase)
	}
	writer := bufio.NewWriter(os.Stdout)
	for i := 0; i < q; i++ {
		box := reader.number()
		if i > 0 {
			writer.WriteByte(' ')
		}
		if box <= uint64(n) {
			writer.WriteString(text[box])
		} else {
			writer.WriteByte('1')
		}
	}
	writer.WriteByte('\n')
	writer.Flush()
}
