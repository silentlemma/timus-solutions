package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	bufferSize = 32 * 1024
	lineSize   = 24
	base       = 10
)

type scanner struct {
	buffer    [bufferSize]byte
	next, end int
}

func (s *scanner) readByte() byte {
	if s.next == s.end {
		s.end, _ = os.Stdin.Read(s.buffer[:])
		s.next = 0
		if s.end == 0 {
			return 0
		}
	}
	ch := s.buffer[s.next]
	s.next++
	return ch
}

func (s *scanner) number() int {
	ch := s.readByte()
	for ch != 0 && ch <= ' ' {
		ch = s.readByte()
	}
	value := 0
	for ch >= '0' && ch <= '9' {
		value = value*base + int(ch-'0')
		ch = s.readByte()
	}
	return value
}

func divisorTable(size int) ([]int32, []uint16) {
	offsets := make([]int32, size+2)
	for d := 1; d*d <= size; d++ {
		for multiple := d * d; multiple <= size; multiple += d {
			offsets[multiple]++
		}
	}
	for i := 1; i <= size; i++ {
		offsets[i] += offsets[i-1]
	}
	offsets[size+1] = offsets[size]
	divisors := make([]uint16, offsets[size])
	// Fill each slice backwards, turning its end offset into its start offset.
	for d := 1; d*d <= size; d++ {
		for multiple := d * d; multiple <= size; multiple += d {
			offsets[multiple]--
			divisors[offsets[multiple]] = uint16(d)
		}
	}
	return offsets, divisors
}

type fenwick []int64

func (f fenwick) add(at int, delta int64) {
	for at < len(f) {
		f[at] += delta
		at += at & -at
	}
}

func (f fenwick) point(at int) int64 {
	var total int64
	for at != 0 {
		total += f[at]
		at &= at - 1
	}
	return total
}

func main() {
	var input scanner
	size := input.number()
	charge := make([]uint32, size+1)
	for i := 1; i <= size; i++ {
		charge[i] = uint32(input.number())
	}
	offsets, divisors := divisorTable(size)
	tree := make(fenwick, size+1)
	output := bufio.NewWriterSize(os.Stdout, bufferSize)
	var line [lineSize]byte
	for count := input.number(); count > 0; count-- {
		if input.number() == 1 {
			particle := input.number()
			total := int64(charge[particle])
			for _, small := range divisors[offsets[particle]:offsets[particle+1]] {
				d := int(small)
				total += tree.point(d)
				other := particle / d
				if other != d {
					total += tree.point(other)
				}
			}
			digits := strconv.AppendInt(line[:0], total, base)
			output.Write(append(digits, '\n'))
		} else {
			left, right, power := input.number(), input.number(), int64(input.number())
			tree.add(left, power)
			tree.add(right+1, -power)
		}
	}
	output.Flush()
}
