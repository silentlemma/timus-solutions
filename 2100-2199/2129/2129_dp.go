package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

func countWays(n, base, coins int64) int64 {
	if n < coins {
		return 0
	}
	digits := make([]int64, 0)
	digitSum := int64(0)
	for value := n; value > 0; value /= base {
		digit := value % base
		digits = append(digits, digit)
		digitSum += digit
	}
	if digitSum > coins || (coins-digitSum)%(base-1) != 0 {
		return 0
	}
	budget := int((coins - digitSum) / (base - 1))
	if budget == 0 {
		return 1
	}
	dp := make([][]int64, budget+1)
	for used := range dp {
		dp[used] = make([]int64, used+1)
	}
	dp[0][0] = 1
	for level := len(digits) - 1; level > 0; level-- {
		next := make([][]int64, budget+1)
		for used := range next {
			next[used] = make([]int64, used+1)
		}
		for used, row := range dp {
			suffix := int64(0)
			hasValue := false
			for _, ways := range row {
				suffix += ways
				if suffix >= modulus {
					suffix -= modulus
				}
				hasValue = hasValue || ways != 0
			}
			if !hasValue {
				continue
			}
			threshold := 0
			for splits := 0; splits <= budget-used; splits++ {
				// Previous splits must supply enough coins at this level.
				for threshold < len(row) &&
					digits[level]+base*int64(threshold) < int64(splits) {
					suffix -= row[threshold]
					if suffix < 0 {
						suffix += modulus
					}
					threshold++
				}
				if threshold == len(row) {
					break
				}
				next[used+splits][splits] = suffix
			}
		}
		dp = next
	}
	answer := int64(0)
	for _, ways := range dp[budget] {
		answer += ways
		if answer >= modulus {
			answer -= modulus
		}
	}
	return answer
}

func main() {
	input := bufio.NewReader(os.Stdin)
	output := bufio.NewWriter(os.Stdout)
	defer output.Flush()
	var cases int
	fmt.Fscan(input, &cases)
	for ; cases > 0; cases-- {
		var n, base, coins int64
		fmt.Fscan(input, &n, &base, &coins)
		fmt.Fprintln(output, countWays(n, base, coins))
	}
}
