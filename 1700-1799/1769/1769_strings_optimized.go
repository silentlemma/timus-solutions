package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
)

const base = 10
const digits = 6
const wordBits = 64

func main() {
	input, _ := ioutil.ReadAll(os.Stdin)
	text := bytes.TrimSpace(input)
	first := 1
	// Try lengths in order; the first absent value is the global answer.
	for length := 1; length <= digits; length++ {
		count, modulus, value := (base-1)*first, first*base, 0
		seen := make([]uint64, (count+wordBits-1)/wordBits)
		for i, digit := range text {
			value = (value*base + int(digit-'0')) % modulus
			if i+1 >= length && value >= first {
				offset := value - first
				seen[offset/wordBits] |= uint64(1) << uint(offset%wordBits)
			}
		}
		for offset := 0; offset < count; offset++ {
			if seen[offset/wordBits]&(uint64(1)<<uint(offset%wordBits)) == 0 {
				fmt.Println(first + offset)
				return
			}
		}
		first *= base
	}
}
