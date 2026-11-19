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

func distances(first, to, next []int32, source int32) ([]int32, []int32) {
	distance, order := make([]int32, len(first)), make([]int32, len(first))
	for i := range distance {
		distance[i] = -1
	}
	distance[source], order[0] = 0, source
	used := 1
	for at := 0; at < used; at++ {
		vertex := order[at]
		for edge := first[vertex]; edge >= 0; edge = next[edge] {
			child := to[edge]
			if distance[child] < 0 {
				distance[child] = distance[vertex] + 1
				order[used] = child
				used++
			}
		}
	}
	return distance, order[:used]
}

func main() {
	defer flushOutput()
	count, edges := int(number()), int(number())
	if count == 0 {
		return
	}
	first := make([]int32, count)
	for i := range first {
		first[i] = -1
	}
	to, next := make([]int32, 2*edges), make([]int32, 2*edges)
	used := int32(0)
	add := func(a, b int32) { to[used] = b; next[used] = first[a]; first[a] = used; used++ }
	for i := 0; i < edges; i++ {
		a, b := int32(number()-1), int32(number()-1)
		add(a, b)
		add(b, a)
	}
	start, finish, origin := int32(number()-1), int32(number()-1), int32(number()-1)
	depth, order := distances(first, to, next, start)
	clearance, _ := distances(first, to, next, origin)
	best := make([]int32, count)
	for i := range best {
		best[i] = -1
	}
	best[start] = clearance[start]
	for _, vertex := range order {
		for edge := first[vertex]; edge >= 0; edge = next[edge] {
			child := to[edge]
			if depth[child] == depth[vertex]+1 {
				value := best[vertex]
				if clearance[child] < value {
					value = clearance[child]
				}
				if value > best[child] {
					best[child] = value
				}
			}
		}
	}
	writeNumber(int64(best[finish]))
	writeByte('\n')
}
