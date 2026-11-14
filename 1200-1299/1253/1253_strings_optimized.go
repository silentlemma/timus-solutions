package main

import (
	"bytes"
	"syscall"
)

const (
	maxTemplates  = 9
	maxLength     = 1000
	maxReferences = 10
	limit         = 1000000
	inputSize     = 2*maxTemplates*maxLength + 4*maxTemplates
	blockSize     = 4096
	visiting      = -1
	unseen        = -2
)

var input [inputSize]byte

type piece struct {
	text []byte
	next int
}

var templates [maxTemplates + 1][maxReferences + 1]piece
var lengths [maxTemplates + 1]int
var block [blockSize]byte
var used int
var cache [blockSize]byte
var expanded [maxTemplates + 1][]byte

func measure(i int) int {
	switch lengths[i] {
	case visiting:
		return limit + 1
	case unseen:
		lengths[i] = visiting
	default:
		return lengths[i]
	}
	length := 0
	for _, part := range &templates[i] {
		length += len(part.text)
		if part.next == 0 {
			break
		}
		length += measure(part.next)
		if length > limit {
			break
		}
	}
	lengths[i] = length
	return length
}

func write(text []byte) {
	for len(text) != 0 {
		count := copy(block[used:], text)
		used += count
		text = text[count:]
		if used == len(block) {
			writeAll(block[:])
			used = 0
		}
	}
}

func writeAll(text []byte) {
	for len(text) != 0 {
		written, err := syscall.Write(syscall.Stdout, text)
		if err == syscall.EINTR {
			continue
		}
		if written <= 0 {
			return
		}
		text = text[written:]
	}
}

func emit(i int) {
	if expanded[i] != nil {
		write(expanded[i])
		return
	}
	for _, part := range &templates[i] {
		write(part.text)
		if part.next == 0 {
			break
		}
		if lengths[part.next] != 0 {
			emit(part.next)
		}
	}
}

func flatten(i int, destination []byte) int {
	if expanded[i] != nil {
		return copy(destination, expanded[i])
	}
	used := 0
	for _, part := range &templates[i] {
		used += copy(destination[used:], part.text)
		if part.next == 0 {
			break
		}
		if lengths[part.next] > 0 {
			used += flatten(part.next, destination[used:])
		}
	}
	return used
}

func cacheExpansions(count int) {
	remaining := cache[:]
	for len(remaining) > 0 {
		// Cache the largest expansion that fits, to replace the most work.
		best := 0
		for i := 2; i <= count; i++ {
			if expanded[i] == nil && lengths[i] <= len(remaining) && lengths[i] > lengths[best] {
				best = i
			}
		}
		if best == 0 {
			return
		}
		used := flatten(best, remaining[:lengths[best]])
		expanded[best], remaining = remaining[:used], remaining[used:]
	}
}

func main() {
	size := 0
	for size < len(input) {
		n, err := syscall.Read(syscall.Stdin, input[size:])
		if err == syscall.EINTR {
			continue
		}
		if n <= 0 {
			break
		}
		size += n
	}
	data := input[:0]
	for _, c := range input[:size] {
		if c != '\r' {
			data = append(data, c)
		}
	}
	first := bytes.IndexByte(data, '\n')
	count := int(bytes.TrimSpace(data[:first])[0] - '0')
	rest := data[first+1:]
	for i := 1; i <= count; i++ {
		end := bytes.IndexByte(rest, '#')
		text := rest[:end]
		for j := 0; ; j++ {
			marker := bytes.IndexByte(text, '*')
			if marker < 0 {
				templates[i][j].text = text
				break
			}
			templates[i][j] = piece{text[:marker], int(text[marker+1] - '0')}
			text = text[marker+2:]
		}
		lengths[i] = unseen
		rest = bytes.TrimPrefix(rest[end+1:], []byte("\n"))
	}
	if measure(1) > limit {
		writeAll([]byte("#\n"))
		return
	}
	if lengths[1] > blockSize {
		cacheExpansions(count)
	}
	emit(1)
	write([]byte("\n"))
	writeAll(block[:used])
}
