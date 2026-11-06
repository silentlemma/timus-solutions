package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	fresh byte = iota
	walking
	done
)

const (
	bufferSize = 4096
	lineSize   = 24
	base       = 10
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	size := nextInt(input)
	successor := make([]uint32, size+1)
	incoming := make([]byte, size+1)
	for i := 1; i <= size; i++ {
		next := nextInt(input)
		successor[i] = uint32(next)
		if incoming[next] < 2 {
			incoming[next]++
		}
	}
	state := make([]byte, size+1)
	starts, cycles, cycleNodes, isolatedCycles := 0, 0, 0, 0
	for start := uint32(1); int(start) <= size; start++ {
		if incoming[start] == 0 {
			starts++
		}
		node := start
		for state[node] == fresh {
			state[node] = walking
			node = successor[node]
		}
		if state[node] == walking {
			cycles++
			first := node
			isolated := true
			for {
				cycleNodes++
				isolated = isolated && incoming[node] == 1
				node = successor[node]
				if node == first {
					break
				}
			}
			if isolated {
				isolatedCycles++
			}
		}
		for node = start; state[node] == walking; node = successor[node] {
			state[node] = done
		}
	}
	var output [lineSize]byte
	line := strconv.AppendInt(output[:0], int64(starts+isolatedCycles), base)
	line = append(line, ' ')
	line = strconv.AppendInt(line, int64(size-cycleNodes+cycles), base)
	os.Stdout.Write(append(line, '\n'))
}
