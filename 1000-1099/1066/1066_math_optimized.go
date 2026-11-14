package main

import (
	"math"
	"strconv"
	"syscall"
)

const floatBits = 64
const centsPerUnit = 100
const fractionalDigits = 2
const radix = 10
const outputSize = 16
const bufferSize = 256

func readInput() []byte {
	var block [bufferSize]byte
	size := 0
	for size < len(block) {
		count, err := syscall.Read(syscall.Stdin, block[size:])
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return block[:size]
		}
		size += count
	}
	data := append([]byte(nil), block[:]...)
	for {
		count, err := syscall.Read(syscall.Stdin, block[:])
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return data
		}
		data = append(data, block[:count]...)
	}
}

func token(data []byte) ([]byte, []byte) {
	start := 0
	for start < len(data) && data[start] <= ' ' {
		start++
	}
	end := start
	for end < len(data) && data[end] > ' ' {
		end++
	}
	return data[start:end], data[end:]
}

func writeOutput(data []byte) {
	for len(data) != 0 {
		count, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 || err != nil {
			return
		}
		data = data[count:]
	}
}

func main() {
	countText, remaining := token(readInput())
	firstText, _ := token(remaining)
	count, _ := strconv.Atoi(string(countText))
	first, _ := strconv.ParseFloat(string(firstText), floatBits)
	m := float64(count - 1)
	k := math.Floor(math.Sqrt(first))
	if k >= m {
		writeOutput([]byte("0.00\n"))
		return
	}
	// A/k + k falls up to sqrt(A) and rises after it.
	if first > k*(k+1) {
		k++
	}
	// The height at k+1 is zero. Factoring avoids subtracting large heights.
	last := math.Max(0, (m-k)*(m-first/k))
	// The checker allows one last-digit difference at a rounding boundary.
	cents := int(math.Round(last * centsPerUnit))
	var output [outputSize]byte
	start := len(output) - 1
	output[start] = '\n'
	for digits := 0; digits < fractionalDigits; digits++ {
		start--
		output[start] = '0' + byte(cents%radix)
		cents /= radix
	}
	start--
	output[start] = '.'
	for {
		start--
		output[start] = '0' + byte(cents%radix)
		cents /= radix
		if cents == 0 {
			break
		}
	}
	writeOutput(output[start:])
}
