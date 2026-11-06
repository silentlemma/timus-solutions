package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	bufferSize = 4096
	fieldSize  = 8
	base       = 10
)

type interval struct{ start, end, value int16 }

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func nextInterval(input *bufio.Scanner) interval {
	start, end, value := nextInt(input), nextInt(input), nextInt(input)
	return interval{int16(start), int16(end), int16(value)}
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	first := make([]interval, nextInt(input))
	for i := range first {
		first[i] = nextInterval(input)
	}
	remaining := nextInt(input)
	result := make([]interval, 0, len(first)+remaining)
	var mask interval
	haveMask := false
	for _, current := range first {
		for start := current.start; start < current.end; {
			for remaining > 0 && (!haveMask || mask.end <= start) {
				mask = nextInterval(input)
				remaining--
				haveMask = true
			}
			if haveMask && mask.start <= start && start < mask.end {
				start = mask.end
				continue
			}
			end := current.end
			if haveMask && start < mask.start && mask.start < end {
				end = mask.start
			}
			result = append(result, interval{start, end, current.value})
			start = end
		}
	}

	output := bufio.NewWriter(os.Stdout)
	var digits [fieldSize]byte
	output.Write(strconv.AppendInt(digits[:0], int64(len(result)), base))
	for _, item := range result {
		for _, field := range [...]int16{item.start, item.end, item.value} {
			output.WriteByte(' ')
			output.Write(strconv.AppendInt(digits[:0], int64(field), base))
		}
	}
	output.WriteByte('\n')
	output.Flush()
}
