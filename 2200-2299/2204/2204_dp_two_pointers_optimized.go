package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	options        = 2
	outputCapacity = 32
)

type interval struct {
	left, right uint32
}

func next(input *bufio.Reader) uint32 {
	ch, err := input.ReadByte()
	for err == nil && ch <= ' ' {
		ch, err = input.ReadByte()
	}
	var value uint32
	for err == nil && ch >= '0' && ch <= '9' {
		value = 10*value + uint32(ch-'0')
		ch, err = input.ReadByte()
	}
	return value
}

func readIntervals(input *bufio.Reader, count int) []interval {
	ranges := make([]interval, count)
	for i := range ranges {
		ranges[i] = interval{next(input), next(input)}
	}
	return ranges
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	input := bufio.NewReader(os.Stdin)
	n, m := int(next(input)), int(next(input))
	exams := readIntervals(input, n*options)
	trips := readIntervals(input, m)
	cost, last := [options]int{}, [options]int{-1, -1}
	first, end := 0, 0
	for i := 0; i < len(exams); i += options {
		var nextCost, nextLast [options]int
		for j, exam := range exams[i : i+options] {
			for first < m && trips[first].right < exam.left {
				first++
			}
			for end < m && trips[end].left <= exam.right {
				end++
			}
			nextLast[j] = -1
			if end == first {
				nextCost[j] = min(cost[0], cost[1])
				continue
			}
			previous := cost
			for k, previousLast := range last {
				if previousLast == first {
					previous[k]--
				}
			}
			nextCost[j] = min(previous[0], previous[1]) + end - first
			nextLast[j] = end - 1
		}
		cost, last = nextCost, nextLast
	}
	var output [outputCapacity]byte
	os.Stdout.Write(append(strconv.AppendInt(output[:0], int64(m-min(cost[0], cost[1])), 10), '\n'))
}
