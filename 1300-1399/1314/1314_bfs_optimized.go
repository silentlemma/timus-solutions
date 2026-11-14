package main

import (
	"math/bits"
	"strconv"
	"syscall"
)

const (
	stationIDs     = 32768
	stationDigits  = 5
	stationsInWord = 64
	stationWords   = stationIDs / stationsInWord
	maxLines       = 50
	maxLineStops   = 50
	maxStops       = maxLines * maxLineStops
	maxEdges       = maxLines * (maxLineStops - 1)
	inputSize      = 4096
	outputSize     = 1024
	decimal        = 10
	possible       = uint16(1 << 15)
)

type edge struct{ a, b uint16 }

var (
	input    [inputSize]byte
	start    int
	end      int
	output   [outputSize]byte
	present  [stationWords]uint64
	prefix   [stationWords + 1]uint16
	edges    [maxEdges]edge
	offset   [maxStops + 2]uint16
	adjacent [2 * maxEdges]uint16
	layer    [maxStops + 1]uint16
	frontier [maxStops]uint16
)

func nextByte() byte {
	if start == end {
		for {
			n, err := syscall.Read(syscall.Stdin, input[:])
			if err == syscall.EINTR {
				continue
			}
			if n <= 0 {
				return 0
			}
			start, end = 0, n
			break
		}
	}
	value := input[start]
	start++
	return value
}

func number() int {
	c := nextByte()
	for c != 0 && c <= ' ' {
		c = nextByte()
	}
	value := 0
	for '0' <= c && c <= '9' {
		value = value*decimal + int(c-'0')
		c = nextByte()
	}
	return value
}

func add(station uint16) {
	present[station/stationsInWord] |= uint64(1) << (station % stationsInWord)
}

func rank(station uint16) uint16 {
	word := station / stationsInWord
	mask := uint64(1) << (station % stationsInWord)
	if present[word]&mask == 0 {
		return 0
	}
	return prefix[word] + uint16(bits.OnesCount64(present[word]&(mask-1))) + 1
}

func buildGraph() {
	count := 0
	lines := number()
	for i := 0; i < lines; i++ {
		length := number()
		previous := uint16(number())
		add(previous)
		for j := 1; j < length; j++ {
			next := uint16(number())
			add(next)
			edges[count] = edge{previous, next}
			count++
			previous = next
		}
	}
	for i, word := range present {
		prefix[i+1] = prefix[i] + uint16(bits.OnesCount64(word))
	}
	size := prefix[stationWords]
	for i, e := range edges[:count] {
		a, b := rank(e.a), rank(e.b)
		edges[i] = edge{a, b}
		offset[a]++
		offset[b]++
	}
	for i := uint16(1); i <= size; i++ {
		offset[i] += offset[i-1]
	}
	offset[size+1] = offset[size]
	// Filling each range backwards turns the end offsets into start offsets.
	for _, e := range edges[:count] {
		offset[e.a]--
		adjacent[offset[e.a]] = e.b
		offset[e.b]--
		adjacent[offset[e.b]] = e.a
	}
}

func neighbors(station uint16) []uint16 {
	return adjacent[offset[station]:offset[station+1]]
}

func follows(from, to uint16) bool {
	for _, neighbor := range neighbors(from) {
		if neighbor == to {
			return true
		}
	}
	return false
}

func markTargets(first uint16, count int) bool {
	if first == 0 {
		return false
	}
	last := first
	for i := 1; i < count; i++ {
		next := rank(uint16(number()))
		if !follows(last, next) {
			return false
		}
		last = next
	}
	layer[first], frontier[0] = 1, first
	used := 1
	for i := 0; i < used; i++ {
		station := frontier[i]
		for _, next := range neighbors(station) {
			if layer[next] == 0 {
				layer[next] = layer[station] + 1
				frontier[used] = next
				used++
			}
		}
	}
	if int(layer[last]) != count {
		return false
	}
	// Distances fit below the high bit, which marks shortest-path continuations.
	layer[last] |= possible
	for _, station := range frontier[:used] {
		if layer[station]&possible == 0 {
			continue
		}
		want := (layer[station] &^ possible) + 1
		for _, next := range neighbors(station) {
			if layer[next] == want {
				layer[next] |= possible
			}
		}
	}
	return true
}

func write(data []byte) {
	for len(data) > 0 {
		n, err := syscall.Write(syscall.Stdout, data)
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			return
		}
		data = data[n:]
	}
}

func printTargets() {
	buffer := output[:0]
	for i, word := range present {
		station := prefix[i] + 1
		for word != 0 {
			if layer[station]&possible != 0 {
				if len(buffer)+stationDigits+1 > cap(buffer) {
					write(buffer)
					buffer = buffer[:0]
				}
				id := i*stationsInWord + bits.TrailingZeros64(word)
				buffer = append(strconv.AppendInt(buffer, int64(id), decimal), '\n')
			}
			word &= word - 1
			station++
		}
	}
	write(buffer)
}

func main() {
	buildGraph()
	count, first := number(), rank(uint16(number()))
	if markTargets(first, count) {
		printTargets()
	}
}
