package main

import (
	"bufio"
	"os"
	"strconv"
)

const bits = 20 // every number of the message is below 2^20

func main() {
	size := 1 << bits
	// has[j][x]: some prime below 2^20 has its top j bits equal to x
	has := make([][]bool, bits+1)
	has[bits] = make([]bool, size)
	for i := 2; i < size; i++ {
		has[bits][i] = true
	}
	for i := 2; i*i < size; i++ {
		if has[bits][i] {
			for j := i * i; j < size; j += i {
				has[bits][j] = false
			}
		}
	}
	for level := bits - 1; level >= 0; level-- {
		has[level] = make([]bool, 1<<level)
		for x := range has[level] {
			has[level][x] = has[level+1][2*x] || has[level+1][2*x+1]
		}
	}
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	readInt := func() int {
		n := 0
		c, _ := reader.ReadByte()
		for c == ' ' || c == '\n' || c == '\r' {
			c, _ = reader.ReadByte()
		}
		for c >= '0' && c <= '9' {
			n = n*10 + int(c-'0')
			c, _ = reader.ReadByte()
		}
		return n
	}
	t := readInt()
	for ; t > 0; t-- {
		a := readInt()
		// The smallest key is the smallest a xor p over primes p below 2^20,
		// since a key below 2^20 reaches the prime 2; choose the bits of p
		// from the top, keeping the bit of a whenever some prime allows it.
		prefix := 0
		for bit := bits - 1; bit >= 0; bit-- {
			want := prefix*2 + (a >> uint(bit) & 1)
			if has[bits-bit][want] {
				prefix = want
			} else {
				prefix = want ^ 1
			}
		}
		writer.WriteString(strconv.Itoa(a ^ prefix))
		writer.WriteByte('\n')
	}
}
