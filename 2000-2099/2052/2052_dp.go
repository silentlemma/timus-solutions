package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const decimalBase = 10
const maxDigit = decimalBase - 1

func buildTables(digits int) [][]int64 {
	maximum := maxDigit * digits
	ways := make([]int64, maximum+1)
	ways[0] = 1
	var prefix [][]int64
	for length := 0; length < digits; length++ {
		row := make([]int64, maximum+1)
		running := int64(0)
		for total := range row {
			running += ways[total]
			row[total] = running
		}
		prefix = append(prefix, row)
		if length+1 == digits {
			break
		}
		nextWays := make([]int64, maximum+1)
		window := int64(0)
		for total := range nextWays {
			window += ways[total]
			if total >= decimalBase {
				window -= ways[total-decimalBase]
			}
			nextWays[total] = window
		}
		ways = nextWays
	}
	return prefix
}

func clamped(index, maximum int) int {
	if index > maximum {
		return maximum
	}
	return index
}

func countLeq(value int64, target int, prefix [][]int64) int64 {
	digits := strconv.FormatInt(value, decimalBase)
	maximum, remaining := len(prefix[0])-1, target
	result := int64(0)
	for position := 0; position < len(digits); position++ {
		digit := int(digits[position] - '0')
		row := prefix[len(digits)-position-1]
		if digit != 0 && remaining >= 0 {
			result += row[clamped(remaining, maximum)]
			if remaining >= digit {
				result -= row[clamped(remaining-digit, maximum)]
			}
		}
		remaining -= digit
		if remaining < 0 {
			return result
		}
	}
	if remaining == 0 {
		result++
	}
	return result
}

func digitSum(value int64) int {
	total := 0
	for value != 0 {
		total += int(value % decimalBase)
		value /= decimalBase
	}
	return total
}

func solve(number int64) int {
	digits := len(strconv.FormatInt(number, decimalBase))
	prefix := buildTables(digits)
	lower, answer := int64(0), 0
	for target := 1; target <= maxDigit*digits; target++ {
		count := countLeq(number, target, prefix)
		if count == 0 {
			continue
		}
		start := lower + 1
		left, right := start, lower+count
		for left <= right {
			middle := (left + right) / 2
			if middle-countLeq(middle, target, prefix) <= lower {
				left = middle + 1
			} else {
				right = middle - 1
			}
		}
		if right >= start && digitSum(right) == target && right-countLeq(right, target, prefix) == lower {
			answer++
		}
		lower += count
	}
	return answer
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var number int64
	fmt.Fscan(in, &number)
	fmt.Println(solve(number))
}
