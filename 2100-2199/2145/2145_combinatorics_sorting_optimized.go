package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const (
	bufferSize = 4096
	outputSize = 16
	decimal    = 10
)

func nextInt(input *bufio.Scanner) uint32 {
	input.Scan()
	var value uint32
	for _, digit := range input.Bytes() {
		value = value*decimal + uint32(digit-'0')
	}
	return value
}

type events []uint32

func (e events) Len() int           { return len(e) }
func (e events) Less(i, j int) bool { return e[i] < e[j] }
func (e events) Swap(i, j int)      { e[i], e[j] = e[j], e[i] }

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	size := int(nextInt(input))
	order := make(events, 2*size)
	// At equal value, put the problem before the student who can solve it.
	for i := 0; i < size; i++ {
		order[i] = nextInt(input)<<1 | 1
	}
	for i := size; i < len(order); i++ {
		order[i] = nextInt(input) << 1
	}
	modulus := uint64(nextInt(input))
	sort.Sort(order)
	ways, free := 1%modulus, uint64(0)
	for _, event := range order {
		if event&1 == 0 {
			free++
		} else {
			ways = ways * free % modulus
			if ways == 0 {
				break
			}
			free--
		}
	}
	var storage [outputSize]byte
	line := strconv.AppendUint(storage[:0], ways, decimal)
	os.Stdout.Write(append(line, '\n'))
}
