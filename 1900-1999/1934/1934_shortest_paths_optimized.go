package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
)

const (
	probabilityScale = 100
	probabilityBits  = 7
	probabilityMask  = 1<<probabilityBits - 1
	decimalPlaces    = 12
	floatBits        = 64
	bufferSize       = 4096
	lineSize         = 48
	base             = 10
)

type edge struct {
	packed, next uint32
}

func nextInt(input *bufio.Scanner) uint32 {
	input.Scan()
	var value uint32
	for _, ch := range input.Bytes() {
		value = value*base + uint32(ch-'0')
	}
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	var buffer [bufferSize]byte
	input.Buffer(buffer[:], len(buffer))
	input.Split(bufio.ScanWords)
	size, roads := nextInt(input), nextInt(input)
	start, target := nextInt(input), nextInt(input)
	head := make([]uint32, size+1)
	edges := make([]edge, 1, 2*roads+1)
	for i := uint32(0); i < roads; i++ {
		a, b, probability := nextInt(input), nextInt(input), nextInt(input)
		edges = append(edges, edge{b<<probabilityBits | probability, head[a]})
		head[a] = uint32(len(edges) - 1)
		edges = append(edges, edge{a<<probabilityBits | probability, head[b]})
		head[b] = uint32(len(edges) - 1)
	}
	var cost [probabilityScale]float64
	for probability := range cost {
		cost[probability] = -math.Log1p(-float64(probability) / probabilityScale)
	}
	distance := make([]uint32, size+1)
	parent := make([]uint32, size+1)
	best := make([]float64, size+1)
	queue := make([]uint32, 0, size)
	distance[start] = 1
	queue = append(queue, start)
	for i := 0; i < len(queue); i++ {
		city := queue[i]
		if city == target {
			break
		}
		nextDistance := distance[city] + 1
		prefixCost := best[city]
		for index := head[city]; index != 0; index = edges[index].next {
			packed := edges[index].packed
			neighbor := packed >> probabilityBits
			candidate := prefixCost + cost[packed&probabilityMask]
			if distance[neighbor] == 0 {
				distance[neighbor] = nextDistance
				best[neighbor], parent[neighbor] = candidate, city
				queue = append(queue, neighbor)
			} else if distance[neighbor] == nextDistance && candidate < best[neighbor] {
				best[neighbor], parent[neighbor] = candidate, city
			}
		}
	}
	queue = queue[:0]
	for city := target; city != 0; city = parent[city] {
		queue = append(queue, city)
	}
	output := bufio.NewWriter(os.Stdout)
	var storage [lineSize]byte
	line := strconv.AppendInt(storage[:0], int64(len(queue)), base)
	line = append(line, ' ')
	line = strconv.AppendFloat(line, -math.Expm1(-best[target]), 'f', decimalPlaces, floatBits)
	output.Write(append(line, '\n'))
	for i := len(queue) - 1; i >= 0; i-- {
		if i != len(queue)-1 {
			output.WriteByte(' ')
		}
		output.Write(strconv.AppendUint(storage[:0], uint64(queue[i]), base))
	}
	output.WriteByte('\n')
	output.Flush()
}
