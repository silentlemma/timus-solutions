package main

import "os"

const maxInt64Digits = 20

const ioCapacity = 4096

var inputBuffer [ioCapacity]byte
var inputAt, inputSize int
var outputBuffer [ioCapacity]byte
var outputSize int

func nextByte() int {
	for inputAt == inputSize {
		count, err := os.Stdin.Read(inputBuffer[:])
		inputAt, inputSize = 0, count
		if count == 0 && err != nil {
			return -1
		}
	}
	value := inputBuffer[inputAt]
	inputAt++
	return int(value)
}

func readNumber() (int64, bool) {
	character := nextByte()
	for character >= 0 && character <= ' ' {
		character = nextByte()
	}
	if character < 0 {
		return 0, false
	}
	negative := character == '-'
	if negative || character == '+' {
		character = nextByte()
	}
	var value int64
	for character >= '0' && character <= '9' {
		// Negative accumulation also handles the minimum signed 64-bit value.
		value = value*10 - int64(character-'0')
		character = nextByte()
	}
	if negative {
		return value, true
	}
	return -value, true
}

func number() int64 { value, _ := readNumber(); return value }

func wordByte() byte {
	character := nextByte()
	for character >= 0 && character <= ' ' {
		character = nextByte()
	}
	first := byte(character)
	for character > ' ' {
		character = nextByte()
	}
	return first
}

func flushOutput() {
	for start := 0; start < outputSize; {
		count, err := os.Stdout.Write(outputBuffer[start:outputSize])
		if err != nil || count == 0 {
			os.Exit(1)
		}
		start += count
	}
	outputSize = 0
}

func writeByte(value byte) {
	if outputSize == len(outputBuffer) {
		flushOutput()
	}
	outputBuffer[outputSize] = value
	outputSize++
}

func writeNumber(value int64) {
	magnitude := uint64(value)
	if value < 0 {
		writeByte('-')
		magnitude = uint64(-(value + 1)) + 1
	}
	var digits [maxInt64Digits]byte
	first := len(digits)
	for {
		first--
		digits[first] = '0' + byte(magnitude%10)
		magnitude /= 10
		if magnitude == 0 {
			break
		}
	}
	for _, digit := range digits[first:] {
		writeByte(digit)
	}
}

func writeText(text string) {
	for index := 0; index < len(text); index++ {
		writeByte(text[index])
	}
}

func main() {
	defer flushOutput()
	count := int(number())
	first := make([]int32, count+1)
	for i := range first {
		first[i] = -1
	}
	to, next := make([]int32, 2*(count-1)), make([]int32, 2*(count-1))
	edge := int32(0)
	add := func(a, b int32) { to[edge] = b; next[edge] = first[a]; first[a] = edge; edge++ }
	for i := 1; i < count; i++ {
		a, b := int32(number()), int32(number())
		add(a, b)
		add(b, a)
	}
	parent, depth := make([]int32, count+1), make([]int32, count+1)
	order := make([]int32, count)
	order[0], parent[1] = 1, -1
	used := 1
	for at := 0; at < used; at++ {
		vertex := order[at]
		for edge := first[vertex]; edge >= 0; edge = next[edge] {
			child := to[edge]
			if child != parent[vertex] {
				parent[child], depth[child] = vertex, depth[vertex]+1
				order[used] = child
				used++
			}
		}
	}
	size, heavy := make([]int32, count+1), make([]int32, count+1)
	for i := 1; i <= count; i++ {
		size[i] = 1
	}
	for i := count - 1; i > 0; i-- {
		vertex := order[i]
		p := parent[vertex]
		size[p] += size[vertex]
		if heavy[p] == 0 || size[vertex] > size[heavy[p]] {
			heavy[p] = vertex
		}
	}
	chain, position := make([]int32, count+1), make([]int32, count+1)
	index := int32(0)
	for _, vertex := range order {
		if vertex == 1 || heavy[parent[vertex]] != vertex {
			for child := vertex; child != 0; child = heavy[child] {
				chain[child], position[child] = vertex, index
				index++
			}
		}
	}
	width := int32(1)
	for width < int32(count) {
		width <<= 1
	}
	// At most 100000 increments of 10000 keep every level within signed int32.
	tree := make([]int32, 2*width)
	maximum := func(low, high int32) int32 {
		var best int32
		for low, high = low+width, high+width+1; low < high; low, high = low>>1, high>>1 {
			if low&1 != 0 {
				if tree[low] > best {
					best = tree[low]
				}
				low++
			}
			if high&1 != 0 {
				high--
				if tree[high] > best {
					best = tree[high]
				}
			}
		}
		return best
	}
	queries := int(number())
	for query := 0; query < queries; query++ {
		kind := wordByte()
		a, b := int32(number()), int32(number())
		if kind == 'I' {
			at := position[a] + width
			tree[at] += b
			for at >>= 1; at > 0; at >>= 1 {
				tree[at] = tree[2*at]
				if tree[2*at+1] > tree[at] {
					tree[at] = tree[2*at+1]
				}
			}
			continue
		}
		var best int32
		for chain[a] != chain[b] {
			if depth[chain[a]] < depth[chain[b]] {
				a, b = b, a
			}
			if value := maximum(position[chain[a]], position[a]); value > best {
				best = value
			}
			a = parent[chain[a]]
		}
		low, high := position[a], position[b]
		if low > high {
			low, high = high, low
		}
		if value := maximum(low, high); value > best {
			best = value
		}
		writeNumber(int64(best))
		writeByte('\n')
	}
}
