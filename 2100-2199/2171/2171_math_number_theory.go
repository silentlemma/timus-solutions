package main

import (
	"bufio"
	"fmt"
	"os"
)

type progression struct {
	first int64
	step  int64
}

func extendedGCD(a, b int64) (int64, int64) {
	x, nextX := int64(1), int64(0)
	for b != 0 {
		quotient := a / b
		a, b = b, a%b
		x, nextX = nextX, x-quotient*nextX
	}
	return a, x
}

func countUnion(items []progression, limit int64, begin int, first, step, sign int64) int64 {
	answer := int64(0)
	for i := begin; i < len(items); i++ {
		otherFirst, otherStep := items[i].first, items[i].step
		mergedFirst, mergedStep := first, step
		if step == 0 {
			if first < otherFirst || (first-otherFirst)%otherStep != 0 {
				continue
			}
		} else {
			divisor, inverse := extendedGCD(step, otherStep)
			difference := otherFirst - first
			if difference%divisor != 0 {
				continue
			}
			modulus := otherStep / divisor
			offset := (difference / divisor * inverse) % modulus
			if offset < 0 {
				offset += modulus
			}
			mergedStep = step * modulus
			mergedFirst = first + step*offset
			if mergedFirst < otherFirst {
				gap := otherFirst - mergedFirst
				mergedFirst += ((gap-1)/mergedStep + 1) * mergedStep
			}
			if mergedFirst > limit {
				continue
			}
			// A zero step stores an intersection with just one in-range value.
			if mergedStep > limit-mergedFirst {
				mergedStep = 0
			}
		}
		count := int64(1)
		if mergedStep != 0 {
			count = (limit-mergedFirst)/mergedStep + 1
		}
		answer += sign * count
		answer += countUnion(items, limit, i+1, mergedFirst, mergedStep, -sign)
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	var limit int64
	var count int
	if _, err := fmt.Fscan(input, &limit, &count); err != nil {
		return
	}
	items := make([]progression, count)
	for i := range items {
		fmt.Fscan(input, &items[i].first, &items[i].step)
	}
	fmt.Println(countUnion(items, limit, 0, 1, 1, 1))
}
