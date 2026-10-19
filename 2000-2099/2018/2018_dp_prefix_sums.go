package main

import (
	"bufio"
	"fmt"
	"os"
)

const modulus int64 = 1000000007

func solve(n, a, b int) int64 {
	endsOne := make([]int64, b+1)
	endsTwo := make([]int64, a+1)
	endsOne[0], endsTwo[0] = 1, 1
	var windowOne, windowTwo int64 = 1, 1
	var lastOne, lastTwo int64
	for length := 1; length <= n; length++ {
		lastOne, lastTwo = windowOne, windowTwo
		var expiredTwo, expiredOne int64
		if length >= a {
			expiredTwo = endsTwo[(length-a)%(a+1)]
		}
		if length >= b {
			expiredOne = endsOne[(length-b)%(b+1)]
		}
		windowOne = (windowOne + lastTwo + modulus - expiredTwo) % modulus
		windowTwo = (windowTwo + lastOne + modulus - expiredOne) % modulus
		endsOne[length%(b+1)] = lastOne
		endsTwo[length%(a+1)] = lastTwo
	}
	return (lastOne + lastTwo) % modulus
}

func main() {
	in := bufio.NewReader(os.Stdin)
	var n, a, b int
	fmt.Fscan(in, &n, &a, &b)
	fmt.Println(solve(n, a, b))
}
