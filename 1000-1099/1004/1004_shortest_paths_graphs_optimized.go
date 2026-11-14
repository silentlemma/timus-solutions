package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxVertices  = 100
	infinity     = 32767
	endOfInput   = -1
	decimalBase  = 10
	vertexDigits = 3
)

func number(input *bufio.Reader) int {
	c, err := input.ReadByte()
	for err == nil && c <= ' ' {
		c, err = input.ReadByte()
	}
	if err != nil || c == '-' {
		return endOfInput
	}
	value := 0
	for err == nil && c >= '0' && c <= '9' {
		value = value*decimalBase + int(c-'0')
		c, err = input.ReadByte()
	}
	return value
}

func solve(n, m int, input *bufio.Reader, output *bufio.Writer) {
	var road, distance [maxVertices][maxVertices]uint16
	var next [maxVertices][maxVertices]uint8
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i != j {
				road[i][j], distance[i][j] = infinity, infinity
			}
			next[i][j] = uint8(j)
		}
	}
	for e := 0; e < m; e++ {
		a, b, length := number(input)-1, number(input)-1, uint16(number(input))
		if length < road[a][b] {
			road[a][b], road[b][a] = length, length
			distance[a][b], distance[b][a] = length, length
		}
	}
	best, count := infinity, 0
	var cycle [maxVertices]int
	for k := 0; k < n; k++ {
		for i := 0; i < k; i++ {
			left := int(road[k][i])
			if left >= best {
				continue
			}
			for j := i + 1; j < k; j++ {
				length := left + int(road[k][j]) + int(distance[i][j])
				if length < best {
					best, count = length, 0
					for v := i; v != j; v = int(next[v][j]) {
						cycle[count] = v
						count++
					}
					cycle[count], cycle[count+1] = j, k
					count += 2
				}
			}
		}
		for i := 0; i < n; i++ {
			left := int(distance[k][i])
			if i == k || left >= best {
				continue
			}
			for j := i + 1; j < n; j++ {
				length := left + int(distance[k][j])
				if length < best && length < int(distance[i][j]) {
					distance[i][j], distance[j][i] = uint16(length), uint16(length)
					next[i][j], next[j][i] = next[i][k], next[j][k]
				}
			}
		}
	}
	if count == 0 {
		output.WriteString("No solution.\n")
		return
	}
	var digits [vertexDigits]byte
	for i, v := range cycle[:count] {
		if i != 0 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendInt(digits[:0], int64(v+1), decimalBase))
	}
	output.WriteByte('\n')
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	for n := number(input); n != endOfInput; n = number(input) {
		solve(n, number(input), input, output)
	}
}
