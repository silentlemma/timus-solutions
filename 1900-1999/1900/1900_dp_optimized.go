package main

import (
	"bufio"
	"os"
	"strconv"
)

const infinity uint32 = 1000000000
const inputSize = 4096
const outputSize = 4096
const decimalBase = 10

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, inputSize)
	n, k := number(in), number(in)
	offset := make([]int, n)
	for right := range offset {
		offset[right] = right * (right + 1) / 2
	}
	cost := make([]uint32, n*(n+1)/2)
	for left := 0; left+1 < n; left++ {
		for right := left + 1; right < n; right++ {
			cost[offset[right]+left] = uint32(number(in))
		}
	}
	for left := n - 2; left >= 0; left-- {
		prefix := uint32(0)
		for right := left + 1; right < n; right++ {
			index := offset[right] + left
			prefix += cost[index]
			cost[index] = cost[index+1] + prefix
		}
	}
	span := n - k
	previous, current := make([]uint32, span), make([]uint32, span)
	for index := range previous {
		previous[index] = cost[offset[index]]
	}
	parents := make([]uint16, k*span)
	for group := 2; group <= k+1; group++ {
		parentBase := (group - 2) * span
		var fill func(int, int, int, int)
		fill = func(left, right, first, last int) {
			if left > right {
				return
			}
			middle := (left + right) / 2
			column := offset[group+middle-1] + group - 1
			limit := last
			if limit > middle {
				limit = middle
			}
			best, split := infinity, first
			for cut := first; cut <= limit; cut++ {
				value := previous[cut] + cost[column+cut]
				if value < best {
					best, split = value, cut
				}
			}
			current[middle] = best
			parents[parentBase+middle] = uint16(group - 1 + split)
			fill(left, middle-1, first, split)
			fill(middle+1, right, split, last)
		}
		fill(0, span-1, 0, span-1)
		previous, current = current, previous
	}
	cuts := make([]int, k)
	end := n
	for group := k + 1; group > 1; group-- {
		end = int(parents[(group-2)*span+end-group])
		cuts[group-2] = end
	}
	output := make([]byte, 0, outputSize)
	output = strconv.AppendUint(output, uint64(cost[offset[n-1]]-previous[span-1]), decimalBase)
	output = append(output, '\n')
	for index, cut := range cuts {
		if index != 0 {
			output = append(output, ' ')
		}
		output = strconv.AppendInt(output, int64(cut), decimalBase)
	}
	output = append(output, '\n')
	os.Stdout.Write(output)
}
