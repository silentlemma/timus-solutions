package main

import (
	"bufio"
	"io"
	"strconv"
	"syscall"
)

const inputSize = 512
const outputSize = 16
const decimal = 10

type standardInput struct{}

func (standardInput) Read(buffer []byte) (int, error) {
	for {
		n, err := syscall.Read(syscall.Stdin, buffer)
		if err == syscall.EINTR {
			continue
		}
		if n > 0 {
			return n, err
		}
		if err == nil {
			err = io.EOF
		}
		return 0, err
	}
}

func number(input *bufio.Scanner) int {
	input.Scan()
	value := 0
	for _, digit := range input.Bytes() {
		value = decimal*value + int(digit-'0')
	}
	return value
}

func main() {
	input := bufio.NewScanner(standardInput{})
	var buffer [inputSize]byte
	input.Buffer(buffer[:], bufio.MaxScanTokenSize)
	input.Split(bufio.ScanWords)
	count := number(input)
	largest, total := 0, 0
	for i := 0; i < count; i++ {
		size := number(input)
		total += size
		if size > largest {
			largest = size
		}
	}
	best := 2*largest - total
	if best < 1 {
		best = 1
	}
	var digits [outputSize]byte
	output := strconv.AppendInt(digits[:0], int64(best), decimal)
	output = strconv.AppendInt(append(output, ' '), int64(largest), decimal)
	for rest := append(output, '\n'); len(rest) > 0; {
		size, err := syscall.Write(syscall.Stdout, rest)
		if err == syscall.EINTR {
			continue
		}
		if size <= 0 {
			return
		}
		rest = rest[size:]
	}
}
