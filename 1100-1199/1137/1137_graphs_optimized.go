package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxStop   = 1000
	fieldSize = 16
	decimal   = 10
)

func number(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	var roads [maxStop + 1][]uint16
	var start uint16
	edges := 0
	for routes := number(input); routes > 0; routes-- {
		length, stop := number(input), uint16(number(input))
		if start == 0 {
			start = stop
		}
		edges += length
		for step := 0; step < length; step++ {
			next := uint16(number(input))
			roads[stop] = append(roads[stop], next)
			stop = next
		}
	}
	if start == 0 {
		os.Stdout.WriteString("0\n")
		return
	}
	// The active walk grows from the front; finished stops fill the back.
	route := make([]uint16, edges+1)
	route[0] = start
	depth, end := 1, len(route)
	for depth > 0 {
		stop := route[depth-1]
		next := roads[stop]
		if len(next) != 0 {
			route[depth] = next[len(next)-1]
			roads[stop] = next[:len(next)-1]
			depth++
		} else {
			depth--
			end--
			route[end] = stop
		}
	}
	if end != 0 {
		os.Stdout.WriteString("0\n")
		return
	}
	output := bufio.NewWriter(os.Stdout)
	var buffer [fieldSize]byte
	output.Write(strconv.AppendInt(buffer[:0], int64(edges), decimal))
	for _, stop := range route {
		output.WriteByte(' ')
		output.Write(strconv.AppendUint(buffer[:0], uint64(stop), decimal))
	}
	output.WriteByte('\n')
	output.Flush()
}
