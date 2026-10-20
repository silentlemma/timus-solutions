package main

import (
	"bufio"
	"os"
	"strconv"
)

const modulus int64 = 998244353
const primitiveRoot int64 = 3
const ioBufferSize = 1 << 16

func power(base int64, exponent int64) int64 {
	result := int64(1)
	for exponent > 0 {
		if exponent&1 != 0 {
			result = result * base % modulus
		}
		base = base * base % modulus
		exponent >>= 1
	}
	return result
}

func makeRoots(size int) []int64 {
	roots := make([]int64, size)
	roots[1] = 1
	for length := 2; length < size; length <<= 1 {
		step := power(primitiveRoot, (modulus-1)/int64(length*2))
		for index := length / 2; index < length; index++ {
			roots[index*2] = roots[index]
			roots[index*2+1] = roots[index] * step % modulus
		}
	}
	return roots
}

func forwardTransform(values, roots []int64) {
	size := len(values)
	for length := size; length > 1; length >>= 1 {
		half := length / 2
		for start := 0; start < size; start += length {
			for offset := 0; offset < half; offset++ {
				first := values[start+offset]
				second := values[start+offset+half]
				sum := first + second
				if sum >= modulus {
					sum -= modulus
				}
				difference := first - second
				if difference < 0 {
					difference += modulus
				}
				values[start+offset] = sum
				values[start+offset+half] = difference * roots[half+offset] % modulus
			}
		}
	}
}

func reverseTransform(values, roots []int64) {
	size := len(values)
	for length := 2; length <= size; length <<= 1 {
		half := length / 2
		for start := 0; start < size; start += length {
			for offset := 0; offset < half; offset++ {
				first := values[start+offset]
				second := values[start+offset+half] * roots[half+offset] % modulus
				sum := first + second
				if sum >= modulus {
					sum -= modulus
				}
				difference := first - second
				if difference < 0 {
					difference += modulus
				}
				values[start+offset] = sum
				values[start+offset+half] = difference
			}
		}
	}
}

type fastInput struct {
	reader *bufio.Reader
}

func (input *fastInput) nextInt() int {
	value := 0
	character, err := input.reader.ReadByte()
	for err == nil && character <= ' ' {
		character, err = input.reader.ReadByte()
	}
	for err == nil && character >= '0' && character <= '9' {
		value = value*10 + int(character-'0')
		character, err = input.reader.ReadByte()
	}
	return value
}

func main() {
	input := fastInput{bufio.NewReaderSize(os.Stdin, ioBufferSize)}
	n, m := input.nextInt(), input.nextInt()
	total := n + m
	size := 1
	for size < n+total-1 {
		size <<= 1
	}
	factorial := make([]int64, total)
	inverseFactorial := make([]int64, total)
	factorial[0] = 1
	for index := 1; index < total; index++ {
		factorial[index] = factorial[index-1] * int64(index) % modulus
	}
	inverseFactorial[total-1] = power(factorial[total-1], modulus-2)
	for index := total - 1; index > 0; index-- {
		inverseFactorial[index-1] = inverseFactorial[index] * int64(index) % modulus
	}

	first := make([]int64, size)
	second := make([]int64, size)
	for index := 0; index < n; index++ {
		value := int64(input.nextInt())
		weight := value * inverseFactorial[index] % modulus
		weight = weight * inverseFactorial[n-1-index] % modulus
		if (n-1-index)&1 != 0 && weight != 0 {
			weight = modulus - weight
		}
		first[index] = weight
	}
	for index := 1; index < total; index++ {
		second[index] = factorial[index-1] * inverseFactorial[index] % modulus
	}

	roots := makeRoots(size)
	forwardTransform(first, roots)
	forwardTransform(second, roots)
	for index := 0; index < size; index++ {
		first[index] = first[index] * second[index] % modulus
	}
	reverseTransform(first, roots)

	// The paired passes leave coefficients reversed and multiplied by size.
	inverseSize := power(int64(size), modulus-2)
	output := bufio.NewWriterSize(os.Stdout, ioBufferSize)
	buffer := make([]byte, 0, ioBufferSize)
	for index := n; index < total; index++ {
		answer := first[size-index] * inverseSize % modulus
		answer = answer * factorial[index] % modulus * inverseFactorial[index-n] % modulus
		if index > n {
			buffer = append(buffer, ' ')
		}
		buffer = strconv.AppendInt(buffer, answer, 10)
		if len(buffer) >= ioBufferSize {
			output.Write(buffer)
			buffer = buffer[:0]
		}
	}
	buffer = append(buffer, '\n')
	output.Write(buffer)
	output.Flush()
}
