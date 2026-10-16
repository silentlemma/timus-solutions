package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
	"strconv"
)

const (
	// below this many bits the string is short enough to search directly
	smallBits = 6
	// the palindrome is made of the numbers 2^(k-1) + 5, 2^(k-1) + 6 and
	// the start of 2^(k-1) + 7, three numbers of k bits less two
	numbers = 3
	tail    = 3
)

func longest(n int64) int {
	var b bytes.Buffer
	for i := int64(1); i <= n; i++ {
		b.WriteString(strconv.FormatInt(i, 2))
	}
	s := b.Bytes()
	best := 0
	for centre := 0; centre < 2*len(s)-1; centre++ {
		lo, hi := centre/2, (centre+1)/2
		for lo >= 0 && hi < len(s) && s[lo] == s[hi] {
			lo--
			hi++
		}
		if hi-lo-1 > best {
			best = hi - lo - 1
		}
	}
	return best
}

func main() {
	// the number can have a million digits, so it is read as a stream: its
	// length, its value while short, the first one after the leading one and
	// the last three digits are all that matter
	reader := bufio.NewReader(os.Stdin)
	k, firstOne, last := 0, -1, 0
	var value int64
	for {
		c, err := reader.ReadByte()
		if err != nil {
			break
		}
		if c != '0' && c != '1' {
			continue
		}
		bit := int(c - '0')
		if bit == 1 && k > 0 && firstOne < 0 {
			firstOne = k
		}
		if k < smallBits {
			value = value*2 + int64(bit)
		}
		last = (last*2 + bit) & (1<<tail - 1)
		k++
	}
	if k < smallBits {
		fmt.Println(longest(value))
		return
	}
	// n reaches 2^(k-1) + 7 when a one follows the leading one before the
	// last three bits, or when those bits are all ones
	reached := (firstOne >= 0 && firstOne < k-tail) || last == 1<<tail-1
	bits := k - 1
	if reached {
		bits = k
	}
	fmt.Println(numbers*bits - 2)
}
