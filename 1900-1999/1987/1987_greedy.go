package main

import (
	"bufio"
	"fmt"
	"os"
)

func locate(left, right, queries []int) []int {
	stack := make([]int, 0, len(left))
	answers := make([]int, 0, len(queries))
	index := 0
	for _, point := range queries {
		for index < len(left) && left[index] <= point {
			for len(stack) > 0 && right[stack[len(stack)-1]] < left[index] {
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, index)
			index++
		}
		for len(stack) > 0 && right[stack[len(stack)-1]] < point {
			stack = stack[:len(stack)-1]
		}
		answer := -1
		if len(stack) > 0 {
			answer = stack[len(stack)-1] + 1
		}
		answers = append(answers, answer)
	}
	return answers
}

func main() {
	in := bufio.NewReader(os.Stdin)
	next := func() int { var value int; fmt.Fscan(in, &value); return value }
	n := next()
	left, right := make([]int, n), make([]int, n)
	for i := range left {
		left[i] = next()
		right[i] = next()
	}
	m := next()
	queries := make([]int, m)
	for i := range queries {
		queries[i] = next()
	}
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	for _, answer := range locate(left, right, queries) {
		fmt.Fprintln(out, answer)
	}
}
