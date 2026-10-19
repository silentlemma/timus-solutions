package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

func power(value int64, exponent int) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * value % modulus
		}
		value = value * value % modulus
		exponent >>= 1
	}
	return result
}

func settingsCounts(size int) []int64 {
	ways := make([]int64, size+1)
	for count := 1; count <= size; count++ {
		closed := int64(0)
		base := int64(count)
		for prefix := 1; prefix < count; prefix++ {
			closed = (closed*base + ways[prefix]) % modulus
		}
		difference := (power(base, count-1) - closed + modulus) % modulus
		ways[count] = base * difference % modulus
	}
	return ways
}

func main() {
	var size int
	fmt.Fscan(bufio.NewReader(os.Stdin), &size)
	fmt.Println(settingsCounts(size)[size])
}
