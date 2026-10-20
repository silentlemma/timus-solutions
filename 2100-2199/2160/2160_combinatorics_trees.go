package main

import (
	"fmt"
	"io/ioutil"
	"os"
)

const (
	mod       int64 = 1_000_000_007
	digitZero byte  = '0'
	space     byte  = ' '
)

type entry struct {
	value int
	size  int
}

type scanner struct {
	data  []byte
	index int
}

func (input *scanner) nextInt() int {
	for input.index < len(input.data) && input.data[input.index] <= space {
		input.index++
	}
	value := 0
	for input.index < len(input.data) && input.data[input.index] > space {
		value = value*10 + int(input.data[input.index]-digitZero)
		input.index++
	}
	return value
}

func modularPower(base, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent%2 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		exponent /= 2
	}
	return result
}

func main() {
	data, _ := ioutil.ReadAll(os.Stdin)
	input := scanner{data: data}
	n := input.nextInt()
	stack := make([]entry, 0, n)
	factorial := int64(1)
	denominator := int64(1)

	for i := 1; i <= n; i++ {
		value := input.nextInt()
		size := 0
		// Popped nodes now have complete Cartesian subtrees.
		for len(stack) > 0 && stack[len(stack)-1].value > value {
			size += stack[len(stack)-1].size
			stack = stack[:len(stack)-1]
			denominator = denominator * int64(size) % mod
		}
		stack = append(stack, entry{value: value, size: size + 1})
		factorial = factorial * int64(i) % mod
	}

	size := 0
	for len(stack) > 0 {
		size += stack[len(stack)-1].size
		stack = stack[:len(stack)-1]
		denominator = denominator * int64(size) % mod
	}

	// The tree hook-length formula counts the equivalent permutations.
	fmt.Println(factorial * modularPower(denominator, mod-2) % mod)
}
