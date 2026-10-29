package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

const inputBufferSize = 4096

// the numbers are parsed by hand from a small buffer, faster than fmt.Fscan
type fastInput struct {
	reader *bufio.Reader
}

func (in fastInput) nextInt() int64 {
	c, err := in.reader.ReadByte()
	for err == nil && c <= ' ' {
		c, err = in.reader.ReadByte()
	}
	sign := int64(1)
	if c == '-' {
		sign = -1
		c, err = in.reader.ReadByte()
	}
	var value int64
	for err == nil && c >= '0' && c <= '9' {
		value = value*10 + int64(c-'0')
		c, err = in.reader.ReadByte()
	}
	return value * sign
}

// subsetSums lists the sums of all subsets of the weights, sorted
func subsetSums(weights []int) []int {
	sums := make([]int, 1, 1<<uint(len(weights)))
	for _, weight := range weights {
		count := len(sums)
		for i := 0; i < count; i++ {
			sums = append(sums, sums[i]+weight)
		}
	}
	sort.Ints(sums)
	return sums
}

func main() {
	in := fastInput{bufio.NewReaderSize(os.Stdin, inputBufferSize)}
	n := int(in.nextInt())
	weights := make([]int, n)
	total := 0
	for i := range weights {
		weights[i] = int(in.nextInt())
		total += weights[i]
	}
	left := subsetSums(weights[:n/2])
	right := subsetSums(weights[n/2:])
	// a pile is a subset of each half; walk the left sums up and the right sums
	// down, moving the side that brings the pile closer to total / 2
	best := total
	for i, j := 0, len(right)-1; i < len(left) && j >= 0; {
		difference := total - 2*(left[i]+right[j])
		absolute := difference
		if absolute < 0 {
			absolute = -absolute
		}
		if absolute < best {
			best = absolute
		}
		// the difference has the parity of the total, so it cannot be smaller
		if best == total%2 {
			break
		}
		if difference > 0 {
			i++
		} else {
			j--
		}
	}
	os.Stdout.WriteString(strconv.Itoa(best) + "\n")
}
