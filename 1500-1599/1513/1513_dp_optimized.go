package main

import (
	"bufio"
	"math/big"
	"os"
	"strconv"
)

func nextInt(input *bufio.Scanner) int {
	input.Scan()
	value, _ := strconv.Atoi(input.Text())
	return value
}

func main() {
	input := bufio.NewScanner(os.Stdin)
	input.Split(bufio.ScanWords)
	size, limit := nextInt(input), nextInt(input)

	var current big.Int
	current.SetInt64(1)
	if limit == size {
		current.Lsh(&current, uint(size))
	} else if limit > 0 {
		// Keep only still-needed counts. Index i represents length i-1.
		needed := size - limit
		slots := limit + 2
		if slots > needed {
			slots = needed
		}
		history := make([]big.Int, slots)
		history[0].SetInt64(1)
		if slots > 1 {
			history[1].SetInt64(1)
		}
		for length := 1; length <= size; length++ {
			current.Lsh(&current, 1)
			if length > limit {
				current.Sub(&current, &history[(length-limit-1)%slots])
			}
			if length+1 < needed {
				history[(length+1)%slots].Set(&current)
			}
		}
	}
	os.Stdout.WriteString(current.String() + "\n")
}
