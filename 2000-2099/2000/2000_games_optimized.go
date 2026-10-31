package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(values []uint16, first, second int) (int64, int64) {
	total, score := int64(0), int64(0)
	for _, value := range values {
		total += int64(value)
	}
	if first == second {
		left := int64(0)
		for i := 0; i < first; i++ {
			left += int64(values[i])
		}
		right := total - left - int64(values[first])
		score = int64(values[first]) + left
		if right > left {
			score = int64(values[first]) + right
		}
	} else if first < second {
		boundary := (first + second) / 2
		for i := 0; i <= boundary; i++ {
			score += int64(values[i])
		}
	} else {
		boundary := (first + second + 1) / 2
		for i := boundary; i < len(values); i++ {
			score += int64(values[i])
		}
	}
	return score, total - score
}

// digits are parsed by hand instead of fmt.Fscan; the buffered reader refills,
// so no total input-size bound is needed.
var input = bufio.NewReader(os.Stdin)

func number() int {
	c, _ := input.ReadByte()
	for c < '0' || c > '9' {
		c, _ = input.ReadByte()
	}
	value := 0
	for c >= '0' && c <= '9' {
		value = value*10 + int(c-'0')
		next, err := input.ReadByte()
		if err != nil {
			break
		}
		c = next
	}
	return value
}

func main() {
	n := number()
	// values <= 10000 fit uint16; widen before every addition.
	values := make([]uint16, n)
	for i := range values {
		values[i] = uint16(number())
	}
	first, second := number(), number()
	a, b := solve(values, first-1, second-1)
	fmt.Println(a, b)
}
