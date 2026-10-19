package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	bufferSize = 1 << 16
	unknown    = -1
)

func nextInt(reader *bufio.Reader) int64 {
	character, _ := reader.ReadByte()
	for character <= ' ' {
		character, _ = reader.ReadByte()
	}
	sign := int64(1)
	if character == '-' {
		sign = -1
		character, _ = reader.ReadByte()
	}
	value := int64(0)
	for character >= '0' && character <= '9' {
		value = value*10 + int64(character-'0')
		character, _ = reader.ReadByte()
	}
	return value * sign
}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, bufferSize)
	n := nextInt(reader)
	remaining := n - 2
	fixedWeight := int64(0)
	unknownCount := int64(0)
	unknownSum := int64(0)
	for vertex := int64(1); vertex <= n; vertex++ {
		degree := nextInt(reader)
		if degree == unknown {
			unknownCount++
			unknownSum += vertex
		} else {
			remaining -= degree - 1
			fixedWeight += vertex * (degree - 1)
		}
	}
	answer := n*(n+1)/2 + n*fixedWeight
	if unknownCount != 0 {
		// Divide before multiplying by n to keep every product in 64 bits.
		product := remaining * unknownSum
		answer += n * (product / unknownCount)
		answer += n * (product % unknownCount) / unknownCount
	}
	fmt.Println(answer)
}
