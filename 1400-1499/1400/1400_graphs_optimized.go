package main

import (
	"bufio"
	"os"
	"strconv"
)

const maxCells = 256
const unseen = 255
const bufferSize = 4096
const directions = 4
const floatBits = 64

func number(in *bufio.Reader) int {
	c, _ := in.ReadByte()
	for c != 0 && c <= ' ' {
		c, _ = in.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		c, _ = in.ReadByte()
	}
	return value
}

func bfs(n, start int, neighbors *[maxCells][directions]uint8, dist, queue *[maxCells]uint8) int {
	for i := 0; i < n; i++ {
		dist[i] = unseen
	}
	dist[start] = 0
	queue[0] = uint8(start)
	tail := 1
	sum := 0
	for head := 0; head < tail; head++ {
		v := queue[head]
		for _, u := range neighbors[v] {
			if dist[u] == unseen {
				dist[u] = dist[v] + 1
				sum += int(dist[u])
				queue[tail] = u
				tail++
			}
		}
	}
	return sum
}

func main() {
	in := bufio.NewReaderSize(os.Stdin, bufferSize)
	n, m := number(in), number(in)
	var neighbors [maxCells][directions]uint8
	for v := 0; v < n; v++ {
		up, down := v, v
		if v >= m {
			up = v - m
		}
		if v+m < n {
			down = v + m
		}
		neighbors[v] = [directions]uint8{
			uint8((v + n - 1) % n), uint8((v + 1) % n), uint8(up), uint8(down),
		}
	}
	// Horizontal edges contain an n-cycle, hence every distance is at most n/2.
	var dist, queue [maxCells]uint8
	bestStart, bestSum := 0, maxCells*maxCells
	// Reversal v -> n-1-v preserves every edge and pairs equal-sum starting cells.
	for start := 0; start < (n+1)/2; start++ {
		if sum := bfs(n, start, &neighbors, &dist, &queue); sum < bestSum {
			bestStart, bestSum = start, sum
		}
	}
	bfs(n, bestStart, &neighbors, &dist, &queue)
	output := make([]byte, 0, bufferSize)
	output = append(output, "Mean = "...)
	output = strconv.AppendFloat(output, float64(bestSum)/float64(n), 'f', 2, floatBits)
	output = append(output, '\n')
	for i := 0; i < n; i++ {
		output = strconv.AppendUint(output, uint64(dist[i]), 10)
		if (i+1)%m == 0 || i+1 == n {
			output = append(output, '\n')
		} else {
			output = append(output, ' ')
		}
	}
	os.Stdout.Write(output)
}
