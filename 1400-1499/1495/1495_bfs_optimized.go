package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	base        = 10
	maxDigits   = 30
	divisorFive = 5
)

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	if !input.Scan() {
		return
	}
	modulus, _ := strconv.Atoi(input.Text())
	if modulus%divisorFive == 0 {
		os.Stdout.WriteString("Impossible\n")
		return
	}

	// The low bit stores the last digit minus one, and zero means unseen.
	parent := make([]uint32, modulus)
	queue := make([]uint32, 0, modulus)
	add := func(previous, digit, remainder int) {
		if parent[remainder] == 0 {
			parent[remainder] = uint32(previous+1)<<1 | uint32(digit-1)
			queue = append(queue, uint32(remainder))
		}
	}
	add(modulus, 1, 1%modulus)
	add(modulus, 2, 2%modulus)
	head := 0
	for length := 1; length < maxDigits && head < len(queue) && parent[0] == 0; length++ {
		end := len(queue)
		for head < end && parent[0] == 0 {
			remainder := int(queue[head])
			head++
			add(remainder, 1, (remainder*base+1)%modulus)
			add(remainder, 2, (remainder*base+2)%modulus)
		}
	}
	if parent[0] == 0 {
		os.Stdout.WriteString("Impossible\n")
		return
	}
	var output [maxDigits + 1]byte
	offset := maxDigits
	output[offset] = '\n'
	for remainder := 0; remainder != modulus; {
		entry := parent[remainder]
		offset--
		output[offset] = '1' + byte(entry&1)
		remainder = int(entry>>1) - 1
	}
	os.Stdout.Write(output[offset:])
}
