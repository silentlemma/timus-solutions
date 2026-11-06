package main

import (
	"bufio"
	"os"
	"strconv"
)

const (
	maxCities = 200
	road      = 1
	forest    = 2
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
	size, roads := number(input), number(input)
	var edges [maxCities + 1][maxCities + 1]byte
	for i := 0; i < roads; i++ {
		a, b := number(input), number(input)
		edges[a][b], edges[b][a] = road, road
	}
	var depth, parent [maxCities + 1]int
	var queue [maxCities]int
	tours := roads
	for root := 1; root <= size; root++ {
		if depth[root] != 0 {
			continue
		}
		depth[root], queue[0] = 1, root
		end := 1
		for head := 0; head < end; head++ {
			u := queue[head]
			for v := 1; v <= size; v++ {
				if edges[u][v] != 0 && depth[v] == 0 {
					depth[v], parent[v] = depth[u]+1, u
					edges[u][v], edges[v][u] = forest, forest
					queue[end] = v
					end++
					tours--
				}
			}
		}
	}
	output := bufio.NewWriter(os.Stdout)
	var digits [fieldSize]byte
	writeNumber := func(value int) {
		output.Write(strconv.AppendInt(digits[:0], int64(value), decimal))
	}
	writeNumber(tours)
	output.WriteByte('\n')
	var left, right [maxCities]int
	for u := 1; u <= size; u++ {
		for v := u + 1; v <= size; v++ {
			if edges[u][v] != road {
				continue
			}
			a, b := u, v
			l, r := 0, 0
			for a != b {
				if depth[a] >= depth[b] {
					left[l] = a
					l++
					a = parent[a]
				} else {
					right[r] = b
					r++
					b = parent[b]
				}
			}
			writeNumber(l + r + 1)
			for _, city := range left[:l] {
				output.WriteByte(' ')
				writeNumber(city)
			}
			output.WriteByte(' ')
			writeNumber(a)
			for j := r - 1; j >= 0; j-- {
				output.WriteByte(' ')
				writeNumber(right[j])
			}
			output.WriteByte('\n')
		}
	}
	output.Flush()
}
