package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	goals   = 3
	modulus = 1000000007
)

func minInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func countForecasts(size int) int {
	total := goals * size * (size - 1) / 2
	maximum := goals * (size - 1)
	stride := maximum + 1
	maxRows := 1
	for used := 0; used <= size; used++ {
		maxRows = maxInt(maxRows, total*used/size-goals*used*(used-1)/2+1)
	}
	current, following := make([]int32, maxRows*stride), make([]int32, maxRows*stride)
	current[0] = 1
	lower, upper := 0, 0
	for used := 0; used < size; used++ {
		nextUsed := used + 1
		nextLower, nextUpper := goals*nextUsed*used/2, total*nextUsed/size
		for index := range following {
			following[index] = 0
		}
		for partial := lower; partial <= upper; partial++ {
			minimumLast := 0
			if used > 0 {
				minimumLast = (partial + used - 1) / used
			}
			first := maxInt(0, maxInt(nextLower-partial, minimumLast))
			last := minInt(maximum, minInt(nextUpper-partial, (total-partial)/(size-used)))
			if first > last {
				continue
			}
			row := (partial - lower) * stride
			var prefix int64
			for value := 0; value < first; value++ {
				prefix += int64(current[row+value])
			}
			for value := first; value <= last; value++ {
				prefix += int64(current[row+value])
				if prefix != 0 {
					following[(partial+value-nextLower)*stride+value] = int32(prefix % modulus)
				}
			}
		}
		current, following = following, current
		lower, upper = nextLower, nextUpper
	}
	var answer int64
	for value := 0; value < stride; value++ {
		answer += int64(current[value])
	}
	return int(answer % modulus)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var size int
	fmt.Fscan(in, &size)
	fmt.Println(countForecasts(size))
}
