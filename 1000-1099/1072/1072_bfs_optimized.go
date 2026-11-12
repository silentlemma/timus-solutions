package main

import "syscall"

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

const inputSize = 256

var input [inputSize]byte
var position, length int

func nextByte() byte {
	if position == length {
		length = readInput(input[:])
		position = 0
		if length == 0 {
			return 0
		}
	}
	value := input[position]
	position++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	sign := 1
	if c == '-' {
		sign = -1
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*10 + int(c-'0')
		c = nextByte()
	}
	return sign * value
}

const outputSize = 512

var output [outputSize]byte
var used int

func writeNumber(value int) {
	const maxDigits = 20
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
	used += copy(output[used:], digits[first:])
}

const octetBits = 8

func address() uint32 {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	var value, octet uint32
	for c > ' ' {
		if c == '.' {
			value = value<<octetBits | octet
			octet = 0
		} else {
			octet = octet*10 + uint32(c-'0')
		}
		c = nextByte()
	}
	return value<<octetBits | octet
}

func main() {
	n := number()
	nets := make([][]uint32, n)
	members := make(map[uint32][]int)
	for computer := range nets {
		k := number()
		nets[computer] = make([]uint32, k)
		for i := range nets[computer] {
			ip := address()
			network := ip & address()
			nets[computer][i] = network
			members[network] = append(members[network], computer)
		}
	}
	start, end := number()-1, number()-1
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	parent[start] = start
	queue := make([]int, 1, n)
	queue[0] = start
	for head := 0; head < len(queue) && parent[end] < 0; head++ {
		computer := queue[head]
		for _, network := range nets[computer] {
			for _, next := range members[network] {
				if parent[next] < 0 {
					parent[next] = computer
					queue = append(queue, next)
				}
			}
			// The first expansion reaches every member at its shortest possible distance.
			delete(members, network)
		}
	}
	if parent[end] < 0 {
		writeAll([]byte("No\n"))
		return
	}
	path := make([]int, 0, n)
	for vertex := end; ; vertex = parent[vertex] {
		path = append(path, vertex)
		if vertex == start {
			break
		}
	}
	used = copy(output[:], "Yes\n")
	for i := len(path) - 1; i >= 0; i-- {
		writeNumber(path[i] + 1)
		output[used] = ' '
		used++
	}
	output[used-1] = '\n'
	writeAll(output[:used])
}
