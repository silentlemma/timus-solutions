package main

import "syscall"

const (
	inputSize   = 64
	outputSize  = 16
	maxDigits   = 20
	maxSoldiers = 100
	trio        = 3
)

var input [inputSize]byte
var inputPosition, inputLength int

// Use standard handles directly; retry interrupts and finish short writes.
func readInput(buffer []byte) int {
	for {
		count, err := syscall.Read(syscall.Stdin, buffer)
		if count > 0 {
			return count
		}
		if err != syscall.EINTR {
			return 0
		}
	}
}

func writeAll(buffer []byte) {
	for len(buffer) > 0 {
		count, err := syscall.Write(syscall.Stdout, buffer)
		if count > 0 {
			buffer = buffer[count:]
		}
		if err == syscall.EINTR {
			continue
		}
		if count <= 0 {
			return
		}
	}
}

func nextByte() byte {
	if inputPosition == inputLength {
		inputLength = readInput(input[:])
		inputPosition = 0
		if inputLength == 0 {
			return 0
		}
	}
	value := input[inputPosition]
	inputPosition++
	return value
}

func symbol() byte {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	return c
}

func number() int64 {
	c := symbol()
	value := int64(0)
	for c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c = nextByte()
	}
	return value
}

func appendNumber(output []byte, value int64) []byte {
	var digits [maxDigits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(value%10)
		value /= 10
		if value == 0 {
			break
		}
	}
	return append(output, digits[first:]...)
}

var times [maxSoldiers]uint16

func siftDown(root, length int) {
	for {
		child := 2*root + 1
		if child >= length {
			return
		}
		if child+1 < length && times[child] < times[child+1] {
			child++
		}
		if times[root] >= times[child] {
			return
		}
		times[root], times[child] = times[child], times[root]
		root = child
	}
}

func main() {
	n := int(number())
	for i := 0; i < n; i++ {
		times[i] = uint16(number())
	}
	for root := n/2 - 1; root >= 0; root-- {
		siftDown(root, n)
	}
	for length := n - 1; length > 0; length-- {
		times[0], times[length] = times[length], times[0]
		siftDown(0, length)
	}
	first, second := int(times[0]), int(times[1])
	total := 0
	for n > trio {
		escort := 2*first + int(times[n-2])
		pair := first + 2*second
		if pair < escort {
			escort = pair
		}
		total += int(times[n-1]) + escort
		n -= 2
	}
	total += second
	if n == trio {
		total += first + int(times[trio-1])
	}
	var storage [outputSize]byte
	output := appendNumber(storage[:0], int64(total))
	writeAll(append(output, '\n'))
}
