package main

import (
	"io"
	"os"
	"strconv"
)

const (
	maxSize    = 100
	base       = 1000000000
	limbDigits = 9
	maxLimbs   = 18
	decimal    = 10
)

func readPositions() (int, [maxSize + 1]int) {
	var positions [maxSize + 1]int
	var chunk [maxSize]byte
	size, index, value := 0, 0, 0
	reading := false
	for {
		count, err := os.Stdin.Read(chunk[:])
		for _, b := range chunk[:count] {
			if b >= '0' && b <= '9' {
				value = value*decimal + int(b-'0')
				reading = true
			} else if reading {
				if index == 0 {
					size = value
				} else {
					positions[value] = index
					if index == size {
						return size, positions
					}
				}
				index++
				value, reading = 0, false
			}
		}
		if err == io.EOF {
			if reading && index == size {
				positions[value] = index
			}
			return size, positions
		}
		if err != nil {
			return 0, positions
		}
	}
}

func main() {
	size, positions := readPositions()
	var tree [maxSize + 1]uint8
	var rank [maxLimbs]uint64
	limbs := 1
	for value := 1; value <= size; value++ {
		pos := positions[value]
		left := 0
		for i := pos - 1; i > 0; i -= i & -i {
			left += int(tree[i])
		}
		for i := pos; i <= size; i += i & -i {
			tree[i]++
		}
		step := value - 1 - left
		if rank[0]&1 != 0 {
			step = left
		}
		carry := uint64(step)
		for i := 0; i < limbs; i++ {
			number := rank[i]*uint64(value) + carry
			rank[i], carry = number%base, number/base
		}
		if carry != 0 {
			rank[limbs] = carry
			limbs++
		}
	}
	i := 0
	for i < limbs && rank[i] == base-1 {
		rank[i] = 0
		i++
	}
	rank[i]++
	if i == limbs {
		limbs++
	}
	var output [maxLimbs*limbDigits + 1]byte
	line := strconv.AppendUint(output[:0], rank[limbs-1], decimal)
	var buffer [limbDigits]byte
	for i := limbs - 2; i >= 0; i-- {
		digits := strconv.AppendUint(buffer[:0], rank[i], decimal)
		for pad := len(digits); pad < limbDigits; pad++ {
			line = append(line, '0')
		}
		line = append(line, digits...)
	}
	os.Stdout.Write(append(line, '\n'))
}
